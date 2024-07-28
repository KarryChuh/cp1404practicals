from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

class ConvertMilesKmApp(App):
    output_km = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, text):
        try:
            miles = float(text)
            kilometers = miles * 1.60934
            self.output_km = f"{kilometers:.5f}"
        except ValueError:
            self.output_km = "0.0"

    def handle_increment(self, text, increment):
        try:
            miles = float(text) + increment
        except ValueError:
            miles = increment
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert(self.root.ids.input_miles.text)

class MainBox(BoxLayout):
    pass

if __name__ == '__main__':
    ConvertMilesKmApp().run()