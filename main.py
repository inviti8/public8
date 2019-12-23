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
import arweave_com
import app_builder
import file_action
import os

GUI = Builder.load_file("main.kv")

def Dialog(title, content, width, height):
        return Popup(title=title, content=content,size_hint=(None, None), size=(width, height))

def FileChooser_LoadWalletKey(button):
    container = BoxLayout(orientation='vertical')
    App.filechooser = FileChooserIconView()
    
    button = AppButton(text='SELECT', name="LOAD_WALLET_KEY_FILE_BUTTON", size_hint=(1, .2))
    button.selected = App.filechooser.selection
    button.bind(on_release=lambda x: button.LOAD_WALLET_KEY_BUTTON_selected(App.filechooser.selection))

    container.add_widget(App.filechooser)
    container.add_widget(button)

    return container

class TabLayout(TabbedPanel):
    pass

class AppButton(Button):
    filechooser = None
    
    def LOAD_WALLET_KEY_BUTTON_selected(self, selection_list):
        print(App.filechooser.selection)

    def on_press(self):
        if self.name is "DEPLOY_APP_BUTTON":
            arweave_com.deploy_app()

        elif self.name is "EST_APP_BUTTON":
            print("test app")
            file_action.open_test_page()

        elif self.name is "CONTENT_PATH_LOAD_BUTTON":
            print("load content path")

        elif self.name is "THEME_LOAD_BUTTON":
            print("load theme")

        elif self.name is "GENERATE_KEY_BUTTON":
            print("generate signature keys")
        
        elif self.name is "LOAD_KEY_BUTTON":
            print("load signature keys")

        elif self.name is "LOAD_WALLET_KEY_BUTTON":
            print("load wallet key")
            container = FileChooser_LoadWalletKey(self)

            App.popup = Dialog("Load Wallet Key Path",container, 400, 400)
            App.popup.open()

        elif self.name is "LOAD_WALLET_KEY_FILE_BUTTON":
            print("this works")
            App.popup.dismiss()
            

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

        self.key_file_path = None

        self.filechooser = None
        self.popup = None

    # def set_filechooser(self, filechooser):
    #     self.filechoooser(filechooser)

        return TabLayout()


if __name__ == '__main__':
    TabbedPanelApp().run()