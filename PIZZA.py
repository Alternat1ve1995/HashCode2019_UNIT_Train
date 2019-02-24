from Task import Task

def get_possible_shapes_v1(task):
    min_size = task.min_ing * 2
    shape = []
    i = 0
    shape.append([0, min_size - 1])
    while True:
        while (shape[-1][0] + 1) * (shape[-1][1] + 2) <= task.max_cells:
            shape.append([shape[-1][0], shape[-1][1] + 1])

        if (shape[-1][0] + 1) * (shape[-1][1] + 1)  > task.max_cells:
            break
        m = 0
        while (shape[-1][0] + 2) * (m + 1) < min_size:
            m += 1
        shape.append([shape[-1][0] + 1, m])
    return shape


def get_possible_shapes(task):
    min_size = task.min_ing * 2
    shape = []
    for i in range(task.max_cells):
        for j in range(task.max_cells):
            shape.append([i, j])
    out = []
    for sh in shape:
        if (sh[0] + 1) * (sh[1] + 1) >=min_size and (sh[0] + 1) * (sh[1] + 1) <= task.max_cells:
            out.append(sh)
    return out



def read_file(fname):
    data = None
    with open(fname, 'r') as f:
        data = f.readlines()
    inp = list(map(int, data[0].split(' ')))
    task = Task(inp[0], inp[1], inp[2], inp[3], data[1:])
    return task

def get_input(filename):
    task = read_file(filename)
    shapes = get_possible_shapes(task)
    return shapes, task

print()