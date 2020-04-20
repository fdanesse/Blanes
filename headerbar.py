import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class HeaderBar(Gtk.HeaderBar):
    def __init__(self):
        Gtk.HeaderBar.__init__(self)

        self.set_show_close_button(True)
        self.props.title = "Blanes"

        self.show_all()
