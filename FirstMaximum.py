def LargestNumber(numbers):
    """
    Finds the largest number in a given list.

    Agrs:
        numbers (list): A list of numbers.

    Returns:
        int: The largest number in the list.
    """

    biggest_num= numbers[0]

    for num in numbers:
        if num > biggest_num:
            biggest_num = num
    
    return biggest_num

def SecondLargest(numbers):
    """
    Finds the second largest number in a given list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The second largest number in the list.
    
    """
    first_max= max(numbers[0], numbers[1])
    second_max= min(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        if numbers[i] > first_max:
            second_max = first_max
            first_max = numbers[i]
        elif numbers[i] > second_max and first_max != numbers[i]:
            second_max = numbers[i]

    return second_max

def main():
    """
    Takes user input for a list of numbers, finds the highest and second highest numbers and
    calculates the difference

    Args:
        None
    
    Returns:
        None
    
    """
    numbers= [int(x) for x in input("Enter the numbers: ").split()]

    highest= LargestNumber(numbers)
    second_highest= SecondLargest(numbers)

    if highest is not None and second_highest is not None:
        difference= highest - second_highest
        print("The difference between the highest and second highest number is: ", difference)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
