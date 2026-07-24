count = {'b' : 0,
         'a' : 0,
         'n' : 0}

word = "banana"
for c in word:
    if c == 'b':
        count['b'] +=1
    elif c == 'a':
        count['a'] += 1
    else:
        count['n'] += 1

print (count)

count = {}
word = "apple"
for c in word:
    if c in count:
        count[c] += 1
    else :
        count[c] = 1
print(count)