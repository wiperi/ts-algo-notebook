# Assume the function to be tested is named solution(laps)
# You would replace 'pass' with the actual implementation
from time import sleep


def solution(laps: list[list[int]]):
    # Placeholder for the actual implementation
    # Example implementation logic outline:
    # 1. Parse initial drivers and times from lap 0.
    # 2. Initialize personal bests for each driver.
    # 3. Keep track of active drivers (initially all).
    # 4. Initialize an empty list for eliminated drivers.
    # 5. Loop through laps (starting from lap 0):
    #    a. If less than 2 active drivers, break the loop.
    #    b. Update personal bests for active drivers based on the current lap's times.
    #    c. Find the slowest personal best time among active drivers.
    #    d. Identify all active drivers who have this slowest personal best time.
    #    e. Sort the names of these drivers alphabetically.
    #    f. Add these sorted names to the eliminated drivers list.
    #    g. Remove these drivers from the set of active drivers.
    # 6. Get the names of the final remaining active drivers.
    # 7. Sort the remaining drivers' names alphabetically.
    # 8. Append the sorted remaining drivers to the eliminated list.
    # 9. Return the combined list.
    # Replace this with your actual code
    # res = []

    # eliminated = set()

    # for lap in laps:
    #     lap_data = [s.split(" ") for s in lap]
    #     for data in lap_data:
    #         data[1] = int(data[1])

    #     # Remove eliminated
    #     lap_data = [v for v in lap_data if v[0] not in eliminated]
    #     # print("remove eliminated", lap_data)

    #     # Find the largest time
    #     maxTime = float("-inf")
    #     for data in lap_data:
    #         maxTime = max(maxTime, data[1])
    #     # print("max time", maxTime)

    #     # Find slowest driver list
    #     slowest = list(filter(lambda data: data[1] == maxTime, lap_data))
    #     # print("slow list", slowest)

    #     # Sort slowest driver list
    #     slowest = list(map(lambda x: x[0], slowest))
    #     slowest.sort()
    #     # print("sort slow list", slowest)

    #     # Add to res
    #     eliminated.update(slowest)
    #     res.extend(slowest)

    #     # print("lap_data", lap_data, end="\n\n\n")

    # res.extend([v[0] for v in lap_data if v[0] not in eliminated])
    # return res
    died = set()
    res = []
    
    for lap in laps:
        # 转换并过滤数据
        processed_lap = [
            (name, int(time))  # 元组替代数组
            for name, time in (item.split() for item in lap)
            if name not in died
        ]
        
        if not processed_lap:
            continue
            
        # 找出最大时间
        max_time = max(time for _, time in processed_lap)
        
        # 找出最慢的选手并排序
        slowest = sorted(
            [name for name, time in processed_lap if time == max_time]
        )
        
        # 更新结果
        died.update(slowest)  # 使用 update 替代循环 add
        res.extend(slowest)   # 使用 extend 替代循环 append

    remaining = sorted([name for name, _ in processed_lap if name not in died])
    res.extend(remaining)
        
    return res


# --- Test Cases ---

# Test Case 1: Example from the description
laps1 = [
    ["Harold 154", "Gina 155", "Juan 160"],
    ["Juan 152", "Gina 153", "Harold 160"],
    ["Harold 148", "Gina 150", "Juan 151"],
]
expected1 = ["Juan", "Harold", "Gina"]
# Explanation:
# Lap 1 Bests: H=154, G=155, J=160. Slowest: Juan (160). Elim: Juan. Active: H, G.
# Lap 2 Bests: H=154 (from Lap 1), G=153. Slowest: Harold (154). Elim: Harold. Active: G.
# Lap 3 Bests: G=150. Gina remains.
# Order: Juan, Harold, Gina

# Test Case 2: Tie for elimination (alphabetical order matters)
laps2 = [["Alice 100", "Bob 90", "Charlie 100"], ["Alice 95", "Bob 85", "Charlie 98"]]
expected2 = ["Alice", "Charlie", "Bob"]
# Explanation:
# Lap 1 Bests: A=100, B=90, C=100. Slowest: Alice, Charlie (100). Elim: Alice, Charlie (alpha order). Active: B.
# Lap 2 Bests: B=85. Bob remains.
# Order: Alice, Charlie, Bob

# Test Case 3: Single Lap
laps3 = [["DriverA 210", "DriverB 200", "DriverC 210", "DriverD 205"]]
expected3 = ["DriverA", "DriverC", "DriverB", "DriverD"]
# Explanation:
# Lap 1 Bests: A=210, B=200, C=210, D=205. Slowest: A, C (210). Elim: A, C (alpha order). Active: B, D.
# End of race. Remaining: B, D (alpha order).
# Order: DriverA, DriverC, DriverB, DriverD

# Test Case 4: Personal Best Improvement prevents elimination
laps4 = [["Eve 150", "Frank 140"], ["Eve 130", "Frank 145"]]
expected4 = ["Eve", "Frank"]
# Explanation:
# Lap 1 Bests: E=150, F=140. Slowest: Eve (150). Elim: Eve. Active: F.
# Lap 2 Bests: F=140 (from Lap 1). Frank remains.
# Order: Eve, Frank

# Test Case 5: Early Personal Best helps later
laps5 = [["Grace 130", "Heidi 140"], ["Grace 150", "Heidi 145"]]
expected5 = ["Heidi", "Grace"]
# Explanation:
# Lap 1 Bests: G=130, H=140. Slowest: Heidi (140). Elim: Heidi. Active: G.
# Lap 2 Bests: G=130 (from Lap 1). Grace remains.
# Order: Heidi, Grace

# Test Case 6: Single Driver
laps6 = [["Ivy 200"], ["Ivy 190"]]
expected6 = ["Ivy"]
# Explanation:
# Only one driver, Ivy. She remains.
# Order: Ivy

# Test Case 7: All drivers eliminated simultaneously
laps7 = [["Ken 100", "Leo 100", "Mia 100"]]
expected7 = ["Ken", "Leo", "Mia"]
# Explanation:
# Lap 1 Bests: K=100, L=100, M=100. Slowest: All (100). Elim: K, L, M (alpha order). Active: None.
# End of race. No remaining drivers.
# Order: Ken, Leo, Mia

# Test Case 8: More laps and drivers
laps8 = [
    ["A 50", "B 55", "C 60", "D 58"],
    ["A 51", "B 52", "C 59", "D 61"],
    ["A 49", "B 53", "C 57", "D 56"],
]
expected8 = ["C", "D", "B", "A"]
# Explanation:
# Lap 1 Bests: A=50, B=55, C=60, D=58. Slowest: C (60). Elim: C. Active: A, B, D.
# Lap 2 Bests: A=50, B=52, D=58. Slowest: D (58). Elim: D. Active: A, B.
# Lap 3 Bests: A=49, B=52. Slowest: B (52). Elim: B. Active: A.
# End of race. A remains.
# Order: C, D, B, A

# Test Case 9: Only two drivers, one clearly slower
laps9 = [["Fast 100", "Slow 200"], ["Fast 99", "Slow 201"], ["Fast 98", "Slow 199"]]
expected9 = ["Slow", "Fast"]
# Explanation:
# Lap 1 Bests: Fast=100, Slow=200. Slowest: Slow(200). Elim: Slow. Active: Fast.
# Fast remains.
# Order: Slow, Fast


# --- Running the tests ---
# You would run your implemented solution function against these inputs
# For example:
# result1 = solution(laps1)
# assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {result1}"
# print("Test Case 1 Passed")

# result2 = solution(laps2)
# assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {result2}"
# print("Test Case 2 Passed")

# ... and so on for all test cases

print(
    "Test definitions complete. Replace 'pass' in the solution function and uncomment assertion lines to run."
)

# Example of how you might run them (assuming solution is implemented)
test_cases = [
    (laps1, expected1),
    (laps2, expected2),
    (laps3, expected3),
    (laps4, expected4),
    (laps5, expected5),
    (laps6, expected6),
    (laps7, expected7),
    (laps8, expected8),
    (laps9, expected9),
]

for i, (laps_input, expected_output) in enumerate(test_cases):
    try:
        result = solution(laps_input)  # Call your function here
        assert result == expected_output, f"Expected {expected_output}, Got {result}"
        print(f"Test Case {i+1} Passed")
    except AssertionError as e:
        print(f"Test Case {i+1} Failed: {e}")
    except Exception as e:
        print(f"Test Case {i+1} Failed with unexpected error: {e}")
