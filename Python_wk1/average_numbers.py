def average_numbers(numbers):
    average = sum(numbers) / len(numbers)
    return average
    
    
first_average = average_numbers([1,2,3])
second_average = average_numbers([4,5,6])

print(first_average,second_average)