def decode(code):

    """
    Converts one or more space-separated octal numbers into decimal numbers
    :param code: A string containing octal numbers separated by spaces.
    :return: A string containing the equivalent decimal numbers.
    
    """
    # Splits the input string into individual octal numbers.
    octal_numbers = code.split() #
    
    # Creates an empty string to store converted decimal numbers.
    decimal_results = []
    
    # Loop through each octal number in the list.
    for octal_number in octal_numbers: #  
        decimal_value = 0 # Stores the decimal value as its calculated.
        position = len(octal_number) - 1  # Start with the highest power of 8 (left-most digit).

         # Loop through each digit in the current octal number.
        for digit in octal_number:
             
            # Convert digit to integer, multiplies by the correct power, adds to running total.
            decimal_value += int(digit) * (8 ** position) 
            position -= 1 # Move to the next lower power of 8.

        # Converts decimal number to a string and stores in the list.
        decimal_results.append(str(decimal_value))

      # Joins all decimal numbers together into single string separated by spaces.
    return " ".join(decimal_results) 
   