class Task:

    def __init__(self, rows, columns, min_ing, max_cells, map):
        self.rows = rows
        self.columns = columns
        self.min_ing = min_ing
        self.max_cells = max_cells
        map_new = []
        for l in map:
            if l[-1] == '\n':
                l = l[:-1]
            map_new.append(l)
        self.map = map_new
