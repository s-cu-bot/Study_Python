import math
import itertools

def is_prime(number) : #소수인지 확인
	for i in range(2, int(math.floor(math.sqrt(float(number))))+1) :
		if(number % i == 0) :
			return 0;
	return 1;


def solution(s):
	result = [] #전체 순열 값을 담는 배열
	answer = 0 #소수가 몇개인지 카운트

	for i in range(len(s)) :
		result.append(list(map(''.join, itertools.permutations(s,i+1))))
	result = list(set(map(int, sum(result, []))))

	for i in result :
		if(i>=2) : 
			if(is_prime(i) == 1) :
				answer += 1 

	return answer;

s = "123"
print(solution(s))