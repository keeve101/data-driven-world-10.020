from ast import main
import time
import random
import copy
from tkinter import RIDGE

# ls = [4,1,2,3,5,5,6]

def bubble_sort(ls):
    #keeping track of outer_iterations
    o_i = 0
    #keeping track of inner_iterations
    ls_i_i = []
    swapped = True
    last_swapped = len(ls) - 1 
    while swapped:
        swapped = False
        o_i += 1
        i_i = 0
        for i in range(last_swapped):
            i_i += 1
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                last_swapped = i
                swapped = True
        ls_i_i.append(i_i)
    
    return ls, o_i, ls_i_i

# print(bubble_sort(ls))
# ##bubble_sort last_swapped index. better than swapped boolean variable 

array = [4,1,7,2,1,9,0,0,1,2]

# my merge_sort, recursive
def merge_sort_mine(ls):
    size = len(ls)
    if size == 1:
        return ls

    else:
        size = size//2
        array1, array2 = ls[:size], ls[size:]
        return merge_inplace(merge_sort_mine(array1), merge_sort_mine(array2))

def merge_inplace(array_1, array_2):
    sorted_array = []
    size_1 = len(array_1)
    size_2 = len(array_2)
    i_1 = 0
    i_2 = 0
    while i_1 != size_1 and i_2 != size_2:
        if array_1[i_1] > array_2[i_2]:
            sorted_array.append(array_2[i_2])
            i_2 += 1
        else:
            sorted_array.append(array_1[i_1])
            i_1 += 1

    # if i_1 != size_1:
    #     sorted_array += array_1[i_1:]
    # else:
    #     sorted_array += array_2[i_2:]
    while i_1 != size_1:
        sorted_array.append(array_1[i_1])
        i_1 += 1

    while i_2 != size_2:
        sorted_array.append(array_2[i_2])
        i_2 += 1

    return sorted_array

def merge_sort_mine_1(ls):
    size = len(ls)
    if size == 1:
        return ls

    else:
        size = size//2
        array1, array2 = ls[:size], ls[size:]
        return merge_1(merge_sort_mine(array1), merge_sort_mine(array2))

def merge_1(array_1, array_2):
    sorted_array = []
    size_1 = len(array_1)
    size_2 = len(array_2)
    i_1 = 0
    i_2 = 0
    while i_1 != size_1 and i_2 != size_2:
        if array_1[i_1] > array_2[i_2]:
            sorted_array.append(array_2[i_2])
            i_2 += 1
        else:
            sorted_array.append(array_1[i_1])
            i_1 += 1

    if i_1 != size_1:
        sorted_array += array_1[i_1:]
    else:
        sorted_array += array_2[i_2:]

    return sorted_array


#iterative
def merge_sort(array):
    if len(array) > 1:
        midpt = len(array)//2
        L_pos = R_pos = main_pos = 0
        L = array[:midpt]
        R = array[midpt:]
        merge_sort(L)
        merge_sort(R)
        while L_pos < len(L) and R_pos < len(R):
            if L[L_pos] > R[R_pos]:
                array[main_pos] = R[R_pos]
                R_pos += 1
            else:
                array[main_pos] = L[L_pos]
                L_pos += 1
            main_pos += 1

        while L_pos < len(L):
            array[main_pos] = L[L_pos]
            L_pos += 1
            main_pos +=1

        while R_pos < len(R):
            array[main_pos] = R[R_pos]
            R_pos += 1
            main_pos +=1


array = [14,2,1,6,2,0,2,8]

def merge_sort_inplace(arr):
    size = len(arr)
    if size == 1:
        return arr
    size = size//2
    return merge(arr, merge_sort_inplace(arr[:size]), merge_sort_inplace(arr[size:]))
    
def merge(arr, left, right):
    len_left = len(left)
    len_right = len(right)
    l_index = r_index = main_index = 0
    while l_index < len_left and r_index < len_right:
        if left[l_index] > right[r_index]:
            arr[main_index] = right[r_index]
            r_index += 1
        else:
            arr[main_index] = left[l_index]
            l_index += 1
        main_index += 1
    

    while l_index < len_left:
        arr[main_index] = left[l_index]
        l_index += 1
        main_index += 1

    while r_index < len_right:
        arr[main_index] = right[r_index]
        r_index += 1
        main_index += 1
    return arr




def run_function(f, x):
    start = time.time()
    f(x)
    end = time.time()
    return end-start

def gen_random_int(number, seed):
    ls = [i for i in range(number)]
    random.shuffle(ls, random.seed(seed))
    return ls

 
def run_speed_test():
    time_builtin = []
    time_builtin_2 = []
    # set the maximum power for 10^power number of inputs
    maxpower = 6
    for n in range(1, maxpower + 1):
        # create array for 10^1, 10^2, etc 
        # use seed 100
        array = gen_random_int(10**n, 100)
        array_2 = copy.deepcopy(array)
        
        # call run_function with sorted() and array as arguments
        # result = run_function(None, None) 
        result = run_function(merge_sort, array)
        result_2 = run_function(merge_sort_inplace, array_2)
        ###
        ### YOUR CODE HERE
        ###
        time_builtin_2.append(result_2)
        time_builtin.append(result)
    return time_builtin, time_builtin_2

# print(run_speed_test())


# merge_sort_inplace(array)
# print(array)

class User():
    def __init__(self, username):
        self.username = username
users_array = []
names = ["keith", "lexuan", "beb", "loves you", "anna", "banana", "Anna", "charle", "213skd", "zack", "zcsa"]
for name in names:
    users_array.append(User(name))

def merge_sort_users(arr, byfunc=None):
    size = len(arr)
    if size == 1:
        return arr
    size = size//2
    return merge_users(arr, merge_sort_users(arr[:size], byfunc), merge_sort_users(arr[size:], byfunc), byfunc)

def merge_users(arr, left, right, byfunc):
    end_left, end_right = len(left), len(right)
    l_index = r_index = main_index = 0
    while l_index < end_left and r_index < end_right:
        if byfunc(left[l_index]).lower() > byfunc(right[r_index]).lower():
            arr[main_index] = right[r_index]
            r_index += 1
        else:
            arr[main_index] = left[l_index]
            l_index += 1
        main_index +=1
    while l_index < end_left:
        arr[main_index] = left[l_index]
        l_index += 1
        main_index += 1 
    while r_index < end_right:
        arr[main_index] = right[r_index]
        r_index += 1
        main_index += 1
    
    return arr

# merge_sort_users(users_array, lambda x: x.username)
# print([user.username for user in users_array])
