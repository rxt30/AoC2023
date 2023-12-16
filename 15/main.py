def readFileContent(filename):
    with open(filename) as file:
        return file.read().strip().split(",")


def calculateHash(value):
    currentValue = 0
    for letter in value:
        currentValue += ord(letter)
        currentValue *= 17
        currentValue = currentValue % 256
    return currentValue


def getHashValues(game):
    endHashes = []
    for value in game:
        endHashes.append(calculateHash(value))
    return endHashes


def getLenses(game):
    lenses = {i: {} for i in range(256)}
    for value in game:
        addition = "=" in value
        splitted = value.split("=") if addition else value.split("-")
        currentHash = calculateHash(splitted[0])
        if addition:
            lenses[currentHash][splitted[0]] = int(splitted[1])
        else:
            lenses[currentHash].pop(splitted[0], None)
    return lenses


def getFocusingPower(lenses):
    focusingPower = []
    for i, box in lenses.items():
        for j, (_, focalLength) in enumerate(box.items()):
            focusingPower.append((i + 1) * (j + 1) * focalLength)
    return focusingPower


def solution1(filecontent):
    hashes = getHashValues(filecontent)
    print(sum(hashes))


def solution2(filecontent):
    lenses = getLenses(filecontent)
    focusingPower = getFocusingPower(lenses)
    print(sum(focusingPower))


if __name__ == "__main__":
    filecontent = readFileContent("./test.txt")
    solution1(filecontent)
    solution2(filecontent)
    filecontent = readFileContent("./input.txt")
    solution1(filecontent)
    solution2(filecontent)
