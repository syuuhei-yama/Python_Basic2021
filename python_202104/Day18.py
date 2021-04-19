#radix

# from typing import List
#
# def counting_sort(numbers: List[int], place: int) -> List[int]:
#     counts = [0] * 10
#     result = [0] * len(numbers)
#
#     for num in numbers:
#         index = int(num / place) % 10
#         counts[index] += 1
#
#     for i in range(1, 10):
#         counts[i] += counts[i - 1]
#
#     i = len(numbers) -1
#     while i >= 0:
#         index = int(numbers[i]/place) % 10
#         result[counts[index]-1] = numbers[i]
#         counts[index] -= 1
#         i -= 1
#
#     return result
#
# def radix_sort(numbers: List[int]) -> List[int]:
#     max_num = max(numbers)
#     place = 1
#     while max_num > place:
#         numbers = counting_sort(numbers, place)
#         place *= 10
#     return  numbers
#
# if __name__ == "__main__":
#     import random
#     nums = [random.randint(0, 100) for _  in range(10)]
#     print(radix_sort(nums))


#quick

from typing import List

def partition(numbers: List[int],low: int, high:int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j],numbers[i]
    numbers[i+1], numbers[high] = numbers[high],numbers[i + 1]
    return i + 1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int],low: int,high:int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index - 1)
            _quick_sort(numbers, partition_index+1, high)


    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers



if __name__ == "__main__":
    import random
    nums = [random.random(0, 1000) for _ in range(10)]
    print(quick_sort(nums))
