def solution(a, b):
        day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
        num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total = 0
        for i in range(0, a-1):
            total += num[i]
        total = total+b-1
        ans = total % 7    
        answer = day[ans]
        return answer