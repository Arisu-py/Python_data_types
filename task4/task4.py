items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]

grouped_items = dict()

for name, category in items:
    grouped_items[category] = grouped_items.get(category, []) + [name]

print(grouped_items)
