i = 1

while i <= 10:
    print("Current number:", i)

    if i % 5 == 0:
        print("Number divisible by 5 found. Stopping loop.")
        break

    i += 1
Output
Current number: 1
Current number: 2
Current number: 3
Current number: 4
Current number: 5
Number divisible by 5 found. Stopping loop.
