import re
import math


def readFileContent(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def getRaces(filecontent, solution2=False):
    times = re.findall(r"\d+", filecontent[0])
    distance = re.findall(r"\d+", filecontent[1])
    if solution2:
        times = ["".join(times)]
        distance = ["".join(distance)]
    times = list(map(int, times))
    distance = list(map(int, distance))
    return zip(times, distance)


def solveRaces(races):
    wonRaces = []
    for race in races:
        time = race[0]
        goal = race[1]
        # racesWon = 0
        # i = 1
        # something = 0
        if time % 2 == 1:
            maxtime = (time // 2) * ((time // 2) + 1)
            difference = 0
        else:
            maxtime = (time // 2) ** 2
            difference = 1
        # while (maxtime - difference) > goal:
        #     difference += 2 * i + something
        #     i += 1
        #     racesWon += 2
        print(maxtime - goal)
        wonRaces.append(int(math.log2(maxtime - goal + 1)) * 2 + difference)
    print(wonRaces)
    return wonRaces


def solution1(filecontent):
    races = getRaces(filecontent)
    wonRaces = solveRaces(races)
    print(math.prod(wonRaces))


def solution2(filecontent):
    race = getRaces(filecontent, solution2=True)
    wonRaces = solveRaces(race)
    print(math.prod(wonRaces))


if __name__ == "__main__":
    filecontent = readFileContent("././test.txt")
    solution1(filecontent)
    solution2(filecontent)
    filecontent = readFileContent("././input.txt")
    solution1(filecontent)
    solution2(filecontent)
