def solution(participant, completion):
	count={}
	index = 0
	participant.extend(completion)

	for i in participant :
		try: count[i] += 1
		except: count[i] = 1
	
	for i in participant :
		if count[i] % 2 == 1 :
			return i

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))