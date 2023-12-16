def painRemains(filename):
    with open(filename) as file:
        filecontent = file.read().split("\n\n")
    return [game.split() for game in filecontent]


def getStats(game):
    for i in range(len(game) // 2, 0, -1):
        if game[0:i] == game[i : i * 2][::-1]:
            return i
    return 0


def findAllInitialSequences(game):
    stats = []
    leftStats = [0, getStats(game) * 2]
    if leftStats[0] != leftStats[1]:
        stats.append(leftStats)
    rightStats = [len(game) - getStats(game[::-1]) * 2, len(game)]
    if rightStats[0] != rightStats[1]:
        stats.append(rightStats)
    return stats


def findSideBoundSequence(game, isLeftBound):
    # print(game)
    if isLeftBound:
        stats = [0, getStats(game) * 2]
    else:
        stats = [len(game) - getStats(game[::-1]) * 2, len(game)]
    # print(stats)
    if stats[0] == stats[1]:
        return []
    return stats


def checkAll(game, start, end):
    for line in game:
        if (
            line[start : end - ((end - start) // 2)]
            != line[end - ((end - start) // 2) : end][::-1]
        ):
            return False
    return True


def afterAllIveDone(game):
    initalSequences = findAllInitialSequences(game[0])
    if len(initalSequences) == 0:
        return 0
    for start, end in initalSequences:
        broken = False
        initalSequence = [start, end]
        for line in game:
            newSequence = findSideBoundSequence(line[start:end], start == 0)
            if len(newSequence) == 0:
                broken = True
                break
            if start == 0:
                start, end = newSequence
            else:
                start += newSequence[0]
            if [start, end] != initalSequence:
                if not checkAll(game, start, end):
                    broken = True
                    break
        if broken:
            continue
        return (start + end + 1) // 2
    return 0


def illDisapear(game):
    outputGame = []
    for i in range(len(game[0])):
        currentLine = ""
        for line in game:
            currentLine += line[i]
        outputGame.append(currentLine)
    return outputGame


def dancingLikeFlames(games):
    endResult = 0
    notFound = 0
    for game in games:
        foundMirror = afterAllIveDone(game)
        if foundMirror == 0:
            foundMirror = afterAllIveDone(illDisapear(game))
            endResult += foundMirror * 100
            if foundMirror == 0:
                print("--------------")
                print("\n".join(game))
                print("--------------")
                print("\n".join(illDisapear(game)))
                notFound += 1
        else:
            endResult += foundMirror
    print(endResult)


def solution1(filecontent):
    dancingLikeFlames(filecontent)


if __name__ == "__main__":
    filecontent = painRemains("././test.txt")
    solution1(filecontent)
    # filecontent = painRemains("././yes.txt")
    # solution1(filecontent)
    filecontent = painRemains("././input.txt")
    solution1(filecontent)
    filecontent = painRemains("././bla.txt")
    solution1(filecontent)
