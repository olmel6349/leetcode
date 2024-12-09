#https://leetcode.com/problems/sort-list/

head = [4,2,1,3]
#Output: [1,2,3,4]

#head = [-1,5,3,4,0]
#Output: [-1,0,3,4,5]

def insert_sort(head):
    for i in range(1, len(head)):
        temp = head[i]
        j = i-1
        
        while j >= 0 and head[j] > temp:
            head[j+1] = head[j]
            j -= 1
            
        head[j+1] = temp

def bubble_sort(head):
    for i in range(len(head) - 1):
        for j in range(len(head) - i - 1):
            if head[j] > head[j + 1]:
                temp = head[j]
                head[j] = head[j + 1]
                head[j + 1] = temp
                
insert_sort(head)
print(head)