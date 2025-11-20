from generator.dungeon import generate_dungeon
from generator.renderer import render, print_ascii
from random import randint
from config import *
import argparse

def main():
    parser = argparse.ArgumentParser(description="Procedural Dungeon Generator")

    parser.add_argument("--seed", type=int)
    parser.add_argument("--ascii", action="store_true")

    args = parser.parse_args()

    seed = args.seed if args.seed is not None else randint(0, 10 ** 20)

    grid, rooms, used_seed = generate_dungeon(
        width=WIDTH,
        height=HEIGHT,
        max_rooms=MAX_ROOMS,
        seed=seed
    )

    if args.ascii:
        print_ascii(grid)

    path = render(grid)
    print(f"Saved : {path}")
    print(f"Seed  : {used_seed}")

if __name__ == "__main__":
    main()
