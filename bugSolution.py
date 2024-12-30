def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    if total == 0:
        return 0 #Handle list with only zeros
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average is: {average}")

my_list_with_zero = [1,0,2,0,3]
average = calculate_average(my_list_with_zero)
print(f"The average is: {average}")

my_zero_list = [0,0,0]
average = calculate_average(my_zero_list)
print(f"The average is: {average}") #This will print 0 which is correct