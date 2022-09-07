
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input("Write a setence or word: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")