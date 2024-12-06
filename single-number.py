#https://leetcode.com/problems/single-number/
nums = [2,2,1]
#Output: 1

#nums = [4,1,2,1,2]
#Output: 4

#nums = [1]
#Output: 1

#https://leetcode.com/problems/single-number-ii/
#nums = [2,2,3,2]
#Output: 3

#nums = [0,1,0,1,0,1,99]
#Output: 99

result = 0
for i in range(len(nums)):
    if result == 0:
        number_to_find = nums[i]
        exists = []
        for j in range(len(nums)):
            if number_to_find == nums[j]:
                exists.append(1)

        if len(exists) == 1:
            result = number_to_find

print(result)