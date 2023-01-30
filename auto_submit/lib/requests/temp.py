
def your_function(matrix, m , n):
    sum = 0
    for i in range(m):
        for j in range(n):
            if(i== j):
                sum += matrix[i][j]
    return isArmstrong(sum) ? sum: 

# function to check if a number is armstrong
def isArmstrong(num):
    sum = 0
    temp = num
    while(num > 0):
        digit = num % 10
        sum += digit ** 3
        num //= 10
    if(sum == temp):
        return True
    else:
        return False



# function to merge two sorted linked list
def Merge(list1, list2):
    if(list1 is None):
        return list2
    if(list2 is None):
        return list1
    if(list1.data < list2.data):
        list1.next = Merge(list1.next, list2)
        return list1
    else:
        list2.next = Merge(list1, list2.next)
        return list2