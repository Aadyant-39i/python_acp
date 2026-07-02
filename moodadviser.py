import datetime

# Part 1: User input
name = input("Enter your name: ")
mood = input("Enter your mood (happy/sad/stressed/tired): ")
energy = int(input("Enter energy level (1-10): "))

print(f"\n--- Report for {name} ---")

# Part 2 & 3: Energy checks (if / if-else)
if energy <= 2:
    print("⚠️ Warning: Your energy is critically low!")

if energy >= 5:
    print("🔋 You have enough energy for your tasks today.")
else:
    print("🪫 Your energy is low. Take it easy.")

# Part 4: Mood advice (if-elif-else)
if mood == "happy":
    print("🌟 Keep spreading that positive energy!")
elif mood == "sad":
    print("💙 It's okay to feel down. Take care of yourself.")
elif mood == "stressed":
    print("🧘 Take a deep breath and take things one step at a time.")
else:
    print("☕ Remember to take a break if you need it.")

# Part 5: Current date and time
current_time = datetime.datetime.now()
print(f"Generated on: {current_time}")