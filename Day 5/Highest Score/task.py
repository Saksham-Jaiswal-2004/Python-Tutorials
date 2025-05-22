student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

total = sum(student_scores)
print(total)

sum = 0
for score in student_scores:
    sum += score

print(sum)

print(max(student_scores))

maximum = 0

for data in student_scores:
    if(data>maximum):
        maximum = data

print(maximum)