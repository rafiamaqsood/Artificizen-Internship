# Merge two dictionaries; if a key exists in both, sum the values. 

semester1_marks = {
    "AI": 90,
    "ML": 95,
    "DL": 87
}
semester2_marks = {
    "PF": 90,
    "ML": 95,
    "DB": 87
}
merge = semester1_marks.copy()
for key, value in semester2_marks.items():
    if key in merge:
        merge[key] += value
    else:
        merge[key] = value
print(merge)