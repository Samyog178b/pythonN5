print("Please enter your maths test score:")
mathstestscore = int(input())

print("Please enter your English test score:")
englishtestscore = int(input())

print("Please enter your computing test score:")
computingtestscore = int(input())

total_score = mathstestscore + englishtestscore + computingtestscore
average_score = total_score / 3

print("Total score:", total_score)
print("Average score:", average_score)
