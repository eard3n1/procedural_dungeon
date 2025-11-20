import random

class Room:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def center(self):
        return self.x + self.w // 2, self.y + self.h // 2

def generate_dungeon(
        width=128,
        height=128,
        max_rooms=15,
        max_size=30,
        min_size=5,  
        seed=None
    ):
    
    random.seed(seed)

    grid = [[1 for _ in range(width)] for _ in range(height)]
    rooms = []

    for _ in range(max_rooms):
        w = random.randint(min_size, max_size)
        h = random.randint(min_size, max_size)
        x = random.randint(1, width - w - 1)
        y = random.randint(1, height - h - 1)
        new_room = Room(x, y, w, h)

        if any(intersects(new_room, r) for r in rooms):
            continue

        for yy in range(y, y + h):
            for xx in range(x, x + w):
                grid[yy][xx] = 0

        if rooms:
            prev_center = clamp_point(rooms[-1].center(), width, height)
            new_center = clamp_point(new_room.center(), width, height)
            carve_corridor(grid, prev_center, new_center)
        rooms.append(new_room)
    return grid, rooms, seed

def intersects(r1, r2):
    return not (r1.x + r1.w < r2.x or r1.x > r2.x + r2.w or
                r1.y + r1.h < r2.y or r1.y > r2.y + r2.h)

def clamp_point(p, width, height):
    x, y = p
    x = max(0, min(x, width - 1))
    y = max(0, min(y, height - 1))
    return x, y

def carve_corridor(grid, a, b):
    ax, ay = a
    bx, by = b
    height = len(grid)
    width = len(grid[0])

    ax = max(0, min(ax, width - 1))
    bx = max(0, min(bx, width - 1))
    ay = max(0, min(ay, height - 1))
    by = max(0, min(by, height - 1))

    if random.random() < 0.5:
        for x in range(min(ax, bx), max(ax, bx) + 1):
            grid[ay][x] = 0
        for y in range(min(ay, by), max(ay, by) + 1):
            grid[y][bx] = 0
    else:
        for y in range(min(ay, by), max(ay, by) + 1):
            grid[y][ax] = 0
        for x in range(min(ax, bx), max(ax, bx) + 1):
            grid[by][x] = 0
