import os
import customtkinter as ctk
from dotenv import load_dotenv
from api_calls import Quote_api_call, Bard_api_call
from ui_elements import Custom_button, Custom_icon
from CTkMessagebox import CTkMessagebox
from PIL import Image

load_dotenv()

dummy_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu lorem aliquam, fermentum ligula sit amet, luctus diam. Duis condimentum finibus tortor, eget sollicitudin metus porta sit amet. Suspendisse auctor molestie accumsan. Donec eu gravida ligula, eu pellentesque libero. In lacinia, mauris non dapibus hendrerit, nisi quam venenatis diam, vel sodales elit ipsum ut orci. Nulla imperdiet cursus lacus, molestie ullamcorper diam semper a. Nunc sed feugiat nunc, vitae rhoncus purus. Ut ac risus sed eros rutrum ultricies. Vivamus non ultricies metus. Mauris imperdiet rutrum ligula non tempor. Vivamus viverra pharetra tellus, eget luctus ligula dignissim ut."

qoutes_api_key = os.environ.get("QUOTE_API_KEY")
bard_api_key = os.environ.get("BARD_API_KEY")
quotes_headers = {"X-Api-Key": qoutes_api_key}
bard_logo_path = "icons/Google_Bard_logo.png"
kanye_logo_path = "icons/Kanye_icon.png"
send_logo_path = "icons/send_icon_white.png"

quotes_url = "https://api.api-ninjas.com/v1/quotes"
kanye_url = "https://api.kanye.rest"

quote_api = Quote_api_call(url=quotes_url, headers=quotes_headers)
current_quote_data = {"quote": "", "author": ""}
kanye_api = Quote_api_call(url=kanye_url)
bard_api = Bard_api_call(token=bard_api_key)


def dummy_command():
    test = f"{ask_bard_entry.get()} {current_quote_data['quote']}"
    bard_label.configure(text=test)


def call_quote_api_command():
    global current_quote_data
    quote_data = quote_api.call_api()
    current_quote_data = quote_data
    kanye_label.configure(text=current_quote_data[0]["quote"])


def call_kanye_api_command():
    global current_quote_data
    kanye_data = kanye_api.call_api()
    current_quote_data = kanye_data
    kanye_label.configure(text=current_quote_data["quote"])


def ask_bard_about():
    try:
        question = f"{ask_bard_entry.get()} {current_quote_data['quote']}"
        answer = bard_api.ask_bard(question=question)
        bard_label.configure(text=answer["content"])
    except KeyError:
        CTkMessagebox(
            master=root,
            title="Error",
            message="Please Generate A Random Kanye Quote First",
        )


root = ctk.CTk()
root.title("Barded Quotes App")
root.geometry("400x500")
root.resizable(False, False)
ctk.set_appearance_mode("light")
kanye_frame = ctk.CTkFrame(root, width=300, height=150)
kanye_frame.pack_propagate(False)
bard_frame = ctk.CTkFrame(root, width=300, height=150, fg_color="transparent")
bard_frame.pack_propagate(False)
bard_canvas = ctk.CTkCanvas(
    bard_frame,
    bg="#272829",
    bd="3",
)
bard_scrollbar = ctk.CTkScrollbar(
    bard_frame, orientation="vertical", command=bard_canvas.yview, button_color="black"
)
scrollable_bard_frame = ctk.CTkFrame(
    bard_canvas, fg_color="transparent", bg_color="transparent"
)
# scrollable_bard_frame.propagate(False)
scrollable_bard_frame.bind(
    "<Configure>", lambda e: bard_canvas.configure(scrollregion=bard_canvas.bbox("all"))
)
bard_canvas.create_window((0, 0), window=scrollable_bard_frame, anchor="nw")
bard_canvas.configure(yscrollcommand=bard_scrollbar.set)


bard_label = ctk.CTkLabel(
    master=scrollable_bard_frame,
    text="",
    anchor="center",
    justify="left",
    text_color="white",
    wraplength=270,
)


kanye_label = ctk.CTkLabel(
    kanye_frame, text="", anchor="center", justify="center", wraplength=250
)


ask_bard_entry = ctk.CTkEntry(
    root,
    width=300,
    height=35,
    border_color="silver",
    corner_radius=30,
    fg_color="#272829",
    text_color="white",
)

get_quote_button = Custom_button(
    parent=root,
    command=call_kanye_api_command,
    text="Get Kanye Quote",
    tooltip_text="Generate a random Kanye West quote",
)

send_logo_icon = ctk.CTkImage(Image.open(send_logo_path), size=(20, 20))
ask_bard_button = ctk.CTkButton(
    root,
    width=35,
    height=25,
    text="",
    command=ask_bard_about,
    image=send_logo_icon,
    fg_color="#272829",
)

bard_logo_label = ctk.CTkLabel(root, text="")
bard_icon = Custom_icon(label=bard_logo_label, logo=bard_logo_path, width=20, height=20)

kanye_logo_label = ctk.CTkLabel(root, text="", text_color="white")
kanye_icon = Custom_icon(
    label=kanye_logo_label, logo=kanye_logo_path, width=30, height=30
)

get_quote_button.pack_button(pady=20)
kanye_label.pack(
    pady=10,
    padx=10,
)


kanye_frame.pack(pady=10)
ask_bard_entry.pack(pady=10)
ask_bard_button.place(x=355, y=255)
bard_logo_label.place(x=20, y=252)
kanye_logo_label.place(x=13, y=77)
bard_label.pack(pady=10, padx=10)
bard_frame.pack(pady=10)
bard_canvas.pack(side="left", fill="both", expand=True)
bard_scrollbar.place(x=285, y=0)

root.mainloop()
