scores = [3, 7, 2, 9, 4, 1, 8, 5, 6]
n = len(scores)




input("\n--- METHOD 2: Linear Search (Left to Right) --- Press Enter ")
print("List:", scores, "  n =", n)
user_target = input("Enter a number to search for [Default 9]: ")

try:
    target_linear = int(user_target) if user_target.strip() else 9
except ValueError:
    print("  Invalid input! Searching for default value 9.")
    target_linear = 9

steps_linear = 0
for score in scores:
    steps_linear += 1
    if score == target_linear:
        break

print("  Target =", target_linear, "  found at position", steps_linear, "  checks =", steps_linear)

input("Compare with best and worst case. Press Enter ")
mid = n // 2
print("  Best: 1 check -> O(1)   Average:", mid, "checks -> O(n)   Worst:", n, "checks -> O(n)   Yours:", steps_linear)
print("  Big-O = worst case = O(n).")



