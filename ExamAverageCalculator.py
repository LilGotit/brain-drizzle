examCount = 0
examTotal = 0
score = 0
while score != 5309:
    score = float(input("Enter your exam score. 5309 to stop and calculate: "))
    if score == 5309:
        break
    elif score < 0 or score > 100:
        print("Incorrect score entered; re-enter actual exam score: ")
        continue
    else:
        examTotal += score
        examCount += 1
examAverage = examTotal / examCount
print("These " + str(examCount) + " scores produce a work average, when rounded to a single decimal digit, of " + str(round(examAverage, 1)) + " per exam.")