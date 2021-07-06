def solution(n):
    answer = 0
    ans = []

    while True :
        a = int(n/3)
        b = int(n%3)
        ans.append(b)
        if a < 3 :
            if a == 0 :
                break
            else:
                ans.append(a)
                break
        n = a
    idx = len(ans)-1
    for i in range(0, len(ans)):
        print(i, ans[i])
        answer += ans[i]*(3**idx)
        idx-=1
    return answer

solution(45)
