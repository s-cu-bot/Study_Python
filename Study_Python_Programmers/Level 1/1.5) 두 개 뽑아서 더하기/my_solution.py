def solution(numbers):
    result = [];
    for i in range(len(numbers)) :
    	for j in range(len(numbers)) :
    		if(i != j) :
    			result.append(numbers[i] + numbers[j]);
    print(sorted(list(set(result))));
    
numbers = [1,2,3,4];
solution(numbers);