<<<<<<< HEAD
def solution(absolutes, signs):
	result = 0;
	
	for i in range(len(signs)) :
		if(signs[i] == True) :
			signs[i] = 1;
		else :
			signs[i] = -1;
		result += absolutes[i] * signs[i];
		
	return result;
    
absolutes = [4,7,12];
signs = [True, False, True];
print(solution(absolutes, signs));
=======
def solution(absolutes, signs):
	result = 0;
	
	for i in range(len(signs)) :
		if(signs[i] == True) :
			signs[i] = 1;
		else :
			signs[i] = -1;
		result += absolutes[i] * signs[i];
		
	return result;
    
absolutes = [4,7,12];
signs = [True, False, True];
print(solution(absolutes, signs));
>>>>>>> 8661fe358b3407e64bcf3d06f6083f82835d1882
