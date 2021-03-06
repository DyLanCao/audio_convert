from dearpygui.core import *
from dearpygui.simple import *
from file_oper import file_operation

# callbacks
def hide_menu(sender, data):
    hide_item("Tools")


def show_menu(sender, data):
    show_item("Tools")

def open_file(sender,data):
    print("open file")
    #file_operation.file_read(data)

def close_file(sender,data):
    print("close file")

def save_file(sender,data):
    print("save file")
    
def change_callback(sender, data):
    callback_name=get_item_callback("Show Docs")
    print(callback_name)
    if callback_name == show_docs:
        set_item_callback("Show Docs", show_metrics_call)
    else:
        set_item_callback("Show Docs", show_docs)


def show_docs(sender, data):
    show_documentation()


def show_metrics_call(sender, data):
    show_metrics()


def add_themes(sender, data):
    with menu("Themes", parent="MenuBar"):
        pass
    add_color_picker4("Color Selector", source="color1", parent="Themes")
    add_color_edit4("Color Item", source="color1", parent="Themes")
    show_item("Delete Themes")
    hide_item("Add Themes")


def delete_themes(sender, data):
    delete_item("Themes")
    delete_item("Color Item")
    show_item("Add Themes")
    hide_item("Delete Themes")

with window("Main Window"):
    with menu_bar("MenuBar"):
        with menu("File"):
            add_menu_item("create", callback=show_menu)
            add_menu_item("open", callback=open_file)
            add_menu_item("close", callback=close_file)
            add_menu_item("save", callback=save_file)
            add_menu_item('Change "Show Docs" Callback', callback=change_callback)
            with tooltip('Change "Show Docs" Callback', "tooltip1"):
                add_dummy(width=150)  # this is because the popup doesnt have a width to set
                add_text('this will change the "show Docs" callback to a show metrics callback')
            with menu("Empty Menu"):
                add_menu_item("Nothing")
        with menu("Tools"):
            add_menu_item("Show Docs", callback=show_docs)
            with menu("Add/Remove"):
                add_menu_item("Add Themes", callback=add_themes)
                add_menu_item("Delete Themes", callback=delete_themes)
                hide_item("Delete Themes")
        with menu("Views"):
            add_menu_item("tools", callback=show_docs)
        with menu("Edit"):
            add_menu_item("cuts", callback=show_docs)
        with menu("Help"):
            add_menu_item("Show Docs", callback=show_docs)

    """
    add_text("This menu bar demonstrates:")
    add_text('standard menu bar, menus, and menu items', bullet=True)
    add_text('adding menus to menus', bullet=True)
    add_text('showing and hiding the "Tools menu"', bullet=True)
    add_text("changing the callback of an already existing menu item", bullet=True)
    add_text("adding and deleting menus, menu items, app widgets from a menu item", bullet=True)
    add_text("placing a widget into the menu that controlling another widget on the body of the app", bullet=True)
    add_spacing(count=50)
    """

def start_gui():
    start_dearpygui(primary_window="Main Window")
