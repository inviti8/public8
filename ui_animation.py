from kivy.animation import Animation


def on_button_press(widget):
    anim = Animation(opacity=0.5, duration=0.1)
    anim += Animation(opacity=1)
    anim.start(widget)

def tab_on(tab):
    anim = Animation(opacity=1, duration=0.3)
    anim.start(tab)

def tab_off(tab):
    anim = Animation(opacity=0.5, duration=0.3)
    anim.start(tab)