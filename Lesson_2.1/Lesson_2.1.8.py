def index_of_nearest(numbers, number):
    res = [abs(number - numbers[i]) for i in range(len(numbers))]
    return -1 if numbers == [] else res.index(min(res))
