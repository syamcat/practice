gil = {'국어' : 80, '영어' : 75, '수학' : 55}

score = list(gil.values())
subjects = list(gil.keys())
total = 0

while score:
    total += score.pop()

print(total / len(subjects))