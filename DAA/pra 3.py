class Item:
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight
def fractional_knapsack(items,capacity):
    items.sort(key = lambda x:x.profit/x.weight,reverse = True)
    total_profit = 0
    for item in items:
        if capacity - item.weight >= 0:
            capacity = capacity - item.weight
            total_profit += item.profit
        else:
            fract = capacity/item.weight
            total_profit += item.profit*fract
    return total_profit 

# Example usage
items = [Item(5,1),Item(10,3),Item(15,5),Item(7,4),Item(8,1),Item(9,3),Item(4,2)]
capacity = 15

max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in knapsack = {max_value}")


