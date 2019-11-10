#Check if two string are permutations with each other

def permutations(string1, string2):
    if len(string1) != len(string2):
        return False

    string1dict = {}
    countStr = 0
    for str in string1:
        if string1dict.has_key(str):
            countStr = string1dict.get(str)
        string1dict[str] = countStr + 1

    for strString2 in string2:
        if string1dict.has_key(strString2):
            string1dict[strString2] = string1dict.get(strString2) - 1
            if string1dict.get(strString2) < 0:
                return False
        else:
            return False

    return True


string1 = "atitt"
string2 = "taitt"

print permutations(string1,string2)
