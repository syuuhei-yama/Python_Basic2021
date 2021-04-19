#Shell sort
# from typing import List
#
# def shell_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     gap = len_numbers // 2
#     while gap > 0:
#         for i in range(gap, len_numbers):
#             temp = numbers[i]
#             j = i
#             while j >= gap and numbers[j - gap] > temp:
#                 numbers[j] = numbers[j -gap]
#                 j -= gap
#             numbers[j] = temp
#         gap //= 2
#
#     return numbers
#
# if __name__ == "__main__":
#     import random
#     nums = [random.randint(0, 100) for _ in range(10)]
#     print(shell_sort(nums))


#counting sort
# from typing import List
#
# def counting_sort(numbers: List[int]) -> List[int]:
#     max_num = max(numbers)
#     counts = [0] * (max_num + 1)
#     result = [0] * len(numbers)
#
#     for num in numbers:
#         counts[num] += 1
#
#     for i in range(1, len(counts)):
#         counts[i] += counts[i - 1]
#
#     i = len(numbers) -1
#     while i >= 0:
#         index = numbers[i]
#         result[counts[index]-1] = numbers[i]
#         counts[index] -= 1
#         i -= 1
#
#     return result
#
# if __name__ == "__main__":
#     import random
#     nums = [random.randint(0, 100) for _  in range(10)]
#     print(counting_sort(nums))

