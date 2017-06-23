import urwid
from urllib2 import urlopen
from HTMLParser import HTMLParser
from simplejson import loads
import thread, logging
from time import sleep


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
    joke_json = loads(urlopen('https://www.google.com/finance/info?q=HKG:0968').read()[3:])
    return HTMLParser().unescape('Xinyi Solar:'+ joke_json[0]['l_cur']).encode('utf-8')

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
