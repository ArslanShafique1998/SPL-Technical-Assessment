#initialize fibonacci dictionary
fibonnacci_dict={}
def fibonnacci(n):
    #initialize the memoization concept to remember that the number is in dictionary and return its value
    if n in fibonnacci_dict:
        return fibonnacci_dict[n]
    #The else conditions for calculating Fibonacci
    elif n==1:
        value=1
    elif n==2:
        value = 1
    elif n>2:
        value = fibonnacci(n-1)+fibonnacci(n-2)
    fibonnacci_dict[n]=value
    return value

#Take the number upto which the Fibonacci series is print
n=int(input("Enter the positive number greater than 0:"))

#Main function in which we pass numbers from Fibonacci function
for i in range  (1,n):
    print(fibonnacci(i),end=" ")