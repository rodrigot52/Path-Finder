import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#","#","#","#","#","#","#"],
    ["#", " ", " "," "," "," "," "," ","#"],
    ["#", " ", "#","#"," ","#","#"," ","#"],
    ["#", " ", "#"," "," "," ","#"," ","#"],
    ["#", " ", "#"," ","#"," ","#"," ","#"],
    ["#", " ", "#"," ","#"," ","#"," ","#"],
    ["#", " ", "#"," ","#"," ","#"," ","#"],
    ["#", " ", " "," "," "," "," "," ","#"],
    ["#", " ", "#"," ","#"," ","#","X","#"],
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path
        
        vizinhos = find_vizinhos(maze, row, col)
        for vizinho in vizinhos:
            if vizinho in visited:
                continue

            r, c = vizinho
            if maze[r][c] == "#":
                continue

            new_path = path + [vizinho]
            q.put((vizinho, new_path))
            visited.add(vizinho)

def find_vizinhos(maze, row, col):
    vizinhos = []

    if row > 0: # UP
        vizinhos.append((row - 1, col))
    if row + 1 < len(maze): # Down
        vizinhos.append((row + 1, col))
    if col > 0: # LEFT
        vizinhos.append((row, col -1))
    if col + 1 < len(maze[0]): # Right
        vizinhos.append((row, col + 1))
    
    return vizinhos

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.getch()

wrapper(main)