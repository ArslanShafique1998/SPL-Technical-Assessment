# String Manipulation Problems:

## Problem 1: Compare the strands of two genomes report similarity index in percentages.

    Given Two Strings of same length genomes return the similarity index in percentage.

    Example:

        For Two String 'ATATGTATG' and 'ATATATATG' 7 characters are aligned and total
        characters are 9 so the similarity index is 7/9 *100

        Hint: Consider using a tree for genome

        Function Description

        Complete the function SimilarityIndexGenome with following details:

        SimilarityIndexGenome has the following parameter(s):
            string a[n]: first genome
            string b[n]: second genmoe

        Returns
           double a'

        Questions:
            Can we find the positions of characters that do not match using this
            function?
            Answer: Yes, we take another array and we put those indexes whose elements are not match in it.

    Command/Script to Run Problem 1:(D:\SPL-Techincal-Assessment-Assessment\Basic\StringManipulation>python genomes_report.py
) (Fill this in when submitting)

## Problem 2: Remove a character from the entire string.

    Given a string and a charcter remove that character from entire string.

    Example:

        string name = 'We Are Your Technology Partners' and char x = ' '
        returns 'WeAreYourTechnologyPartners'

    Questions:
       Can we use the Tree data structure or hashing to optimize this?
       Answer: Yes, we can use.

    Command/Script to Run Problem 2:(D:\SPL-Techincal-Assessment-Assessment\Basic\StringManipulation>python removing_character.py
) (Fill this in when submitting)
