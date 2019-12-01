from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.button import Button
from kivy.lang import Builder



GUI = Builder.load_file("main.kv")
class TabLayout(TabbedPanel):
    pass

class AppButton(Button):

    def on_press(self):
        print(self.name)
        pass



class TabbedPanelApp(App):
    def build(self):
        return TabLayout()


if __name__ == '__main__':
    TabbedPanelApp().run()