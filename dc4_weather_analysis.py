import sys

# Mapper function
def mapper():
    for line in sys.stdin:
        line = line.strip()
        if line:
            columns = line.split(',')
            if len(columns) >= 4:  # Ensure the line has at least 4 columns
                try:
                    year = columns[0]
                    temperature = float(columns[3])  # Temperature is in the 4th column
                    print(f"{year}\t{temperature}")
                except ValueError:
                    # Skip lines with invalid data
                    pass

# Reducer function
def reducer():
    current_year = None
    max_temp = float('-inf')
    min_temp = float('inf')
    hottest_year = None
    coldest_year = None

    # Initialize global hottest and coldest year variables
    global_max_temp = float('-inf')
    global_min_temp = float('inf')
    global_hottest_year = None
    global_coldest_year = None

    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                year, temperature_str = line.split('\t')
                temperature = float(temperature_str)

                if year != current_year:
                    # Update hottest and coldest year across all years
                    if current_year is not None:
                        if max_temp > global_max_temp:
                            global_max_temp = max_temp
                            global_hottest_year = current_year
                        if min_temp < global_min_temp:
                            global_min_temp = min_temp
                            global_coldest_year = current_year

                    # Reset for the new year
                    current_year = year
                    max_temp = temperature
                    min_temp = temperature
                else:
                    # Update max and min for the same year
                    if temperature > max_temp:
                        max_temp = temperature
                    if temperature < min_temp:
                        min_temp = temperature

            except ValueError:
                # Skip lines with invalid format
                pass

    # Final update for the last year processed
    if current_year is not None:
        if max_temp > global_max_temp:
            global_max_temp = max_temp
            global_hottest_year = current_year
        if min_temp < global_min_temp:
            global_min_temp = min_temp
            global_coldest_year = current_year

    # Output results for each year as well as the hottest and coldest years globally
    print(f"Year-wise Max and Min Temperatures:")
    print(f"{current_year}\tMax Temperature: {max_temp}\tMin Temperature: {min_temp}")

    print("\nGlobal Hottest and Coldest Year:")
    print(f"Hottest Year: {global_hottest_year} with Max Temperature: {global_max_temp}")
    print(f"Coldest Year: {global_coldest_year} with Min Temperature: {global_min_temp}")

# Main logic to call the correct function based on arguments
if __name__ == "__main__":
    if '--mapper' in sys.argv:
        mapper()
    elif '--reducer' in sys.argv:
        reducer()
    else:
        print("Invalid argument. Please use --mapper or --reducer.")
# def reducer():
#     current_year = None
#     max_temp = float('-inf')
#     min_temp = float('inf')

#     for line in sys.stdin:
#         line = line.strip()
#         if line:
#             try:
#                 year, temperature = line.split('\t')
#                 temperature = float(temperature)

#                 if year != current_year:
#                     # Print the result for the previous year
#                     if current_year is not None:
#                         print(f"{current_year}\tMax Temperature: {max_temp}\tMin Temperature: {min_temp}")

#                     # Reset the max and min for the new year
#                     current_year = year
#                     max_temp = temperature
#                     min_temp = temperature
#                 else:
#                     # Update the max and min temperature for the same year
#                     if temperature > max_temp:
#                         max_temp = temperature
#                     if temperature < min_temp:
#                         min_temp = temperature

#             except ValueError:
#                 # Skip lines with invalid format
#                 pass
    
#     # Output the result for the last year
#     if current_year is not None:
#         print(f"{current_year}\tMax Temperature: {max_temp}\tMin Temperature: {min_temp}")