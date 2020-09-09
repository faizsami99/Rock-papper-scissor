import tkinter
import tkinter.messagebox as msg
import random
# variables 

play_left = 5
com_win  = 0
player_win = 0
number = [0,1,2]
x = ["rock", "papper", "scissor"]

### play fucntion

def play(players_choice):
    global play_left, com_win, player_win , number, img_lst
    random.shuffle(number)
    com_choice = number[0]
    player_img.config(image=img_lst[players_choice])
    com_img.config(image=img_lst[com_choice])
    com_x = x[com_choice]
    player_x = x[players_choice]
    if player_x != com_x:
        if play_left != 0:
            if player_x == "rock":
                if com_x == "papper":
                    com_win += 1
                    com_hit.config(text=com_win)
                elif com_x == "scissor":
                    player_win += 1
                    player_hit.config(text=player_win)
                play_left -= 1
                play_left_.config(text=play_left)
            
            elif player_x == "papper":
                if com_x == "rock":
                    player_win += 1
                    player_hit.config(text=player_win)
                elif com_x == "scissor":
                    com_win += 1
                    com_hit.config(text=com_win)
                play_left -= 1
                play_left_.config(text=play_left)                  
            
            elif player_x == "scissor":
                if com_x == "rock":
                    com_win += 1
                    com_hit.config(text=com_win)
                elif com_x == "papper":
                    player_win += 1
                    player_hit.config(text=player_win)
                play_left -= 1
                play_left_.config(text=play_left)
        else:
            play_left -= 1
        

    else:
        play_left -= 1
        play_left_.config(text=play_left)
    
    if play_left == 0:
        if com_win > player_win:
            who_win.config(text="Computer")
        elif com_win == player_win:
            who_win.config(text="Draw")
        else:
            who_win.config(text="You")
    if play_left < 0:
        msg.showwarning("Warning", "Please restart game")

def restart():
    global play_left, com_win, player_win , number, img_lst
    play_left = 5
    play_left_.config(text=play_left)
    com_win  = 0
    com_hit.config(text=com_win)
    player_win = 0
    player_hit.config(text=player_win)
    who_win.config(text="restart")

main_frame = tkinter.Tk()
main_frame.geometry("585x620")
main_frame.resizable(0,0)
main_frame.config(background="light green")

## images which is going to be use
img_lst = [tkinter.PhotoImage(file="./images/rock.png"), tkinter.PhotoImage(file="./images/paper.png"), tkinter.PhotoImage(file="./images/scissors.png")]

# Lables score and heading


heading = tkinter.Label(main_frame, text="Rock, Papper, Scissors", bg="light green", fg="blue", font="helvetica 22 bold")
heading.place(x=125, y=12)

info = tkinter.Label(main_frame, text="Info: ", bg="light green", fg="red", font="helvetica 23 bold")
info.place(x=20,y=320)

who_win = tkinter.Label(main_frame, text="Who win", bg="light green", fg="red", font="helvetica 23 bold")
who_win.place(x=100,y=320)

score_left = tkinter.Label(main_frame, text="Life left :", bg="light green", fg="red", font="helvetica 23 bold")
score_left.place(x=20, y=80)

play_left_ = tkinter.Label(main_frame, text=play_left, bg="light green", fg="red", font="helvetica 23 bold")
play_left_.place(x=160, y=80)

computer_label = tkinter.Label(main_frame, text="Com win:",  bg="light green", fg="red", font="helvetica 23 bold")
computer_label.place(x=20, y=200)

com_hit = tkinter.Label(main_frame, text=com_win,   bg="light green", fg="red", font="helvetica 23 bold")
com_hit.place(x=180, y=200)

player_label = tkinter.Label(main_frame, text="player win:",  bg="light green", fg="red", font="helvetica 23 bold")
player_label.place(x=20, y=420)

player_hit = tkinter.Label(main_frame, text=player_win,   bg="light green", fg="red", font="helvetica 23 bold")
player_hit.place(x=190, y=420)

###Images
com_img = tkinter.Label(main_frame,bg="light green")
com_img.place(x=270,y=100)

player_img = tkinter.Label(main_frame,bg="light green")
player_img.place(x=270, y=320)

###Buttons


restart_button = tkinter.Button(main_frame, text="Restart", padx=7, pady=5, bg="orange", font="times 10 italic",activebackground="red",activeforeground="white", command= restart)
restart_button.place(x=45, y=510)

rock_button = tkinter.Button(main_frame, text="Rock", padx=50, pady=5, bg="orange", font="times 15 bold",activebackground="red",activeforeground="white", command=lambda: play(0))
rock_button.place(x=45,y=560)

papper_button = tkinter.Button(main_frame, text="Papper", padx=50, pady=5, bg="orange", font="times 15 bold",activebackground="red",activeforeground="white", command=lambda: play(1))
papper_button.place(x=200,y=560)

scissors_button = tkinter.Button(main_frame, text="Scissor", padx=50, pady=5, bg="orange", font="times 15 bold",activebackground="red", activeforeground="white", command=lambda: play(2))
scissors_button.place(x=372,y=560)

main_frame.mainloop()