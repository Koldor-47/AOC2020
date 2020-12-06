"""
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy,
it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which
angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map
(your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome
stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row
on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the
position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X
where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1,
how many trees would you encounter?

"""

test_map = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]

def getMap(mapFile):
    with open(mapFile, 'r') as F:
        mapData =  F.read().split("\n")
        return mapData


def Find_Route(The_Map, rightstep):
    right = 0
    Trees = 0
    Free_spots = 0

    for count, value in enumerate(The_Map):
        print(f"{count} : {right}")
        if The_Map[count][right] == "#":
            Trees += 1
        else:
            Free_spots += 1

        if (right + rightstep) >= len(value):
            right = (right + rightstep) - (len(value))
        else:
            right += rightstep

    print(f" Trees {Trees} : Free Spots {Free_spots}")


def Find_Route_2(The_Map, rightstep, downstep):
    right = 0
    Trees = 0
    Free_spots = 0

    for step in range(0, len(The_Map), downstep):
        #print(f"{The_Map[step]} : {right}")
        if The_Map[step][right] == "#":
            Trees += 1
        else:
            Free_spots += 1

        if (right + rightstep) >= len(The_Map[step]):
            right = (right + rightstep) - (len(The_Map[step]))
        else:
            right += rightstep

    return Trees

def Join_Routes(slopes, The_map):
    slope_trees = []
    total_trees = 1
    for slope in slopes:
        slope_trees.append(Find_Route_2(The_map, slope[0], slope[1]))

    for i in slope_trees:
        total_trees = i * total_trees

    return total_trees


Slope_Angles = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]


#Find_Route(test_map, 1)
#Find_Route_2(test_map, 1, 2)

Join_Routes(Slope_Angles, getMap("Day3Data.txt"))
