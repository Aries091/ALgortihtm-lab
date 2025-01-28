def solve_fractional_knapsack(item_weights, item_values, max_capacity):
    # Calculate value-to-weight ratio
    value_to_weight = [(item_values[i] / item_weights[i], item_weights[i], item_values[i]) 
                        for i in range(len(item_weights))]
    
    # Sort by value-to-weight ratio in descending order
    value_to_weight.sort(reverse=True)
    
    total_value = 0
    remaining_capacity = max_capacity
    
    for ratio, weight, value in value_to_weight:
        if remaining_capacity >= weight:
            # Take the full item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take a fractional part of the item
            total_value += ratio * remaining_capacity
            break
    
    return total_value

def solve_zero_one_knapsack_dp(item_weights, item_values, max_capacity):
    num_items = len(item_weights)

    dp_table = [[0 for _ in range(max_capacity + 1)] for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(1, max_capacity + 1):
            if item_weights[i - 1] <= w:
                dp_table[i][w] = max(item_values[i - 1] + dp_table[i - 1][w - item_weights[i - 1]], dp_table[i - 1][w])
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    selected_items = [0] * num_items
    remaining_capacity = max_capacity
    for i in range(num_items, 0, -1):
        if dp_table[i][remaining_capacity] != dp_table[i - 1][remaining_capacity]:
            selected_items[i - 1] = 1
            remaining_capacity -= item_weights[i - 1]

    return dp_table[num_items][max_capacity], tuple(selected_items)

def solve_fractional_knapsack_brute_force(item_weights, item_values, max_capacity):
    num_items = len(item_weights)
    max_total_value = 0

    for mask in range(1 << num_items):  # Generate all subsets
        current_weight = 0
        current_value = 0

        for i in range(num_items):
            if mask & (1 << i):  # Check if the i-th item is included
                if current_weight + item_weights[i] <= max_capacity:
                    current_weight += item_weights[i]
                    current_value += item_values[i]
                else:
                    # Take fractional part of the item
                    remaining_capacity = max_capacity - current_weight
                    fraction = remaining_capacity / item_weights[i]
                    current_weight += remaining_capacity
                    current_value += item_values[i] * fraction
                    break

        max_total_value = max(max_total_value, current_value)

    return max_total_value

def solve_zero_one_knapsack_brute_force(item_weights, item_values, max_capacity):
    num_items = len(item_weights)
    max_total_value = 0
    best_item_combination = [0] * num_items

    for mask in range(1 << num_items):  # Generate all subsets
        current_weight = 0
        current_value = 0
        current_combination = [0] * num_items

        for i in range(num_items):
            if mask & (1 << i):  # Check if the i-th item is included
                if current_weight + item_weights[i] <= max_capacity:
                    current_weight += item_weights[i]
                    current_value += item_values[i]
                    current_combination[i] = 1
                else:
                    break

        if current_value > max_total_value:
            max_total_value = current_value
            best_item_combination = current_combination

    return max_total_value, tuple(best_item_combination)
