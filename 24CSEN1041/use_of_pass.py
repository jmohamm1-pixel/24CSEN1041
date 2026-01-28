1st code
for i in range(1, 8):

    if i == 3 or i == 6:
        pass      # value is skipped but loop continues
    else:
        print("Number:", i)

print("Loop completed")
>output
Number: 1
Number: 2
Number: 4
Number: 5
Number: 7
Loop completed

2nd code
for i in range(1, 8):

    if i == 3 or i == 6:
        pass      # value is skipped but loop continues
    else:
        print("Number:", i)

print("Loop completed")
>Output
Number: 1
Number: 2
Number: 4
Number: 5
Number: 7
Loop completed
