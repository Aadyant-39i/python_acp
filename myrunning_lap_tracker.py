
def calculate_points_formula(n):
    return n * (n + 1) // 2

def calculate_points_loop(n):
    total_points = 0
    for i in range(1, n + 1):
        total_points += i
    return total_points


def calculate_points_nested(n):
    total_points = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            total_points += 1
    return total_points


if __name__ == "__main__":
    laps = 100
    print(f"Total points for {laps} laps:")
    print(f"Formula Method: {calculate_points_formula(laps)}")
    print(f"Single Loop Method: {calculate_points_loop(laps)}")
    print(f"Nested Loop Method: {calculate_points_nested(laps)}")
