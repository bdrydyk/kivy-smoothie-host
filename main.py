import kivy

from kivy.app import App

from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.app import App
from kivy.lang import Builder

#Builder.load_file('kbd.kv')

Builder.load_string('''
# a template Butt of type Button
<Butt@Button>
    font_size: 16
    on_press: self.parent.parent.do_action(self.text)

<KbdWidget>:
	display: entry
    rows: 9
    padding: 10
    spacing: 10

    BoxLayout:
	    TextInput:
	    	id: entry
	    	multiline: False
	    	font_size: 16
	    	on_text_validate: self.parent.parent.handle_input(self.text)

	BoxLayout:
        Butt:
        	text: 'G'
        Butt:
        	text: 'M'
        Butt:
        	text: 'T'
        Butt:
        	text: 'F'

    BoxLayout:
        Butt:
        	text: 'X'
        Butt:
        	text: 'Y'
        Butt:
        	text: 'Z'
        Butt:
        	text: 'E'

	BoxLayout:
        Butt:
        	text: 'A'
        Butt:
        	text: 'B'
        Butt:
        	text: 'C'
        Butt:
    		text: 'D'
        Butt:
        	text: 'H'
        Butt:
        	text: 'I'
        Butt:
        	text: 'J'
        Butt:
        	text: 'K'

    BoxLayout:
        Butt:
        	text: 'L'
        Butt:
        	text: 'P'
        Butt:
        	text: 'Q'
        Butt:
        	text: 'R'
        Butt:
        	text: 'S'
        Butt:
        	text: 'U'
        Butt:
        	text: 'V'
        Butt:
        	text: 'W'

    BoxLayout:
        Butt:
            text: '1'
        Butt:
            text: '2'
        Butt:
            text: '3'
        Butt:
            text: '4'

    BoxLayout:
        Butt:
            text: '5'
        Butt:
            text: '6'
        Butt:
            text: '7'
        Butt:
            text: '8'

    BoxLayout:
        Butt:
            text: '9'
        Butt:
            text: '0'
        Butt:
            text: '.'
        Butt:
            text: '-'

    BoxLayout:
        Butt:
        	text: 'BS'
        Butt:
        	text: 'Send'

<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
    	text: root.text

<MainWindow>:
	orientation: 'horizontal'

	ScrollableLabel:
		text: kbd_widget.log

	KbdWidget:
		id: kbd_widget

''')

class ScrollableLabel(ScrollView):
	text= StringProperty()

class KbdWidget(GridLayout):
	log= StringProperty()

	def do_action(self, key):
		print("Key " + key)
		if key == 'Send':
			print("Sending " + self.display.text)
			self.log += self.display.text + '\n'
			self.display.text = ''
		elif key == 'BS':
			self.display.text = self.display.text[:-1]
		else:
			self.display.text += key

	def handle_input(self, s):
		self.log += self.display.text + '\n'
		self.display.text = ''

class MainWindow(BoxLayout):
	pass

class KPronterfaceApp(App):
	def build(self):
		return MainWindow()

if __name__ == "__main__":
	KPronterfaceApp().run()



