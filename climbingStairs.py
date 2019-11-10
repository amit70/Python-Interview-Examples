#You are climbing a stair case. It takes n steps to reach to the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climb_stairs(i, n, memo):
    if i > n:
        return 0
    if i == n:
        return 1
    if memo[i] > 0:
        return memo[i]

    memo[i] = climb_stairs(i + 1, n, memo) + climb_stairs(i + 2, n, memo)

    return memo[i]

print climbStairs(5)
