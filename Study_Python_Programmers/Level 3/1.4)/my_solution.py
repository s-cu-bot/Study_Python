from itertools import permutations
import re

##�� ���� ���� �ܾ����� Ȯ��
##word2�� banned_id��, * ���� ����
def match(word_1, word_2) :
    word_temp = re.compile(re.sub(r'\*', '.', word_2))
    if word_temp.match(word_1) and len(word_2) == len(word_1) :
        return True
    else :
        return False

##�ش� ������ �ߺ� ������ Ȯ��
def overlap_check(origin, new) :
    for value in origin :
        if set(value) == set(new) :
            return False
    return True
    
def solution(user_id, banned_id):
    result = [] #���� ��� ����Ʈ
    for case in permutations(user_id, len(banned_id)) :
        count = 0 #banned_id�� ��Ī�� ���̵� ����
        for index in range(len(banned_id)) :
            if match(case[index], banned_id[index]) :
                count += 1
            else :
                break
        if count == len(banned_id) and overlap_check(result, case) :
            result.append(case)
    
    answer = len(result)    
    return answer
