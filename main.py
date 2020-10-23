import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

from SitePriorities import SitePriorities
from Hardware import Hardware

from datetime import datetime

class WindowManager(ScreenManager):
    pass



sitePriorities = SitePriorities()
siteHardware = Hardware()
hardwareType = ""
package = ""
onboarding = ""

#Algorithm for reading the lookup table into a 2d list
lookupTable = []

file = open("LookUpTable.txt","r")

for x in file:
    lookupTable.append(x.split(" "))

file.close()



class WelcomeInterface(Widget):

    def facilitiesBoxClick(self):
        if self.ids.facilitiesBox.active:
            self.ids.facilitiesBox.active = False
        else:
            self.ids.facilitiesBox.active = True

    def biomedBoxClick(self):
        if self.ids.biomedBox.active:
            self.ids.biomedBox.active = False
        else:
            self.ids.biomedBox.active = True

    def clinicalServicesBoxClick(self):
        if self.ids.clinicalServicesBox.active:
            self.ids.clinicalServicesBox.active = False
        else:
            self.ids.clinicalServicesBox.active = True

    def pharmacyBoxClick(self):
        if self.ids.pharmacyBox.active:
            self.ids.pharmacyBox.active = False
        else:
            self.ids.pharmacyBox.active = True

    def nursingBoxClick(self):
        if self.ids.nursingBox.active:
            self.ids.nursingBox.active = False
        else:
            self.ids.nursingBox.active = True

    def labBoxClick(self):
        if self.ids.labBox.active:
            self.ids.labBox.active = False
        else:
            self.ids.labBox.active = True

    def itBoxClick(self):
        if self.ids.itBox.active:
            self.ids.itBox.active = False
        else:
            self.ids.itBox.active = True

    def cSuiteBoxClick(self):
        if self.ids.cSuiteBox.active:
            self.ids.cSuiteBox.active = False
        else:
            self.ids.cSuiteBox.active = True

    def checkAnswers(self):
        if self.ids.siteNameInput.text == "" or self.ids.bedSizeInput == "" or self.ids.keySiteContactInput == "":
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)
        else:
            App.get_running_app().root.current = "SitePrioritiesScreen"

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Please Answer All Sections"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

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
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)
        else:
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

        try:
            sitePriorities.oneVueDepartments = int(self.ids.oneVueDepartmentsInput.text)
        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)
            return

        if self.ids.teamButtonList.selected == 1:
            sitePriorities.oneVueTeamSize = int(self.ids.teamSizeInput.text)
        else:
            sitePriorities.oneVueTeamSize = 1

        if self.ids.frequencyButtonList.selected != -1:
            sitePriorities.oneVueTime = self.ids.frequencyButtonList.selected

            if self.ids.experienceButtonList.selected != -1:
                sitePriorities.experiencedTeam = not self.ids.experienceButtonList.selected
                try:
                    sitePriorities.alertsPerWeek = int(self.ids.alertsPerWeekInput.text)
                except:
                    self.errorMessageStart()
                    Clock.schedule_once(self.errorMessageEnd, 3)
                    return

            else:
                self.errorMessageStart()
                Clock.schedule_once(self.errorMessageEnd, 3)
                return

        else:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)
            return

        if self.ids.laborRateInput.text != "":
            sitePriorities.laborRate = int(self.ids.laborRateInput.text)

        try:
            sitePriorities.reportsPerWeek = int(self.ids.reportsPerWeekInput.text)
        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)
            return

        if self.ids.managementRateInput.text != "":
            try:
                sitePriorities.managementRate = int(self.ids.managementRateInput.text)
            except:
                self.errorMessageStart()
                Clock.schedule_once(self.errorMessageEnd, 3)
                return

        App.get_running_app().root.current = "SitePrioritiesScreen"

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Please Answer All Sections"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

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



class FeaturesInterface(Widget):
    def clearAlertsList(self):
        self.ids.alertsButton0.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.alertsButton1.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)

    def clearAssetsList(self):
        self.ids.assetButton0.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.assetButton1.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.assetButton2.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.assetButton3.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)

    def clearSettingsList(self):
        self.ids.settingsButton0.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.settingsButton1.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.settingsButton2.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)
        self.ids.settingsButton3.background_color = (0.3803921568627451, 0.6784313725490196, 0.2627450980392157, 1)

    def confirmAnswers(self):

        if self.ids.assetButtons.selected == -1 or self.ids.settingsButtons.selected == -1:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)
        else:
            App.get_running_app().root.current = "SensorSubscriptionScreen"

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Please Answer All Sections"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

class FeaturesBackground(Widget):
    pass

class FeaturesScreen(Screen):
    pass



class SelfStartOnboardingInterface(Widget):

    def setOnboarding(self):
        global onboarding

        onboarding = "Self-Start"

class SelfStartOnboardingBackground(Widget):
    pass

class SelfStartOnboardingScreen(Screen):
    pass



class WhiteGloveOnboardingInterface(Widget):

    def setOnboarding(self):
        global onboarding

        onboarding = "White Glove"

class WhiteGloveOnboardingBackground(Widget):
    pass

class WhiteGloveOnboardingScreen(Screen):
    pass



class SensorSubscriptionInterface(Widget):

    def setHardware(self):
        global hardwareType
        hardwareType = "Subscription"

class SensorSubscriptionBackground(Widget):
    pass

class SensorSubscriptionScreen(Screen):
    pass



class SensorPurchaseInterface(Widget):

    def setHardware(self):
        global hardwareType
        hardwareType = "Purchase"

class SensorPurchaseBackground(Widget):
    pass

class SensorPurchaseScreen(Screen):
    pass




class SensorHardwareInterface(Widget):

    def setSiteInfo(self):
        sm = App.get_running_app().root
        screen = sm.get_screen("WelcomeScreen")

        self.ids.siteName.text = screen.ids.background.ids.interface.ids.siteNameInput.text
        self.ids.bedSize.text = screen.ids.background.ids.interface.ids.bedSizeInput.text

    def setHardwareData(self):
        global siteHardware

        siteHardware.t101=int(self.ids.t101Input.text)
        siteHardware.t102=int(self.ids.t102Input.text)
        siteHardware.a100=int(self.ids.a100Input.text)
        siteHardware.a120=int(self.ids.a120Input.text)
        siteHardware.e121=int(self.ids.e121Input.text)
        siteHardware.e122=int(self.ids.e122Input.text)
        siteHardware.e123=int(self.ids.e123Input.text)

    def confirmAnswers(self):
        try:
            int(self.ids.t101Input.text)
            int(self.ids.t102Input.text)
            int(self.ids.a100Input.text)
            int(self.ids.a120Input.text)
            int(self.ids.e121Input.text)
            int(self.ids.e122Input.text)
            int(self.ids.e123Input.text)
            self.setHardwareData() #data is cleared to move on
            App.get_running_app().root.current = "SummaryScreen"
        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd,3)

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Invalid Answer"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

class SensorHardwareBackground(Widget):
    pass

class SensorHardwareScreen(Screen):
    pass


# The following 5 screens are unfinished and to be implemented later

class ProbeDetailsInterface(Widget):

    def checkAnswers(self):

        try:
            if int(self.ids.t101ACInput.text) + int(self.ids.t101POEInput.text) != int(self.ids.t101Input.text) or int(self.ids.t102ACInput.text) + int(self.ids.t102POEInput.text) != int(self.ids.t102Input.text):
                raise Exception()

            if self.ids.primexProbesCB.active:
                if self.ids.primexProbesInput.text == "":
                    int(self.ids.primexProbesInput.text)
                    raise Exception()

            if self.ids.cryogenicProbesCB.active:
                if self.ids.cryogenicProbesInput.text == "":
                    raise Exception()

            if self.ids.glycolCB.active:
                if self.ids.glycolInput.text == "":
                    raise Exception()

            if self.ids.waxCB.active:
                if self.ids.waxInput.text == "":
                    raise Exception()

            if self.ids.noneCB.active:
                if self.ids.noneInput.text == "":
                    raise Exception()

            if self.ids.probesEnteredInput.text != self.ids.probesNeededInput.text:
                raise Exception()

            if self.ids.buffersEnteredInput.text != self.ids.buffersNeededInput.text:
                raise Exception()

            App.get_running_app().root.current = "PowerSupplyScreen"

        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Invalid Input"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

    def fillDefaultAnswers(self):
        self.ids.t101Input.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.t101Input.text
        self.ids.t102Input.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.t102Input.text
        self.ids.t101ACInput.text = self.ids.t101Input.text
        self.ids.t102ACInput.text = self.ids.t102Input.text
        self.ids.t101POEInput.text = "0"
        self.ids.t102POEInput.text = "0"
        self.ids.probesNeededInput.text = str(int(self.ids.t101Input.text) + (int(self.ids.t102Input.text) * 2))

class ProbeDetailsBackground(Widget):
    pass

class ProbeDetailsScreen(Screen):
    pass



class PowerSupplyInterface(Widget):

    def checkAnswers(self):
        try:
            if self.ids.powerSuppliesInput.text == "":
                raise Exception()
            int(self.ids.powerSuppliesInput.text)
        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)

        App.get_running_app().changeDetailsScreens()


    def errorMessageStart(self):
        self.ids.errorMessage.text = "Invalid Input"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

    def fillDefaultAnswers(self):
        self.ids.powerSuppliesInput.text = str(int(App.get_running_app().root.get_screen("ProbeDetailsScreen").ids.background.ids.interface.ids.t101Input.text) + int(App.get_running_app().root.get_screen("ProbeDetailsScreen").ids.background.ids.interface.ids.t102Input.text))

class PowerSupplyBackground(Widget):
    pass

class PowerSupplyScreen(Screen):
    pass



class TempHumidDetailsInterface(Widget):

    def checkAnswers(self):
        try:
            if int(self.ids.sensorsInput.text) != int(self.ids.acInput.text):
                raise Exception()

            int(self.ids.powerSupplyInput.text)

            App.get_running_app().changeDetailsScreens()
        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Invalid Input"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

    def fillDefaultAnswers(self):
        self.ids.sensorsInput.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.a100Input.text
        self.ids.acInput.text = self.ids.sensorsInput.text
        self.ids.powerSupplyInput.text = self.ids.sensorsInput.text

class TempHumidDetailsBackground(Widget):
    pass

class TempHumidDetailsScreen(Screen):
    pass



class PressureDetailsInterface(Widget):

    def fillDefaultAnswers(self):
        self.ids.sensorsInput.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.a120Input.text
        self.ids.acInput.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.a120Input.text
        self.ids.totalNeeded.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.a120Input.text

    def checkAnswers(self):

        try:

            if int(self.ids.acInput.text) + int(self.ids.poeInput.text) != int(self.ids.sensorsInput.text):
                raise Exception()

            if self.ids.installationCB.active:
                int(self.ids.installationInput.text)

            if self.ids.noInstallationCB.active:
                int(self.ids.noInstallationInput.text)

            if self.ids.totalEntered.text != self.ids.totalNeeded.text:
                raise Exception()

            App.get_running_app().changeDetailsScreens()

        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Invalid Input"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""


class PressureDetailsBackground(Widget):
    pass

class PressureDetailsScreen(Screen):
    pass



class LeakDetailsInterface(Widget):

    def fillDefaultAnswers(self):
        self.ids.e121Input.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.e121Input.text
        self.ids.e122Input.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.e122Input.text
        self.ids.e123Input.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.e123Input.text

        self.ids.e121ACInput.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.e121Input.text
        self.ids.e122ACInput.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.e122Input.text
        self.ids.e123ACInput.text = App.get_running_app().root.get_screen("SensorHardwareScreen").ids.background.ids.interface.ids.e123Input.text

    def checkAnswers(self):

        try:
            if int(self.ids.e121ACInput.text) + int(self.ids.e121POEInput.text) != int(self.ids.e121Input.text):
                raise Exception()

            if int(self.ids.e122ACInput.text) + int(self.ids.e122POEInput.text) != int(self.ids.e122Input.text):
                raise Exception()

            if int(self.ids.e123ACInput.text) + int(self.ids.e123POEInput.text) != int(self.ids.e123Input.text):
                raise Exception()

            if self.ids.additionalSensorsCB.active:
                int(self.ids.additionalSensorsInput.text)

        except:
            self.errorMessageStart()
            Clock.schedule_once(self.errorMessageEnd, 3)

    def errorMessageStart(self):
        self.ids.errorMessage.text = "Invalid Input"

    def errorMessageEnd(self, dt):
        self.ids.errorMessage.text = ""

class LeakDetailsBackground(Widget):
    pass

class LeakDetailsScreen(Screen):
    pass



class SummaryInterface(Widget):

    def fillSiteInformation(self):
        global package
        global onboarding
        global siteHardware
        global hardwareType

        pricePerPoint = self.calculatePricePerMonitoringPoint()

        self.ids.packageButton.text = "Package Selection Summary:\n%s" % (package)
        self.ids.onboardingButton.text = "Onboarding Selection Summary:\n%s" % (onboarding)
        self.ids.hardwareButton.text = "Sensor Hardware Summary:\n%s" % (hardwareType)

        if hardwareType == "Subscription":
            self.ids.priceLayout.visible = False
        else:
            self.ids.priceLayout.visible = True

        self.ids.totalPointsInput.text = str(siteHardware.totalPoints)

        softwarePrice = siteHardware.totalPoints * pricePerPoint
        hardwarePrice = (siteHardware.t101 * 446) + (siteHardware.t102 * 605) + (siteHardware.a100 * 315) + (siteHardware.a120 * 749) + (siteHardware.e121 * 304) + (siteHardware.e122 * 338) + (siteHardware.e123 * 439)

        self.ids.totalPriceInput.text = "$" + str(softwarePrice)
        self.ids.hardwarePriceInput.text = "$" + str(hardwarePrice)

        if onboarding == "Self-Start":
            onboardingPrice = 5600
            self.ids.onboardingPriceInput.text = "$5,600"
        else:
            onboardingPrice = 18750
            self.ids.onboardingPriceInput.text = "$18,750"

        self.ids.initialPriceInput.text = "$" + str(softwarePrice + onboardingPrice)
        self.ids.futurePriceInput.text = "$" + str(softwarePrice)

    def calculatePricePerMonitoringPoint(self):
        global package
        global siteHardware
        global lookupTable

        totalPoints = siteHardware.t101 + siteHardware.a120 + siteHardware.e121 + siteHardware.e122 + 2 * (siteHardware.t102 + siteHardware.a100 + siteHardware.e123)
        siteHardware.totalPoints = totalPoints

        #this loop sets the correct row of the lookup table (rounds points up to nearest 100 or to 50)
        lookupRow = 0
        if totalPoints > 50:
            for i in range(1, 21):
                if totalPoints <= i * 100:
                    i += 1
                    break
                else:
                    totalPoints += 1

        #set lookup column based on the site package
        if package == "Basic":
            lookupColumn = 0
        elif package == "Advanced":
            lookupColumn = 1
        else:
            lookupColumn = 2

        #remove dollar sign and return float value of the price
        return float(lookupTable[lookupRow][lookupColumn][1:])

    def changeHardwareButton(self):
        if self.ids.hardwareButton.text == "Sensor Hardware Summary:\nPurchase":
            self.ids.hardwareButton.text = "Sensor Hardware Summary:\nSubscription"
        else:
            self.ids.hardwareButton.text = "Sensor Hardware Summary:\nPurchase"

class SummaryBackground(Widget):
    pass

class SummaryScreen(Screen):
    pass



class ConfirmWindow(FloatLayout):

    def test(self):
        App.get_running_app().root.current = "WelcomeScreen"
        App.get_running_app().popupWindow.dismiss()



class SenseConfiguration(App):

    show = ConfirmWindow()
    popupWindow = Popup(title="Restart App?", content=show, size_hint=(None, None), size=(200, 150))

    def build(self):
        Window.size=(850,650)
        self.icon = "favicon.png"
        self.title = "Sense Configuration"
        Window.bind(on_request_close=self.on_request_close)
        return Builder.load_file("Style.kv")

    def on_request_close(self,other): #this needed another argument to work, I have no clue why
        show = ConfirmWindow()
        SenseConfiguration.popupWindow = Popup(title="Restart App?", content=show, size_hint=(None, None), size=(200, 150))
        SenseConfiguration.popupWindow.open()

        return True #False closes window, True leaves it open

    # def changeDetailsScreens(self):
    #     sm = App.get_running_app().root
    #     hardwareScreen = sm.get_screen("SensorHardwareScreen").ids.background.ids.interface
    #
    #     if sm.current == "SensorHardwareScreen":
    #
    #         if int(hardwareScreen.ids.t101Input.text) + int(hardwareScreen.ids.t102Input.text) > 0:
    #             sm.get_screen("ProbeDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "ProbeDetailsScreen"
    #
    #         elif int(hardwareScreen.ids.a100Input.text) > 0:
    #             sm.get_screen("TempHumidDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "TempHumidDetailsScreen"
    #
    #         elif int(hardwareScreen.ids.a120Input.text) > 0:
    #             sm.get_screen("PressureDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "PressureDetailsScreen"
    #
    #         elif int(hardwareScreen.ids.e121Input.text) + int(hardwareScreen.ids.e122Input.text) + int(hardwareScreen.ids.e123Input.text) > 0:
    #             sm.get_screen("LeakDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "LeakDetailsScreen"
    #
    #     elif sm.current == "PowerSupplyScreen": #this is in place of the Probe Details Screen because that screen was split into 2
    #
    #         if int(hardwareScreen.ids.a100Input.text) > 0:
    #             sm.get_screen("TempHumidDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "TempHumidDetailsScreen"
    #
    #         elif int(hardwareScreen.ids.a120Input.text) > 0:
    #             sm.get_screen("PressureDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "PressureDetailsScreen"
    #
    #         elif int(hardwareScreen.ids.e121Input.text) + int(hardwareScreen.ids.e122Input.text) + int(hardwareScreen.ids.e123Input.text) > 0:
    #             sm.get_screen("LeakDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "LeakDetailsScreen"
    #
    #     elif sm.current == "TempHumidDetailsScreen":
    #
    #         if int(hardwareScreen.ids.a120Input.text) > 0:
    #             sm.get_screen("PressureDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "PressureDetailsScreen"
    #
    #         elif int(hardwareScreen.ids.e121Input.text) + int(hardwareScreen.ids.e122Input.text) + int(hardwareScreen.ids.e123Input.text) > 0:
    #             sm.get_screen("LeakDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "LeakDetailsScreen"
    #
    #     elif sm.current == "PressureDetailsScreen":
    #
    #         if int(hardwareScreen.ids.e121Input.text) + int(hardwareScreen.ids.e122Input.text) + int(hardwareScreen.ids.e123Input.text) > 0:
    #             sm.get_screen("LeakDetailsScreen").ids.background.ids.interface.fillDefaultAnswers()
    #             sm.current = "LeakDetailsScreen"

    #Method to generate text file of the sites information
    def generateTxt(self):
        global package
        global hardwareType
        global siteHardware
        global onboarding
        global sitePriorities

        siteName = App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.siteNameInput.text
        bedSize = App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.bedSizeInput.text
        keySite = App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.keySiteContactInput.text

        departments = []
        if App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.facilitiesBox.active:
            departments.append("facilities")
        if App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.biomedBox.active:
            departments.append("biomed")
        if App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.clinicalServicesBox.active:
            departments.append("clinical services")
        if App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.pharmacyBox.active:
            departments.append("pharmacy")
        if App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.nursingBox.active:
            departments.append("nursing")
        if App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.labBox.active:
            departments.append("lab")
        if App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.itBox.active:
            departments.append("it")
        if App.get_running_app().root.get_screen("WelcomeScreen").ids.background.ids.interface.ids.cSuiteBox.active:
            departments.append("c suite")

        auditCompanies = []
        if App.get_running_app().root.get_screen("AuditsScreen").ids.background.ids.interface.ids.button0.selected:
            auditCompanies.append("joint commission or dnv")
        if App.get_running_app().root.get_screen("AuditsScreen").ids.background.ids.interface.ids.button1.selected:
            auditCompanies.append("fda")
        if App.get_running_app().root.get_screen("AuditsScreen").ids.background.ids.interface.ids.button2.selected:
            auditCompanies.append("cdc")
        if App.get_running_app().root.get_screen("AuditsScreen").ids.background.ids.interface.ids.button3.selected:
            auditCompanies.append("state's vaccine program")
        if App.get_running_app().root.get_screen("AuditsScreen").ids.background.ids.interface.ids.button4.selected:
            auditCompanies.append("health and human services")
        auditCompanies.append(App.get_running_app().root.get_screen("AuditsScreen").ids.background.ids.interface.ids.otherCompanyInput.text)
        auditPrepTime = App.get_running_app().root.get_screen("AuditsScreen").ids.background.ids.interface.ids.auditPrepTimeInput.text

        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.lossButtonList.selected == -1:
            lossFrequency = "not answered"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.lossButtonList.selected == 0:
            lossFrequency = "less than once per year"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.lossButtonList.selected == 1:
            lossFrequency = "about once per year"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.lossButtonList.selected == 2:
            lossFrequency = "2-3 times a year"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.lossButtonList.selected == 3:
            lossFrequency = "4-6 times a year"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.lossButtonList.selected == 4:
            lossFrequency = "6-11 times a year"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.lossButtonList.selected == 5:
            lossFrequency = "once a month"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.lossButtonList.selected == 6:
            lossFrequency = "once a week"

        averageLoss = App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.averageLossInput.text

        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.valueButtonList.selected == -1:
            primexGaurunteeValue = "not answered"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.valueButtonList.selected == 0:
            primexGaurunteeValue = "high value"
        if App.get_running_app().root.get_screen("LossScreen").ids.background.ids.interface.ids.valueButtonList.selected == 1:
            primexGaurunteeValue = "low value"

        departmentsUsed = App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.oneVueDepartmentsInput.text
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.teamButtonList.selected == -1:
            onevueAdmins = "not answered"
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.teamButtonList.selected == 0:
            onevueAdmins = "one person"
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.teamButtonList.selected == 1:
            onevueAdmins = App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.teamSizeInput.text

        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.frequencyButtonList.selected == -1:
            onevueFTE = "not answered"
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.frequencyButtonList.selected == 0:
            onevueFTE = "<10%"
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.frequencyButtonList.selected == 1:
            onevueFTE = "11-25%"
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.frequencyButtonList.selected == 2:
            onevueFTE = "26-50%"
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.frequencyButtonList.selected == 3:
            onevueFTE = ">50%"

        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.experienceButtonList.selected == -1:
            staffExperience = "not answered"
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.experienceButtonList.selected == 0:
            staffExperience = "yes"
        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.experienceButtonList.selected == 1:
            staffExperience = "no"

        alertsPerWeek = App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.alertsPerWeekInput.text

        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.laborRateInput.text != "":
            laborRate = App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.laborRateInput.text
        else:
            laborRate = 15

        reportsPerWeek = App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.reportsPerWeekInput.text

        if App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.managementRateInput.text != "":
            managementRate = App.get_running_app().root.get_screen("EfficiencyScreen").ids.background.ids.interface.ids.managementRateInput.text
        else:
            managementRate = 50

        otherComment = App.get_running_app().root.get_screen("OtherScreen").ids.background.ids.interface.ids.criteriaInput.text

        subscriptionPrice = App.get_running_app().root.get_screen("SummaryScreen").ids.background.ids.interface.ids.totalPriceInput.text

        if onboarding == "Self-Start":
            onboardingPrice = 18750
        else:
            onboardingPrice = 5600

        upFrontPrice = App.get_running_app().root.get_screen("SummaryScreen").ids.background.ids.interface.ids.initialPriceInput.text
        perYearPrice = App.get_running_app().root.get_screen("SummaryScreen").ids.background.ids.interface.ids.futurePriceInput.text

        file = open("%s-Site-Information.txt" % (siteName),"w")

        file.write("Sense Configuration App:\n")
        file.write("Date/time stamp: %s\n" % (datetime.now()))
        file.write("Bed size of site: %s" % (bedSize))
        file.write("Key site contact: %s" % (keySite))
        file.write("Departments involved:\n")
        for x in departments:
            file.write(x + "\n")
        file.write("Audit Companies:\n")
        for x in auditCompanies:
            file.write(x + "\n")
        file.write("Time spent preparing: %s\n" % (auditPrepTime))
        file.write("Loss Frequency: %s\n" % (lossFrequency))
        file.write("Average value of loss: %s\n" % (averageLoss))
        file.write("Guarantee value: %s\n" % (primexGaurunteeValue))
        file.write("Number of departments: %s\n" % (departmentsUsed))
        file.write("OneVue admins: %s\n" % (onevueAdmins))
        file.write("OneVue FTE: %s\n" % (onevueFTE))
        file.write("Staff experience: %s\n" % (staffExperience))
        file.write("Alerts per week: %s\n" % (alertsPerWeek))
        file.write("Labor rate per hour: %s\n" % (laborRate))
        file.write("Reports per week: %s\n" % (reportsPerWeek))
        file.write("Management rate per hour: %s\n" % (managementRate))
        file.write("Other priorities: %s\n" % (otherComment))
        file.write("Package confirmed: %s\n" % (package))
        file.write("Onboarding confirmed: %s\n" % (onboarding))
        file.write("Hardware confirmed: %s\n" % (hardwareType))
        file.write("Quantity T101: %s\n" % (siteHardware.t101))
        file.write("Quantity T102: %s\n" % (siteHardware.t102))
        file.write("Quantity A100: %s\n" % (siteHardware.a100))
        file.write("Quantity A120: %s\n" % (siteHardware.a120))
        file.write("Quantity E121: %s\n" % (siteHardware.e121))
        file.write("Quantity E122: %s\n" % (siteHardware.e122))
        file.write("Quantity E123: %s\n" % (siteHardware.e123))
        file.write("Total monitoring points: %s\n" % (siteHardware.totalPoints))
        file.write("Price total order per year: %s\n" % (subscriptionPrice))
        file.write("Onboarding Price: %s\n" % (onboardingPrice))
        file.write("Payment up front: %s\n" % (upFrontPrice))
        file.write("Payment year 2 onward: %s\n" % (perYearPrice))

        file.close()


if __name__=="__main__":
    SenseConfiguration().run()