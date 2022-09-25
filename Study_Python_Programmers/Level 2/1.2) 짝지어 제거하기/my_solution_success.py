def solution(s):
	answer = []
	answer_i = -1
	for i in s :	
		answer.append(i)		
		if(answer_i >= 0) :
			if(answer[answer_i] == answer[answer_i+1]) :
				del answer[answer_i : answer_i + 2]	
				answer_i -= 2
		answer_i += 1

	if len(answer) == 0 :
		return 1;
	else : return 0;

s = "bcbccbc"
print(solution(s))
