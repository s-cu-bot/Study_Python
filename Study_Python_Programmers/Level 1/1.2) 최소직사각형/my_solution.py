# -*- coding: cp949 -*-
def compare(para1, para2) : # ºñ±³ ÇÔ¼ö
	global max_w;
	global max_h; 
	if para1 > max_w and para1 > max_h :
		if max_w >= max_h :
			max_w = para1;
		else :
			max_h = para1;
	elif para1 >= max_w and para1 <= max_h :
		if para2 >= max_w :
			if para1 >= para2 :
				max_w = para2;
			else :
				max_w = para1;
	
	elif para1 <= max_w and para1 >= max_h :
		if para2 >= max_h :
			if para1 >= para2 :
				max_h = para2;
			else :
				max_h = para1;
	return;

def solution(sizes): #solution ÇÔ¼ö (½ÇÁ¦ µ¿ÀÛ)
	global max_w;
	global max_h;
	for i in range(len(sizes)) :
		compare(sizes[i][0], sizes[i][1]);
		compare(sizes[i][1], sizes[i][0]);
	print(max_w, max_h)
#	answer = max_w * max_h;
#	return answer
    
    
max_w = 0;
max_h = 0;

size = [[1, 1], [2, 2], [3, 5], [4, 4], [6,6]]; #test case
solution(size); 
