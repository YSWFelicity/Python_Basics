student_scores = [150, 142, 185, 120, 171, 183, 69, 59]

total_score = sum(student_scores)
print(total_score)

sum = 0
for score in student_scores:
  sum += score

print(sum)

print(max(student_scores))

max = 0
for score in student_scores:
  if score > max:
    max = score

print(max)

