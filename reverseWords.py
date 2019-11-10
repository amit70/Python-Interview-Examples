# Given an input string, reverse the string word by word.

def reverseWords(s):
    arrSplit = s.split(" ")
    start = 0
    end = len(arrSplit) - 1
    while start <= end:
        if arrSplit[start] == "":
            arrSplit.pop(start)
            end-=1
        elif arrSplit[end] == "":
            arrSplit.pop(end)
            end-=1
        else:
            temp = arrSplit[start]
            arrSplit[start] = arrSplit[end]
            arrSplit[end] = temp
            start+=1
            end-=1

    return " ".join(arrSplit)


print reverseWords("   a   b ")


# Given a string, you need to reverse the order of characters in each word within a sentence while
# still preserving whitespace and initial word order.

def reverseWords(s):
    arr = s.split(" ")
    for index,word in enumerate(arr):
        wordArr = list(word)
        start = 0
        end = len(wordArr) - 1
        while start < end:
            temp = wordArr[start]
            wordArr[start] = wordArr[end]
            wordArr[end] = temp
            start+=1
            end-=1
        arr[index] = "".join(wordArr)
    return " ".join(arr)

print reverseWords("Let's take LeetCode contest")
