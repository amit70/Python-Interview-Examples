#On the first row, we write a 0. Now in every subsequent row, we look at the
# previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

def kthGrammar(N, K):
    if N == 1:
        return 0
    elif N == 2:
        return [0, 1][K - 1]

    L2 = (2 ** (N-1)) / 2
    if K <= L2:
        return int(kthGrammar(N - 1, K))
    else:
        return int(not kthGrammar(N - 1, K - L2))

print kthGrammar(4,5)
