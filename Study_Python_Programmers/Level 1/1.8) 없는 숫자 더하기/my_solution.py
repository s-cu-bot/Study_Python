def solution(numbers):
	result = 45;
	for i in numbers :
		result -= i
	return result

numbers = [1,2,3,4,6,7,8,0]

print(solution(numbers))