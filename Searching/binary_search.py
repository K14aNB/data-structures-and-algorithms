"""
Binary Search Algorithm
"""

def binary_search(arr:list[int], num:int) -> bool:
    """
    Function to perform binary search on a sorted list of integers to check if an integer
    is present.

    Arguments
    ---------
        arr (list[int]): List of integers.
        num (int): Any integer.

    Returns
    -------
        True if `num` is present in `arr` else False
    """
    if arr[0] == num or arr[-1] == num:
        return True

    low = 0
    high = len(arr) - 1
    mid = low + ((high - low) // 2)

    while low < high:
        if num == arr[mid]:
            return True
        elif num < arr[mid]:
            high = mid - 1
        elif num > arr[mid]:
            low = mid + 1

        mid = low + ((high - low) // 2)

    return False


if __name__ == "__main__":
    list_of_integers = [1, 2, 3, 6, 8, 11, 13, 15]
    number = 11
    if binary_search(arr=list_of_integers, num=number):
        print("Number is Present")
    else:
        print("Number is not Present")


