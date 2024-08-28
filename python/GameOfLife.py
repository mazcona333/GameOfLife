import numpy as np

class Cell: ## TODO Cell max lifespan
    position: tuple[int, int]
    _neighbors = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    neighbors = tuple[tuple[int, int]]
    
    def __init__(self, x, y):
        self.position = (x, y)
        self.neighbors = ()
        for i in range(len(self._neighbors)):
            self.neighbors += ((self._neighbors[i][0] + self.position[0], self._neighbors[i][1] + self.position[1]),)
    def __eq__(self, other: tuple[int, int]) -> bool:
        return self.position == other
    def __str__(self) -> str:
        return self.position.__str__()
    def __repr__(self) -> str:
        return self.position.__str__()
    def __hash__(self) -> int:
        return hash(self.position)

class Grid:
    def __init__(self, cells: set[Cell]):
        self.cells = cells

    def count_neighbors(self, cell: Cell) -> int:
        count = 0
        for n in cell.neighbors:
            if(Cell(n[0], n[1]) in self.cells and n != cell):
                count += 1
        return count

    def update(self):
        alive_cells = set()
        born_cells = set()
        for c in self.cells:
            n_neighbors = self.count_neighbors(c)
            if(n_neighbors == 2 or n_neighbors == 3):
                alive_cells.add(c)
            for n in c.neighbors:
                n_neighbors = self.count_neighbors(Cell(n[0],n[1]))
                if(n_neighbors == 3):
                    born_cells.add(Cell(n[0], n[1]))
        self.cells = alive_cells | born_cells
        return self

    def display(self):
        for i in range(-5, 5):
            for j in range(-5, 5):
                if(Cell(i,j) in self.cells):
                    print("x", end = "")
                else:
                    print(".", end = "")
            print()
        print()
    
initial = [Cell(2,0), Cell(1,0), Cell(0,0)]

grid = Grid(initial)
grid.display()
for i in range(10):
    grid.update().display()