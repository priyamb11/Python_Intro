terms = int(input("How many terms: "))

t1, t2, = 0, 1
count = 0

if terms < 1:
    print("Please enter a term equal to 1 or more")
elif terms == 1:
    print("Fibonacci sequence: ", t1)
else:
    print("Fibonacci sequence: ")
    while count < terms:
        print(t1)
        tv = t1 + t2
        # update values
        t1 = t2
        t2 = tv
        count += 1