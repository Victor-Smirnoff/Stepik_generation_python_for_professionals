def same_parity(numbers):
    if len(numbers) == 0:
        return numbers
    elif numbers[0] % 2 == 0:
        return [num for num in numbers if num % 2 == 0]
    elif numbers[0] % 2 != 0:
        return [num for num in numbers if num % 2 != 0]
