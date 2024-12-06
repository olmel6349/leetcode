#https://leetcode.com/problems/valid-palindrome/
s = "A man, a plan, a canal: Panama"
#s = "race a car"
#s = " "

r = ''
for x in range(len(s)):
    if s[x].isalnum():
        r += s[x].lower()
        
r_rev = r[::1]
print(r == r_rev)