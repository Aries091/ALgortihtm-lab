def zero_one_knapsack_dp(weights, values, capacity):
    n = len(weights)
   
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    
    selected_items = [0] * n
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items[i-1] = 1 
            w -= weights[i-1]
    
    return dp[n][capacity], tuple(selected_items)
