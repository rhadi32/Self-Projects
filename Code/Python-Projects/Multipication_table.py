while True:
    row = int(input("How many rows: "))
    column = int(input("How many columns: "))

# Determine the maximum number of characters needed for any
# multiplication result
    max_width = len(str(row * column))

    for i in range(1, row + 1):  # Loop through each row
        for j in range(1, column + 1):  # Loop through each column
            result = i * j
        # Calculate the appropriate spacing based on the maximum
        # width of the results
            print(f'{result:{max_width}}', end=' ')
        print()  # Move to the next line after each row
