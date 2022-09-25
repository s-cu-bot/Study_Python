def solution(s): #해당 코드는 효율성 실패
	answer = 0 #가능하면 1 아니면 0
	s = list(s); #list로 변환
	s_len = len(s);
	i = 0
	while i < (s_len - 1) :
		if(i<=-1) :
			i = 0;
		if(s[i] == s[i+1]) :
			del s[i:i+2]
			s_len -= 2;
			i -= 2
		i += 1
	if(len(s) == 0) :
			answer = 1;
	return answer;


s = "abcdefggfedcba"
print(solution(s))
