import customtkinter as ctk
from CTkToolTip import CTkToolTip
from PIL import Image


class Custom_button:
    def __init__(
        self,
        parent,
        text,
        command,
        fg_color="#4477CE",
        hover_color="#749BC2",
        text_color="white",
        tooltip_text="",
        width=120,
        height=32,
        image="",
    ):
        self.parent = parent
        self.text = text
        self.command = command
        self.fg_color = fg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.width = width
        self.height = height
        self.tooltip_text = tooltip_text
        self.tooltip_opacity = 0 if tooltip_text == "" else 1
        self.button = ctk.CTkButton(
            self.parent,
            text=self.text,
            command=self.command,
            fg_color=self.fg_color,
            hover_color=self.hover_color,
            text_color=self.text_color,
            width=self.width,
            height=self.height,
        )
        self.tooltip = CTkToolTip(
            self.button, message=self.tooltip_text, alpha=self.tooltip_opacity
        )

    def pack_button(self, pady=0, padx=0):
        self.button.pack(pady=pady, padx=padx)

    def place_button(self, x, y):
        self.button.place(x=x, y=y)


class Custom_icon:
    def __init__(self, label, width, height, logo):
        self.label = label
        self.width = width
        self.height = height
        self.logo = logo
        self.image = ctk.CTkImage(Image.open(logo), size=(self.width, self.height))
        self.label.configure(image=self.image)
