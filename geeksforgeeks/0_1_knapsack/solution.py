def knapsack(W, wt, val):
    n = len(val)
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]

if __name__ == '__main__': 
    W = 5
    wt = [1, 2, 3]
    val = [6, 10, 12] 

    print(knapsack(W, wt, val))
