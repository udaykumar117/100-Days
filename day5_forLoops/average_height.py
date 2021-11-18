# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(student_heights)
count = 0
height = 0
for n in student_heights:
    # print(n)
    count = count+1
    print(count)
    height = height + n
    print(height)
avg_height = height/count
print(f"Average height of the students is {round(avg_height)}")