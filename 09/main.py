from itertools import pairwise


def readFilecontent(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def getSequences(filecontent):
    return [list(map(int, line.split(" "))) for line in filecontent]


def islastSequenceZero(sequence):
    return all(x == 0 for x in sequence)


def getSequencePyramid(sequence):
    nextSequences = [sequence]
    while not islastSequenceZero(nextSequences[-1]):
        nextSequences.append(
            list(map(lambda x: x[1] - x[0], list(pairwise(nextSequences[-1]))))
        )
    return nextSequences


def findNextNumber(sequence, solution2=False):
    sequencePyramid = getSequencePyramid(sequence)
    endNumber = 0
    if solution2:
        for subSequence in sequencePyramid[::-1]:
            endNumber = subSequence[0] - endNumber
    else:
        for subSequence in sequencePyramid[::-1]:
            endNumber += subSequence[-1]
    return endNumber


def getNextNumbers(sequences, solution2=False):
    return [findNextNumber(sequence, solution2) for sequence in sequences]


def solution1(filecontent):
    sequences = getSequences(filecontent)
    endNumbers = getNextNumbers(sequences)
    print(sum(endNumbers))


def solution2(filecontent):
    sequences = getSequences(filecontent)
    endNumbers = getNextNumbers(sequences, solution2=True)
    print(sum(endNumbers))


if __name__ == "__main__":
    filecontent = readFilecontent("././test.txt")
    solution1(filecontent)
    solution2(filecontent)
    filecontent = readFilecontent("././input.txt")
    solution1(filecontent)
    solution2(filecontent)
