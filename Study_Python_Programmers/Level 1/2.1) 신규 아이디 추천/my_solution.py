def solution(new_id):

    new_id = list(new_id)

    for i in range(len(new_id)) : #1단계
        if(ord(new_id[i]) <= 90 and ord(new_id[i]) >= 65) : 
            new_id[i] = str(new_id[i]).lower()

    del_char = "0123456789abcdefghijklmnopqrstuvwxyz-_."#2단계
    count_dot = 0
    i = 0
    while i < len(new_id) :
        if(new_id[i] in list(del_char)) :
            i += 1;
        else :
            del new_id[i]

    i = 0
    while i < len(new_id) : #3단계
        if(new_id[i] == ".") :
            count_dot += 1
        else :
            count_dot = 0
        if(count_dot >= 2) :
            count_dot = 0
            del new_id[i]
            i -= 2
        i+=1

    if len(new_id) >= 1 and new_id[0] == '.' : #4단계
        del new_id[0]
    if len(new_id) >= 1 and new_id[len(new_id)-1] == '.' :
        del new_id[len(new_id)-1]

    if len(new_id) == 0 : #5단계
        new_id.append('a')

    if len(new_id) > 15 : #6단계
        index = len(new_id)
        for i in range(15, index) :
            del new_id[15]
        if new_id[14] == '.' :
            del new_id[14]

    if len(new_id) < 3 : #7단계
        index = len(new_id) - 1
        while(len(new_id) < 3) :
            new_id.append(new_id[index])

    return "".join(new_id);

new_id = "abcdefghijklmn.p"
    
print(solution(new_id)) 
