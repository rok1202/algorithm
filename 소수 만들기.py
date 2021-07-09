def check_num(nums) :
    for i in range(2, nums):
        if nums % i == 0:
            return False
    return True

def solution(nums):
    answer = -1
    cnt = 0
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                total = nums[i] + nums[j] + nums[k]
                if check_num(total) :
                    print(nums[i],"  ",  nums[j], "   ", nums[k], "   ",total)
                    cnt += 1
    return cnt