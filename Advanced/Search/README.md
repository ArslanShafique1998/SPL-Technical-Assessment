# Search Problems:

## Problem 1: Given An Array and a target number Find all the Pairs the sum of which is equal to that target number.

    Find all the pairs in an array the sum of which is equal to
    the provided target number.

    Example:
        Input : arr[] = {10, 12, 14, 16, 18}
        Input: 30,
        Output : [{12,18},{14,16}]
        Function Description

        Complete the function findPairs with following details:

        findPairs has the following parameter(s):
        int a[n]: the array of elements
        int b: Target Number

        Returns
        Array<Objects> a': Pairs

        Questions:
            How do we detect which pairs are identical? i.e. {2,3} and {3,2} are identical.
            Write a program to filter the identical pairs.
        Answer:
    l=len(pairs)
    for i in range (0,l,1):
        for j in range (i+1,l,1):
            if pairs[i][0]==pairs[j][1] and pairs[i][1]==pairs[j][0]:#if we have identical tuples then it remove on tuple
                pairs.remove(pairs[i])
            elif pairs[i][0]==pairs[j][0] and pairs[i][1]==pairs[j][1]:
                pairs.remove(pairs[i])
    This code remove the identical pairs. It check in array that either the tuples are equal or they are identical  

    Command/Script to Run Problem 1: (D:\SPL-Techincal-Assessment-Assessment\Advanced\Search>python pair_of_target_number.py
) (Fill this in when submitting)

## Problem 2: Calculate The Frequency of Numbers in An Array

    Given an array of n elements return the array of maps with number keys
    mapped to the number of times they appeared in the array.

    Example:

        Input Array : [1,2,3,4,5,4,3,1]

        Output Array: [{1:2},{2:1},{3:2},{4:2},{5:1}]

    Questions:

        a. Can we use the output Array to calculate mean of the original array?
        Answer: Yes, we multiple all the numbers to its frequency and divide it by the sum of the all numbers frequency


    Command/Script to Run Problem 2: (D:\SPL-Techincal-Assessment-Assessment\Advanced\Search>python frequency_of_number.py
) (Fill this in when submitting)
