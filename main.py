from Answer import Answer, Piece
from PIZZA import get_input
import numpy as np

ans = Answer()

def check_valid(task, v, i, j, piece, num=0):
    t = 0
    m = 0
    for k in range(piece[0] + 1):
        for l in range(piece[1] + 1):
            if i + k >= task.rows or j + l >= task.columns or i + k < 0 or j + l < 0:
                return False
            if v[i + k][j + l] != 0 and v[i + k][j + l] != num:
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
    pie_count = 1
    for i in range(task.rows):
        for j in range(task.columns):
            for piece in pieces:
                if check_valid(task, v, i, j, piece):
                    ans.put([i, j, i + piece[0], j + piece[1]])
                    for k in range(piece[0] + 1):
                        for l in range(piece[1] + 1):
                            v[i + k][j + l] = pie_count
                    pie_count += 1
    return v


def razpanah(task, v, pieces):
    global ans
    # for pie_coord in range(len(ans.all) - 1, -1, -1):
    for pie_coord in range(len(ans.all)):
        br = False
        pie = ans.all[pie_coord]
        for big_pie in pieces[::-1]:
            if (big_pie[0] + 1) * (big_pie[1] + 1) > (pie.xe - pie.xs + 1) * (pie.ye - pie.ys + 1):
                pie_n = v[pie.xs][pie.ys]
                st_poi = [pie.xs - big_pie[0], pie.ys - big_pie[1]]
                for i in range(big_pie[0] + 1):
                    for j in range(big_pie[1] + 1):
                        if check_valid(task, v, st_poi[0] + i, st_poi[1] + j, big_pie, num=pie_n):
                            v[v == pie_n] = 0
                            ans.all[pie_coord] = Piece(st_poi[0] + i, st_poi[1] + j, st_poi[0] + i + big_pie[0], st_poi[1] + j + big_pie[1])
                            for k in range(big_pie[0] + 1):
                                for l in range(big_pie[1] + 1):
                                    v[st_poi[0] + i + k][st_poi[1] + j + l] = pie_n
                            br = True
                        if br:
                            break
                    if br:
                        break
            if br:
                break
    print(len(v[v == 0]), task.rows * task.columns, len(v[v == 0]) / (task.rows * task.columns))


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
    v = walk_pizza(task, a)
    razpanah(task, v, a)
    print("DONE", file)

go_all()
# main('a_example.in')

# 0 15 0.0
# DONE a_example.in
# 2 42 0.047619047619047616
# DONE b_small.in
# 1072 50000 0.02144
# DONE c_medium.in
# 98135 1000000 0.098135
# DONE d_big.in