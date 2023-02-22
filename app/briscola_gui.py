import os
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from PIL.Image import Resampling


def populate_agent_frame(agent_frame, card_images):
    """
    Insert 3 random hidden initial cards into the frame "agent_frame"
    """
    card_1 = ttk.Label(agent_frame)
    card_2 = ttk.Label(agent_frame)
    card_3 = ttk.Label(agent_frame)

    card_1['image'] = card_images[40]
    card_2['image'] = card_images[40]
    card_3['image'] = card_images[40]

    card_1.grid(column=0, row=0, sticky="NS", padx=5, pady=5)
    card_2.grid(column=1, row=0, sticky="NS", padx=5, pady=5)
    card_3.grid(column=2, row=0, sticky="NS", padx=5, pady=5)


def populate_player_frame(player_frame, card_images):
    """
    Insert 3 random initial cards into the frame "player_frame"
    """
    card_1 = ttk.Label(player_frame)
    card_2 = ttk.Label(player_frame)
    card_3 = ttk.Label(player_frame)

    card_1['image'] = card_images[10]
    card_2['image'] = card_images[11]
    card_3['image'] = card_images[12]

    card_1.grid(column=0, row=0, sticky="NS", padx=5, pady=5)
    card_2.grid(column=1, row=0, sticky="NS", padx=5, pady=5)
    card_3.grid(column=2, row=0, sticky="NS", padx=5, pady=5)


def populate_deck_frame(deck_frame, card_images):
    """
    Insert the deck and the briscola card into the frame "deck_frame"
    """
    briscola_label = ttk.Label(deck_frame)
    deck_label = ttk.Label(deck_frame)

    briscola_label['image'] = card_images[39]
    deck_label['image'] = card_images[40]

    briscola_label.grid(column=0, row=0, sticky="NS", padx=5, pady=5)
    deck_label.grid(column=1, row=0, sticky="NS", padx=5, pady=5)


def populate_table_frame(table_frame):
    """
    Insert two frames into the frame "table_frame"
    """
    pass


def create_main_frames(content):
    """
    Creates the 4 main frames
    :return: the frames
    """
    frame_padding = 5
    agent_frame = ttk.Frame(content, borderwidth=5, relief="groove")
    player_frame = ttk.Frame(content, borderwidth=5, relief="groove")
    table_frame = ttk.Frame(content, borderwidth=5, relief="groove")
    deck_frame = ttk.Frame(content, borderwidth=5, relief="groove")

    player_frame.grid(column=0, row=2, sticky="NS", padx=frame_padding, pady=frame_padding)
    agent_frame.grid(column=0, row=0, sticky="NS", padx=frame_padding, pady=frame_padding)
    table_frame.grid(column=0, row=1, sticky="NS", padx=frame_padding, pady=frame_padding)
    deck_frame.grid(column=1, row=1, sticky="NS", padx=frame_padding, pady=frame_padding)

    deck_frame.columnconfigure(0, weight=1)
    deck_frame.columnconfigure(1, weight=1)
    deck_frame.rowconfigure(0, weight=1)
    player_frame.columnconfigure(0, weight=1)
    player_frame.columnconfigure(1, weight=1)
    player_frame.columnconfigure(2, weight=1)
    player_frame.rowconfigure(0, weight=1)
    agent_frame.columnconfigure(0, weight=1)
    agent_frame.columnconfigure(1, weight=1)
    agent_frame.columnconfigure(2, weight=1)
    agent_frame.rowconfigure(0, weight=1)

    return agent_frame, player_frame, table_frame, deck_frame


def start_gui():
    """
    This method starts the gui for the Briscola game
    """
    root = Tk()

    content_padding = (50, 50, 50, 50)  # w-n-e-s
    content = ttk.Frame(root, padding=content_padding)
    content.grid(column=0, row=0, sticky="NSEW")

    # load all images
    card_images = []
    image_size = (98, 162)
    for filename in os.listdir("../card_images"):
        img_path = os.path.join("../card_images", filename)
        img = Image.open(img_path).resize(image_size, resample=Resampling.LANCZOS)
        card_images.append(ImageTk.PhotoImage(image=img))

    agent_frame, player_frame, table_frame, deck_frame = create_main_frames(content)
    populate_player_frame(player_frame, card_images)
    populate_deck_frame(deck_frame, card_images)
    populate_agent_frame(agent_frame, card_images)

    # grid resizing when resolution change
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=1)
    content.rowconfigure(0, weight=1)
    content.rowconfigure(1, weight=1)
    content.rowconfigure(2, weight=1)

    root.mainloop()


if __name__ == '__main__':
    start_gui()
