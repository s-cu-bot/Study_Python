def solution(board, moves):
	board_stack=[]; #board 스택 가로로 재정렬
	board_temp=[];
	board_top=[];
	result_stack=[]; #터트려질 스택
	result_top = -1; 
	result = 0; #터트려진 값

	for i in range(len(board)) : #스택 값을 초기화 시키는 과정
		board_top.append(0);
		for j in range(len(board[i])) :
			result_stack.append(0);
			board_temp.append(board[j][i]);
			if(board[j][i] != 0 and board_top[i] == 0) : #board의 top값을 넣어줌
				board_top[i] = len(board[i]) - j - 1;
		board_stack.append(list(reversed(board_temp)));
		board_temp = [];
	
	for i in range(len(moves)) : #moves 배열 순서대로 움직이는 과정
		if(board_top[moves[i]-1] >= 0) : #board 스택에서 꺼낼 값이 있으면
			result_top += 1;
			result_stack[result_top] = board_stack[moves[i]-1][board_top[moves[i]-1]]
			board_stack[moves[i]-1][board_top[moves[i]-1]] = 0;
			board_top[moves[i]-1] -= 1;
			if(result_top >= 1) : #result 배열이 두개 이상 들어있으면
				if(result_stack[result_top] == result_stack[result_top-1]) : #result 배열의 top값과 밑의 같으면
					result += 1;
					result_stack[result_top] = 0;
					result_stack[result_top-1] = 0;
					result_top -= 2;
		else :
			continue;
	
	print(result * 2);

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]];
moves = [1,5,3,5,1,2,1,4];
solution(board, moves)
