from PIL import Image
import os

def render(grid, path=None, tile_size=8):
    height = len(grid)
    width = len(grid[0])
    img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            color = (40, 40, 40) if grid[y][x] == 1 else (200, 200, 200)
            img.putpixel((x, y), color)

    img = img.resize((width * tile_size, height * tile_size), Image.NEAREST)

    if path is None:
        os.makedirs("output", exist_ok=True)
        path = f"output/dungeon.png"
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    return path

def print_ascii(grid):
    for row in grid:
        print("".join("#" if cell else " " for cell in row))
