from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import urllib2
class screen1(BoxLayout):
	pass
class ControllerApp(App):
        def build(self):
                return screen1()
if __name__ == '__main__':
        ControllerApp().run()


