# CTI-110
# P4HW1 - Score List
# Angela Joplin
# 11/10/2022

# Create variable and ask user for number of scores to be recorded. Assign count
# increment variable. Create loop asking for number of scores up to the number
# to be recorded. Verify that scores entered are between 0-100, if not, notify
# and prompt user to re-enter the score. Add scores to a list. Calculate and
# display lowest score, drop it from the list and display the new list. Calculate
# and display average. Determine and display letter grade for average.


numScores = int(input('How many scores do you want to enter? '))
i = 0

scoreList = []
print()
while i < numScores:
    scoreList.append(float(input(f'Enter Score #{i + 1}: '))) 
         
    while scoreList[i] < 0 or scoreList[i] > 100:
        print()
        print('INVALID Score entered!!!!')
        print('Score entered should be between 0 and 100')
        scoreList[i] = float(input(f'Enter score #{i + 1} again: '))
    i = i + 1

print()
print()
print('************ Results ************')
print(f'Lowest Score  : {min(scoreList):.2f}')

scoreList.remove(min(scoreList))
avg = sum(scoreList) / len(scoreList)

print(f'Modified List : {scoreList}')
print(f'Scores Average: {sum(scoreList) / len(scoreList):.2f}')
        
if avg >= 90:
    print('Grade         : A')
elif avg >= 80:
    print('Grade         : B')
elif avg >= 70:
    print('Grade         : C')
elif avg >= 60:
    print('Grade         : D')       
else:
    print('Grade         : F')
print('*********************************')


