import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

class WindowManager(ScreenManager):
    pass



class WelcomeInterface(Widget):
    pass

class WelcomeBackground(Widget):
    pass

class WelcomeScreen(Screen):
    pass



class PackageSelectionInterface(Widget):
    pass

class PackageSelectionBackground(Widget):
    pass

class PackageSelectionScreen(Screen):
    pass



class SenseConfiguration(App):
    def build(self):
        Window.size=(850,650)
        self.icon = "primex logo.png"
        self.title = "Sense Configuration"
        return Builder.load_file("Style.kv")

if __name__=="__main__":
    SenseConfiguration().run()