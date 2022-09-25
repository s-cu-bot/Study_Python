def solution(lottos, win_nums) :
	count_lottos_0 = 0;
	count_win_nums_0 = 7;
	for i in range(len(lottos)) :
		if lottos[i] == 0 :
			count_lottos_0 += 1;
		for j in range(len(win_nums)) :
			if (lottos[i] == win_nums[j]) and (win_nums[j] != 0) :
				win_nums[j] = 0;
				
	for i in range(len(win_nums)) :
		if win_nums[i] == 0 :
			count_win_nums_0 -= 1;
		
	good = count_win_nums_0 - count_lottos_0;
	bad = count_win_nums_0;
			
	if good <= 0 :
		good = 1;
	elif good >= 7 :
		good = 6;
		
	if bad >= 7 :
		bad = 6;
	elif bad <= 0 :
		bad = 1;
			
	answer = [];
	answer.append(good);
	answer.append(bad);
	return answer
