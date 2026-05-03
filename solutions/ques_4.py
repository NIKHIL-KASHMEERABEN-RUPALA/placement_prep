from collections import defaultdict

def max_price_selector(items, n, k):

    item_collection = defaultdict(list)

    
    for item in items:
        price, category = item.split(":")
        price = int(price)

        item_collection[category].append(price)

    selected_prices = []

    
    for category, prices in item_collection.items():

        prices.sort(reverse=True)

        selected_prices.extend(prices[:k])

    
    selected_prices.sort(reverse=True)

    
    final_selected = selected_prices[:n]

    final_total = sum(final_selected)

    return final_total, final_selected



items = [
    "500:Electronics",
    "400:Electronics",
    "300:Electronics",
    "200:Sports",
    "150:Beauty",
    "100:Beauty"
]

total, selected = max_price_selector(items, n=4, k=2)

print(f"Maximum Price = {total}")
print(f"Selected Prices = {selected}")