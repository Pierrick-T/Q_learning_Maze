#importing the packages
import numpy as np
import time
import sys
import tkinter as tk

UNIT = 40
Maze_H = 6  #size of the maze
Maze_W = 6

class Maze:

    def __init__(self):
        self.window=tk.Tk()
        self.window.title("maze with Q-learning")
        self.window.geometry('{0}x{1}'.format(Maze_W*UNIT, Maze_H*UNIT))
        self.action_space= ['u','d','l','r']
        self.n_action = len(self.action_space)
        self.build_maze()

    def build_maze(self):
        self.canvas = tk.Canvas(self.window, bg='white', width=Maze_W*UNIT, height=Maze_H*UNIT)

        for c in range(0,Maze_W*UNIT, UNIT): #creating the columns
            x0, y0, x1, y1 = c, 0, c, Maze_W*UNIT
            self.canvas.create_line(x0, y0, x1, y1)

        for r in range(0, Maze_H*UNIT, UNIT): #creating the rows
            x0, y0, x1, y1 = 0, r, Maze_H*UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        origin = np.array([20, 20])

        hell1_center = origin + np.array([UNIT*2, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15, fill='black'
        )

        hell2_center = origin + np.array([UNIT, UNIT*2])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15, fill='black'
        )

        oval_center = origin + UNIT*2
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15, fill='yellow'
        )


        self.rectangle = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15, fill='red'
        )
        self.canvas.pack()

    def render(self):
        time.sleep(0.1)
        self.window.update()

    def reset(self):
        self.window.update()
        time.sleep(.5)
        self.canvas.delete(self.rectangle)


        origin = np.array([20, 20])
        self.rectangle = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15, fill='red'
        )
        return self.canvas.coords(self.rectangle)

    def get_state_reward(self, action):
        s = self.canvas.coords(self.rectangle)
        base_action = np.array([0,0])
        if action == 0: # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1: #down
             if s[1] < (Maze_H - 1)*UNIT:
                    base_action[1] +=UNIT
        elif action == 2: #right
            if s[0] < (Maze_W - 1)*UNIT:
                    base_action[0] += UNIT
        elif action == 3: #left
            if s[0] > UNIT:
                    base_action[0] -= UNIT

        self.canvas.move(self.rectangle, base_action[0], base_action[1])
        s_ = self.canvas.coords(self.rectangle)
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
            s_ = 'terminal'

        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2)]:
            reward = -1
            done = True
            s_ = 'terminal'

        else:
            reward = 0
            done = False
        return s_, reward, done



if __name__=="__main__":
    maze = Maze()
    maze.build_maze()
    maze.window.mainloop()
