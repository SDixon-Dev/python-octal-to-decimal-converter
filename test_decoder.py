from decoder import decode

def main():
    """
    Tests the decode() function using a variety of octal values.

    Each test case contains:
    - An octal input string.
    - The expected decimal output.

    The function compares the actual output returned by decode()
    against the expected output and reports whether each test passes.
    """

    # Create a list containing all test cases.
    # Each test case is stored as a tuple: (octal_input, expected_decimal_output)
    test_cases = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("7", "7"),
        ("10", "8"),
        ("16", "14"),
        ("100", "64"),
        ("34 56", "28 46"),
        ("120 156 206", "80 110 134"),
        ("17", "15"),
        ("20", "16"),
        ("77", "63"),
        ("777", "511"),
        ("1 10 100", "1 8 64")
    ]

    # Counter to keep track of how many tests pass.
    passed = 0

    # Loop through every test case.
    # enumerate() automatically numbers each test, starting from 1.
    for i, (octal_input, expected_output) in enumerate(test_cases, start=1):

        print(f"Test {i}")
        print(f"Input:          {octal_input}")

        # Calls the function using the current octal input and stores the returned result.
        actual_output = decode(octal_input)

        print(f"Expected:       {expected_output}")
        print(f"Actual:         {actual_output}")

         #Compare the actual & expected outputs.
        if actual_output == expected_output:
            print("Result:         PASSED\n")
            passed += 1
        else:
            print("Result:         FAILED\n")

    # Display the overall testing summary.
    print("-" * 40)
    print(f"Tests Passed: {passed}/{len(test_cases)}")

# Only executes tests if this file is run directly.
# Prevents tests from auto running if this file is imported into another program.
if __name__ == "__main__":
    main()