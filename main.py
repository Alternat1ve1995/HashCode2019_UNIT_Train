from Answer import Answer
from PIZZA import get_input
import numpy as np

ans = Answer()

def check_valid(task, v, i, j, piece):
    t = 0
    m = 0
    for k in range(piece[0] + 1):
        for l in range(piece[1] + 1):
            if i + k >= task.rows or j + l >= task.columns:
                return False
            if v[i + k][j + l] != 0:
                return False
            if task.map[i + k][j + l] == 'T':
                t += 1
            else:
                m += 1
    if t >= task.min_ing and m >= task.min_ing:
        return True
    return False


def walk_pizza(task, pieces):
    global ans
    arr = task.map
    v = np.zeros((task.rows, task.columns))
    for i in range(task.rows):
        for j in range(task.columns):
            for piece in pieces:
                if check_valid(task, v, i, j, piece):
                    ans.put([i, j, i + piece[0], j + piece[1]])
                    for k in range(piece[0] + 1):
                        for l in range(piece[1] + 1):
                            v[i + k][j + l] = 1


def go_all():
    global ans
    files = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_big.in']
    for file in files:
        main(file)
        with open(file.split('.')[0] + '.out', 'w') as f:
            f.write(str(ans))
        ans.clear()

def main(file):
    global ans
    a, task = get_input(file)
    a.sort(key=lambda x: (x[0] + 1) * (x[1] + 1))
    walk_pizza(task, a)
    print("DONE", file)

go_all()