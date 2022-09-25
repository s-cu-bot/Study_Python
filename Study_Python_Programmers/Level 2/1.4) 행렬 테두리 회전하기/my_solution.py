def make_matrix(rows, columns) : #Matrix 기본값 넣어주는 함수
	result = []
	temp = []
	index = 0

	for i in range(rows * columns) :
		temp.append(i+1)
		if(len(temp) == columns) :
			result.append(temp)
			temp = []

	return result

def find_min(min_value, value) : #최소값 찾아주는 함수
	if(min_value >= value) :
		min_value = value
	return min_value

def rotate(matrix, query) : #query 하나를 기준으로 matrix 변환 함수
	temp = matrix[query[0]-1][query[1] - 1]; #변환전 제일 첫번째 값 임시 저장
	min_value = find_min(10001, temp)

	for i in range(query[0] - 1, query[2] - 1) : #위로
		matrix[i][query[1]-1] = matrix[i+1][query[1]-1]
		min_value = find_min(min_value, matrix[i][query[1]-1])
		
	for i in range(query[1] - 1, query[3] - 1) : #왼쪽으로
		matrix[query[2]-1][i] = matrix[query[2]-1][i+1]
		min_value = find_min(min_value, matrix[query[2]-1][i])

	for i in range(query[2] - 1, query[0] - 1, -1) : #아래로
		matrix[i][query[3]-1] = matrix[i-1][query[3]-1]
		min_value = find_min(min_value, matrix[i-1][query[3]-1])

	for i in range(query[3] - 1, query[1], -1) : #오른쪽으로
		matrix[query[0]-1][i] = matrix[query[0]-1][i-1]
		min_value = find_min(min_value, matrix[query[0]-1][i-1])

	matrix[query[0]-1][query[1]] = temp

	return min_value, matrix;

def solution(rows, columns, queries):
	basic_matrix = make_matrix(rows, columns)
	min_value = 0;
	result = [];

	for i in range(len(queries)) : 
		min_value, basic_matrix = rotate(basic_matrix, queries[i])
		result.append(min_value)

	return result