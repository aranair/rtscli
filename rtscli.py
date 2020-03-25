import urwid
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
try:
    # For Python3.0 and later
    from html.parser import HTMLParser
except ImportError:
    # Fall back to Python 2's HTMLparser
    from HTMLparser import HTMLparser
from simplejson import loads
from time import sleep


def parse_lines(lines):
    for l in lines:
        ticker = l.strip().split(",")
        yield ticker

# Read files and get symbols

with open("tickers.txt") as file:
    tickers = list(parse_lines(file.readlines()))


with open("alphavantage-creds.txt") as file:
    apikey = list(parse_lines(file.readlines()))[0]


# Set up color scheme
palette = [
    ('titlebar', 'dark red', ''),
    ('refresh button', 'dark green,bold', ''),
    ('quit button', 'dark red', ''),
    ('getting quote', 'dark blue', ''),
    ('headers', 'white,bold', ''),
    ('change ', 'dark green', ''),
    ('change negative', 'dark red', '')]

header_text = urwid.Text(u' Stock Quotes')
header = urwid.AttrMap(header_text, 'titlebar')

# Create the menu
menu = urwid.Text([
    u'Press (', ('refresh button', u'R'), u') to manually refresh. ',
    u'Press (', ('quit button', u'Q'), u') to quit.'
])

# Create the quotes box
quote_text = urwid.Text(u'Press (R) to get your first quote!')
quote_filler = urwid.Filler(quote_text, valign='top', top=1, bottom=1)
v_padding = urwid.Padding(quote_filler, left=1, right=1)
quote_box = urwid.LineBox(v_padding)

# Assemble the widgets
layout = urwid.Frame(header=header, body=quote_box, footer=menu)

def pos_neg_change(change):
    if not change:
        return "0"
    else:
        return ("+{}".format(change) if change >= 0 else str(change))

def get_color(change):
    color = 'change '
    if change < 0:
        color += 'negative'
    return color

def append_text(l, s, tabsize=10, color='white'):
    l.append((color, s.expandtabs(tabsize)))

def calculate_gain(price_in, current_price, shares):
    gain_per_share = float(current_price) - float(price_in)
    gain_percent = round(gain_per_share / float(price_in) * 100, 3)

    return gain_per_share * int(shares), gain_percent

def get_update():
    results = []

    try:
        for t in tickers:
            ticker_sym = t[1]
            url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(ticker_sym, apikey)
            res = loads(urlopen(url).read())
            results.append(res["Global Quote"])
    except Exception as err:
        print(err)
        return

    updates = [
        ('headers', u'Stock \t '.expandtabs(25)),
        ('headers', u'Last Price \t Change '.expandtabs(5)),
        ('headers', u'\t % Change '.expandtabs(5)),
        ('headers', u'\t Gain '.expandtabs(3)),
        ('headers', u'\t % Gain \n'.expandtabs(5)) ]

    total_portfolio_change = 0.0

    for i, r in enumerate(results):
        change = float(r['09. change'])
        percent_change = r['10. change percent']

        append_text(updates, '{} \t '.format(tickers[i][0]), tabsize=25)
        append_text(updates, '{} \t '.format(r['05. price']), tabsize=15)
        append_text(
            updates,
            '{} \t {}% \t'.format(
                pos_neg_change(change),
                percent_change),
            tabsize=13,
            color=get_color(change))

        gain = gain_percent = ''
        if len(tickers[i]) > 2:
            gain, gain_percent = calculate_gain(
                price_in = tickers[i][2],
                current_price = r['05. price'],
                shares = tickers[i][3])

            total_portfolio_change += gain

        append_text(
            updates,
            '{} \t {}% \n'.format(pos_neg_change(gain), pos_neg_change(gain_percent)),
            color=get_color(gain))

    append_text(updates, '\n\n\nNet Portfolio Gain: ')
    append_text(updates, pos_neg_change(total_portfolio_change), color=get_color(total_portfolio_change))

    return updates

# Handle key presses
def handle_input(key):
    if key == 'R' or key == 'r':
        refresh(main_loop, '')

    if key == 'Q' or key == 'q':
        raise urwid.ExitMainLoop()

def refresh(_loop, _data):
    main_loop.draw_screen()
    quote_box.base_widget.set_text(get_update())
    main_loop.set_alarm_in(60, refresh)

main_loop = urwid.MainLoop(layout, palette, unhandled_input=handle_input)

def cli():
    main_loop.set_alarm_in(0, refresh)
    main_loop.run()
cli()
