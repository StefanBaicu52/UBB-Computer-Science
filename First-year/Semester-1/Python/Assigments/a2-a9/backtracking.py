def is_mountain(subset):
    n = len(subset)
    if n < 3:
        return False  # A mountain requires at least 3 points
    peak_found = False
    increasing = True

    for i in range(1, n):
        if increasing:
            if subset[i] > subset[i - 1]:
                continue
            elif subset[i] < subset[i - 1]:
                increasing = False
                peak_found = True
            else:
                return False  # Equal elements not allowed
        else:
            if subset[i] < subset[i - 1]:
                continue
            else:
                return False  # After peak, it must decrease
    return peak_found  # Must have found a peak

def backtrack(start, current, nums, result, peak_found):
    n = len(current)

    # If we have a valid current mountain, add it to results
    if n >= 3 and is_mountain(current):
        result.append(current.copy())

    for i in range(start, len(nums)):
        # Check if we can add nums[i] to current
        if n == 0 or (n < 2 or (current[-1] < nums[i] and not peak_found)) or (current[-1] > nums[i]):
            # Update peak_found based on the current value
            new_peak_found = peak_found or (n > 0 and current[-1] < nums[i])
            current.append(nums[i])
            backtrack(i + 1, current, nums, result, new_peak_found)
            current.pop()

def mountain_subsets(nums):

    result = []
    backtrack(0, [], nums, result, False)  # Initialize peak_found as False
    return result

# Exemplu
nums = [10, 16, 27, 18, 14, 7]
mountain_aspect_subsets = mountain_subsets(nums)

for subset in mountain_aspect_subsets:
   print(subset)