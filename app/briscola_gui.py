import os
from functools import partial
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from PIL.Image import Resampling


class BriscolaGui:
    card_images = {}
    content = None
    root = None
    agent_frame = None
    player_frame = None
    table_frame = None
    deck_frame = None
    frame_padding = 5

    def __init__(self):
        self.root = Tk()
        content_padding = (50, 50, 50, 50)  # w-n-e-s
        self.content = ttk.Frame(self.root, padding=content_padding)
        self.content.grid(column=0, row=0, sticky="NSEW")
        # root and content resizing when resolution changes
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)
        self.content.rowconfigure(1, weight=1)
        self.content.rowconfigure(2, weight=1)
        # load all images
        image_size = (98, 162)
        for filename in os.listdir("../card_images"):
            img_path = os.path.join("../card_images", filename)
            img = Image.open(img_path).resize(image_size, resample=Resampling.LANCZOS)
            self.card_images[filename] = (ImageTk.PhotoImage(image=img))

    # TODO: this method should be called wrt the algorithm of the Briscola game
    def player_play_card(self, card_btn, card_name):
        """
        This function moves the chosen card from the "player_frame" to the "table_frame".
        Cards in the player hand are indexed from left (1) to right (3).
        :param card_btn: button of the card to be removed form the player hand
        :param card_name: image filename of the played card
        :return image filename of the played card
        """
        # creating and showing a label that represents the player played card into the table frame
        new_card_btn = ttk.Label(self.table_frame.winfo_children()[1], image=card_btn['image'])
        new_card_btn.grid(column=0, row=0)
        # destroying the card object from the player frame
        card_btn.destroy()
        return card_name

    # TODO: this method should be called wrt the algorithm of the Briscola game
    def agent_play_card(self, card_name):
        """
        This function moves a card from the "agent_frame" to the "table_frame".
        :param card_name: image filename of the card that the agent played
        """
        # remove a "retro card" from the agent frame
        self.agent_frame.winfo_children()[0].destroy()
        # showing the played card inside the table frame
        card = ttk.Button(self.table_frame.winfo_children()[0], image=self.card_images[card_name])
        card.grid(column=0, row=0)

    def populate_agent_frame(self):
        """
        Insert 3 retro card images into the frame "agent_frame".
        """
        card_1 = ttk.Label(self.agent_frame)
        card_2 = ttk.Label(self.agent_frame)
        card_3 = ttk.Label(self.agent_frame)

        card_1['image'] = self.card_images["Carte_Napoletane_retro.jpg"]
        card_2['image'] = self.card_images["Carte_Napoletane_retro.jpg"]
        card_3['image'] = self.card_images["Carte_Napoletane_retro.jpg"]

        card_1.grid(column=0, row=0, sticky="NS", padx=5, pady=5)
        card_2.grid(column=1, row=0, sticky="NS", padx=5, pady=5)
        card_3.grid(column=2, row=0, sticky="NS", padx=5, pady=5)

    # TODO: this method should be called wrt the algorithm of the Briscola game
    def populate_player_frame(self, cards_name):
        """
        Insert 3 cards into the frame "player_frame".
        :param cards_name: array containing 3 image filenames
        """
        card_1 = ttk.Button(self.player_frame, command=lambda: self.player_play_card(card_1, cards_name[0]))
        card_2 = ttk.Button(self.player_frame, command=lambda: self.player_play_card(card_2, cards_name[1]))
        card_3 = ttk.Button(self.player_frame, command=lambda: self.player_play_card(card_3, cards_name[2]))

        card_1['image'] = self.card_images[cards_name[0]]
        card_2['image'] = self.card_images[cards_name[1]]
        card_3['image'] = self.card_images[cards_name[2]]

        card_1.grid(column=0, row=0, sticky="NS", padx=5, pady=5)
        card_2.grid(column=1, row=0, sticky="NS", padx=5, pady=5)
        card_3.grid(column=2, row=0, sticky="NS", padx=5, pady=5)

    # TODO: this method should be called wrt the algorithm of the Briscola game
    def populate_deck_frame(self, briscola_name):
        """
        Insert images of the deck and of the briscola card into the frame "deck_frame".
        :param briscola_name: image filename of the briscola
        """
        briscola_label = ttk.Label(self.deck_frame)
        deck_label = ttk.Label(self.deck_frame)

        briscola_label['image'] = self.card_images[briscola_name]
        deck_label['image'] = self.card_images["Carte_Napoletane_retro.jpg"]

        briscola_label.grid(column=0, row=0, sticky="NS", padx=5, pady=5)
        deck_label.grid(column=1, row=0, sticky="NS", padx=5, pady=5)

    def populate_table_frame(self):
        """
        Insert 2 frames into the frame "table_frame".
        """
        agent_card_frame = ttk.Frame(self.table_frame)
        player_card_frame = ttk.Frame(self.table_frame)

        agent_card_frame.grid(column=0, row=0, sticky="NS", padx=self.frame_padding, pady=self.frame_padding)
        player_card_frame.grid(column=1, row=0, sticky="NS", padx=self.frame_padding, pady=self.frame_padding)

    def create_main_frames(self):
        """
        Creates the 4 main frames.
        """
        self.agent_frame = ttk.Frame(self.content)
        self.player_frame = ttk.Frame(self.content)
        self.table_frame = ttk.Frame(self.content)
        self.deck_frame = ttk.Frame(self.content)

        self.player_frame.grid(column=0, row=2, sticky="NS", padx=self.frame_padding, pady=self.frame_padding)
        self.agent_frame.grid(column=0, row=0, sticky="NS", padx=self.frame_padding, pady=self.frame_padding)
        self.table_frame.grid(column=0, row=1, sticky="NS", padx=self.frame_padding, pady=self.frame_padding + 10)
        self.deck_frame.grid(column=1, row=1, sticky="NS", padx=self.frame_padding, pady=self.frame_padding)

        # resizing frames with resolution changes
        self.deck_frame.columnconfigure(0, weight=1)
        self.deck_frame.columnconfigure(1, weight=1)
        self.deck_frame.rowconfigure(0, weight=1)
        self.player_frame.columnconfigure(0, weight=1)
        self.player_frame.columnconfigure(1, weight=1)
        self.player_frame.columnconfigure(2, weight=1)
        self.player_frame.rowconfigure(0, weight=0)
        self.agent_frame.columnconfigure(0, weight=1)
        self.agent_frame.columnconfigure(1, weight=1)
        self.agent_frame.columnconfigure(2, weight=1)
        self.agent_frame.rowconfigure(0, weight=1)

    def start_gui(self):
        """
        This method populate the content and starts the gui for the Briscola game
        """
        self.create_main_frames()

        # TODO: these methods should be called wrt the algorithm of the Briscola game
        self.populate_player_frame(["17_Sette_di_coppe.jpg", "17_Sette_di_coppe.jpg", "17_Sette_di_coppe.jpg"])
        self.populate_deck_frame("37_Sette_di_bastoni.jpg")
        self.populate_agent_frame()
        self.populate_table_frame()

        self.root.mainloop()


if __name__ == '__main__':
    briscola_gui = BriscolaGui()
    briscola_gui.start_gui()
