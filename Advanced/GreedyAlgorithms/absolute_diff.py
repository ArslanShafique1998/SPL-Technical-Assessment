def findAbsMin(array):
    l=len(array)
    b=[]
    #We choose one element and take its difference from all other elements and
    #take its absolute value and store this difference in seperate array
    for i in range (0,l,1):
       for j in range (i+1,l,1):
           value=abs(array[i]-array[j])
           b.append(value)
    #sort the array and take its first element which is the smallest value give minimum absolute value
    b.sort()
    x=b[0]
    return x
array=[]
#Enter the length of array
n=int(input("Enter the  length of array:"))
# Input the array elements
for i in range (0,n,1):
    num=int(input("Enter the element of array:"))
    array.append(num)
#Pass this array from function to find minimum absolute
minimum_abs_diff=findAbsMin(array)
print("Minimum Absolute Difference is:",minimum_abs_diff)
