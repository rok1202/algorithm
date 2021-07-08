def solution(absolutes, signs):
    answer = 123456789
    list_a = []
    for i in range(0, len(signs)) :
        if signs[i] == True :
            list_a.append(absolutes[i])
        else : list_a.append(absolutes[i]*-1)
    answer = sum(list_a)
    return answer