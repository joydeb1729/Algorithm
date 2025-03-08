n = 5
W = 10

weight = [3, 3, 2, 5, 1]
profit = [10, 15, 10, 12, 8]

weight_left = W
total_profit = 0

taken = [False] * n

while weight_left > 0:
    max_profit_index = -1

    # Find the item with the best profit-to-weight ratio
    for i in range(n):
        if not taken[i]:
            if max_profit_index == -1 or (profit[i] / weight[i] > profit[max_profit_index] / weight[max_profit_index]):
                max_profit_index = i

    if max_profit_index == -1:
        break  # No more items to take

    taken[max_profit_index] = True

    # If the item can only be partially added
    if weight_left < weight[max_profit_index]:
        fraction_taken = weight_left / weight[max_profit_index]
        added_profit = profit[max_profit_index] * fraction_taken
        print(f"Taking {fraction_taken * 100:.2f}% of item {max_profit_index + 1} (Weight: {weight_left:.2f}, Profit: {added_profit:.2f})")
        total_profit += added_profit
        weight_left = 0  # Knapsack is full
    else:
        print(f"Taking full item {max_profit_index + 1} (Weight: {weight[max_profit_index]}, Profit: {profit[max_profit_index]})")
        weight_left -= weight[max_profit_index]
        total_profit += profit[max_profit_index]

print(f"Total profit: {total_profit:.2f}")
