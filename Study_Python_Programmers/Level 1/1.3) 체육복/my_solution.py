def solution(n, lost, reserve): #0벌이면 0, 1벌이면 1, 2벌이면 2를 삽입
	dict = [];
	for i in range(n) : #모든 인원이 체육복을 가지고있다 가정
		dict.insert(i, 1);
	for i in lost : #체육복이 없는 인원
		dict[i-1] = 0;
	for i in reserve : #체육복 여벌이 있는 인원
		if(dict[i-1] == 0) :
			dict[i-1] = 1;
		else :
			dict[i-1] = 2;
	
	for i in range(1, n-1) :
		if((dict[i] == 2 and dict[i-1] == 0) or (dict[i] == 0 and dict[i-1] == 2)) :
			dict[i] = 1;
			dict[i-1] = 1;
		elif((dict[i+1] == 2 and dict[i] == 0) or (dict[i+1] == 0 and dict[i] == 2)) :
			dict[i+1] = 1;
			dict[i] = 1;

	answer = dict.count(1) + dict.count(2);
	# return answer

	print(dict);	
	print(answer);
 #   answer = 0
 #   return answer
    
n = 5;
lost = [2, 4];
reserve = [1, 3, 5];
solution(n, lost, reserve);
