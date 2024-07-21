import turtle
import time
import random
import tkinter as tk
import collections

class TurtleRaceGame:
    def __init__(self,master):
        self.master = master
        self.master.title("Turtle Race")
        self.master.geometry("900x650")
        self.master.configure(bg='light blue')
        
        self.width=700
        self.height=600
        self.colors=['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
        self.initialize_gui()
        self.count_enter=0
        self.no_of_players=0
        self.input_no_of_players()
        # self.no_of_players=5
        self.enter_val=''
        # self.dic=collections.defaultdict(list)
        
    
    def initialize_gui(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        
        self.input_no_of_players_display = tk.Label(self.master, text='', font=("Helvetica", 20), bg='light blue')
        self.input_no_of_players_display.pack(pady=(30, 10))
        self.word_display = tk.Label(self.master, text="_ " *12, font=("Helvetica", 30), bg='light blue')
        self.word_display.pack(pady=(90, 100))
        # self.restart_button = tk.Button(self.master, text='', command=self.restart(), width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        # self.restart_button.pack(pady=(10, 0))
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        self.setup_alphabet_buttons()
        
        

    def setup_alphabet_buttons(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")

        # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = '1234567890'
        # upper_row = alphabet[:13]
        # lower_row = alphabet[13:]

        # upper_frame = tk.Frame(self.buttons_frame)
        # upper_frame.pack()
        # lower_frame = tk.Frame(self.buttons_frame)
        # lower_frame.pack()
        num_frame = tk.Frame(self.buttons_frame)
        num_frame.pack()

        # for letter in upper_row:
        #     button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.typing_data(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
        #     button.pack(side="left", padx=2, pady=2)

        # for letter in lower_row:
        #     button = tk.Button(lower_frame, text=letter, command=lambda l=letter: self.typing_data(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
        #     button.pack(side="left", padx=2, pady=2)
            
        for num in number:
            button = tk.Button(num_frame, text=num, command=lambda l=num: self.typing_data(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=2, pady=2)
        
        button = tk.Button(num_frame, text='Enter', command=lambda l='enter': self.cal_enter_val(l), width=8, height=2, bg=button_bg, fg=button_fg, font=button_font)
        button.pack(side="left", padx=2, pady=2)
        
    def cal_enter_val(self,l):
        
        self.no_of_players=int(self.enter_val)
        self.count_enter+=1
            
        self.enter_val=''
        self.word_display.config(text=self.enter_val)
        self.input_no_of_players_display.config(text='')
        self.start_game()
        
        # print(l)
        # if(self.count_enter==0):
        #     # print(l+'1')
        #     self.no_of_players=int(self.enter_val)
        #     self.count_enter+=1
            
        #     self.enter_val=''
            
            
                
            # self.start_game()
        

    def typing_data(self,letter):
        self.enter_val+=letter 
        self.word_display.config(text=self.enter_val)
        
    def input_no_of_players(self):
        self.input_no_of_players_display.config(text='Enter the number of racers (2 - 10)')
        
    
    def init_turtle(self):
        screen = turtle.Screen()
        screen.setup(self.width, self.height)
        screen.title('Turtle Racing!')
        
        
    def game_over(self,winner):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        
        print("The winner is the turtle with color:", winner)
        # self.input_no_of_players_display.config(text='')
        self.word_display.config(text=f"The winner is the turtle with color: {winner}")
        time.sleep(5)
        turtle.clear()
        if not hasattr(self, 'restart_button'):
            self.restart_button = tk.Button(self.master, text="Restart Game", command=self.restart, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        self.restart_button.pack(pady=(10, 20))
    
    def start_game(self):
        self.init_turtle()
        
        random.shuffle(self.colors)
        colors = self.colors[:self.no_of_players]
        
        winner = self.race(colors)
        print("The winner is the turtle with color:", winner)
        self.game_over(winner)
        # self.input_no_of_players_display.config(text='')
        # self.word_display.config(text=f"The winner is the turtle with color: {winner}")
        # self.restart_button.config(text='Restart')
        
    
    def race(self, colors):
        turtles = self.create_turtles(colors)

        while True:
            for racer in turtles:
                distance = random.randrange(1, 20)
                racer.forward(distance)

                x, y = racer.pos()
                if y >= self.height // 2 - 10:
                    return colors[turtles.index(racer)]
    
    def create_turtles(self, colors):
        turtles = []
        spacingx = self.width // (len(colors) + 1)
        for i, color in enumerate(colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-self.width//2 + (i + 1) * spacingx, -self.height//2 + 20)
            racer.pendown()
            turtles.append(racer)
        return turtles

    def restart(self):
        self.count_enter=0
        self.no_of_players=0
        self.enter_val=''
        self.word_display.config(text='_ '*12)
        # self.dic=collections.defaultdict(list)
        
        self.buttons_frame.pack_forget()
        
        for frame in self.buttons_frame.winfo_children():
            for button in frame.winfo_children():
                button.configure(state=tk.NORMAL)
        
        # self.restart_button.pack(pady=(10, 0))
        
        if hasattr(self, 'restart_button') and self.restart_button.winfo_exists():
            self.restart_button.pack_forget()
        
        self.buttons_frame.pack()
        self.input_no_of_players()
    
def main():
    root = tk.Tk()
    TurtleRaceGame(root)
    root.mainloop()


main()


