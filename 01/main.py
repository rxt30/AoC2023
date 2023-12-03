def readFile():
    with open("./first.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines


def solution1(fileContent):
    endValue = 0
    for line in fileContent:
        firstNumberRead = False
        lastNumber = 0
        for letter in line:
            if letter.isdigit():
                if not firstNumberRead:
                    firstNumberRead = True
                    endValue += int(letter) * 10
                lastNumber = int(letter)
        endValue += lastNumber
    print(endValue)


def solution2(fileContent):
    numberStrings = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    endValue = 0
    for line in fileContent:
        firstIndices = {}
        lastIndices = {}
        for key, value in numberStrings.items():
            if key in line:
                firstIndices[value] = line.index(key)
                lastIndices[value] = line.rindex(key)
        for pos, letter in enumerate(line):
            if letter.isdigit():
                if int(letter) in firstIndices and pos < firstIndices[int(letter)]:
                    firstIndices[int(letter)] = pos
                elif int(letter) not in firstIndices:
                    firstIndices[int(letter)] = pos
                if int(letter) in lastIndices and pos > lastIndices[int(letter)]:
                    lastIndices[int(letter)] = pos
                elif int(letter) not in lastIndices:
                    lastIndices[int(letter)] = pos
        firstValue = min(firstIndices, key=firstIndices.get)
        lastValue = max(lastIndices, key=lastIndices.get)
        endValue += firstValue * 10 + lastValue
    print(endValue)


if __name__ == "__main__":
    fileContent = readFile()
    solution1(fileContent)
    solution2(fileContent)
