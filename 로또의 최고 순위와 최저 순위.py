def solution(lottos, win_nums):
    answer = [7,7]
    for i in range(0, len(lottos)) :
        if lottos[i] == 0 :
            answer[0] -= 1
        for j in range(0, len(win_nums)):
            if lottos[i] == win_nums[j] :
                answer[0] -= 1
                answer[1] -= 1
            else : continue    
    for i in range(0, len(answer)):
        if answer[i] ==7 :
            answer[i] = 6
    return answer