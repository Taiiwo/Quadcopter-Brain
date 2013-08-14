from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import urllib2
class main(BoxLayout):
	def dostuff(self):
		try:
			self.article.text = urllib2.urlopen('http://thescoop.io/ots.php?to_sum=' + self.url.text + '&ratio=50').read()
		except:
			self.article.text = 'Invalid URL'
		#self.article.text = self.input.text
		return self.url.text
class MainApp(App):
	def build(self):
		return main()
if __name__ == '__main__':
	MainApp().run()
