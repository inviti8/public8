from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
import arweave_com
import app_builder

GUI = Builder.load_file("main.kv")


class TabLayout(TabbedPanel):
    
    pass

class AppButton(Button):

    def on_press(self):
        if self.name is "DEPLOY_APP":
            arweave_com.deploy_app()
        pass

class AppTextInput(TextInput):
    print(TextInput)

    def on_text_validate(self):
        print(self.text)

class AppSpinner(Spinner):
    print(Spinner)

    def on_release(self):
        print(self.text)


        



class TabbedPanelApp(App):
    def build(self):
        return TabLayout()


if __name__ == '__main__':
    TabbedPanelApp().run()