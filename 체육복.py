def solution(n, lost, reserve):
    idx = 0
    l_len = len(lost)
    r_len = len(reserve)
    flag = False
    for i in range(0, len(lost)):
        for j in range(0, len(reserve)):
            if lost[i] == reserve[j] :
                print("lost, reserve = ",lost[i], reserve[j])
                lost[i] = 0
                reserve[j] = 0
                flag = True
    
    lost = sorted(set(lost))
    reserve = sorted(set(reserve))
    print("정렬 전 lost : ",lost)
    print("정렬 전 reserve : ",reserve)
    if flag :
        lost = lost[1::]
        reserve = reserve[1::]
    print("정렬 후 lost : ",lost)
    print("정렬 후 reserve : ",reserve)    
    answer = n-len(lost)
    
    for r in reserve :
        while True :
            if idx >= len(lost) :
                break
            if (lost[idx] + 1 == r) or (lost[idx] -1 == r) or (lost[idx]  == r):
                answer += 1
                del lost[idx]
                idx +=2
                continue
            idx += 1
        idx = 0
                
    return answer

solution(4, [3, 1, 2], [2, 4, 3])