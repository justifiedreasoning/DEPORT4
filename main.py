from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast
from kivy.core.window import Window

class DeportScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=15)

        # BIG TITLE - exactly like your mockup
        title = MDLabel(
            text="DEPORT\nREPORT\nv13 FRESH REPO - DARK MOCKUP MATCH",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            bold=True,
            size_hint_y=None,
            height=160
        )
        layout.add_widget(title)

        # Clean dark card (matches your mockup)
        card = MDCard(
            orientation="vertical",
            padding=20,
            spacing=15,
            size_hint_y=None,
            height=520,
            md_bg_color=(0.08, 0.08, 0.15, 1),
            elevation=6
        )

        self.location = MDTextField(hint_text="Location (City, State, Address)", mode="rectangle", size_hint_y=None, height=50)
        card.add_widget(self.location)

        self.description = MDTextField(hint_text="Description of incident", mode="rectangle", multiline=True, size_hint_y=None, height=120)
        card.add_widget(self.description)

        upload_box = MDBoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=60)
        self.upload_btn = MDIconButton(icon="camera", theme_text_color="Custom", text_color=(0, 0.7, 1, 1), on_release=lambda x: toast("Camera opening..."))
        upload_label = MDLabel(text="Picture/Video Upload", size_hint_x=0.8)
        upload_box.add_widget(self.upload_btn)
        upload_box.add_widget(upload_label)
        card.add_widget(upload_box)

        self.aliases = MDTextField(hint_text="Known aliases", mode="rectangle", size_hint_y=None, height=50)
        card.add_widget(self.aliases)

        self.category = MDTextField(hint_text="Category (e.g. Illegal Entry)", mode="rectangle", size_hint_y=None, height=50)
        card.add_widget(self.category)

        layout.add_widget(card)

        submit_btn = MDRaisedButton(
            text="SUBMIT",
            md_bg_color=(0.4, 0.2, 0.9, 1),
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=60,
            on_release=lambda x: toast("Report packaged and ready!")
        )
        layout.add_widget(submit_btn)

        self.add_widget(layout)

    def on_start(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        Window.clearcolor = (0.07, 0.07, 0.12, 1)

class DeportApp(MDApp):
    def build(self):
        return DeportScreen()

if __name__ == "__main__":
    DeportApp().run()
