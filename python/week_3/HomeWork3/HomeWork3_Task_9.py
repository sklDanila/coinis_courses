# task_9

import random

class Tournament:
    def __init__(self):
        self.tournament_name = ""
        self.player_list = []
        self.number_of_rounds = 0
        
    def get_tournament_name(self):
        return self.tournament_name
    def set_tournament_name(self, name):
        self.tournament_name = name
    def get_player_list(self):
        return self.player_list
    def set_player_list(self, player_list):
        self.player_list = player_list
    def get_number_of_rounds(self):
        return self.number_of_rounds
    def set_number_of_rounds(self, number_of_rounds):
        if 0 < number_of_rounds <= 10:
            self.number_of_rounds = number_of_rounds
        else:
            print("Error! Number of rounds should be between 1 and 10.")
            
    def add_player(self, player_name):
        self.player_list.append(tuple(player_name, 0))
    def remove_player(self, player_name):
        for player in self.player_list:
            if player[0] == player_name:
                self.player_list.remove(player)
                break
        else:
            print("Player not found!")
    def display_best_player(self):
        max_points = 0
        name_of_best_player = ""
        for player in self.player_list:
            if player[1] > max_points:
                max_points = player[1]
                name_of_best_player = player[0]
        print(f"The best player is {name_of_best_player} with {max_points} points.")
    def start_round(self):
        player1, player2 = random.sample(self.player_list, 2)
        
        print(f"Round: {self.number_of_rounds + 1}")
        print(f"Players: {player1[0]} vs {player2[0]}")
    
        winner = None
        if random.random() < 0.6:
            winner = player1
        else:
            winner = player2
    
        winner[1] += 1
        print(f"Winner: {winner[0]}")
    
        self.number_of_rounds += 1