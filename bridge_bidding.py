import tkinter as tk
from after1NT_opening import after1NT_opening
class BridgeGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("橋牌叫牌展示")

        self.reset_frame = tk.Frame(self.root, width=100, height=100)
        self.reset_frame.pack(side="right")
        
        self.c_frame = tk.Frame(self.root, width=200, height=800)
        self.c_frame.pack(side= "right")

        self.a_frame = tk.Frame(self.root, width=600, height=400)
        self.a_frame.pack(side="top")

        self.b_frame = tk.Frame(self.root, width=300, height=400)
        self.b_frame.pack(side="bottom")

        self.bid_options = ['1C', '1D', '1H', '1S', '1NT', '2C', '2D', '2H', '2S', '2NT', '3C', '3D', '3H', '3S', '3NT', '4C', '4D', '4H', '4S', '4NT', '5C', '5D', '5H', '5S', '5NT', '6C', '6D', '6H', '6S', '6NT', '7C', '7D', '7H', '7S', '7NT', 'P', 'X', 'XX']
        self.progress = {'N': [], 'E': [], 'S': [], 'W': []}
        self.player_positions = {'N': (200, 50), 'E': (350, 200), 'S': (200, 350), 'W': (50, 200)}
        self.current_player = 'N'
        self.current_bid = 'none'
        self.current_bid2 = 'none'
        self.current_bid3 = 'none'
        self.current_bid4 = 'none'
        self.max_bid = 'none'
        self.min_bid = 'none'
        self.open_player = 'none'
    
        self.draw_bid_options()

    def draw_bid_options(self):
        num_cols = 5
        num_rows = len(self.bid_options) // num_cols + 1

        for i, bid in enumerate(self.bid_options):
            row = i // num_cols
            col = i % num_cols
            button_state = 'normal' if self.is_bid_enabled(bid,self.max_bid) else 'disabled'

            button = tk.Button(self.b_frame, text=bid, command=lambda b=bid: self.update_progress(b), state=button_state)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        

    def is_bid_enabled(self, bid, max_bid):
        if max_bid != 'none' and self.current_bid == 'P' and self.current_bid2 == 'P' and self.current_bid3 == 'P':
            return False
        elif max_bid == 'none' and self.current_bid == 'P' and self.current_bid2 == 'P' and self.current_bid3 == 'P' and self.current_bid4 == 'P':
            return False
        elif max_bid == 'none' and self.current_bid == 'P' and self.current_bid2 == 'P' and self.current_bid3 == 'P':
            return True
        elif bid == 'X':
            return self.current_bid !='none' and self.current_bid != 'X'  and self.current_bid != 'XX' and self.max_bid != 'none' and not(self.current_bid == 'P' and (self.current_bid2 == 'XX' or self.current_bid2 =='X')) and not(self.current_bid == 'P' and self.current_bid2 == 'P' and (self.current_bid3 == 'X' or self.current_bid3 =='XX'))# 当前玩家不是'X'时，'X'按钮才可用
        elif bid == 'XX':
            return self.current_bid == 'X' or (self.current_bid == 'P' and self.current_bid2 == 'X') or (self.current_bid == 'P' and self.current_bid2 == 'P' and self.current_bid3 == 'X') # 当前玩家为'X'时，'XX'按钮才可用
        elif self.current_bid != 'X' and self.current_bid != 'XX' and self.current_bid != 'P':
            smaller_bids = self.bid_options[self.bid_options.index(bid):]
            return self.current_bid not in smaller_bids
        elif self.current_bid == 'X' or self.current_bid == 'XX' or self.current_bid == 'P':
            smaller_bids = self.bid_options[self.bid_options.index(bid):]
            return max_bid not in smaller_bids
        else:
            return True

    def update_progress(self, bid):
        if bid != 'P' and self.current_bid == 'none' and self.current_bid2 == 'none' and self.current_bid3 =='none':
            self.min_bid = bid
            self.open_player = self.current_player
        self.current_bid4 = self.current_bid3
        self.current_bid3 = self.current_bid2
        self.current_bid2 = self.current_bid
        self.current_bid = bid
        if self.current_bid != 'X' and self.current_bid != 'XX' and self.current_bid != 'P':
            self.max_bid = self.current_bid
        self.progress[self.current_player].append(bid)
        if self.current_player == 'N':
            self.current_player = 'E'
        elif self.current_player == 'E':
            self.current_player = 'S'
        elif self.current_player == 'S':
            self.current_player = 'W'
        elif self.current_player == 'W':
            self.current_player = 'N'
        # print(self.max_bid,'86')
        self.update_reset_frame()
        self.update_c_frame()
        self.update_a_frame()
        self.b_frame.destroy()
        self.b_frame = tk.Frame(self.root, width=300, height=400)
        self.b_frame.pack(side="bottom")
        self.draw_bid_options()
    def update_reset_frame(self):
        self.reset_frame.destroy()
        self.reset_frame = tk.Frame(self.root, width=100, height=100)
        self.reset_frame.pack(side="right")
        if self.current_bid == 'none' and self.current_bid2 == 'none' and self.current_bid3 =='none':
            state_buttom = 'disable'
        else:
            state_buttom = 'active'
        self.undo_button = tk.Button(self.reset_frame, text="上一步", command=self.undo_progress, state=state_buttom)
        self.undo_button.pack(side="right", padx=10, pady=10)
        self.reset_button = tk.Button(self.reset_frame, text="重置", command=self.reset_game)
        self.reset_button.pack(side="left", padx=10, pady=10)
    def update_a_frame(self):
        self.a_frame.destroy()
        self.a_frame = tk.Frame(self.root, width=600, height=400)
        self.a_frame.pack(side="top")

        for player, bid in self.progress.items():
            label_text = f'{player}: {", ".join(self.progress[player])}'
            label = tk.Label(self.a_frame, text=label_text, font=('Arial', 16))
            label.place(x=self.player_positions[player][0], y=self.player_positions[player][1])
    
    def update_c_frame(self):
        self.c_frame.destroy()
        self.c_frame = tk.Frame(self.root, width=200, height=800)
        self.c_frame.pack(side="right")
        bid_mean = 'nothing to say'
        bid_list_temp = []
        bid_list = []
        for player,bid in self.progress.items():
            bid_list_temp.append(bid)
        i = 0
        while True:
            try:
                for j in range(4):
                    bid_list.append(bid_list_temp[j][i])
                i+=1
            except:
                break
        if self.open_player == 'N':
            open_player_number = 0
        elif self.open_player == 'E':
            open_player_number = 1
        elif self.open_player == 'S':
            open_player_number = 2
        elif self.open_player == 'W':
            open_player_number = 3
        #1NT後續
        if self.min_bid == '1NT':
            bid_mean = after1NT_opening(open_player_number, self.current_bid, self.min_bid, bid_list)
        #之後可以補其他
        label = tk.Label(self.c_frame, text=bid_mean, font=('Arial',16))
        label.pack()
    def start(self):
        self.root.mainloop()
    
    def reset_game(self):
        self.current_player = 'N'
        self.current_bid = 'none'
        self.current_bid2 = 'none'
        self.current_bid3 = 'none'
        self.max_bid = 'none'
        self.progress = {'N': [], 'E': [], 'S': [], 'W': []}
        self.c_frame.destroy()
        self.reset_frame.destroy()
        self.update_a_frame()
        self.b_frame.destroy()
        self.b_frame = tk.Frame(self.root, width=300, height=400)
        self.b_frame.pack(side="top")
        self.draw_bid_options()

    def undo_progress(self):
        self.current_player = self.undo_player(self.current_player)
        self.progress[self.current_player] = self.progress[self.current_player][:-1]

        current_player = self.undo_player(self.current_player)
        current_player2 = self.undo_player(current_player)
        current_player3 = self.undo_player(current_player2)
        current_player4 = self.undo_player(current_player3)
        # print('173',current_player,current_player2,current_player3,current_player4)
        try:
            self.current_bid = self.progress[current_player][-1]
        except:
            self.current_bid = 'none'
        try:
            self.current_bid2 = self.progress[current_player2][-1]
        except:
            self.current_bid2 = 'none'
        try:
            self.current_bid3 = self.progress[current_player3][-1]
        except:
            self.current_bid3 = 'none'
        try:
            self.current_bid4 = self.progress[current_player4][-1]
        except:
            self.current_bid4 = 'none'
        try:
            if  self.progress[current_player][-1] not in {'P', 'X', 'XX'}:
                self.max_bid = self.progress[current_player][-1]
        except:
            self.progress[current_player] = []
            self.max_bid = 'none'
        
        if self.current_bid == 'P':
            if self.current_bid2 == 'P':
                if self.current_bid3 == 'P':
                    self.max_bid = 'none'
                    if self.current_bid4 == 'P':
                        self.max_bid = 'none'
                    else:
                        self.max_bid = self.current_bid4
                else:
                    self.max_bid = self.current_bid3
            else:
                self.max_bid = self.current_bid2
        else:
            self.max_bid = self.current_bid
        # print(self.max_bid,'211')
        # print(self.current_bid,self.current_bid2,self.current_bid3,self.current_bid4)
        self.update_reset_frame()        
        self.update_c_frame()
        self.update_a_frame()
        self.b_frame.destroy()
        self.b_frame = tk.Frame(self.root, width=300, height=400)
        self.b_frame.pack(side="bottom")
        self.draw_bid_options()
    def undo_player(self,current_player):
        if current_player == 'N':
            temp = 'W'
        elif current_player == 'W':
            temp = 'S'
        elif current_player == 'S':
            temp = 'E'
        elif current_player == 'E':
            temp = 'N'
        return temp

if __name__ == "__main__":
    game = BridgeGameGUI()
    game.start()
