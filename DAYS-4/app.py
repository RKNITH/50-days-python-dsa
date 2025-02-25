"""
===============================================
WHAT IS BACKTRACKING?
===============================================
Backtracking is an algorithmic technique used to solve problems recursively 
by building a solution incrementally and removing those solutions that fail 
to satisfy the constraints of the problem.

It explores all possibilities but eliminates those that are not feasible, 
thus optimizing the search process. It is commonly used in constraint 
satisfaction problems such as:
- Sudoku
- N-Queens Problem
- Maze Solving
- Permutations and Combinations

The main idea behind backtracking is **trying out all possibilities** 
and then **undoing the last choice** when a path does not lead to a solution.

"""



"""
===============================================
HOW IS IT DIFFERENT FROM RECURSION?
===============================================
Recursion is a general concept where a function calls itself to solve smaller 
subproblems of a larger problem. 

Backtracking is a **specialized form of recursion** where:
- We make a choice.
- If the choice leads to a solution, we continue.
- If it does not, we undo the last choice and try a different path.

### **Key Differences**
| Feature        | Recursion  | Backtracking  |
|---------------|------------|---------------|
| Definition    | A function calls itself to solve a problem | Uses recursion but undoes incorrect choices |
| Goal          | Solve problems by dividing them into subproblems | Explore all possible solutions by making choices and undoing incorrect ones |
| Example      | Fibonacci, Factorial | Sudoku, N-Queens, Graph Coloring |
| Time Complexity | Varies | Usually exponential O(2^N) |
"""

"""
===============================================
HOW DOES BACKTRACKING WORK?
===============================================
Backtracking follows the Depth-First Search (DFS) approach. It constructs 
a solution step-by-step and eliminates paths that are not viable.

### **Steps of Backtracking:**
1. Choose a possible option.
2. If the option is valid:
   - Move forward and make another choice.
   - If a solution is found, return.
3. If the option is not valid:
   - Undo the last choice (backtrack).
   - Try the next available option.

### **Example: Solving N-Queens**
- Place a queen on the first row.
- Move to the next row and place another queen.
- If it is safe, continue; if not, backtrack and try a different position.

"""

"""
===============================================
PASS BY REFERENCE / CHANGE INPLACE:
===============================================
Backtracking often involves modifying a data structure (like an array or 
a list) in-place rather than creating new copies.

### **Why Pass by Reference?**
- Helps save memory (no need to create multiple copies of the solution).
- Makes backtracking efficient by undoing changes (restoring the state).

### **Example of Pass by Reference in Backtracking**
```python
def generate_permutations(arr, index):
    if index == len(arr):
        print(arr)
        return
    
    for i in range(index, len(arr)):
        arr[i], arr[index] = arr[index], arr[i]  # Swap (change inplace)
        generate_permutations(arr, index + 1)    # Recursive call
        arr[i], arr[index] = arr[index], arr[i]  # Undo swap (backtrack)

arr = [1, 2, 3]
generate_permutations(arr, 0)


"""




"""
Q 1--> PERMUTATION OF ARRAY
                    
                    Given an array nums of distinct integers, 
                    return all the possible permutations. You 
                    can return the answer in any order.
                       Example 1:
                       nums = [1,4]
                       Output :[[1,4],[4,1]]
                       Example 2:
                       nums = [1,4,5]
                       Output :[[1,4,5],[1,5,4],[4,1,5],[4,5,1],[5,1,4],[5,4,1]]

TC:O(n*n!)
SC:O(n)
"""



"""
Tree view explanation:

Suppose nums = [1, 2, 3]

1. Start with an empty result list.
2. Begin with index 0, swapping elements at index 0 with all indices from 0 to 2.
3. Move to index 1 and repeat swaps from index 1 to 2.
4. Move to index 2 and append the completed permutation when index reaches end.

Tree structure:

                    [1,2,3]
                   /   |   \
            [1,2,3] [2,1,3] [3,2,1]  
            /   \      /   \      /   \
      [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
    
- Each level of the tree represents a different depth of recursion.
- At each step, we swap elements to generate new arrangements.
- When `start` reaches `end`, we append the permutation to `result`.


"""

def permute(nums):
    result = []  # Stores all permutations

    def backtrack(start, end):
        if start == end:  # Base case: when start reaches end, store permutation
            result.append(nums[:])  # Append a copy of nums to result
            return
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]  # Swap elements
            backtrack(start + 1, end)  # Recur for the next index
            nums[start], nums[i] = nums[i], nums[start]  # Swap back (backtracking)

    backtrack(0, len(nums))  # This should be in `permute`, not in `backtrack`
    return result  # Return the final result

# print(permute([1, 2, 3]))  # Expected Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]








"""
Q 1--> PERMUTATION OF ARRAY
                           Given a collection of numbers, nums, 
                           that might contain duplicates, return 
                           all possible unique permutations in any order.

                                Example:
                                nums = [3,3,2]
                                Output :
                                [[3,3,2] , [3,2,3], [2,3,3] ]
                                                    
                   

TC:O(n*n!)
SC:O(n)
"""



"""
Tree View for permutateUnique([3,3,2]):

1. Start with an empty `path = []`.
2. Use frequency dictionary: {3:2, 2:1}.
3. Pick a number, reduce frequency, recurse.
4. Restore frequency (backtracking) after recursion.

                []
              /    \
           (3)      (2)
          /   \       |
       (3,2)  (2,3)  (3,3)
       /         \     |
   (3,2,3)     (2,3,3) (3,3,2)
   
Permutations found:
1. [3,3,2]
2. [3,2,3]
3. [2,3,3]
"""



def permutateUnique(nums):
    result=[]
    frequency={}
    def backtrack(path):
        if(len(path)==len(nums)):
            result.append(path[:])
            return
        for num in frequency:
            if frequency[num]>0:
                path.append(num)
                frequency[num] -=1

                backtrack(path)
                path.pop()
                frequency[num] +=1
    for num in nums:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num]=1


    backtrack([])
    return result

# print(permutateUnique([3,3,2]))  # Expected Output: [[3,3,2], [3,2,3], [2,3,3]]
 