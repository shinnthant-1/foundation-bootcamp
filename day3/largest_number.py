num = [0, 5, 2, 7, 4, 6]

def largestNum(num):
    largest = num[0]
    for n in num:
        if n > largest:
            largest = n
    return largest
print (largestNum(num))