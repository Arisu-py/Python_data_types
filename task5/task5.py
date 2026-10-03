data = [
    {"student": "Alice", "subject": "Math", "grade": 5},
    {"student": "Bob", "subject": "Math", "grade": 4},
    {"student": "Alice", "subject": "History", "grade": 3},
    {"student": "Bob", "subject": "History", "grade": 5},
]
new_data = {}

for item in data:
    if item["subject"] in new_data:
        new_data[item["subject"]][item['student']] = item["grade"]
    else:
        new_data[item["subject"]] = {item['student']: item["grade"]}

print(new_data)
