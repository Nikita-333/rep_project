import os

from FindByNameTur import FindStudentByNameOfTur
from FindBySport import FindStudentBySport
from FindByWinningSize import FindStudentByWinningSize

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.core.window import Window
from Controller import StudentControllerImpl

Window.fullscreen = 'auto'

# Config.set('graphics','resizable','0')
# Config.set('graphics','width','800')
# Config.set('graphics','height','600')

StudentControllerImpl = StudentControllerImpl()
main_labels = StringProperty()


class MainWindow(Screen):
    def __init__(self, **kw):
        super(MainWindow, self).__init__(**kw)
        self.main_labels = StudentControllerImpl.print_all()


class WindowManager(ScreenManager):
    pass


class ChoiceMethod(Screen):
    def __init__(self, **kw):
        super(ChoiceMethod, self).__init__(**kw)
        self.main_labels = StudentControllerImpl.print_all()


class Earnings(Screen):
    def __init__(self, **kw):
        super(Earnings, self).__init__(**kw)
        self.main_labels = StudentControllerImpl.print_all()

    def search_winning_size(self):
        try:
            if len(self.input.text) == 0:
                self.label.text = 'You not did enter, repeat input'

            if self.input.text.isdigit() is False:
                self.label.text = "Accept only integer number"
                # self.clear()
            #elif len(self.input.text)>=3:
               # self.label.text='Accept only number'
            #elif int(self.input.text) is False:
                #self.label.text = 'Accept only integer number'
            else:
                if int(self.input.text) < 0:
                    self.label.text = 'Invalid number entered, please try again'
                    # self.clear()
                else:
                    self.label.text = ''
                    self.label.text = StudentControllerImpl.find_student_by_winning_size(self.input.text)
                    FindStudentByWinningSize.students.clear()
        except:
            self.label.text = 'Error'
    def delete_winning_size(self):
        try:
            if len(self.input.text) == 0:
                self.label.text = '''you didn't enter anything, please try again'''
                #self.clear()
            if self.input.text.isdigit() is False:
                self.label.text = 'Invalid number entered, please try again'
                #self.clear()
            else:
               if int(self.input.text) < 0:
                   self.label.text = 'Invalid number entered, please try again'
                #self.clear()
               else:
                   self.label.text = ''
                   self.label.text=StudentControllerImpl.delete_student_by_winning_size(self.input.text)
                   FindStudentByWinningSize.students.clear()
        except:
            self.label.text = 'Error'

    def clear(self):
        self.label.text = ""
        self.input.text = ""


class SportOderName(Screen):
    def __init__(self, **kw):
        super(SportOderName, self).__init__(**kw)
        self.main_labels = StudentControllerImpl.print_all()

    def search_by_sport(self):
        if len(self.input.text) == 0:
            self.label.text = 'You not did enter, repeat input'
            # self.clear()
        else:
            if  self.input.text.isdigit() is True:
                self.label.text = 'Invalid number entered, please try again'
                # self.clear()

            else:
                self.label.text = ''
                self.label.text = StudentControllerImpl.find_student_by_sport(self.input.text)
                FindStudentBySport.students.clear()

    def delete_by_sport(self):
        if len(self.input.text) == 0:
            self.label.text = 'You not did enter, repeat input'
            # self.clear()
        else:
            if  self.input.text.isdigit() is True:
                self.label.text = 'Invalid number entered, please try again'
                # self.clear()

            else:
                self.label.text = ''
                self.label.text=StudentControllerImpl.delete_student_by_sport(self.input.text)
                FindStudentBySport.students.clear()

    def clear(self):
        self.label.text = ""
        self.input.text = ""


class TournamentName(Screen):
    def __init__(self, **kw):
        super(TournamentName, self).__init__(**kw)
        self.main_labels = StudentControllerImpl.print_all()

    def search_name_tur(self):
        if len(self.input.text) == 0:
            self.label.text = 'You not did enter, repeat input'
            # self.clear()
        else:
            if  self.input.text.isdigit() is True:
                self.label.text = 'Invalid number entered, please try again'
                # self.clear()

            else:
                self.label.text = ''
                self.label.text = StudentControllerImpl.find_student_by_name_tur(self.input.text)
                FindStudentByNameOfTur.students.clear()

    def delete_name_tur(self):
        if len(self.input.text) == 0:
            self.label.text = 'You not did enter, repeat input'
            # self.clear()
        else:
            if  self.input.text.isdigit() is True:
                self.label.text = 'Invalid number entered, please try again'
                # self.clear()
            else:
                self.label.text = ''
                self.label.text=StudentControllerImpl.delete_student_by_name_tur(self.input.text)
                FindStudentByNameOfTur.students.clear()

    def clear(self):
        self.label.text = ""
        self.input.text = ""


kv = Builder.load_file("my.kv")


class MyApp(App):  # <- Main Class
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
