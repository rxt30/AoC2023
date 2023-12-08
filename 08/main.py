import re
import itertools
import numpy as np


def readFileContent(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def getDirections(filecontent):
    movement = filecontent[0]
    directions = {}
    for line in filecontent[2:]:
        source = line.split("=")[0].strip()
        try:
            target = re.search(r"\(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", line).groups()
        except:
            continue
        directions[source] = target
    return movement, directions


def nextPosition(directions, currentMovement):
    if currentMovement == "L":
        return directions[0]
    return directions[1]


def getStartPositions(directions):
    return re.findall(r"([A-Z0-9]{2}A)", "\n".join(directions))


def getSteps(movement, directions, start, solution2=False):
    movementCycle = itertools.cycle(movement)
    currentPosition = start
    stepsCounter = 0
    targetReached = False
    while not targetReached:
        currentPosition = nextPosition(directions[currentPosition], next(movementCycle))
        stepsCounter += 1
        targetReached = (
            currentPosition == "ZZZ" if not solution2 else currentPosition[-1] == "Z"
        )
    return stepsCounter


def getCycleSteps(movement, directions):
    startPositions = getStartPositions(directions)
    cycleSteps = [
        getSteps(movement, directions, start, solution2=True)
        for start in startPositions
    ]
    return cycleSteps


def solution1(filecontent):
    movement, directions = getDirections(filecontent)
    totalSteps = getSteps(movement, directions, "AAA")
    print(totalSteps)


def solution2(filecontent):
    movement, directions = getDirections(filecontent)
    cycleSteps = getCycleSteps(movement, directions)
    print(np.lcm.reduce(cycleSteps))


if __name__ == "__main__":
    filecontent = readFileContent("./test.txt")
    solution1(filecontent)
    filecontent = readFileContent("./test2.txt")
    solution1(filecontent)
    filecontent = readFileContent("./test3.txt")
    solution2(filecontent)
    filecontent = readFileContent("./input.txt")
    solution1(filecontent)
    solution2(filecontent)
