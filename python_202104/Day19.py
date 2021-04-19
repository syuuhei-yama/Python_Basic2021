# #marge
#
# from typing import List
#
# def marge_sort(numbers: List[int]) -> List[int]:
#     if len(numbers) <= 1:
#         return numbers
#
#     center = len(numbers) // 2
#     left = numbers[:center]
#     right = numbers[center:]
#
#     marge_sort(left)
#     marge_sort(right)
#
#     i = j = k = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             numbers[k] = left[i]
#             i += 1
#         else:
#             numbers[k] = right[j]
#             j += 1
#         k += 1
#
#     while i < len(left):
#         numbers[k] = left[i]
#         i += 1
#         k += 1
#
#     while j < len(right):
#         numbers[k] = right[j]
#         j += 1
#         k += 1
#
#     return  numbers
#
# if __name__ == "__main__":
#     nums = [5,4,1,8,7,3,2,9]
#     print(marge_sort(nums))

