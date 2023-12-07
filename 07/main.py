import collections


def getFileContent(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def getPriorityClass(item):
    letterDict = collections.Counter(item)
    letterDict.pop("0", None)
    try:
        maxletterDictValue = max(letterDict.values()) + item.count("0")
    except:
        maxletterDictValue = 5
    if maxletterDictValue == 5 or maxletterDictValue == 4:
        return maxletterDictValue + 2
    if maxletterDictValue == 3:
        if len(letterDict) == 2:
            return 5
        return 4
    if maxletterDictValue == 2:
        if len(letterDict) == 3:
            return 3
        return 2
    return 1


def replacePicutreCards(item):
    mapping = {"A": "E", "K": "D", "Q": "C", "J": "B", "T": "A"}
    for source, target in mapping.items():
        item = item.replace(source, target)
    return item


def replaceJoker(item):
    return item.replace("B", "0")


def createGamePairs(fileContent, solution2=False):
    fileContent = list(map(replacePicutreCards, fileContent))
    if solution2:
        fileContent = list(map(replaceJoker, fileContent))
    return dict(item.split(" ") for item in fileContent)


def getHandClasses(games):
    return {game: getPriorityClass(game) for game in games}


def getEndResult(classes, gamePairs):
    sortedClasses = sorted(classes.items(), key=lambda x: (x[1], x[0]))
    endSum = 0
    for i, thing in enumerate(sortedClasses):
        endSum += (i + 1) * int(gamePairs[thing[0]])
    return endSum


def solution1(fileContent):
    gamePairs = createGamePairs(fileContent)
    classes = getHandClasses(gamePairs)
    print(getEndResult(classes, gamePairs))


def solution2(fileContent):
    gamePairs = createGamePairs(fileContent, solution2=True)
    classes = getHandClasses(gamePairs)
    print(getEndResult(classes, gamePairs))


if __name__ == "__main__":
    fileContent = getFileContent("./test.txt")
    solution1(fileContent)
    solution2(fileContent)
    fileContent = getFileContent("./input.txt")
    solution1(fileContent)
    solution2(fileContent)
