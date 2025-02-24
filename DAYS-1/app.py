
"""
Monotonic Array -
 An array is monotonic if it is either monotone
increasing or monotone decreasing. An array is monotone increasing
if all its elements from left to right are non-decreasing.
An array is monotone decreasing if all  its elements from left
to right are non-increasing. Given an integer array return true 
if the given array is monotonic, or false otherwise.
"""


"""
DATA STRUCTURE:
data structures are just a collection of data values
and relationships among them.
And the functions or operations that can be applied to the data.
"""

"""
TIME COMPLEXITY: 
number of simple operations computer has to do.
as input grow , in what propertion number of operations grow.
how runtime(number of operation) grow as input size grow.

ASYMPTOTIC ANALYSIS:(BIG O) 
   f(n) = n+3; as n tends to infinity then f(n) tends to n,
     does not depend on 3 (constant part)  : O()
"""


"""
SPACE COMPLEXITY: 
extra space consumed by algorithm as input size increases.

how much auxiliary memory needed to run the algorithm
"""


"""
| Operation                     | Time Complexity | Space Complexity | Notes |
|--------------------------------|----------------|------------------|-------|
| Access (arr[i])               | O(1)           | O(1)             | Direct access using an index takes constant time. |
| Traverse (for loop)           | O(n)           | O(1)             | Iterating through all elements takes linear time. |
| Search (Linear Search)        | O(n)           | O(1)             | In the worst case, the element might be at the end. |
| Search (Binary Search)        | O(log n)       | O(1)             | Only works if the array is sorted. |
| Insert at Beginning (unshift) | O(n)           | O(1)             | All elements must shift right. |
| Insert at End (push)          | O(1)           | O(1)             | Direct insertion, unless resizing occurs (O(n)). |
| Insert in Middle (splice)     | O(n)           | O(1)             | Shifting elements takes linear time. |
| Remove from Beginning (shift) | O(n)           | O(1)             | All elements must shift left. |
| Remove from End (pop)         | O(1)           | O(1)             | Direct removal, no shifting needed. |
| Remove from Middle (splice)   | O(n)           | O(1)             | Shifting elements takes linear time. |
| Copy an Array                 | O(n)           | O(n)             | A new array of the same size is created. |
| Resize (Dynamic Array Growth) | O(n)           | O(n)             | When capacity is reached, a new larger array is created. |


"""



"""
Q1:   Sorted Squared Array

You are given an array of Integers in which each subsequent value 
is not less than the previous value. Write a function that takes 
this array as an input and returns a new array with the squares of 
each number sorted in ascending order.

Remember
You can solve this question in multiple ways.
Think about the following -
1.What would be the brute force way of solving this question ?
 What would be the Time and Space complexity of this approach?
2.Is there a better way to solve this with a more optimum 
Time complexity than the Brute force way ? 
"""

"""
METHOD:1-> BRUTE FORCE METHOD:
 TC: O(n+ nlog(n)) : for appeding tc:n , for sorting : nlong(n);
   finally TC: nlog(n)

 SC: O(n) : for creating extra space as much as number of elements in array  
"""
def sorted_squared(array):
    a =[]
    if len(array) == 0:
        return []
    else:
        for i in array:
            a.append(i**2)
        return sorted(a)  


"""
METHOD:2-> BRUTE FORCE METHOD: take benefit of sorted array given in question
 TC: O(n) : for appeding tc:n ;
   finally TC: n

 SC: O(n) : for creating extra space as much as number of elements in array  
"""
  
def sorted_square(array):
    n = len(array)
    i, j =0,n-1
    res =[0]*n

    for k in reversed(range(n)):
        if array[i]**2 > array[j]**2:
            res[k] =array[i]**2
            i+=1
        else:
            res[k] =array[j]**2
            j-=1
    return res 


"""
Q:2 -> MONOTONIC ARRAY:

An array is monotonic if it is either monotone increasing or monotone 
decreasing. An array is monotone increasing if all its elements from 
left to right are non-decreasing. An array is monotone decreasing 
if all  its elements from left to right are non-increasing.
Given an integer array return true if the given array is monotonic,
or false otherwise.
"""


"""
TC: O(n)
SC:O(1) : no extra memory created
"""
def monotonic_array(array):
    if len(array)<=1:
        return True
    increasing =decreasing =True

    for i in range(1, len(array)):
        if array[i] >= array[i-1]:
            decreasing =False
        if array[i] <= array[i-1]:
            increasing = False
    return increasing or decreasing            
     










