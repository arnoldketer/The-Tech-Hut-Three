def LargestNumber(numbers):
    biggest_num= numbers[0]

    for num in numbers:
        if num > biggest_num:
            biggest_num = num
    
    return biggest_num

def SecondLargest(numbers):
    first_max= max(numbers[0], numbers[1])
    second_max= min(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        if numbers[i] > first_max:
            second_max = first_max
            first_max = numbers[i]
        elif numbers[i] > second_max and first_max != numbers[i]:
            second_max = numbers[i]

    return second_max
