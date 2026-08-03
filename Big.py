import math
import sys  # TEST 1: Unused import (Flake8 should catch this)
import os, sys  # TEST 2: Multiple imports on one line & duplicate import


# TEST 3: Too many blank lines above this function
def deeply_nested_complex_function(x, y, z):
    # TEST 4: High Cyclomatic Complexity (Radon should flag this)
    # Deeply nested if/else statements trigger high complexity scores.
    if x > 0:
        if y > 0:
            if z > 0:
                print("All positive")
                if x == y:
                    for i in range(10):
                        if i == z:
                            return math.sqrt(x)
            else:
                print("Z is negative")
        else:
            if z > 0:
                print("Y is negative")
            else:
                print("Y and Z are negative")
    else:
        print("X is negative")

    # TEST 5: Line too long (Flake8 standard maximum is 79 characters)
    very_long_string_variable_that_violates_pep8_standards_because_it_has_way_too_many_characters_in_a_single_line = (
        x + y + z
    )

    # TEST 6: Bad white spacing around operators
    result = x + y * z  # No spaces around operators
    bad_spacing = [1, 2, 3]  # Spaces after opening bracket

    return result


# TEST 7: Missing blank lines between functions
def another_bad_function():
    # TEST 8: Indentation error (3 spaces instead of 4)
   print("Bad indentation")
