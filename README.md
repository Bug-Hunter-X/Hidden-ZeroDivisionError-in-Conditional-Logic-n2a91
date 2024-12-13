# Hidden ZeroDivisionError in Conditional Logic

This example showcases a ZeroDivisionError in Python that is triggered only under a specific condition.  It demonstrates how a seemingly simple conditional statement can mask a potential runtime error.  The solution demonstrates using exception handling to gracefully manage this scenario and prevent unexpected program termination.

## Bug

The `function_with_uncommon_error` function will raise a ZeroDivisionError if the input `a` is 0. This error is hidden within the `if` statement, making it harder to detect during initial code review.