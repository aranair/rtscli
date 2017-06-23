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
    ('titlebar', 'dark red,bold', 'black'),
    ('refresh button', 'dark green,bold', 'black'),
    ('quit button', 'dark red,bold', 'black'),
    ('getting quote', 'dark blue', 'black')]

header_text = urwid.Text(u'Stock Quotes')
header = urwid.AttrMap(header_text, 'titlebar')

# Create the menu
menu = urwid.Text([
    u'Press (', ('refresh button', u'R'), u') to manually refresh. ',
    u'Press (', ('quit button', u'Q'), u') to quit.'])

# Create the quotes box
quote_text = urwid.Text(u'Press (R) to get your first quote!')
quote_filler = urwid.Filler(quote_text, valign='top', top=1, bottom=1)
v_padding = urwid.Padding(quote_filler, left=1, right=1)
quote_box = urwid.LineBox(v_padding)

# Assemble the widgets
layout = urwid.Frame(header=header, body=quote_box, footer=menu)

def get_update():
    ticker_syms = [t[1] for t in tickers]
    ticker_names = [t[0] for t in tickers]
    results = loads(urlopen('https://www.google.com/finance/info?q=' + ",".join(ticker_syms)).read()[3:])
    s = ""
    for i, r in enumerate(results):
        s += "%s: %s \n" % (ticker_names[i], r['l_cur'])

    return HTMLParser().unescape(s).encode('utf-8')

# Handle key presses
def handle_input(key):
    if key == 'R' or key == 'r':
        refresh(main_loop, '')
    if key == 'Q' or key == 'q':
        raise urwid.ExitMainLoop()

def refresh(_loop, _data):
    quote_box.base_widget.set_text(('getting quote', 'Getting new quote ...'))
    main_loop.draw_screen()
    quote_box.base_widget.set_text(get_update())
    main_loop.set_alarm_in(10, refresh)

main_loop = urwid.MainLoop(layout, palette, unhandled_input=handle_input)
main_loop.set_alarm_in(0, refresh)

# Kick off the program
main_loop.run()
