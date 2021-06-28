def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    answer = ''
    for i in range(0,len(participant)):
        if i == len(participant)-1:
            answer = participant[i];
            break
        if completion[i]==participant[i]:
            continue
        else : 
            answer = participant[i]
            break
        
    return answer