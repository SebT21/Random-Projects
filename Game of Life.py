#Author: Sebastian Tampu

#The purpose of this code is to create a representation of 
#Conway's "Game of Life" using random initial conditions.

import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from pylab import clf, pause, draw


N = 100 #Array size


#Initializes zero-array
automaton = np.zeros([N,N,2*N],int)


for i in range(10*N):
    
    #Generate two random numbers
    x,y = randrange(1,N-1),randrange(1,N-1)
    
    #Makes sure the set of number is not the same as a previous set
    while automaton[y,x,0] == 1:
        x,y = randrange(1,N-1),randrange(1,N-1)
    
    #Initialize cell value to 1, makes it a live cell
    automaton[y,x,0] = 1


#Checks number of live cells around a cell by adding all surrounding values
def neighbourCheck(automaton):
    return automaton[i+1,j-1,k]+automaton[i+1,j,k]+automaton[i+1,j+1,k]+automaton[i,j-1,k]+automaton[i,j+1,k]+automaton[i-1,j-1,k]+automaton[i-1,j,k]+automaton[i-1,j+1,k]
    

#Defines the various rules of the "Game of Life"
def rules(automaton):
    if automaton[i,j,k] == 1 and neighbourCheck(automaton) < 2:
        return 0
    elif automaton[i,j,k] == 1 and neighbourCheck(automaton) == 2:
        return 1
    elif automaton[i,j,k] == 1 and neighbourCheck(automaton) == 3:
        return 1
    elif automaton[i,j,k] == 1 and neighbourCheck(automaton) > 3:
        return 0
    elif automaton[i,j,k] == 0 and neighbourCheck(automaton) == 3:
        return 1
    elif automaton[i,j,k] == 0 and neighbourCheck(automaton) != 3:
        return 0


#Main Loop
for k in range(2*N-1):
    for i in range(1,N-1):
        for j in range(1,N-1):
            #Assigns value of the cells at the next time-step
            automaton[i,j,k+1] = rules(automaton) 
 
    
#Plots a simple animation
for i in range(2*N):
    clf() # clear the plot
    plt.imshow(automaton[:,:,i],"gray",origin='lower') 
    plt.ylabel("y-Position")
    plt.xlabel("x-Position")
    plt.title("Game of Life")
    draw()
    pause(0.03) #pause to allow a smooth animation
    
