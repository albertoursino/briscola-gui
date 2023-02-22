from tkinter import *
from tkinter import ttk


def start_gui():
    """
    This method starts the gui for the Briscola game
    """
    root = Tk()

    frame_padding = 30
    content_padding = (100, 100, 30, 30)  # w-n-e-s

    content = ttk.Frame(root, padding=content_padding)
    player_frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=300, height=100)
    agent_frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=300, height=100)
    table_frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=300, height=100)
    deck_frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)

    content.grid(column=0, row=0, sticky="NSEW")
    player_frame.grid(column=0, row=2, sticky="NSEW", padx=frame_padding, pady=frame_padding)
    agent_frame.grid(column=0, row=0, sticky="NSEW", padx=frame_padding, pady=frame_padding)
    table_frame.grid(column=0, row=1, sticky="NSEW", padx=frame_padding, pady=frame_padding)
    deck_frame.grid(column=1, row=1, sticky="NSEW", padx=frame_padding, pady=frame_padding)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3)
    content.columnconfigure(1, weight=3)
    content.columnconfigure(2, weight=3)
    content.columnconfigure(3, weight=1)
    content.columnconfigure(4, weight=1)
    content.rowconfigure(1, weight=1)

    root.mainloop()
