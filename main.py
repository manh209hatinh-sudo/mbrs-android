from kivy.app import App
from kivy.uix.label import Label

class MustBeReallySuccessfulApp(App):
    def build(self):
        return Label(text="MUST BE REALLY SUCCESSFUL - Android Demo")

if __name__ == "__main__":
    MustBeReallySuccessfulApp().run()
