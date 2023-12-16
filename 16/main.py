from collections import deque


def readFileContent(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def getHighlightedFields(playField, startx, starty, deltax, deltay):
    maxX = len(playField[0]) - 1
    maxY = len(playField) - 1
    positionQueue = deque([(startx, starty, deltax, deltay)])
    seen = set()
    while len(positionQueue) != 0:
        startx, starty, deltax, deltay = positionQueue.popleft()
        if (
            not 0 <= startx <= maxX
            or not 0 <= starty <= maxY
            or (startx, starty, deltax, deltay) in seen
        ):
            continue
        seen.add((startx, starty, deltax, deltay))
        match playField[starty][startx]:
            case "|" if deltax != 0:
                positionQueue.append((startx, starty - 1, 0, -1))
                positionQueue.append((startx, starty + 1, 0, 1))
            case "-" if deltay != 0:
                positionQueue.append((startx - 1, starty, -1, 0))
                positionQueue.append((startx + 1, starty, 1, 0))
            case "/":
                positionQueue.append(
                    (startx - deltay, starty - deltax, -deltay, -deltax)
                )
            case "\\":
                positionQueue.append((startx + deltay, starty + deltax, deltay, deltax))
            case _:
                positionQueue.append((startx + deltax, starty + deltay, deltax, deltay))
    return set([(i, j) for i, j, _, _ in seen])


def solution1(filecontent):
    highlightedFields = getHighlightedFields(filecontent, 0, 0, 1, 0)
    print(len(highlightedFields))


def solution2(filecontent):
    maxX = len(filecontent[0])
    maxY = len(filecontent)
    highlightedFields = []
    for i in range(maxX):
        highlightedFields.append(len(getHighlightedFields(filecontent, i, 0, 0, 1)))
        highlightedFields.append(
            len(getHighlightedFields(filecontent, i, maxY - 1, 0, -1))
        )
    for i in range(maxY):
        highlightedFields.append(len(getHighlightedFields(filecontent, 0, i, 1, 0)))
        highlightedFields.append(
            len(getHighlightedFields(filecontent, maxX - 1, i, -1, 0))
        )
    print(max(highlightedFields))


if __name__ == "__main__":
    filecontent = readFileContent("./test.txt")
    solution1(filecontent)
    solution2(filecontent)
    filecontent = readFileContent("./input.txt")
    solution1(filecontent)
    solution2(filecontent)
