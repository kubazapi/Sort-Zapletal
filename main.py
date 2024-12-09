import random
array = [88,45,1,23,8,74,23,36,99,6]

def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
            print(array) 
    return array         
print(bubble_sort())

def is_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True  

def bogosort(array):
    count = 0
    while not is_sorted(array):
        random.shuffle(array)
        count += 1
        print(f"Pokus {count}: {array}")
    print(f"Seznam seřazen po {count} pokusech.")

bogosort(array)
print("Seřazený seznam:", array)

def selection_sort(array):
    n = len(array)  
    for i in range(n):  
        min_i = i  
        for j in range(i + 1, n):  
            if array[j] < array[min_i]: 
                min_idx = j  
        array[i], array[min_i] = array[min_i], array[i] 
    return array

selection_sort(array)
print("Seřazený seznam:", array)

def insertion_sort(array):
    for i in range(1, len(array)): 
        key = array[i]  
        j = i - 1  
        while j >= 0 and key < array[j]:  
            array[j + 1] = array[j]  
            j -= 1 
        array[j + 1] = key  
    return array  

insertion_sort(array)
print("Seřazený seznam:", array)
