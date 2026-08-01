def find_pair_with_sum(arr, target_sum):
    """
    Finds if there's a pair in a sorted array that sums up to the target_sum
    using the Two Pointers pattern.
    """
    # Initialize two pointers: one at the beginning, one at the end.
    left = 0 # Left pointer
    right = len(arr) - 1 # Right pointer

    print(f"Searching for a pair that sums to {target_sum} in array: {arr}")

    # Continue as long as the left pointer is before the right pointer
    while left < right:
        current_sum = arr[left] + arr[right]

        print(f"  Pointers at indices {left} ({arr[left]}) and {right} ({arr[right]}). Current sum: {current_sum}")

        if current_sum == target_sum:
            # If the current sum equals the target, we found a pair.
            # This is where the Two Pointers pattern successfully identifies a solution.
            print(f"  Found pair: ({arr[left]}, {arr[right]}) at indices {left}, {right}")
            return True, (arr[left], arr[right])
        elif current_sum < target_sum:
            # If the current sum is less than the target, we need a larger sum.
            # Move the left pointer to the right to increase the sum, as the array is sorted.
            print(f"  Current sum {current_sum} < {target_sum}. Moving left pointer right.")
            left += 1
        else: # current_sum > target_sum
            # If the current sum is greater than the target, we need a smaller sum.
            # Move the right pointer to the left to decrease the sum, as the array is sorted.
            print(f"  Current sum {current_sum} > {target_sum}. Moving right pointer left.")
            right -= 1

    # If the loop finishes, no such pair was found.
    print(f"  No pair found that sums to {target_sum}.")
    return False, None

if __name__ == "__main__":
    print("--- Example 1: Pair found ---")
    sorted_array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target1 = 15
    found, pair = find_pair_with_sum(sorted_array1, target1)
    if found:
        print(f"Result: Yes, {pair[0]} + {pair[1]} = {target1}\n")
    else:
        print(f"Result: No pair found.\n")

    print("--- Example 2: No pair found ---")
    sorted_array2 = [10, 20, 30, 40, 50]
    target2 = 100
    found, pair = find_pair_with_sum(sorted_array2, target2)
    if found:
        print(f"Result: Yes, {pair[0]} + {pair[1]} = {target2}\n")
    else:
        print(f"Result: No pair found.\n")

    print("--- Example 3: Edge case - empty array ---")
    sorted_array3 = []
    target3 = 5
    found, pair = find_pair_with_sum(sorted_array3, target3)
    if found:
        print(f"Result: Yes, {pair[0]} + {pair[1]} = {target3}\n")
    else:
        print(f"Result: No pair found.\n")

    print("--- Example 4: Edge case - single element array ---")
    sorted_array4 = [7]
    target4 = 7
    found, pair = find_pair_with_sum(sorted_array4, target4)
    if found:
        print(f"Result: Yes, {pair[0]} + {pair[1]} = {target4}\n")
    else:
        print(f"Result: No pair found.\n")

    print("--- Example 5: Another pair found with negative numbers ---")
    sorted_array5 = [-5, -2, 0, 1, 3, 6, 8, 10]
    target5 = 5
    found, pair = find_pair_with_sum(sorted_array5, target5)
    if found:
        print(f"Result: Yes, {pair[0]} + {pair[1]} = {target5}\n")
    else:
        print(f"Result: No pair found.\n")