import re
import math


def readLines(fileName):
    with open(fileName) as file:
        fileContent = [line.strip() for line in file]
    return fileContent


def getPositions(startNumber, endNumber, lineNumber):
    return [
        (i, j)
        for i in range(lineNumber - 1, lineNumber + 2)
        for j in range(startNumber - 1, endNumber + 1)
    ]


def getNumbersList(gameField, symbolsPositionList, increaseLine=0):
    numbersList = []
    for lineNumber, line in enumerate(gameField):
        for number in re.finditer(r"[0-9]+", line):
            numberPositions = getPositions(
                number.start(0), number.end(0), lineNumber + increaseLine
            )
            if len(set(numberPositions) & set(symbolsPositionList)) != 0:
                numbersList.append(int(number.group(0)))
    return numbersList


def getSymbolsPosition(gameField, onlyAsterik=False):
    positionsList = []
    for lineNumber, line in enumerate(gameField):
        for symbol in re.finditer(r"[^(0-9)|.]", line):
            if symbol.group(0) == "*" or not onlyAsterik:
                positionsList.append((lineNumber, symbol.start(0)))
    return positionsList


def solve2(gameField, symbolsPositionList):
    numbersList = []
    for asterik in symbolsPositionList:
        foundNumbers = getNumbersList(
            gameField[asterik[0] - 1 : asterik[0] + 2],
            [asterik],
            increaseLine=asterik[0] - 1,
        )
        if len(foundNumbers) == 2:
            numbersList.append(math.prod(foundNumbers))
    return numbersList


def solution1(fileContent):
    symbolsPositionList = getSymbolsPosition(fileContent)
    numbersList = getNumbersList(fileContent, symbolsPositionList)
    print(sum(numbersList))


def solution2(fileContent):
    symbolsPositionList = getSymbolsPosition(fileContent, onlyAsterik=True)
    numberList = solve2(fileContent, symbolsPositionList)
    print(sum(numberList))


if __name__ == "__main__":
    fileContent = readLines("././test.txt")
    solution1(fileContent)
    solution2(fileContent)
    fileContent = readLines("././input.txt")
    solution1(fileContent)
    solution2(fileContent)
