import numpy as np
import itertools


def readFileContent(filename):
    with open(filename) as file:
        return [list(line.strip()) for line in file]


def getEmptyLines(universe):
    foundLines = []
    for i, line in enumerate(universe):
        if all(position == "." for position in line):
            foundLines.append(i)
    return foundLines


def findEmptyLines(filecontent):
    emptyHorizontal = getEmptyLines(filecontent)
    emptyVertical = getEmptyLines(np.transpose(filecontent))
    return emptyHorizontal, emptyVertical


def getUniversePositions(universe):
    return np.argwhere(np.array(universe) == "#")


def getMinimumDistances(
    universePositions, emptyHorizontal, emptyVertical, solution2=False
):
    distances = []
    for start, target in itertools.combinations(universePositions, 2):
        startHorizontal = min(start[0], target[0])
        endHorizontal = max(start[0], target[0])
        startVertical = min(start[1], target[1])
        endVertical = max(start[1], target[1])
        horizontalAddition = len(
            [i for i in emptyHorizontal if startHorizontal < i < endHorizontal]
        )
        verticalAddition = len(
            [i for i in emptyVertical if startVertical < i < endVertical]
        )
        if solution2:
            horizontalAddition *= 999999
            verticalAddition *= 999999
        horizontalDistance = np.abs(start[0] - target[0]) + horizontalAddition
        verticalDistance = np.abs(start[1] - target[1]) + verticalAddition
        distances.append(horizontalDistance + verticalDistance)
    return distances


def solution1(filecontent):
    emptyHorizontal, emptyVertical = findEmptyLines(filecontent)
    universePositions = getUniversePositions(filecontent)
    minimumDistances = getMinimumDistances(
        universePositions, emptyHorizontal, emptyVertical
    )
    print(sum(minimumDistances))
    minimumDistances = getMinimumDistances(
        universePositions, emptyHorizontal, emptyVertical, solution2=True
    )
    print(sum(minimumDistances))


if __name__ == "__main__":
    filecontent = readFileContent("././test.txt")
    solution1(filecontent)
    filecontent = readFileContent("././input.txt")
    solution1(filecontent)
