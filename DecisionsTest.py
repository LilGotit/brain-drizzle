examCount = 0
examTotal = 0
score = 0
while score != 5309:
    score = float(input("Enter a number. 5309 to quit: "))
    if score < 0 or score > 100:
        print("Incorrect score entered; re-enter actual exam score: ")
        continue
    elif score == 5309:
        break
    else:
        examTotal += score
        examCount += 1
examAverage = examTotal / examCount
print("These " + str(examCount) + " scores average out to " + str(examAverage))

