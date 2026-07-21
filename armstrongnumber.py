
num_str = input("Enter a number: ")
power = len(num_str)


total = 0
for digit in num_str:
    total += int(digit) ** power

if total == int(num_str):
    print(num_str,"is an Armstrong number!")
else:
    print(num_str,"is not an Armstrong number.")

    