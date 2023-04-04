# Input list A
# A = [10, 29, 13, 53, 33, 48, 76, 70, 5, 5]
A = [1, 2, 3, 4, 5, 6, 7, 8]


def check_and_continue(ave, arr):
    """
    :param ave: Average of the original input list
    :param arr: The list in this step, elements might've been taken out
    :return: True if the current list's average is equal to the average of the original input list, false otherwise
    """
    if len(arr):

        if ave == sum(arr) / len(arr):
            return True

        check_and_continue(ave, arr[1:])

        for i in range(len(arr) - 1):
            check_and_continue(ave, arr[:i] + arr[(i + 1):])

        check_and_continue(ave, arr[:-1])

    return False


"""
We don't have to find 2 lists with the same averages because to achieve that the have to have the same average as the
starting list, because list B's average can't get bigger without list C's getting smaller and vica versa.
This simplifies the task to finding a sublist of our list in which the average of the numbers equals to the initial 
average.
"""


def split_array_same_average(nums):
    """
    :param nums: List of numbers to split
    :return: True is the list can be split into two lists with the same average
    """

    # First we sort the list and take the average of it.
    nums = sorted(nums)
    ave = sum(nums) / len(nums)

    """
    We split the list down the middle and reverse the first half, so we can rebuild the list in a way that the 
    elements in the middle of the array get to the front of the array, giving us a better chance to find the 
    element(s) which can remove while keeping the average the same
    """
    A = nums[:int(len(nums) / 2)]
    B = nums[int(len(nums) / 2 + 1):]

    A.reverse()

    nums = list()

    i = 0

    try:
        while i <= len(B):
            nums.append(A[i])
            nums.append(B[i])
            i += 1
    except IndexError:
        pass

    # Boolean variable to keeping in check if list can be split
    can_split = False

    # Calling the recursive function to find a valid split without the first element
    if check_and_continue(ave, nums[1:]):
        can_split = True

    i = 0

    # Calling the recursive function to find a valid split without elements of the list if split isn't found yet
    while i < len(nums) - 1 and can_split is False:
        if check_and_continue(ave, nums[:i] + nums[(i + 1):]):
            can_split = True
        i += 1

    # Calling the recursive function to find a valid split without the last element if split isn't found yet
    if can_split is False and check_and_continue(ave, nums[:-1]):
        can_split = True

    return can_split


print(split_array_same_average(A))
