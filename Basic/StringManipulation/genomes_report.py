def SimilarityIndexGenome(a,b):
    length=len(a)
    no=0
    for i in range(0,length,1):
        if a[i]!=b[i]:# see the elements of strings are same or not is not then increament the number
            no+=1
        elif a[i]==" " and b[i]==" ":# see the incoming string is space or not if space then do nothing
            pass
        elif a[i]==" " and b[i]!=" ":# similarly if one string element is space and other not then increment the number
            no+=1
        elif a[i]!=" " and b[i]==" ":
            no+=1
    return length-no #minus the number from the total length to find the number by which the elements of strings matched
#Take input of two strings of equal length
string1=input("Enter first string:")
string2=input("Enter second string of same length of string 1:")
length=len(string1)
match=SimilarityIndexGenome(string1,string2)
index=(float(match)/float(length)) * 100# calculate the index
print("Similarity Index is:",index)
