x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if x <= y:
    for i in range(x, y+1, 5):
        print(i, end=' ')
    print()
else:
    print("Second integer can't be less than the first.")
    
