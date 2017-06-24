import urwid
from urllib2 import urlopen
from HTMLParser import HTMLParser
from simplejson import loads
import thread, logging
from time import sleep


def parse_lines(lines):
    for l in lines:
        name, ticker = l.strip().split(",")
        yield (name, ticker)

# Read files and get symbols
with open("tickers.txt") as file:
    tickers = list(parse_lines(file.readlines()))

# Set up color scheme
palette = [
        ('titlebar', 'dark red', ''),
        ('refresh button', 'dark green,bold', ''),
        ('quit button', 'dark red', ''),
        ('getting quote', 'dark blue', ''),
        ('headers', 'white,bold', ''),
        ('change ', 'dark green', ''),
        ('change negative', 'dark red', ''),
        ]

header_text = urwid.Text(u'Stock Quotes')
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
tabsize = 25

def pos_neg_change(change):
    return ("+{}".format(change) if change >= 0 else str(change))

def get_update():
    ticker_syms = [t[1] for t in tickers]
    ticker_names = [t[0] for t in tickers]
    results = loads(urlopen('https://www.google.com/finance/info?q=' + ",".join(ticker_syms)).read()[3:])

    l = [ ('headers', u'Stock \t Last Price \t Change '.expandtabs(tabsize)),
          ('headers', u'\t % Change \n'.expandtabs(3)) ]

    for i, r in enumerate(results):
        change = float(r['c'])
        percent_change = float(r['cp'])
        color = 'change '
        if change < 0:
            color += 'negative'

        change = pos_neg_change(change)
        percent_change = pos_neg_change(percent_change)

        l.append((
            u'{} \t {} \t '.format(
                ticker_names[i],
                r['l_cur'])
            ).expandtabs(tabsize))
        l.append( (color, (u'{} \t {}% \n'.format(change, percent_change)).expandtabs(10)) )

    return l
    # return HTMLParser().unescape(s).encode('utf-8')

# Handle key presses
def handle_input(key):
    if key == 'R' or key == 'r':
        refresh(main_loop, '')
    if key == 'Q' or key == 'q':
        raise urwid.ExitMainLoop()

def refresh(_loop, _data):
    main_loop.draw_screen()
    quote_box.base_widget.set_text(get_update())
    main_loop.set_alarm_in(10, refresh)

main_loop = urwid.MainLoop(layout, palette, unhandled_input=handle_input)

def cli():
    main_loop.set_alarm_in(0, refresh)
    main_loop.run()
