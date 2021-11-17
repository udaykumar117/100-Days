#Write your code below this row 👇
evenSum = 0
for number in range(1, 101):
    if number%2 ==0:
        print(number)
        evenSum += number
print(f"Sum of even numbers is: {evenSum}")

