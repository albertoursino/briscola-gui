import os
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
    card_label_padding = 5

    def __init__(self):
        self.root = Tk()
        self.root.minsize(900, 700)
        content_padding = (50, 50, 50, 50)  # w-n-e-s
        style = ttk.Style()
        style.configure("Green.TFrame", background="green")
        style.configure("Green.TButton", foreground="green", background="green", padding=-1)
        self.content = ttk.Frame(self.root, padding=content_padding, style="Green.TFrame")
        self.content.grid(column=0, row=0, sticky="NSEW")
        # root and content resizing when resolution changes
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)
        self.content.rowconfigure(1, weight=1)
        self.content.rowconfigure(2, weight=1)
        # loading and resizing all images
        image_size = (98, 162)
        for filename in os.listdir("../card_images"):
            img_path = os.path.join("../card_images", filename)
            img = Image.open(img_path).resize(image_size, resample=Resampling.LANCZOS)
            self.card_images[filename] = (ImageTk.PhotoImage(image=img))

    def player_play_card(self, card_btn, card_name):
        """
        This function moves the chosen card from the "player_frame" to the "table_frame".
        :param card_btn: button of the card to be removed form the player hand
        :param card_name: image filename of the played card
        :return image filename of the played card
        """
        # creating and showing a label that represents the player played card into the table frame
        new_card_btn = ttk.Label(self.table_frame.winfo_children()[1], style="Green.TButton", image=card_btn['image'])
        new_card_btn.grid(column=0, row=0)
        # destroying the card object from the player frame
        card_btn.destroy()
        return card_name

    def agent_play_card(self, card_name):
        """
        This function moves a card from the "agent_frame" to the "table_frame".
        :param card_name: image filename of the card that the agent played
        """
        # remove a "retro card" from the agent frame
        self.agent_frame.winfo_children()[0].destroy()
        # showing the played card inside the table frame
        card = ttk.Label(self.table_frame.winfo_children()[0], style="Green.TButton", image=self.card_images[card_name])
        card.grid(column=0, row=0)

    def empty_deck(self):
        """
        This function loads the image "Deck_Finito.jpg" into the frame "deck_frame".
        """
        self.deck_frame.winfo_children()[1].destroy()
        empty_deck_label = ttk.Label(self.deck_frame, style="Green.TButton", image=self.card_images["Deck_Finito.jpg"])
        empty_deck_label.grid(column=1, row=0, padx=self.card_label_padding, pady=self.card_label_padding)

    def empty_briscola(self):
        """
        This function removes the image of the Briscola from the frame "deck_frame".
        """
        self.deck_frame.winfo_children()[0].destroy()

    def agent_draw_card(self):
        """
        This function adds a card to the agent hand.
        """
        agent_frame_children = self.agent_frame.winfo_children()
        card = ttk.Label(self.agent_frame, style="Green.TButton", image=self.card_images["Carte_Napoletane_retro.jpg"])

        card.grid(column=len(agent_frame_children), row=0, padx=self.card_label_padding,
                  pady=self.card_label_padding)

    def player_draw_card(self, card_name):
        """
        This function adds a card to the player hand.
        :param card_name: image filename of the card to be added
        """
        player_frame_children = self.player_frame.winfo_children()
        card = ttk.Button(self.player_frame, style="Green.TButton", image=self.card_images[card_name],
                          command=lambda: self.player_play_card(card, card_name))
        # adding the card at the right most place in the player hand
        card.grid(column=len(player_frame_children), row=0, padx=self.card_label_padding,
                  pady=self.card_label_padding)

    def populate_player_frame(self, cards_name):
        """
        Inserts 3 cards into the frame "player_frame".
        :param cards_name: array containing 3 image filenames
        """
        card_1 = ttk.Button(self.player_frame, style="Green.TButton", image=self.card_images[cards_name[0]],
                            command=lambda: self.player_play_card(card_1, cards_name[0]))
        card_2 = ttk.Button(self.player_frame, style="Green.TButton", image=self.card_images[cards_name[1]],
                            command=lambda: self.player_play_card(card_2, cards_name[1]))
        card_3 = ttk.Button(self.player_frame, style="Green.TButton", image=self.card_images[cards_name[2]],
                            command=lambda: self.player_play_card(card_3, cards_name[2]))

        card_1.grid(column=0, row=0, padx=self.card_label_padding, pady=self.card_label_padding)
        card_2.grid(column=1, row=0, padx=self.card_label_padding, pady=self.card_label_padding)
        card_3.grid(column=2, row=0, padx=self.card_label_padding, pady=self.card_label_padding)

    def populate_deck_frame(self, briscola_name):
        """
        Inserts images of the deck and of the briscola card into the frame "deck_frame".
        :param briscola_name: image filename of the briscola
        """
        briscola_label = ttk.Label(self.deck_frame, style="Green.TButton", image=self.card_images[briscola_name])
        deck_label = ttk.Label(self.deck_frame, style="Green.TButton", image=self.card_images["Carte_Napoletane_retro.jpg"])

        briscola_label.grid(column=0, row=0, sticky="NS", padx=self.card_label_padding, pady=self.card_label_padding)
        deck_label.grid(column=1, row=0, sticky="NS", padx=self.card_label_padding, pady=self.card_label_padding)

    def create_main_frames(self):
        """
        Creates the 4 main frames.
        """
        self.agent_frame = ttk.Frame(self.content, width=350, style="Green.TFrame")
        self.player_frame = ttk.Frame(self.content, width=350, style="Green.TFrame")
        self.table_frame = ttk.Frame(self.content, width=350, style="Green.TFrame")
        self.deck_frame = ttk.Frame(self.content, width=200, style="Green.TFrame")

        self.player_frame.grid(column=0, row=2, sticky="NS")
        self.agent_frame.grid(column=0, row=0, sticky="NS")
        self.table_frame.grid(column=0, row=1, sticky="NS")
        self.deck_frame.grid(column=1, row=1, sticky="NS")

        # --- inserting nested frames ---
        # here we are inside the frame "table_frame"
        agent_played_card_frame = ttk.Frame(self.table_frame, style="Green.TFrame")
        player_played_card_frame = ttk.Frame(self.table_frame, style="Green.TFrame")
        agent_played_card_frame.grid(column=0, row=0, sticky="NS", padx=self.frame_padding, pady=self.frame_padding)
        player_played_card_frame.grid(column=1, row=0, sticky="NS", padx=self.frame_padding, pady=self.frame_padding)
        # here we are inside the frame "agent_frame"
        card_1 = ttk.Label(self.agent_frame, style="Green.TButton", image=self.card_images["Carte_Napoletane_retro.jpg"])
        card_2 = ttk.Label(self.agent_frame, style="Green.TButton", image=self.card_images["Carte_Napoletane_retro.jpg"])
        card_3 = ttk.Label(self.agent_frame, style="Green.TButton", image=self.card_images["Carte_Napoletane_retro.jpg"])

        card_1.grid(column=0, row=0, padx=self.card_label_padding, pady=self.card_label_padding)
        card_2.grid(column=1, row=0, padx=self.card_label_padding, pady=self.card_label_padding)
        card_3.grid(column=2, row=0, padx=self.card_label_padding, pady=self.card_label_padding)

        # resizing frames with resolution changes
        self.deck_frame.columnconfigure(0, weight=1)
        self.deck_frame.columnconfigure(1, weight=1)
        self.deck_frame.rowconfigure(0, weight=0)
        self.player_frame.columnconfigure(0, weight=1)
        self.player_frame.columnconfigure(1, weight=1)
        self.player_frame.columnconfigure(2, weight=1)
        self.player_frame.rowconfigure(0, weight=0)
        self.agent_frame.columnconfigure(0, weight=1)
        self.agent_frame.columnconfigure(1, weight=1)
        self.agent_frame.columnconfigure(2, weight=1)
        self.agent_frame.rowconfigure(0, weight=0)

    def start_gui(self, briscola_name, initial_player_cards):
        """
        This method populates the content with initial values and starts the gui for the Briscola game.
        :param briscola_name: image filename of the briscola
        :param initial_player_cards: array containing 3 image filenames of the 3 initial player cards
        """
        self.create_main_frames()

        # TODO: the algorithm tells us the briscola card
        self.populate_deck_frame(briscola_name)

        # TODO: the algorithm tells us the three initial cards of the player
        self.populate_player_frame(initial_player_cards)

        self.root.mainloop()


if __name__ == '__main__':
    briscola_gui = BriscolaGui()
    briscola_gui.start_gui("37_Sette_di_bastoni.jpg",
                           ["29_Nove_di_spade.jpg", "24_Quattro_di_spade.jpg", "17_Sette_di_coppe.jpg"])
