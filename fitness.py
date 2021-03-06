# -*- coding: utf-8 -*-
"""fitness

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ogSwHwFMbnkVmNKbJhK6ybRRG7vkUsWo
"""

import chess
import sys
import os
import random
py_file_location="/content/drive/MyDrive/Chess/"
sys.path.append(os.path.abspath(py_file_location))
import eval_network
import monte_carlo_opt
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt 
import time
#print('je suis un retard 1')
def fitness(agents):
    #print('je suis un retard 2')
    for agent in range(len(agents)-1):
        game = []
        board = chess.Board()
        
        other_agents = agents
        player_2 = random.choice(agents)
        
        player_1_idx = agent+1
        player_2_idx = agents.index(player_2)+1
        
        player_1 = agents[agent]

        counter = 0
        print('Game Started between Agent',player_1_idx,'and Agent',player_2_idx)
        while counter < 100 and counter %2 ==0 and board.is_game_over() == False:
            model  = player_1.neural_network
            counter+=1
        def evaluation(input):
           
           print(input)
           pred = model(input.reshape(1, 8, 8, 12))
           
           

        
        move =  monte_carlo_opt.monte_carlo_algo(board,evaluation,epochs = 5,depth = 5)
        game.append(move)   
        print(move)
        model = player_2.neural_network
            
        move =  monte_carlo_opt.monte_carlo_algo(board,evaluation,epochs = 5,depth = 5)
        game.append(move)
        counter += 1

        agents[player_1_idx].game = game
        agents[player_2_idx].game = game
        

        if board.is_checkmate:
            if counter % 4 == 0:
                agents[player_1_idx].fitness *= 1.5
                agents[player_2_idx].fitness *= 0.8
            else:
                agents[player_2_idx].fitness *= 1.5
                agents[player_1_idx].fitness *= 0.8
    return agents