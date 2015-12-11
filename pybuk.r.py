import urwid


def exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue')]
welcome = urwid.Text('Welcome to Pybuk')
body = urwid.Text('this is the body')
bodyFrame = urwid.AttrMap(body, 'streak')
fill1 = urwid.Filler(bodyFrame)
otherText = urwid.Text('other text')
welcomeframe = urwid.AttrMap(welcome, 'banner')
otherframe = urwid.AttrMap(otherText, 'bg')
gFrame = urwid.Frame(urwid.SolidFill('/'), header=fill1, footer=otherframe)
loop = urwid.MainLoop(gFrame, unhandled_input=exit)
loop.run()
