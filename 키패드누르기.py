def solution(numbers, hand):
    result = []
    pad = [[1,2,3,],
           [4,5,6],
           [7,8,9],
           ['*',0,'#']]
    L_x = 3
    L_y = 0
    R_x = 3
    R_y = 2
    for i in numbers :
        if i == 0 :
            i = 11
        if i == 1 or i == 4 or i == 7 :
            i = i-1
            L_x = int(i/3)
            L_y = i%3
            result.append('L')
        elif i == 3 or i == 6 or i == 9 :
            i = i-1
            R_x = int(i/3)
            R_y = i%3
            result.append('R')
        elif i == 2 or i==5 or i==8 or i == 11:
            i = i-1
            B_x = int(i/3)
            B_y = i%3
            if (abs(B_x-R_x)+abs(B_y-R_y)) > (abs(B_x-L_x)+abs(B_y-L_y)) :
                L_x = B_x
                L_y = B_y
                result.append('L')
            elif (abs(B_x-R_x)+abs(B_y-R_y)) < (abs(B_x-L_x)+abs(B_y-L_y)) :
                R_x = B_x
                R_y = B_y
                result.append('R')
            else:
                if hand == 'right' :
                    R_x = B_x
                    R_y = B_y
                    result.append('R')
                else :
                    L_x = B_x
                    L_y = B_y
                    result.append('L')
    result = "".join(result)
    return result