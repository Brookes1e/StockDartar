from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from  kivy.uix.switch import Switch
from kivy.uix.label import Label

class MySwitch(Switch):

    def __init__(self, name):
        super(MySwitch,self).__init__()
        self.name = name

    def on_active(self,instance,value):
        if value:
            print "%s is ON" % self.name
        else:
            print "%s is OFF" % self.name

class MySwitchLabel(Label):
    
    def __init__(self, text):
        super(MySwitchLabel,self).__init__()
        self.text = text
        self.font_size = 20


class MyBoxLayout(BoxLayout):

    def __init__(self):
        super(MyBoxLayout,self).__init__()
        self.orientation = 'vertical'

class MyApp(App, MyBoxLayout):

    def build(self):
        self.title = 'Indicator Selection'
        self.main_title = MyBoxLayout.add_widget(self,Label(text='Indicators', font_size = 50))
        self.switch_title_1 = MyBoxLayout.add_widget(self, MySwitchLabel(text='Moving Average'))
        self.switch_1 = MyBoxLayout.add_widget(self, MySwitch('Moving Average'))
        self.switch_title_2 = MyBoxLayout.add_widget(self, MySwitchLabel(text='MACD'))
        self.switch_2 = MyBoxLayout.add_widget(self, MySwitch('MACD'))
        self.switch_title_3 = MyBoxLayout.add_widget(self, MySwitchLabel(text='Stochcastics'))
        self.switch_3 = MyBoxLayout.add_widget(self, MySwitch( 'Stochcastics'))
        return self

if __name__ == '__main__':
    MyApp().run()