#What are negative indexes and why are they used

As we know, indexes are used in arrays in all the programming languages.
 We can access the elements of an array by going through their indexes. 
 But no programming language allows us to use a negative index value
 such as -4. Python programming language supports negative indexing of arrays,
    something which is not available in arrays in most other programming languages.
This means that the index value of -1 gives the last element, and -2 gives the second last element of an array.
  The negative indexing starts from where the array ends.
 This means that the last element of the array is the first element in the negative indexing which is -1.

 Negative Indexing (i2tutorials.com)
Python, Python interview questions, Technology November 4, 2018
What are negative indexes and why are they used?
As we know, indexes are used in arrays in all the programming languages. We can access the elements of an array by going through their indexes. But no programming language allows us to use a negative index value such as -4. Python programming language supports negative indexing of arrays, something which is not available in arrays in most other programming languages. This means that the index value of -1 gives the last element, and -2 gives the second last element of an array. The negative indexing starts from where the array ends. This means that the last element of the array is the first element in the negative indexing which is -1.


arr = [10, 20, 30, 40, 50]
print (arr[-1])
print (arr[-2])