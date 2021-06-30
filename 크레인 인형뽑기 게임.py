def solution(board, moves):
    list_a = []
    answer = 0

    for i in range(0, len(moves)) :
        for j in range(0, len(board)):  
            if board[j][moves[i]-1] == 0 :
                continue
            else : 
                list_a.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
    lenth = len(list_a)
    k = 1  
    while lenth != 0 :
        if lenth != k or k < 1:
            if list_a[k] == list_a[k-1] :
                lenth -= 2
                answer += 2
                del list_a[k]
                del list_a[k-1]
                k = 1
            else :
                k += 1
        else : break
    return answer