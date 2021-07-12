def solution(s):
    answer = ''
    length=len(s)
    if length % 2 == 0:
        k = int(length/2)
        answer =s[k-1]+ s[k]
    else :
        k = int(length/2)
        answer = s[k]
    return answer
