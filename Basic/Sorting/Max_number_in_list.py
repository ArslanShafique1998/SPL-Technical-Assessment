def Max_number(array):
    #we sort the array and then choose its last value because the sorted array have highest number at last
    array.sort()
    number=len(array)
    return array[number-1]
#Take the length of array and array
n=int(input("Enter length of array:"))
array=[]
for i in range(0,n,1):
    a=int(input("Enter integers for array:"))
    array.append(a)
maximum_number=Max_number(array)
print("Maximum number in arrays is:",maximum_number)