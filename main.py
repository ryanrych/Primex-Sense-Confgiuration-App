import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.clock import Clock

from SitePriorities import SitePriorities

class WindowManager(ScreenManager):
    pass



sitePriorities = SitePriorities()
package = ""



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

    def selectPackage(self):
        global sitePriorities
        global package

        basicPoints = 0
        preferredPoints = 0

        if sitePriorities.auditAgencies != [] and sitePriorities.auditPrepTime != -1:

            if sitePriorities.lossFrequency == -1 and sitePriorities.averageLoss == -1 and not sitePriorities.primexValue and sitePriorities.oneVueDepartments == -1 and sitePriorities.oneVueTeamSize == -1 and sitePriorities.oneVueTime == -1 and not sitePriorities.experiencedTeam and sitePriorities.alertsPerWeek == -1 and sitePriorities.laborRate == 15 and sitePriorities.reportsPerWeek == -1 and sitePriorities.managementRate == 50 and sitePriorities.otherPriorities == "":
                basicPoints += 1

        if sitePriorities.lossFrequency != -1 and sitePriorities.averageLoss != -1:

            if sitePriorities.lossFrequency in range(0,3):
                basicPoints +=1
            else:
                preferredPoints += 1

        if sitePriorities.primexValue:
            preferredPoints += 1
        else:
            basicPoints += 1

        if sitePriorities.oneVueTeamSize == 1:

            if sitePriorities.oneVueTime in range(0,4):
                preferredPoints += 1
            else:
                basicPoints += 1
        elif sitePriorities.oneVueTeamSize > 1:

            if sitePriorities.oneVueTime == 0:
                oneVueTimeExact = .01
            elif sitePriorities.oneVueTime == 1:
                oneVueTimeExact = .11
            elif sitePriorities.oneVueTime == 1:
                oneVueTimeExact = .26
            else:
                oneVueTimeExact = .5

            katiesNumber = sitePriorities.oneVueTeamSize / oneVueTimeExact

            if katiesNumber > .5:
                preferredPoints += 1
            else:
                basicPoints += 1

        if sitePriorities.experiencedTeam:
            basicPoints += 1
        else:
            preferredPoints += 1

        #What is manage staff compliance?

        if basicPoints > preferredPoints:
            package = "Basic"
        else:
            package = "Preferred"

    def goToPackageScreen(self):
        global package

        sm = App.get_running_app().root

        if package == "Basic":
            sm.current = "Package1Screen"

        elif package == "Preferred":
            sm.current = "Package3Screen"

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



class AuditsInterface(Widget):

    def confirmAnswers(self):
        global sitePriorities

        for layout in self.ids.buttonList.children[1:-1]:
            if layout.children[1].selected:
                sitePriorities.auditAgencies.append(layout.children[1].text)

        if self.ids.buttonList.children[0].children[1].text != "":
            for agency in self.ids.buttonList.children[0].children[1].text.split(","):
                sitePriorities.auditAgencies.append(agency)

            if self.ids.auditPrepTimeInput.text == "":
                self.errorMessage()
                Clock.schedule_once(self.errorMessageEnd, 3)

        try:
            sitePriorities.auditPrepTime = float(self.ids.auditPrepTimeInput.text)
            App.get_running_app().root.current = "SitePrioritiesScreen"
        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Please enter a number for your audit preparation time"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

class AuditsBackground(Widget):
    pass

class AuditsScreen(Screen):
    pass



class LossInterface(Widget):

    def clearLossSelection(self):
        self.ids.lossButton0.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.lossButton1.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.lossButton2.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.lossButton3.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.lossButton4.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.lossButton5.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.lossButton6.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)

    def clearValueSelection(self):
        self.ids.valueButton0.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.valueButton1.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)

    def confirmAnswers(self):
        global sitePriorities

        if self.ids.lossButtonList.selected != -1:
            sitePriorities.lossFrequency = self.ids.lossButtonList.selected

            if self.ids.valueButtonList.selection != -1:
                sitePriorities.primexValue = not self.ids.valueButtonList.selection

                try:
                    sitePriorities.averageLoss = float(self.ids.averageLossInput.text)
                    App.get_running_app().root.current = "SitePrioritiesScreen"
                except:
                    self.errorMessageStart()
                    Clock.schedule_once(self.errorMessageEnd, 3)

            else:
                self.errorMessageStart()
                Clock.schedule_once(self.errorMessageEnd, 3)

        else:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Please Answer All Sections"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

class LossBackground(Widget):
    pass

class LossScreen(Screen):
    pass



class EfficiencyInterface(Widget):

    def clearTeamButtons(self):
        self.ids.teamButton0.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.teamButton1.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)

    def clearFrequencyButtons(self):
        self.ids.frequencyButton0.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.frequencyButton1.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.frequencyButton2.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.frequencyButton3.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)

    def clearExperienceButtons(self):
        self.ids.experienceButton0.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.experienceButton1.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)

    def confirmAnswers(self):
        global sitePriorities

        sitePriorities.oneVueDepartments = int(self.ids.oneVueDepartmentsInput.text)

        if self.ids.teamButtons.selected == 1:
            sitePriorities.oneVueTeamSize = int(self.ids.teamSizeInput.text)
        else:
            sitePriorities.oneVueTeamSize = 1

        sitePriorities.oneVueTime = self.ids.frequencyButtons.selected
        sitePriorities.experiencedTeam = not self.ids.experienceButtons.selected
        sitePriorities.alertsPerWeek = int(self.ids.alertsPerWeekInput.text)

        if self.ids.laborRateInput.text != "":
            sitePriorities.laborRate = int(self.ids.laborRateInput.text)

        sitePriorities.reportsPerWeek = int(self.ids.reportsPerWeekInput.text)

        if self.ids.managementRateInput.text != "":
            sitePriorities.managementRate = int(self.ids.managementRateInput.text)

class EfficiencyBackground(Widget):
    pass

class EfficiencyScreen(Screen):
    pass



class OtherInterface(Widget):

    def confirmAnswers(self):
        global sitePriorities

        sitePriorities.otherPriorities = self.ids.criteriaInput.text

class OtherBackground(Widget):
    pass

class OtherScreen(Screen):
    pass



class SenseConfiguration(App):
    def build(self):
        Window.size=(850,650)
        self.icon = "favicon.png"
        self.title = "Sense Configuration"
        return Builder.load_file("Style.kv")

if __name__=="__main__":
    SenseConfiguration().run()