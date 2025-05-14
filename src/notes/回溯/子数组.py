input = [1,2,3,4]

# Function to generate all possible subarrays using backtracking
def get_all_subarrays(arr):
    result = []
    n = len(arr)
    
    # Helper function for backtracking
    def backtrack(start, end, current_subarray):
        # If we have a valid subarray, add it to the result
        if start <= end:
            result.append(current_subarray.copy())
        
        # If we've reached the end of the array, return
        if end == n - 1:
            return
        
        # Add the next adjacent element to the current subarray
        current_subarray.append(arr[end + 1])
        # Continue with the next adjacent element
        backtrack(start, end + 1, current_subarray)
        # Backtrack by removing the last element
        current_subarray.pop()
    
    # Start the backtracking process for each possible starting position
    for i in range(n):
        backtrack(i, i - 1, [])  # Start with an empty subarray
        # The second parameter is i-1 so that the first element to be added will be arr[i]
    
    return result

# Get all subarrays of the input
all_subarrays = get_all_subarrays(input)
print(f"Total number of subarrays: {len(all_subarrays)}")
print("All subarrays:")
for subarray in all_subarrays:
    print(subarray)