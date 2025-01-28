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