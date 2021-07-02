def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        print("i = ",i)
        coppy_array = []
        for j in range(commands[i][0]-1, commands[i][1]):
            print("j값 : ", j, "복사시작 : ", commands[i][0]-1, "복사끝 : ",commands[i][1]-1)
            coppy_array.append(array[j])
            print(coppy_array)
            
        coppy_array = sorted(coppy_array)
        answer.append(coppy_array[commands[i][2]-1])

    return answer
