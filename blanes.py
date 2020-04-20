import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from headerbar import HeaderBar
#from menubar import MenuBar
#from toolbar import Toolbar
#from scrolledwindow import ScrolledWindow
#from statusbar import Statusbar


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Blanes")

        self.set_default_size(640, 480)

        self.headerbar = HeaderBar()
        self.set_titlebar(self.headerbar)

        #self.menubar = MenuBar()
        #self.toolbar = Toolbar()
        #scrolledwindow = ScrolledWindow()
        #self.statusbar = Statusbar()

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        #self.box.pack_start(self.menubar, False, False, 0)
        #self.box.pack_start(self.toolbar, False, False, 0)
        #self.box.pack_start(scrolledwindow, True, True, 0)
        #self.box.pack_start(self.statusbar, False, False, 0)

        self.add(self.box)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__=="__main__":
    win = MyWindow()
    Gtk.main()