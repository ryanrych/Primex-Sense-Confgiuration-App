import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

class WindowManager(ScreenManager):
    pass



class WelcomeInterface(Widget):

    def facilitiesBox(self):
        if self.facilities.active:
            self.facilities.active = False
        else:
            self.facilities.active = True

    def biomedBox(self):
        if self.biomed.active:
            self.biomed.active = False
        else:
            self.biomed.active = True

    def clinicalServicesBox(self):
        if self.clinicalServices.active:
            self.clinicalServices.active = False
        else:
            self.clinicalServices.active = True

    def pharmacyBox(self):
        if self.pharmacy.active:
            self.pharmacy.active = False
        else:
            self.pharmacy.active = True

    def nursingBox(self):
        if self.nursing.active:
            self.nursing.active = False
        else:
            self.nursing.active = True

    def labBox(self):
        if self.lab.active:
            self.lab.active = False
        else:
            self.lab.active = True

    def itBox(self):
        if self.it.active:
            self.it.active = False
        else:
            self.it.active = True

    def cSuiteBox(self):
        if self.cSuite.active:
            self.cSuite.active = False
        else:
            self.cSuite.active = True

class WelcomeBackground(Widget):
    pass

class WelcomeScreen(Screen):
    pass



class PackageSelectionInterface(Widget):
    def showOptions(self):
        self.spacer.size_hint_y = .2
        self.options.size_hint_y = .25

class PackageSelectionBackground(Widget):
    pass

class PackageSelectionScreen(Screen):
    pass



class SitePrioritiesInterface(Widget):
    pass

class SitePrioritiesBackground(Widget):
    pass

class SitePrioritiesScreen(Screen):
    pass



class Package1Interface(Widget):
    pass

class Package1Background(Widget):
    pass

class Package1Screen(Screen):
    pass



class Package2Interface(Widget):
    pass

class Package2Background(Widget):
    pass

class Package2Screen(Screen):
    pass



class Package3Interface(Widget):
    pass

class Package3Background(Widget):
    pass

class Package3Screen(Screen):
    pass



class Package4Interface(Widget):
    pass

class Package4Background(Widget):
    pass

class Package4Screen(Screen):
    pass



class SenseConfiguration(App):
    def build(self):
        Window.size=(850,650)
        self.icon = "primex logo.png"
        self.title = "Sense Configuration"
        return Builder.load_file("Style.kv")

if __name__=="__main__":
    SenseConfiguration().run()