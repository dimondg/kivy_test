from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from func.time_now import time_now
from PIL import Image, ImageDraw, ImageFont
from constants import image_text_font_path, image_text_font_size, image_text_pos, image_text_color, LOCAL_IMG_DIR_PATH
from func.get_save_name import get_save_name
from func.cloud_yandex_load import load_image

Builder.load_file("camera.kv")


class CameraClick(Screen):
    def image_draw(self, time_note, save_name):
        img = Image.open(f'images/IMG_{save_name}')
        img_new = ImageDraw.Draw(img)
        font = ImageFont.truetype(image_text_font_path, image_text_font_size)
        img_new.text(image_text_pos, time_note, fill=image_text_color, font=font)
        img.save(f"images/{save_name}", "PNG")

    def capture(self):
        camera = self.ids.camera
        font = ImageFont.truetype(image_text_font_path, image_text_font_size)
        time_note = time_now()
        save_name = get_save_name(time_note)
        camera.export_to_png(f'images/IMG_{save_name}')
        self.image_draw(time_note, save_name)
        load_image(save_name, image_dir_path=LOCAL_IMG_DIR_PATH)


class MenuScreen(Screen):
    pass


class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CameraClick(name='camera'))

        return sm


if __name__ == '__main__':
    TestApp().run()
