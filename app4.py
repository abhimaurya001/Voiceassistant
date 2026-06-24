from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.num1 = TextInput(hint_text="First Number")
        self.num2 = TextInput(hint_text="Second Number")

        btn = Button(text="Add")
        btn.bind(on_press=self.add_numbers)

        self.result = Label(text="Result")

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)
        layout.add_widget(btn)
        layout.add_widget(self.result)

        return layout

    def add_numbers(self, instance):
        try:
            result = float(self.num1.text) + float(self.num2.text)
            self.result.text = f"Result: {result}"
        except:
            self.result.text = "Invalid Input"

CalculatorApp().run()