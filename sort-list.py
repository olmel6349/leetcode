#https://leetcode.com/problems/sort-list/

head = [4,2,1,3]
#Output: [1,2,3,4]

#head = [-1,5,3,4,0]
#Output: [-1,0,3,4,5]

def sort(head):
    for i in range(len(head) - 1):
        for j in range(len(head) - i - 1):
            if head[j] > head[j + 1]:
                temp = head[j]
                head[j] = head[j + 1]
                head[j + 1] = temp
                
sort(head)
print(head)