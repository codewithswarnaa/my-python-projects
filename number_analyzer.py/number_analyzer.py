# Number Analyzer

n = int(input("Enter a number: "))

sum_all = 0
sum_even = 0
sum_odd = 0

print("\nNumbers from 1 to n:")

for i in range(1, n + 1):
    print(i, end=" ")

    sum_all += i

    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("\n\nSum of all numbers =", sum_all)
print("Sum of even numbers =", sum_even)
print("Sum of odd numbers =", sum_odd)

# Check total sum
if sum_all % 2 == 0:
    print("Total sum is EVEN")
else:
    print("Total sum is ODD")