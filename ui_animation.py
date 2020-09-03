from kivy.animation import Animation


def on_button_press(widget):
    anim = Animation(opacity=0.5, duration=0.1)
    anim += Animation(opacity=1)
    anim.start(widget)

def tab_on(tab):
    if tab.active == False:
        anim = Animation(opacity=1, duration=0.3)
        anim.start(tab)
        tab.active = True

def tab_off(tab):
    if tab.active == True:
        anim = Animation(opacity=0.5, duration=0.3)
        anim.start(tab)
        tab.active = False