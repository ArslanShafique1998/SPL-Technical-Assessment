length=int(input("Enter array size:"))
array=[]
for i in range (0,length,1):
    num=int(input("Enter array element:"))
    array.append(num)
print("\nEntered array is:",array)

array.reverse()
print(array)


#Questions Answers

#Yes we can use array rotation code to achieve array reversal
#But the complexity we face is increased because we run inner loop
#equa to the length of array