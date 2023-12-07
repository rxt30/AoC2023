import re


def readFile(fileName):
    with open(fileName) as file:
        return file.read()


def convertToInt(item):
    return [int(x) for x in item.split(" ")]


def createCategoryDict(category):
    values = re.findall(r"\d+\ \d+\ \d+", category)
    values = list(map(convertToInt, values))
    stage = re.findall(r"\w+-\w+-\w+", category)[0]
    return [stage, values]


def splitFileContent(fileContent):
    splittedParts = fileContent.split("\n\n")
    seeds = splittedParts[0].split(":")[1].strip()
    seeds = {int(seed): "seed" for seed in seeds.split(" ")}
    categories = splittedParts[1:]
    categories = list(map(createCategoryDict, categories))
    return seeds, categories


def changeSeeds(seeds, sourceList, difference, stageName):
    outputSeeds = seeds
    print("Hello world")
    print(set(seeds.keys() & set(sourceList)))
    for i, seed in enumerate(set(seeds.keys()) & set(sourceList)):
        # for i, seed in enumerate(seeds):
        if seeds[seed] != stageName:
            changedSeedValue = seed + difference
            outputSeeds[changedSeedValue] = stageName
            outputSeeds.pop(seed, None)
    return outputSeeds


def getLocations(seeds, categories):
    for i, stage in enumerate(categories):
        print(f"{i}/{len(categories)}")
        stageName = stage[0]
        for j, values in enumerate(stage[1]):
            print(f"{j}/{len(stage[1])}")
            sourceList = range(values[1], values[1] + values[2])
            difference = values[0] - values[1]
            seeds = changeSeeds(seeds, sourceList, difference, stageName)
    return seeds


def alternateSeeds(seeds):
    seedsGeneration = zip(list(seeds.keys())[::2], list(seeds.keys())[1::2])
    outSeeds = {seed[0] + x: "seed" for seed in seedsGeneration for x in range(seed[1])}
    return outSeeds


def solution1(fileContent, solution2=False):
    seeds, categories = splitFileContent(fileContent)
    if solution2:
        seeds = alternateSeeds(seeds)
    locations = getLocations(seeds, categories)
    print(min(locations))


if __name__ == "__main__":
    fileContent = readFile("././test.txt")
    solution1(fileContent)
    solution1(fileContent, solution2=True)
    fileContent = readFile("././input.txt")
    solution1(fileContent)
    # solution1(fileContent, solution2=True)
