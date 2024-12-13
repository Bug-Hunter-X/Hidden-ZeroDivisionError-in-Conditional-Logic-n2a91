def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return 1 / a
        else:
            return a + b
    except ZeroDivisionError:
        return float('inf')  # Or handle the error as appropriate

# Example usage:
print(function_with_uncommon_error(5, 2))  # Output: 7
print(function_with_uncommon_error(0, 2))  # Output: inf