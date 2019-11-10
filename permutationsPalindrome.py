#Given a string, determine if a permutation of the string could form a palindrome.

def permutationsPalindrome(string1):

    string1dict = {}
    countStr = 0
    for str in string1:
        if string1dict.has_key(str):
            countStr = string1dict.get(str)
        string1dict[str] = countStr + 1

    oddFound = False
    for key in string1dict:
        if string1dict.get(key) % 2 == 1:
            if not oddFound:
                oddFound = True
            else:
                return False
    return True

print permutationsPalindrome("tactcoapapa")
