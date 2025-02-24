
"""
The Josephus Problem is named after Flavius Josephus, a Jewish 
historian who lived during the 1st century. The story behind this
mathematical problem is quite dramatic. According to Josephus's account,
during the Jewish-Roman war, he and his 40 soldiers were trapped in 
a cave, surrounded by Roman forces. Preferring suicide to capture,
they decided to form a circle and proceed around it, systematically
killing every third remaining person until no one was left.
Josephus, not wishing to die, quickly figured out where to
position himself in the circle so as to be the last survivor.
He used this clever strategy to spare his own life,
and then surrendered to the Romans. This tale later
inspired the Josephus Problem in mathematics,
which explores the outcome of this elimination 
process for different numbers of people
and intervals
"""

"""
RECURSION :-->
 Recursion is a programming technique where a function calls
itself to solve a smaller instance of the same problem.
The function continues to call itself until it reaches a base case
that stops further recursion.

  1> if base condition is wrong or missing then show error: STACKOVERFLOW error

    a>--> base case: last valid input or first invalid input

  when to use recursion:--> 
  You should use recursion when:
✅ The problem can be broken down into smaller subproblems of the same type.
✅ You can define a base case (a stopping condition).
✅ The problem has tree-like structures (e.g., file systems, graphs, backtracking).
✅ Mathematical problems like factorial, Fibonacci, and power calculations.
✅ You need depth-first search (DFS) in graphs or trees.

When NOT to Use Recursion? : ---->
❌ When the function has too many recursive calls, leading to stack overflow.
❌ If an iterative solution is more efficient (e.g., looping is better for simple iterations).
❌ When recursion leads to excessive duplicate calculations (e.g., Fibonacci without memoization).
"""


"""
===============================================
 Recursion vs Iteration in Python
===============================================

 Feature         | Recursion                      | Iteration                        
----------------|--------------------------------|----------------------------------
 Definition     | A function calls itself       | Uses loops (for/while)          
 Speed         | Can be slow (stack overhead)  | Usually faster                  
 Memory        | Uses extra stack memory       | Uses a single loop variable      
 Code Length   | Shorter & elegant             | Longer but efficient             
 Use Cases     | Trees, DFS, Divide & Conquer  | Simple loops                    
 Risk          | Stack Overflow (deep recursion) | No risk of stack overflow       

===============================================
 Example of Recursion
===============================================
"""
def factorial_rec(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial_rec(n - 1)  # Recursive call



"""
===============================================
 Example of Iteration
===============================================
"""
def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""
Recursion Tree for factorial(5):

factorial(5)
    ├── 5 * factorial(4)
    │       ├── 4 * factorial(3)
    │       │       ├── 3 * factorial(2)
    │       │       │       ├── 2 * factorial(1)
    │       │       │       │       ├── 1  (Base Case Reached)
    │       │       │       │       ▼
    │       │       │       ├── Returns: 2 * 1 = 2
    │       │       │       ▼
    │       │       ├── Returns: 3 * 2 = 6
    │       │       ▼
    │       ├── Returns: 4 * 6 = 24
    │       ▼
    ├── Returns: 5 * 24 = 120  (Final Answer)
"""


"""
Recursion Call Stack for factorial(5):

Step 1: Call factorial(5)  → Pushed onto stack
Step 2: Call factorial(4)  → Pushed onto stack
Step 3: Call factorial(3)  → Pushed onto stack
Step 4: Call factorial(2)  → Pushed onto stack
Step 5: Call factorial(1)  → Pushed onto stack  (Base Case Reached)

Now, we start returning values (popping from stack):

Step 6: Return 1 from factorial(1) → Popped from stack
Step 7: Return 2 * 1 = 2 from factorial(2) → Popped from stack
Step 8: Return 3 * 2 = 6 from factorial(3) → Popped from stack
Step 9: Return 4 * 6 = 24 from factorial(4) → Popped from stack
Step 10: Return 5 * 24 = 120 from factorial(5) → Popped from stack

Final Answer: 120

Visual Representation of Call Stack:

|---------------------|
| factorial(1)  → 1  |  <-- Top (Base Case)
| factorial(2)  → 2  |  
| factorial(3)  → 6  |  
| factorial(4)  → 24 |  
| factorial(5)  → 120|  <-- Bottom (First Call)
|---------------------|

Stack works as **LIFO (Last In, First Out)**:
- **Last function called is the first to finish and return.**
- **First function called is the last to return.**
"""





"""
===============================================
 Q 1:--> PRINTING PATTERN LIKE 32123

     TC :  O(n) (Each number is printed once in recursion and once in backtracking)
     SC :  O(n) (Recursive call stack depth)
===============================================
"""

def print_pattern(n, current):
    if current == 0:  # Base case: stop recursion at 0
        return
    
    print(current, end=" ")  # Print decreasing part
    print_pattern(n, current - 1)  # Recursive call
   
    print(current, end=" ")

# Call the function
# print_pattern(5, 5)



"""
===============================================
 Q 1:--> fibonaci series : f(n) = f(n-1) + f(n-2)

     TC : O(2^n) (Exponential due to repeated calls)
     SC : O(n) (Max recursion depth)
===============================================
"""

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# Call the function and print Fibonacci numbers up to n
n = 5
for i in range(n + 1):
    # print(fibo(i), end=" ")
    pass




"""
===============================================
 Q 1:--> sum of natural number : 1+2+3+...+n

     TC : O(n) (Linear, one addition per call)
     SC : O(n) (Recursive call stack depth)
===============================================
"""
def natural_sum(curr, n):
    if curr ==n:
        return n
    return curr + natural_sum(curr+1, n)

# print(natural_sum(1, 100))



"""
===============================================
 Q 2:--> kth symbol in grammar:
         We build a table of n rows (1-indexed).
         We start by writing 0 in the 1st row.
         Now in every subsequent row, we look at the previous row
         and replace each occurrence of 0 with 01, and each occurrence
         of 1 with 10. For example, for n = 3, the 1st row is 0,
         the 2nd row is 01, and the 3rd row is 0110. Given two integer
         n and k, return the kth (1-indexed) symbol in the nth row of 
         a table of n rows.

     TC : O(n) : 
     SC : O(n) 
===============================================
"""

def kth_symbol(n, k):
    if n==1:
        return 0
    lenght_of_previous_row =2**(n-2)

    if k<=lenght_of_previous_row:
        return kth_symbol(n-1, k)
    else:
        return 1-kth_symbol(n-1, k-lenght_of_previous_row)






#
"""
===============================================
 Q 2:--> JOSEPHUS PROBLEM:
          
            There are n friends that are playing a game.
            The friends are sitting in a circle and are numbered
            from 1 to n in clockwise order. More formally, moving
            clockwise from the ith friend brings you to the (i+1)th
            friend for 1 <= i < n, and moving clockwise from the nth 
            friend brings you to the 1st friend. The rules of the game
            are as follows: Start at the 1st friend. Count the next k 
            friends in the clockwise direction including the friend you 
            started at. The counting wraps around the circle and may 
            count some friends more than once. The last friend you 
            counted leaves the circle and loses the game. If there 
            is still more than one friend in the circle, go back to 
            step 2 starting from the friend immediately clockwise of 
            the friend who just lost and repeat. Else, the last friend 
            in the circle wins the game. Given the number of friends, n, 
            and an integer k, return the winner of the game.
          
===============================================
"""

"""
METHOD-1-->
       TC : O(n**2) 
       SC : O(n) 
"""
def findTheWinner(n, k):
    a=[i+1 for i in range(n)]

    def helper(a, start_index):
        if len(a)==1:
            return a[0]
        remove_index = (start_index+k-1)%len(a)
        del a[remove_index]
        return helper(a, remove_index)
    return helper(a, 0)
print(findTheWinner(5, 3))    






"""
METHOD-2-->
       TC : O(n) 
       SC : O(n) 

       idea:
            in case of n=5 and k=3, 4 is the safe postion,
            in case of n=4 and k=3, 1 is the safe position,

            if i already known that in case of (4, 3) 1 is safe postion ,
            can i use it to solve (5, 3).

                 4 <------1  : (1+3)      here k=3 
                 5 <------2  : (2+3)      here k=3
                 1 <------3  : (3+3)%5    here k=3
                 2 <------4  : (4+3)%5    here k=3

"""

"""
Recursion Tree for findTheWinner(5,3):

findTheWinner(5,3)
 |
 ├── helper(5)  
 |    ├── helper(4)  
 |    |    ├── helper(3)  
 |    |    |    ├── helper(2)  
 |    |    |    |    ├── helper(1) → returns 0  (Base case)
 |    |    |    |    └── (helper(1) + 3) % 2 = (0 + 3) % 2 = 1
 |    |    |    ├── (helper(2) + 3) % 3 = (1 + 3) % 3 = 1
 |    |    ├── (helper(3) + 3) % 4 = (1 + 3) % 4 = 0
 |    ├── (helper(4) + 3) % 5 = (0 + 3) % 5 = 3
 | 
 └── helper(5) returns 3+1 = **4 (Final Safe Position)**

Final Answer: **4**
"""


def findTheWinner(n, k):
    def helper(n):
        if n==1:
            return 0
        return (helper(n-1) + k) % n
    return helper(n)+1





"""
METHOD-3-->
       TC : O(n) 
       SC : O(1)

       idea: just move from recursive to iterative 
"""



"""
Iteration Steps for findTheWinner(5,3):

Step 1: i = 2
    a = (0 + 3) % 2 = 1  

Step 2: i = 3
    a = (1 + 3) % 3 = 1  

Step 3: i = 4
    a = (1 + 3) % 4 = 0  

Step 4: i = 5
    a = (0 + 3) % 5 = 3  

Final Answer: a + 1 = **4 (Final Safe Position)**
"""

def findTheWinner(n, k):
    a=0
    for i in range(2, n+1):
        a= (a+k) % i
    return a+1










