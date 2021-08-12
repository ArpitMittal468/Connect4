import tkinter as tk
from random import randint as rand
import threading
from time import sleep
import pyglet

# from os import system

HEIGHT = 720
WIDTH = 1300
BOARD_PIECES_LABEL_OUTER = [0, 0, 0, 0, 0, 0]
BOARD_PIECES_LABEL_INNER = []
BOARD_PIECES_COUNTER = 0
BOARD_BACK_FRAME = 0
MENU_FRAME = 0
MENU_FRAME_P1_LABEL = 0
MENU_FRAME_P2_LABEL = 0
MENU_FRAME_P1_ENTRY = 0
MENU_FRAME_P2_ENTRY = 0
MENU_PLAY_BUTTON = 0
BOARD_STATES = [0 for i in range(42)]
BOARD_BUTTONS = []
BOARD_BUTTONS_FRAME = 0
BACK_BUTTON = 0
COIN_COUNTER = 0
HOW_TO_PLAY_IMG = 0
HOW_TO_PLAY = 0

THINKING = True
BUTTON_CHAR = ""

PLAYER_1 = ""
PLAYER_2 = ""

COLOR = ["#cdf4e0", "#28a1e0", "#ff2f6b"]
CURRENT_CHANCE = 0

SCORE_1 = 0
SCORE_2 = 0

PLAYER_1_SCOREBOARD = 0
PLAYER_2_SCOREBOARD = 0

PLAYER_1_INDICATOR = 0
PLAYER_2_INDICATOR = 0


def b1_clicked():
    global BUTTON_CHAR
    BUTTON_CHAR = "1"
    key_pressed(BUTTON_CHAR)


def b2_clicked():
    global BUTTON_CHAR
    BUTTON_CHAR = "2"
    key_pressed(BUTTON_CHAR)


def b3_clicked():
    global BUTTON_CHAR
    BUTTON_CHAR = "3"
    key_pressed(BUTTON_CHAR)


def b4_clicked():
    global BUTTON_CHAR
    BUTTON_CHAR = "4"
    key_pressed(BUTTON_CHAR)


def b5_clicked():
    global BUTTON_CHAR
    BUTTON_CHAR = "5"
    key_pressed(BUTTON_CHAR)


def b6_clicked():
    global BUTTON_CHAR
    BUTTON_CHAR = "6"
    key_pressed(BUTTON_CHAR)


def b7_clicked():
    global BUTTON_CHAR
    BUTTON_CHAR = "7"
    key_pressed(BUTTON_CHAR)


def back_button_clicked():
    global BOARD_PIECES_LABEL_INNER, BOARD_STATES
    for i in range(42):
        BOARD_PIECES_LABEL_INNER[i]["bg"] = COLOR[0]
        BOARD_STATES[i] = 0
    pack_menu()
    unpack_board()


def create_board():
    global BOARD_PIECES_LABEL_OUTER, BOARD_PIECES_LABEL_INNER, BOARD_PIECES_COUNTER, BOARD_BACK_FRAME
    global BOARD_BUTTONS, BOARD_BUTTONS_FRAME, BACK_BUTTON
    BOARD_BACK_FRAME = tk.LabelFrame(main, bg="#4f545c")

    BACK_BUTTON = tk.Button(main, image=BACK_BUTTON_IMG, bd=1, width=26, height=27, activebackground="#6a72ee",
                            command=back_button_clicked)

    for i in range(6):

        BOARD_PIECES_LABEL_OUTER[i] = tk.Label(BOARD_BACK_FRAME, bd=0, bg="#4f545c")
        BOARD_PIECES_LABEL_OUTER[i].pack()

        for j in range(7):
            BOARD_PIECES_LABEL_INNER.append(tk.Label(BOARD_PIECES_LABEL_OUTER[i], image=BOARD_PIECES_IMAGE, height=88,
                                                     width=88, bd=0, bg=COLOR[0]))
            BOARD_PIECES_LABEL_INNER[BOARD_PIECES_COUNTER].pack(side="left")
            BOARD_PIECES_COUNTER += 1

    BOARD_PIECES_LABEL_OUTER[0].pack_configure(pady=(10, 0))
    BOARD_PIECES_LABEL_OUTER[5].pack_configure(pady=(0, 10))

    for i in range(0, BOARD_PIECES_COUNTER, 7):
        BOARD_PIECES_LABEL_INNER[i].pack_configure(padx=(10, 0))
        BOARD_PIECES_LABEL_INNER[i + 7 - 1].pack_configure(padx=(0, 10))

    # BOARD_BUTTONS_FRAME = tk.LabelFrame(main, bg="#4f545c")
    BOARD_BUTTONS_FRAME = tk.LabelFrame(main, bg="#4f545c")

    for i in range(7):
        BOARD_BUTTONS.append(tk.Button(BOARD_BUTTONS_FRAME, width=86, bd=0, text="aa", image=BOARD_BUTTONS_IMG,
                                       height=56, bg="#6a72ee", activebackground="#bbcef8"))
        BOARD_BUTTONS[i].pack(side="left")

    BOARD_BUTTONS[0].pack_configure(padx=(10, 0))
    BOARD_BUTTONS[7 - 1].pack_configure(padx=(0, 10))

    BOARD_BUTTONS[0]["command"] = b1_clicked
    BOARD_BUTTONS[1]["command"] = b2_clicked
    BOARD_BUTTONS[2]["command"] = b3_clicked
    BOARD_BUTTONS[3]["command"] = b4_clicked
    BOARD_BUTTONS[4]["command"] = b5_clicked
    BOARD_BUTTONS[5]["command"] = b6_clicked
    BOARD_BUTTONS[6]["command"] = b7_clicked

    global PLAYER_1_SCOREBOARD, PLAYER_2_SCOREBOARD, PLAYER_1_INDICATOR, PLAYER_2_INDICATOR

    PLAYER_1_SCOREBOARD = tk.Label(main, bg="#4f545c", fg="White", font=("Yolissa", 15), anchor=tk.N,
                                   width=20, height=10)
    PLAYER_1_SCOREBOARD.propagate(0)
    PLAYER_2_SCOREBOARD = tk.Label(main, bg="#4f545c", fg="White", font=("Yolissa", 15), anchor=tk.N,
                                   width=20, height=10)
    PLAYER_2_SCOREBOARD.propagate(0)

    PLAYER_1_INDICATOR = tk.Label(PLAYER_1_SCOREBOARD, image=BOARD_IND_IMG, bd=0, width=80, height=50)
    PLAYER_1_INDICATOR.pack(pady=(180, 0))

    PLAYER_2_INDICATOR = tk.Label(PLAYER_2_SCOREBOARD, image=BOARD_IND_IMG, bd=0, width=80, height=50)
    PLAYER_2_INDICATOR.pack(pady=(180, 0))


def string_formatter(name, score):
    return "\n%s\n\n << SCORE >>\n▬▬▬\n%02d\n▬▬▬" % (name, score)
    #return f"\n{name}\n\nScore:\n▬▬▬\n{score}\n▬▬▬"


def pack_board():
    global BOARD_BACK_FRAME, BACK_BUTTON, PLAYER_1_SCOREBOARD, PLAYER_2_SCOREBOARD
    global BOARD_BUTTONS_FRAME, COIN_COUNTER

    COIN_COUNTER = 0

    BOARD_BACK_FRAME.pack(pady=(50, 0))
    BACK_BUTTON.place(x=15, y=15)
    BOARD_BUTTONS_FRAME.pack()

    PLAYER_1_SCOREBOARD.place(x=50, y=150)
    PLAYER_2_SCOREBOARD.place(x=1020, y=150)

    PLAYER_1_SCOREBOARD["text"] = string_formatter(PLAYER_1, SCORE_1)
    PLAYER_2_SCOREBOARD["text"] = string_formatter(PLAYER_2, SCORE_2)

    if CURRENT_CHANCE == 1:
        PLAYER_1_INDICATOR["bg"] = COLOR[CURRENT_CHANCE]
        PLAYER_2_INDICATOR["bg"] = "#4f545c"
    else:
        PLAYER_1_INDICATOR["bg"] = "#4f545c"
        PLAYER_2_INDICATOR["bg"] = COLOR[CURRENT_CHANCE]


def unpack_board():
    global BOARD_BACK_FRAME, BOARD_BUTTONS_FRAME, BACK_BUTTON
    BOARD_BACK_FRAME.pack_forget()
    BOARD_BUTTONS_FRAME.pack_forget()
    BACK_BUTTON.place_forget()
    global PLAYER_1_SCOREBOARD, PLAYER_2_SCOREBOARD
    PLAYER_1_SCOREBOARD.place_forget()
    PLAYER_2_SCOREBOARD.place_forget()
    global SCORE_1, SCORE_2
    SCORE_1 = SCORE_2 = 0


def create_menu():
    global MENU_FRAME, MENU_FRAME_P1_ENTRY, MENU_FRAME_P1_LABEL, MENU_FRAME_P2_ENTRY, MENU_FRAME_P2_LABEL
    global MENU_PLAY_BUTTON
    MENU_FRAME = tk.Label(main, bg="#4f545c", heigh=10, width=40, text="\nC O N N E C T  ◙◙◙◙", fg="White",
                          font=("Bumper Sticker DEMO", 20), anchor="n")
    MENU_FRAME_P1_LABEL = tk.Label(MENU_FRAME, bg="#4f545c", text="    PLAYER 1 NAME  >>", font=("Yolissa", 15),
                                   fg="White", width=50, anchor="w")
    MENU_FRAME_P1_ENTRY = tk.Entry(MENU_FRAME, bg="#2f3136", width=40, bd=1, font=("Yolissa", 20), fg="White")
    MENU_FRAME_P2_LABEL = tk.Label(MENU_FRAME, bg="#4f545c", text="    PLAYER 2 NAME  >>", font=("Yolissa", 15),
                                   fg="White", width=50, anchor="w")
    MENU_FRAME_P2_ENTRY = tk.Entry(MENU_FRAME, bg="#2f3136", width=40, bd=1, font=("Yolissa", 20), fg="White")
    MENU_PLAY_BUTTON = tk.Button(MENU_FRAME, text="P L A Y", bd=1, font=("Yolissa", 15), fg="White", height=1,
                                 bg="#6a72ee", width=47, activebackground="#5e67ee", activeforeground="white",
                                 command=play_clicked)


def pack_menu():
    global MENU_FRAME, MENU_FRAME_P1_ENTRY, MENU_FRAME_P1_LABEL, MENU_FRAME_P2_ENTRY, MENU_FRAME_P2_LABEL
    global MENU_PLAY_BUTTON

    MENU_FRAME.pack(pady=(180, 0))
    MENU_FRAME.propagate(0)
    MENU_FRAME_P1_LABEL.pack(pady=(90, 0))
    MENU_FRAME_P1_ENTRY.pack()
    MENU_FRAME_P2_LABEL.pack(pady=(20, 0))
    MENU_FRAME_P2_ENTRY.pack()
    MENU_PLAY_BUTTON.pack(pady=(20, 0))


def unpack_menu():
    global MENU_FRAME, MENU_FRAME_P1_ENTRY, MENU_FRAME_P1_LABEL, MENU_FRAME_P2_ENTRY, MENU_FRAME_P2_LABEL
    global MENU_PLAY_BUTTON
    MENU_FRAME.pack_forget()


def play_clicked():
    global PLAYER_1
    global PLAYER_2
    global CURRENT_CHANCE, THINKING
    CURRENT_CHANCE = rand(1, 2)
    PLAYER_1 = MENU_FRAME_P1_ENTRY.get().strip().title()
    PLAYER_2 = MENU_FRAME_P2_ENTRY.get().strip().title()

    if PLAYER_1 == "" or PLAYER_2 == "":
        if PLAYER_1 == "":
            PLAYER_1 = "Player-1"
        if PLAYER_2 == "":
            PLAYER_2 = "Player-2"

    elif PLAYER_1 == PLAYER_2:
        PLAYER_1 = PLAYER_1 + "-1"
        PLAYER_2 = PLAYER_2 + "-2"

    #print(PLAYER_1, PLAYER_2)
    unpack_menu()
    pack_board()
    THINKING = False


def game_loop(ch):
    # print(self)
    global CURRENT_CHANCE, BOARD_STATES, BOARD_PIECES_LABEL_INNER, THINKING, COIN_COUNTER
    Found = False
    Found_A = Found_B = 0
    BLINKER_COUNT = 0
    change_flag = False

    if ch in "1234567":

        THINKING = True
        for i in range(41 - (7 - int(ch)), -1, -7):
            if BOARD_STATES[i] == 0:
                COIN_COUNTER += 1
                BOARD_STATES[i] = CURRENT_CHANCE
                change_flag = True
                for j in range(int(ch) - 1, i, 7):
                    BOARD_PIECES_LABEL_INNER[j]["bg"] = COLOR[CURRENT_CHANCE]
                    sleep(0.05)
                    BOARD_PIECES_LABEL_INNER[j]["bg"] = COLOR[0]
                    sleep(0.02)
                BOARD_PIECES_LABEL_INNER[i]["bg"] = COLOR[CURRENT_CHANCE]
                break

        # Upwards search
        if not Found:
            for i in range(41, -1, -7):
                # print(f"ROW {(i+7)//7} {i}")
                for j in range(i, i - 4, -1):
                    flag = True
                    k = BOARD_STATES[j]
                    if k != 0:
                        for z in range(j, j - 4, -1):
                            if k != BOARD_STATES[z]:
                                flag = False
                                break
                        if flag:
                            Found_A, Found_B = j - 3, j
                            Found = True
                            break
                if Found:
                    BLINKER_COUNT = 1
                    break

        # Sidewards Search
        if not Found:
            for i in range(41, 41 - 7, -1):
                for j in range(i, i - 7 * 2 - 1, -7):
                    flag = True
                    k = BOARD_STATES[j]
                    if k != 0:
                        for z in range(j - 7, j - 7 * 3 - 1, -7):
                            if k != BOARD_STATES[z]:
                                flag = False
                                break
                        if flag:
                            Found_A, Found_B = j - 7 * 3, j
                            Found = True
                            break
                if Found:
                    BLINKER_COUNT = 7
                    break

        # Left Diagonal Search
        if not Found:
            for i in range(40, 37, -1):
                for j in range(i, i - 8 * (i - 38) - 1, -8):
                    flag = True
                    k = BOARD_STATES[j]
                    if k != 0:
                        for z in range(j - 8, j - 8 * 3 - 1, -8):
                            if k != BOARD_STATES[z]:
                                flag = False
                                break
                        if flag:
                            Found_A, Found_B = j - 8 * 3, j
                            Found = True
                            break
                if Found:
                    BLINKER_COUNT = 8
                    break

        # Left Diagonal Search
        if not Found:
            for i in range(41, 26, -7):
                for j in range(i, i - 8 * ((i + 1) // 7 - 4) - 1, -8):
                    flag = True
                    k = BOARD_STATES[j]
                    if k != 0:
                        for z in range(j - 8, j - 8 * 3 - 1, -8):
                            if k != BOARD_STATES[z]:
                                flag = False
                                break
                        if flag:
                            Found_A, Found_B = j - 8 * 3, j
                            Found = True
                            break
                if Found:
                    BLINKER_COUNT = 8
                    break

        if not Found:
            for i in range(36, 39, 1):
                for j in range(i, i - 6 * (38 - i) - 1, -6):
                    flag = True
                    k = BOARD_STATES[j]
                    if k != 0:
                        for z in range(j - 6, j - 6 * 3 - 1, -6):
                            if k != BOARD_STATES[z]:
                                flag = False
                                break
                        if flag:
                            Found_A, Found_B = j - 6 * 3, j
                            Found = True
                            break
                if Found:
                    BLINKER_COUNT = 6
                    break

        if not Found:
            for i in range(35, 20, -7):
                for j in range(i, i - 6 * (i // 7 - 3) - 1, -6):
                    flag = True
                    k = BOARD_STATES[j]
                    if k != 0:
                        for z in range(j - 6, j - 6 * 3 - 1, -6):
                            if k != BOARD_STATES[z]:
                                flag = False
                                break
                        if flag:
                            Found_A, Found_B = j - 6 * 3, j
                            Found = True
                            break
                if Found:
                    BLINKER_COUNT = 6
                    break

        # If match is found
        global SCORE_1, SCORE_2

        if COIN_COUNTER == 42:
            sleep(0.5)
            COIN_COUNTER = 0
            SCORE_1 += 1
            SCORE_2 += 1
            for i in range(42):
                BOARD_PIECES_LABEL_INNER[i]["bg"] = COLOR[0]
                BOARD_STATES[i] = 0

        if Found:
            COIN_COUNTER = 0
            m = BOARD_PIECES_LABEL_INNER[Found_A]["bg"]
            sleep(0.4)
            for i in range(4):
                for j in range(Found_A, Found_B + 1, BLINKER_COUNT):
                    BOARD_PIECES_LABEL_INNER[j]["bg"] = "white"
                sleep(0.2)
                for j in range(Found_A, Found_B + 1, BLINKER_COUNT):
                    BOARD_PIECES_LABEL_INNER[j]["bg"] = m
                sleep(0.2)
            for i in range(42):
                BOARD_PIECES_LABEL_INNER[i]["bg"] = COLOR[0]
                BOARD_STATES[i] = 0

            if COLOR.index(m) == 1:
                SCORE_1 += 1
                PLAYER_1_SCOREBOARD["text"] = string_formatter(PLAYER_1, SCORE_1)
            else:
                SCORE_2 += 1
                PLAYER_2_SCOREBOARD["text"] = string_formatter(PLAYER_2, SCORE_2)

        if change_flag:
            if CURRENT_CHANCE == 1:
                PLAYER_1_INDICATOR["bg"] = "#4f545c"
                PLAYER_2_INDICATOR["bg"] = COLOR[2]
            else:
                PLAYER_1_INDICATOR["bg"] = COLOR[1]
                PLAYER_2_INDICATOR["bg"] = "#4f545c"

            CURRENT_CHANCE = {1: 2, 2: 1}[CURRENT_CHANCE]
        THINKING = False


def key_pressed(self):
    if not THINKING:
        threading.Thread(target=game_loop, args=(self,), name="Thread-1").start()


def how_to_play():
    new = tk.Toplevel(main)
    new.title("How To Play ??")
    new.resizable(False, False)
    new.wm_iconbitmap("./images/Icon.ico")
    tk.Label(new, image=HOW_TO_PLAY_IMG, bd=0).pack()
    new.lift()
    new.geometry("{}x{}+{}+{}".format(500, 400, (main.winfo_screenwidth() - 500) // 2,
                                    (main.winfo_screenheight() - 400) // 2 - 50))

    new.mainloop()


if __name__ == "__main__":

    pyglet.font.add_file("./fonts/Bumper Sticker DEMO.otf")
    pyglet.font.add_file("./fonts/Yolissa Demo.otf")

    main = tk.Tk()
    main.resizable(False, False)
    main.wm_iconbitmap("./images/Icon.ico")
    main.title("Connect 4")
    main.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, (main.winfo_screenwidth() - WIDTH) // 2,
                                       (main.winfo_screenheight() - HEIGHT) // 2 - 50))

    BOARD_PIECES_IMAGE = tk.PhotoImage(file="./images/Board1.png")
    BACKGROUND_IMG = tk.PhotoImage(file="./images/BackGround.png")
    BOARD_BUTTONS_IMG = tk.PhotoImage(file="./images/BoardButton.png")
    BACK_BUTTON_IMG = tk.PhotoImage(file="./images/BackButton.png")
    BOARD_IND_IMG = tk.PhotoImage(file="./images/BoardInd.png")
    HOW_TO_PLAY_IMG = tk.PhotoImage(file="./images/HowToPlay.png")
    BACKGROUND = tk.Label(main, image=BACKGROUND_IMG)
    BACKGROUND.place(x=0, y=0, relheight=1, relwidth=1)

    HOW_TO_PLAY = tk.Button(main, text="How To Play ?", font=("Yolissa", 10), fg="White", activebackground="#5e67ee",
                            bg="#6a72ee", bd=1, command=how_to_play)
    HOW_TO_PLAY.place(x=15, y=680)

    create_menu()
    create_board()
    pack_menu()

    main.mainloop()
