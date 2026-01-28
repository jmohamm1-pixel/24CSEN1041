total = 0

for i in range(1, 50):
    if i % 4 == 0:
        continue       
    elif i > 30:
        break       
    else:
        pass           

    total += i
    print("Adding:", i)

print("\nTotal sum:", total)
>OUTPUT
Adding: 1
Adding: 2
Adding: 3
Adding: 5
Adding: 6
Adding: 7
Adding: 9
Adding: 10
Adding: 11
Adding: 13
Adding: 14
Adding: 15
Adding: 17
Adding: 18
Adding: 19
Adding: 21
Adding: 22
Adding: 23
Adding: 25
Adding: 26
Adding: 27
Adding: 29
Adding: 30

Total sum: 330
