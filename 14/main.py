import re
import numpy as np


def readInput(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def rotate(playField):
    rotatedField = []
    for i in range(len(playField[0])):
        column = ""
        for line in playField:
            column += line[i]
        rotatedField.append(column[::-1])
    return rotatedField


def rotateList(roundRockList, squareRockList, totalStats):
    roundRockFinal = [set() for _ in range(totalStats[0])]
    squareRockFinal = [set() for _ in range(totalStats[0])]
    for i, (roundRock, squareRock) in enumerate(zip(roundRockList, squareRockList)):
        for rock in roundRock:
            roundRockFinal[rock].add(totalStats[1] - i - 1)
        for rock in squareRock:
            squareRockFinal[rock].add(totalStats[1] - i - 1)
    return roundRockFinal, squareRockFinal, totalStats[::-1]


def findPositions(line, regex):
    return [m.start(0) for m in re.finditer(regex, line)]


def getRockList(playField):
    roundList = [findPositions(line, r"O") for line in playField]
    squareList = [findPositions(line, r"#") for line in playField]
    return roundList, squareList


def collapse(roundList, squareList):
    endList = []
    roundRockPositionList = []
    for line in playField:
        endRockList = []
        roundList = np.array(findPositions(line, r"O"))
        squareList = findPositions(line, r"#")
        squareList.insert(0, -1)
        squareList.append(len(line))
        for start, end in zip(squareList, squareList[1:]):
            foundRound = len(roundList[(start < roundList) & (roundList < end)])
            endList.append(sum(range(end - foundRound + 1, end + 1)))
            endRockList += list(range(end - foundRound, end))
        roundRockPositionList.append(endRockList)
    return endList, roundRockPositionList


def replacePlayField(playField, rockList):
    endField = []
    for line, rocks in zip(playField, rockList):
        line = line.replace("O", ".")
        line = list(line)
        for rockPos in rocks:
            line[rockPos] = "O"
        endField.append("".join(line))
    return endField


def solution1(filecontent):
    playField = rotate(filecontent)
    structureList, _ = collapse(playField)
    print(sum(structureList))


def solution2(filecontent):
    playField = filecontent
    endFields = []
    something = [len(filecontent), len(filecontent[0])]
    roundList, squareList = getRockList(playField)
    print(roundList, squareList)
    roundList, squareList, something = rotateList(roundList, squareList, something)
    print(roundList, squareList)
    return
    for i in range(4 * 1000000000):
        playField = rotate(playField)
        # print("-------")
        # print("\n".join(playField))
        _, roundList = collapse(playField)
        # print("-------")
        # print(roundList)
        playField = replacePlayField(playField, roundList)
        # print("-------")
        # print("\n".join(playField))
        if i % 4 == 0:
            endFields.append(playField)
            if endFields.count(playField) == 2:
                print(i // 4)
    # print("-------")
    # print("\n".join(playField))
    structureList, _ = collapse(playField)
    print(sum(structureList))


if __name__ == "__main__":
    filecontent = readInput("./test.txt")
    # solution1(filecontent)
    solution2(filecontent)
    # filecontent = readInput("./input.txt")
    # solution1(filecontent)
