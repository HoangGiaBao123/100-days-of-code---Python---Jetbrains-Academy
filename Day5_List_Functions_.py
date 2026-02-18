# Some built-in functions to work with numbers in array
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# You can use max to find the max() to find the highest score in the array:
highest_score = max(student_scores)
print(highest_score)  # Output: 199 (the highest)

# But how does max() work behind the scenes? See:
max_score = student_scores[0]
for scores in student_scores:
    if scores > max_score:
        max_score = scores
print(max_score)  # Output: 199 (the highest)

# Next: You can use the min() to find the lowest score in the array:
lowest_score = min(student_scores)
print(lowest_score)  # Output: 24 (the lowest)

# But how does the min() work behind the scenes? See:
min_score = student_scores[0]
for score in student_scores:
    if score < min_score:
        min_score = score
print(min_score)  # Output: 24 (the lowest)

# Finally: You can use sum() to get the sum of the array:
scores_sum = sum(student_scores)
print(scores_sum)  # Output: 2068

# But how does the sum() work behind the scenes? See:
s_sum = 0
for s in student_scores:
    s_sum += s
print(s_sum)  # Output: 2068
