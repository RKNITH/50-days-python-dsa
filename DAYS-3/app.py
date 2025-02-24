
"""
Q 1-->
    TOWER OF HONOI:------>
                    The tower of Hanoi is a famous puzzle where
                    we have three rods and N disks. The objective of 
                    the puzzle is to move the entire stack to another 
                    rod. You are given the number of discs N. Initially, 
                    these discs are in the rod 1. You need to print all 
                    the steps of discs movement so that all the discs 
                    reach the 3rd rod. Also, you need to find the total 
                    moves.
                    Note: The discs are arranged such that the top disc 
                    is numbered 1 and the bottom-most disc is numbered N. 
                    Also, all the discs have different sizes and a bigger 
                    disc cannot be put on the top of a smaller disc. 
                    Refer the provided link to get a better clarity about 
                    the puzzle.   

TC: O(2**n)
SC:O(n)                      
                   
"""

"""
Tower of Hanoi Recursive Tree for toh(3, 'A', 'C', 'B')

                     toh(3, A, C, B)
                         |
         -----------------------------------
         |                                 |
     toh(2, A, B, C)               move disk 3 A → C
         |                                 |
  ----------------------             toh(2, B, C, A)
  |                    |                |
toh(1, A, C, B)   move disk 2 A → B   toh(1, C, B, A)
  |                    |                |
move disk 1 A → C   toh(1, B, A, C)  move disk 1 C → B
                      |
               move disk 1 B → A

------------------------------------------
Steps for TOH with 3 Disks:
------------------------------------------
1. Move disk 1 from A → C
2. Move disk 2 from A → B
3. Move disk 1 from C → B
4. Move disk 3 from A → C
5. Move disk 1 from B → A
6. Move disk 2 from B → C
7. Move disk 1 from A → C
"""


def toh(N, fromm, to, aux):
    count =0
    def helper(N, fromm, to, aux):
        nonlocal count
        
        if N==1:
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            count +=1
            return
        helper(N-1, fromm, aux, to)
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        count +=1
        helper(N-1, aux, to, fromm)
      
    helper(N, fromm, to, aux) 
    return count 








"""
Q 2-->
    POWER SUM:------>

                 Let’s define a peculiar type of array in which each
                 element is either an integer or another peculiar array. 
                 Assume that a peculiar array is never empty. Write a 
                 function that will take a peculiar array as its input 
                 and find the sum of its elements. If an array is an 
                 element in the peculiar array you have to convert it 
                 to it’s equivalent value so that you can sum it with 
                 the other elements. Equivalent value of an array is 
                 the sum of its elements raised to the number which 
                 represents how far nested it is. For e.g. 
                 [2,3[4,1,2]] = 2+3+ (4+1+2)^2
another example - [1,2,[7,[3,4],2]] = 1 + 2 +( 7+(3+4)^3+2)^2
                     

TC: O(N) : total number of elements in main array and sub arrays: [2,3[4,1,2]] : N=6
SC:O(d)  : d: max depth , for above example d=2                    
                   
"""


def power_sum(array, power=1):
    sum =0
    for i in array:
        if type(i) ==list:
            sum += power_sum(array, power+1)
        else:
            sum +=i  
    return sum ** power         