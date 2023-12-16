import re
import itertools


def readFilecontent(filename):
    with open(filename) as file:
        return [line.strip().split(" ") for line in file]


def getAllPatterns(game, brokenSum):
    patterns = []
    placeholderCount = game.count("?")
    existingBroken = game.count("#")
    game = game.replace("?", "{}")
    for pattern in itertools.product(["#", "."], repeat=placeholderCount):
        if pattern.count("#") != brokenSum - existingBroken:
            continue
        patterns.append(game.format(*pattern))
    return patterns


def getAllPossiblePatters(filecontent):
    games = []
    for i, game in enumerate(filecontent):
        # print(f"{i}/{len(filecontent)}")
        endList = list(map(int, game[1].split(",")))
        allPatterns = getAllPatterns(game[0], sum(endList))
        games.append([allPatterns, endList])
    return games


def isValidPattern(pattern, target):
    brokenLength = list(map(len, re.findall("[#]+", pattern)))
    return brokenLength == target


def getValidCombinations(games):
    validCounterNumbers = []
    for game in games:
        validCounter = 0
        for pattern in game[0]:
            if isValidPattern(pattern, game[1]):
                validCounter += 1
        validCounterNumbers.append(validCounter)
    return validCounterNumbers


def unfoldFilecontent(filecontent):
    return ["?".join([filecontent[0]] * 2), ",".join([filecontent[1]] * 2)]


def unfoldPopCulture(filecontent):
    allMyFriends = "?" + filecontent[0]
    lastThing = filecontent[1]
    if filecontent[0][-1] == "#":
        lastPatter = re.findall("[#]+", filecontent[0])[-1]
        allMyFriends = lastPatter + allMyFriends
        lastThing = f"{lastThing[-1]}," + lastThing
    return [allMyFriends, lastThing]


def unfoldManipulator2(filecontent):
    allMyFriends = filecontent[0] + "?"
    lastThing = filecontent[1]
    if filecontent[0][0] == "#":
        lastPatter = re.findall("[#]+", filecontent[0])[0]
        allMyFriends = allMyFriends + lastPatter
        lastThing = lastThing + f",{lastThing[0]}"
    return [allMyFriends, lastThing]
    # allMyFriends = filecontent[0] + "?" if filecontent[0][0] != "#" else filecontent[0]
    # return [allMyFriends, filecontent[1]]


def fuckyou(validNumbers, validNumbers2):
    knockedLoose = []
    for x, y in zip(validNumbers, validNumbers2):
        deepInTheWillow = y // x
        knockedLoose.append(y * (deepInTheWillow**3))
    return knockedLoose


def solution1(filecontent):
    possiblePatterns = getAllPossiblePatters(filecontent)
    validNumbers = getValidCombinations(possiblePatterns)
    print(sum(validNumbers))


def solution2(filecontent):
    print("Join ? 2x ---------")
    filecontent1 = list(map(unfoldPopCulture, filecontent))
    possiblePatterns = getAllPossiblePatters(filecontent1)
    validNumbers = getValidCombinations(possiblePatterns)
    filecontent2 = list(map(unfoldManipulator2, filecontent))
    possiblePatterns2 = getAllPossiblePatters(filecontent2)
    validNumbers2 = getValidCombinations(possiblePatterns2)
    validNumbers = [x * y for x, y in zip(validNumbers, validNumbers2)]
    print("Patterns generated")
    possiblePatternsNormal = getAllPossiblePatters(filecontent)
    validNumbersNormal = getValidCombinations(possiblePatternsNormal)
    everythingIsQuiedNow = fuckyou(validNumbersNormal, validNumbers)
    print(everythingIsQuiedNow)
    print(sum(everythingIsQuiedNow))
    # print("Join ? 3x ---------")
    # filecontent1 = list(map(unfoldFilecontent4, filecontent))
    # possiblePatterns = getAllPossiblePatters(filecontent1)
    # getValidCombinations(possiblePatterns)
    # print("Append ? ---------")
    # filecontent2 = list(map(unfoldFilecontent2, filecontent))
    # possiblePatterns = getAllPossiblePatters(filecontent2)
    # getValidCombinations(possiblePatterns)
    # print("Prepend ? ---------")
    # filecontent3 = list(map(unfoldFilecontent3, filecontent))
    # possiblePatterns = getAllPossiblePatters(filecontent3)
    # getValidCombinations(possiblePatterns)


if __name__ == "__main__":
    filecontent = readFilecontent("././test.txt")
    solution1(filecontent)
    solution2(filecontent)
    filecontent = readFilecontent("././input.txt")
    solution1(filecontent)
    solution2(filecontent)
