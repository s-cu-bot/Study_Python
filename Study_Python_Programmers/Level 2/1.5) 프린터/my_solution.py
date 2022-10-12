def solution(priorities, location):
    answer = 1 #몇 번째로 출력되는지
    
    while len(priorities) > 0 :
        index = 0 #priorities 인덱스 값
        while index < len(priorities) : # 처음으로 pop이 나올 때 까지 돌리기
            if priorities[0] < priorities[index] :
                if location <= 0 :
                    location = len(priorities) - 1
                else :
                    location -= 1
                index = 0
                priorities.append(priorities[0])
                priorities.pop(0)
            else :
                index +=1

        if location <= 0 : #location이 0이면 pop되는 것이 원하는 수
            return answer 
        else :
            priorities.pop(0) #location이 0이 아니면 나머지 프린터로 다시 확인
            location -= 1
            answer += 1