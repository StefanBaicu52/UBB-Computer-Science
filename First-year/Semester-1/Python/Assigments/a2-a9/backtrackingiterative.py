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


def mountain_subsets(nums):
    result = []
    n = len(nums)

    # Stack to hold (current subset, start index, peak_found flag)
    stack = [([], 0, False)]

    while stack:
        current, start, peak_found = stack.pop()

        # Check if the current subset is a valid mountain
        if len(current) >= 3 and is_mountain(current):
            result.append(current.copy())

        for i in range(start, n):
            # Update peak_found based on the current value
            new_peak_found = peak_found or (len(current) > 0 and (current[-1] < nums[i]))

            # Ensure that the current subset remains valid
            if len(current) == 0 or (
                    len(current) < 2 or (current[-1] < nums[i] and not peak_found) or (current[-1] > nums[i])):
                stack.append((current + [nums[i]], i + 1, new_peak_found))

    return result


# Exemplu
nums = [10, 16, 27, 18, 14, 7]
mountain_aspect_subsets = mountain_subsets(nums)
for subset in mountain_aspect_subsets:
    print(subset)