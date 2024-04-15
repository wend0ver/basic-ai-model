import random

words = [
    "today", "hurt", "myself", "it", "was", "raining", "i", "failed", "my", "test", "have", "a", "is", "day", "sunny", "ate", "an", "apple", "had", "pizza", "am", "happy", "good", "bad"
]
weights = [0] * len(words)
bias = [0] * len(words)
trainBias = [0] * len(words)
trainWeights = [0] * len(words)

accuracy = -999

trainData = True

if (trainData == True):
    for _ in range(0, 1000000):
        prevAccuracy = accuracy
        accuracy = 0
        for i in range(len(words)):
            trainWeights[i] = random.randint(0, 100) / 100
            trainBias[i] = random.randint(-100, 100) / 100

        with open(r"C:\Users\Liams\OneDrive\Desktop\my first ai\happyDataset.txt") as file:
            for line in file:
                total = 0
                wordNum = 0
                for word in line.strip().split():
                    if word.lower() in words:
                        index = words.index(word.lower())
                        total += (trainBias[index]) * trainWeights[index]
                        wordNum += 1
                if wordNum != 0:
                    accuracy += total / wordNum

        with open(r"C:\Users\Liams\OneDrive\Desktop\my first ai\sadDataset.txt") as file:
            for line in file:
                total = 0
                wordNum = 0
                for word in line.strip().split():
                    if word.lower() in words:
                        index = words.index(word.lower())
                        total += (trainBias[index]) * trainWeights[index]
                        wordNum += 1
                if wordNum != 0:
                    accuracy += -total / wordNum

        accuracy /= 2
        if accuracy > prevAccuracy:
            print(accuracy)
            bias = trainBias.copy()
            weights = trainWeights.copy()
        else:
            accuracy = prevAccuracy
else:
    bias = [0.52, -0.93, -0.64, -0.23, 0.94, 0.85, 0.58, -0.69, -0.31, -0.94, -0.05, 0.54, -0.51, -0.94, 0.47, 0.98, 0.22, 0.97, 1.0, 0.53, 0.43, 0.7, 0.7, -0.99]
    weights = [0.55, 0.82, 0.56, 0.1, 0.57, 0.55, 0.16, 0.31, 0.9, 0.97, 0.98, 0.68, 0.42, 0.46, 0.68, 0.52, 0.37, 0.75, 0.85, 0.98, 0.0, 0.79, 0.26, 0.81]


print("AI trained")

for i in range(0,2):
    total = 0
    sentence = input().lower()
    for word in sentence.split():
        if word in words:
            index = words.index(word)
            total += (bias[index]) * weights[index]

    total /= len(sentence.split())
    print("Total:", total)
    if (total > 0):
        print("Your Happy!")
    elif (total < 0):
        print("Your Sad :(")
    elif (total == 0):
        print("Your not happy or sad")

print(bias)
print(weights)