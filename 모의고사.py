def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]  #5
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] #8
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10
    cnt = [0,0,0]

    for i in range(0, len(answers)):
        if answers[i] == p1[i%5] :
            cnt[0] += 1
                
        if answers[i] == p2[i%8] :
            cnt[1] += 1
                
        if answers[i] == p3[i%10] :
            cnt[2] += 1

    for i in range(0, len(cnt)):
        if cnt[i] == max(cnt) :
            answer.append(i+1)
    return answer

solution([[1,3,2,4,2]])