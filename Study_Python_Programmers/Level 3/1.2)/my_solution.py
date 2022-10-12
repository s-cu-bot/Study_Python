from itertools import permutations
import re

##두 개가 같은 단어인지 확인
##word2는 banned_id로, * 포함 가능
def match(word_1, word_2) :
    word_temp = re.compile(re.sub(r'\*', '.', word_2))
    if word_temp.match(word_1) and len(word_2) == len(word_1) :
        return True
    else :
        return False

##해당 조합이 중복 값인지 확인
def overlap_check(origin, new) :
    for value in origin :
        if set(value) == set(new) :
            return False
    return True
    
def solution(user_id, banned_id):
    result = [] #최종 결과 리스트
    for case in permutations(user_id, len(banned_id)) :
        count = 0 #banned_id와 매칭된 아이디 개수
        for index in range(len(banned_id)) :
            if match(case[index], banned_id[index]) :
                count += 1
            else :
                break
        if count == len(banned_id) and overlap_check(result, case) :
            result.append(case)
    
    answer = len(result)    
    return answer
