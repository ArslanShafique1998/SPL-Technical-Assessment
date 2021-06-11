def calMean(array,l):
    #if there is only one element then return 1
    if l==1:
        return float(array[l-1])
    #if length of array is not 1 then recursively run function to get mean
    else:
        return float(calMean(array,l-1)*(l-1)+array[l-1])/float(l)
    # multiply by (l-1) because to compensate the division in recursion process
#Enter the length of array
n=int(input("Enter the length of array:"))
array=[]
#Take array elements
for i in range (0,n,1):
    num=int(input("Enter the array element:"))
    array.append(num)
length=len(array)
#pass it from the function
mean=calMean(array,length)
print("Mean of given array elements:",mean)