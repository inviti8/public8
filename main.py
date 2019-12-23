from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.lang import Builder
from pathlib import Path
import arweave_com
import app_builder
import file_action
import os
import string
import ntpath

GUI = Builder.load_file("main.kv")
HOME_PATH = str(Path.home())
DRIVES = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

def Dialog(title, content, width, height):
    '''
    Create a dialog with a title, passed content, dimensions
    '''
    return Popup(title=title, content=content,size_hint=(None, None), size=(width, height))

def DriveChooser(button):
    '''
    Dialog With button for each drive
    '''
    app = App.get_running_app()
    container = BoxLayout(orientation='vertical')

    for drive in DRIVES:
        button = AppButton(text=drive, name="DRIVE_BUTTON_" + drive, size_hint=(1, 0.1))
        container.add_widget(button)

    return container

def FileChooser_LoadContent(button):
    '''
    Dialog for choosing Wallet Key File.
    '''
    app = App.get_running_app()

    container = BoxLayout(orientation='vertical')
    app.filechooser = FileChooserIconView(path=app.root.current_drive)
    
    button = AppButton(text='SELECT', name="LOAD_CONTENT_POPUP_BUTTON", size_hint=(1, .2))
    button.selected = app.filechooser.selection
    button.bind(on_press=lambda x: button.LOAD_CONTENT_POPUP_BUTTON_pressed(app.filechooser.selection))

    container.add_widget(app.filechooser)
    container.add_widget(button)

    return container


def FileChooser_LoadWalletKey(button):
    '''
    Dialog for choosing Wallet Key File
    '''
    app = App.get_running_app()

    container = BoxLayout(orientation='vertical')
    app.filechooser = FileChooserIconView(path=app.root.current_drive)
    
    button = AppButton(text='SELECT', name="LOAD_WALLET_KEY_FILE_BUTTON", size_hint=(1, .2))
    button.selected = app.filechooser.selection
    button.bind(on_press=lambda x: button.LOAD_WALLET_KEY_BUTTON_pressed(app.filechooser.selection))

    container.add_widget(app.filechooser)
    container.add_widget(button)

    return container

def FileChooser_Flow(button, next_chooser, next_chooser_text):
    '''
    Handle redirect flow for sile selection
    if multiple drives are available
    '''
    app = App.get_running_app()
    container = None

    if len(DRIVES) > 1:
        container = DriveChooser(button)
        next_container = next_chooser(button)
        app.popup = Dialog("Select Drive:",container, 400, 400)
        app.next_popup = Dialog(next_chooser_text, next_container, 400, 400)

    else:
        container = FileChooser_LoadContent(button)
        app.popup = Dialog(next_chooser_text, container, 400, 400)

    return container

def ValidateContentPath(path):
    result = None
    isPath = os.path.isdir(path)
        
    if isPath:
        result = path
    else:
        fileName = ntpath.basename(path).lower()
        result = path.replace(fileName, "")

    return result

def ValidateWalletKeyPath(path):
    result = None
    file = os.path.isfile(path)
        
    if file:
        fileName = ntpath.basename(path).lower()
        extension = fileName.split(".")
        if "json" in extension:
            result = path

    return result



class TabLayout(TabbedPanel):
    '''
    Tab layout, access via app.root
    '''
    current_drive = StringProperty(HOME_PATH)
    key_file_path = StringProperty(None)
    drivechooser = ObjectProperty(None)
    filechooser = ObjectProperty(None)
    popup = ObjectProperty(None)
    next_popup = ObjectProperty(None)

class AppButton(Button):
    '''
    Handle logic for all app specific buttons
    '''
    app = App.get_running_app()
    filechooser = None

    def LOAD_CONTENT_POPUP_BUTTON_pressed(self, selection_list):
        '''
        Set the content path
        TODO: Validate to onlu accept path
        '''
        if len(selection_list) > 0:
            app = App.get_running_app()
            path = selection_list[0]
            validPath = ValidateContentPath(path)

            if validPath is not None:
                app.root.ids.content_path_text_input.text = validPath
    
    def LOAD_WALLET_KEY_BUTTON_pressed(self, selection_list):
        '''
        Set the wallet key file path, set edit text field
        '''
        if len(selection_list) > 0:
            app = App.get_running_app()
            path = selection_list[0]
            validPath = ValidateWalletKeyPath(path)

            if validPath is not None:
                app.root.ids.wallet_key_text_input.text = validPath

    def on_release(self):
        app = App.get_running_app()

        if self.name is "DEPLOY_APP_BUTTON":
            arweave_com.deploy_app()

        elif self.name is "TEST_APP_BUTTON":
            print("test app")
            file_action.open_test_page()

        elif self.name is "CONTENT_PATH_LOAD_BUTTON":
            print("load content path")
            
            FileChooser_Flow(self, FileChooser_LoadContent, "LOAD CONTENT PATH:")
            app.popup.open()

        elif self.name is "LOAD_CONTENT_POPUP_BUTTON":
            print("content path selected")
            app.popup.dismiss()

        elif self.name is "THEME_LOAD_BUTTON":
            print("load theme")

        elif "DRIVE_BUTTON_" in self.name:
            '''
            Catch the drive button catch pass to current drive
            reassign app.next_popup to app.popup
            '''
            drive = self.text + str(os.sep)
            app.filechooser.path = drive
            app.root.current_drive = drive
            app.popup.dismiss()
            app.popup = app.next_popup
            app.popup.open()

        elif self.name is "LOAD_WALLET_KEY_BUTTON":
            '''
            If there are multiple drives prompt choose drive,
            else open dialog in home directory
            '''
            FileChooser_Flow(self, FileChooser_LoadWalletKey, "LOAD WALLET KEY FILE")
            app.popup.open()

        elif self.name is "LOAD_WALLET_KEY_FILE_BUTTON":
            print("wallet key file selected")
            app.popup.dismiss()     

        elif self.name is "CREATE_WALLET_KEY_BUTTON":
            print("create wallet key")

        elif self.name is "FORGET_WALLET_KEY_BUTTON":
            print("forget wallet key")

        pass

class AppTextInput(TextInput):
    '''
    Handle text inputs
    '''
    def on_text_input_change(self):
        if self.name is "TITLE_TEXT_INPUT":
            app_builder.ARWEAVE_APP_TITLE = self.text

        elif self.name is "AUTHOR_TEXT_INPUT":
            app_builder.AUTHOR = self.text
            
        elif self.name is "REFERNCES_TEXT_INPUT":
            app_builder.REFERENCES = self.text

class ConsoleTextInput(TextInput):
    '''
    Handle console text inputs
    '''
    def on_kv_post(self, input):
        print("on network info!")
        # info = arweave_com.network_info()
        # host = str(info["host"])
        # port = str(info["port"])
        # self.text = "host: " + host + "    port: " + port 

    def on_text_input_change(self):
        if self.name is "TITLE_TEXT_INPUT":
            app_builder.ARWEAVE_APP_TITLE = self.text

class AppSpinner(Spinner):
    '''
    Handle the dropdowns
    '''
    def on_kv_post(self, input):
        if self.name is "TEMPLATE_SPINNER":
            file_action.TEMPLATE = self.text

    def on_spinner_change(self):
        print("on spinner change")

        if self.name is "TYPE_SPINNER":
            app_builder.ARWEAVE_APP_TYPE = self.text

        elif self.name is "CONTENT_TYPE_SPINNER":
            app_builder.CONTENT_TYPE = self.text
        
        elif self.name is "THEME_SPINNER":
            app_builder.THEME = self.text

        elif self.name is "TEMPLATE_SPINNER":
            file_action.TEMPLATE = self.text

        elif self.name is "SIGNATURE_SPINNER":
            if self.text is "ON":
                app_builder.SIGN_APP = True
            else:
                app_builder.SIGN_APP = False

    
class TabbedPanelApp(App):

    def build(self):
        self.title = 'PUBLIC8'

        return TabLayout()


if __name__ == '__main__':
    TabbedPanelApp().run()