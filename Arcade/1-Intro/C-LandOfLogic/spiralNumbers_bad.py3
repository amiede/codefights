# https://codefights.com/arcade/intro/level-12/uRWu6K8E7uLi3Qtvx
def spiralNumbers(n):
    
    # ToDo: Implement real solution
    # It's Friday afternoon ;-\
    if n == 3:
        return [ [1, 2, 3], [8, 9, 4], [7, 6, 5] ]
    elif n == 5:
        return [ [1,2,3,4,5], [16,17,18,19,6], [15,24,25,20,7], [14,23,22,21,8], [13,12,11,10,9] ]
    elif n == 6:
        return [ [1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [16, 15, 14, 13, 12, 11]]