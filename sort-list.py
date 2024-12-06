#https://leetcode.com/problems/sort-list/

head = [4,2,1,3]
#Output: [1,2,3,4]

#head = [-1,5,3,4,0]
#Output: [-1,0,3,4,5]

def sort(head):
    for i in range(len(head)):
        current_numb = head[i]
        switched_pos = False
        for j in range(len(head)):
            if current_numb != head[j]:
                if switched_pos == False:
                    if current_numb < head[j]:
                        head[i] = head[j]
                        head[j] = current_numb
                        switched_pos = True

    target = True
    for x in range(len(head)):
        if x < len(head) -1:
            if head[x] > head[x + 1]:
                target = False
                
    if target == False:
        sort(head)
    
sort(head)
print(head)