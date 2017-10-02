def isPal(x):
    """Assumes x is a list
       Returns True if the list is a palindrome; False otherwise"""
    temp = x
    temp.reverse()
    if temp == x:
        print('true')
        return True
    else:
        print('false')
        return False

ls = [2, 3, 4]

isPal(ls)