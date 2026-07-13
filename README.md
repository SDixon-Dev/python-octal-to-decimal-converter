# Octal to Decimal Decoder

## Overview

This project was completed as part of my **BSc (Hons) Computer Science** coursework. The objective was to develop a Python program capable of converting one or more **octal (base-8)** numbers into their **decimal (base-10)** equivalents.

Rather than relying on Python's built-in conversion functions, the solution manually performs the conversion by applying the mathematical method of multiplying each digit by the appropriate power of 8 before summing the results. This demonstrates an understanding of number systems, loops, string manipulation and algorithm design.

---

## Features

- Converts a single octal number into decimal.
- Converts multiple space-separated octal numbers in a single input.
- Returns the converted values as a correctly formatted string.
- Implements the conversion algorithm manually using loops and arithmetic.
- Includes a custom test script containing both the original coursework examples and additional test cases.

---

## Technologies Used

- Python 3

---

## Project Structure

```text
Task_03/
│
├── decoder.py          # Main solution containing the decode() function.
├── helper_3.py         # Original helper file supplied for coursework testing.
└── test_decoder.py     # Additional test program created to verify functionality.
```

---

## How the Program Works

The `decode()` function accepts a string containing one or more octal numbers separated by spaces.

For each octal number, the program:

1. Splits the input into individual values.
2. Processes each digit from left to right.
3. Multiplies each digit by the corresponding power of 8 based on its position.
4. Adds the calculated values together to produce the decimal equivalent.
5. Returns all converted values as a single space-separated string.

### Example

**Input**

```text
120 156 206
```

**Output**

```text
80 110 134
```

---

## Testing

Two methods were used to verify the program:

- **Official helper file** supplied with the coursework to confirm the solution met the required specification.
- **Custom test program** created to perform additional testing and demonstrate independent verification of the solution.

The custom tests include:

- Single-digit octal values
- Multi-digit octal values
- Multiple values in a single input string
- Additional edge cases beyond those provided in the coursework

---

## Skills Demonstrated

This project demonstrates practical experience with:

- Python functions
- String manipulation
- Lists
- Nested loops
- Mathematical algorithms
- Number system conversion (Octal to Decimal)
- Testing and debugging
- Code documentation and commenting

---

## Learning Outcomes

Through completing this project I developed a stronger understanding of:

- Implementing algorithms without relying on built-in conversion functions.
- Breaking larger problems into smaller logical steps.
- Processing collections of data using loops.
- Writing readable, well-commented and maintainable Python code.
- Creating repeatable tests to verify program correctness.

---

## Author

**Sean Dixon**

Computer Science Graduate (BSc Hons)

This repository forms part of my programming portfolio and demonstrates fundamental Python programming and algorithm implementation skills.
