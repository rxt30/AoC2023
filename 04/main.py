import re


def readFile(filename):
    with open(filename) as file:
        filecontent = [line for line in file]
    return filecontent


def getPlayCards(fileContent):
    return [line.split(":")[1].strip() for line in fileContent]


def getPoints(playCards, solution2=False):
    cards = {i: 1 for i in range(len(playCards))}
    endNumbers = []
    for index, card in enumerate(playCards):
        splittedCards = card.split("|")
        leftNumbers = [number for number in re.findall(r"[0-9]+", splittedCards[0])]
        rightNumbers = [number for number in re.findall(r"[0-9]+", splittedCards[1])]
        commonNumbers = len(set(leftNumbers) & set(rightNumbers))
        if solution2:
            for i in range(1, commonNumbers + 1):
                cards[index + i] += cards[index]
        else:
            if commonNumbers != 0:
                endNumbers.append(2 ** (commonNumbers - 1))
    if solution2:
        return cards
    else:
        return endNumbers


def solution1(fileContent):
    playCards = getPlayCards(fileContent)
    points = getPoints(playCards)
    print(sum(points))


def solution2(fileContent):
    playCards = getPlayCards(fileContent)
    totalCards = getPoints(playCards, solution2=True)
    print(sum(totalCards.values()))


if __name__ == "__main__":
    fileContent = readFile("././test.txt")
    solution1(fileContent)
    solution2(fileContent)
    fileContent = readFile("././input.txt")
    solution1(fileContent)
    solution2(fileContent)
