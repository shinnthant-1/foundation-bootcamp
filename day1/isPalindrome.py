def isPalindrome(x: int) -> bool:
    text = str(x)
    left = 0
    right = len(text) - 1
    while (left < right):
        if (text[left] != text[right]):
            return False
        left+=1
        right-=1
    return True
x = 26562
print (isPalindrome(x))