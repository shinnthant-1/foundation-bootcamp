def countWords(word):
    count = {}
    for c in word:
        if c in count:
            count[c] += 1
        else :
            count[c] = 1
    return count

def canConstruct(ransomNote: str, magazine: str) -> bool:
    countMagazine = countWords(magazine)
    for c in ransomNote:
        if c in countMagazine and countMagazine[c] > 0:
            countMagazine[c] -= 1
        else:
            return False
    return True

ransomNote = "aa"
magazine = "ab"
print (canConstruct(ransomNote, magazine))