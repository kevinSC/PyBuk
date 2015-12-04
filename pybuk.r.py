import urwid
text = urwid.Text('Hello World')
fill = urwid.Filler(text, 'top')
loop = urwid.MainLoop(fill)
loop.run()
