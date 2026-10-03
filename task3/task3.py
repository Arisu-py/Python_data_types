list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

ids1 = [el["id"] for el in list1]
ids2 = [el["id"] for el in list2]

common_ids = [i for i in ids1 if i in ids2]
unique_ids = [i for i in ids1 if i not in ids2] + [i for i in ids2 if i not in ids1]

intersection = [el for el in list1 if el["id"] in common_ids]
unique_only  = [el for el in list1 + list2 if el["id"] in unique_ids]

print("Пересечение:", intersection)
print("Уникальные:", unique_only)
