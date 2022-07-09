from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

Builder.load_file("test.kv")


class CameraClick(Screen):

    def capture(self):
        camera = self.ids.camera
        camera.export_to_png(f'images/IMG_1.png')


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class QuitScreen(Screen):
    pass


class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(QuitScreen(name='quit'))
        sm.add_widget(CameraClick(name='camera'))

        return sm


if __name__ == '__main__':
    TestApp().run()
