import re


def readFileContent(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def getNextPositions(symbol, position):
    match symbol:
        case "J":
            return [(position[0] - 1, position[1]), (position[0], position[1] - 1)]
        case "F":
            return [(position[0], position[1] + 1), (position[0] + 1, position[1])]
        case "7":
            return [(position[0] + 1, position[1]), (position[0], position[1] - 1)]
        case "L":
            return [(position[0] - 1, position[1]), (position[0], position[1] + 1)]
        case "-":
            return [(position[0], position[1] + 1), (position[0], position[1] - 1)]
        case "|":
            return [(position[0] - 1, position[1]), (position[0] + 1, position[1])]
    return position


def getStartSymbol(symbols, start):
    return [k for k, v in symbols.items() if start in v]


def getSymbols(filecontent):
    symbols = {}
    start = ()
    for i, line in enumerate(filecontent):
        for symbol in re.finditer(r"[^.]", line):
            if symbol.group(0) == "S":
                start = (i, symbol.start(0))
            else:
                symbols[(i, symbol.start(0))] = getNextPositions(
                    symbol.group(0), (i, symbol.start(0))
                )
    symbols[start] = getStartSymbol(symbols, start)
    return symbols, start


def getTotatlPath(symbols, start):
    lastPosition = start
    currentPosition = symbols[start][0]
    totalSteps = 1
    while currentPosition != start:
        temp = currentPosition
        currentPosition = list(set(symbols[currentPosition]) - set([lastPosition]))[0]
        lastPosition = temp
        totalSteps += 1
    return totalSteps


def solution1(filecontent):
    symbols, start = getSymbols(filecontent)
    totalPathLength = getTotatlPath(symbols, start)
    print(totalPathLength // 2)


def solution2(filecontent):
    symbols, start = getSymbols(filecontent)


if __name__ == "__main__":
    filecontent = readFileContent("./test.txt")
    solution1(filecontent)
    filecontent = readFileContent("./test2.txt")
    solution1(filecontent)
    filecontent = readFileContent("./input.txt")
    solution1(filecontent)
