def solution(board, moves):
	board_stack=[]; #board ���� ���η� ������
	board_temp=[];
	board_top=[];
	result_stack=[]; #��Ʈ���� ����
	result_top = -1; 
	result = 0; #��Ʈ���� ��

	for i in range(len(board)) : #���� ���� �ʱ�ȭ ��Ű�� ����
		board_top.append(0);
		for j in range(len(board[i])) :
			result_stack.append(0);
			board_temp.append(board[j][i]);
			if(board[j][i] != 0 and board_top[i] == 0) : #board�� top���� �־���
				board_top[i] = len(board[i]) - j - 1;
		board_stack.append(list(reversed(board_temp)));
		board_temp = [];
	
	for i in range(len(moves)) : #moves �迭 ������� �����̴� ����
		if(board_top[moves[i]-1] >= 0) : #board ���ÿ��� ���� ���� ������
			result_top += 1;
			result_stack[result_top] = board_stack[moves[i]-1][board_top[moves[i]-1]]
			board_stack[moves[i]-1][board_top[moves[i]-1]] = 0;
			board_top[moves[i]-1] -= 1;
			if(result_top >= 1) : #result �迭�� �ΰ� �̻� ���������
				if(result_stack[result_top] == result_stack[result_top-1]) : #result �迭�� top���� ���� ������
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
