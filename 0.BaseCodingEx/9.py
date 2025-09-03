# 두 개의 3x3 행렬을 입력받아 행렬덧셈 결과행렬을 반환하는 함수

def matrix_add(x, y):
    result = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(x[i][j] + y[i][j])
        result.append(row)
    return result

def input_matrix(word):
    print(word)
    matrix = []
    for i in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

if __name__ == "__main__":
    x = input_matrix("첫 번째 3x3 행렬을 입력하세요 (3x3, 공백으로 구분):")
    y = input_matrix("두 번째 3x3 행렬을 입력하세요 (3x3, 공백으로 구분):")

    result = matrix_add(x, y)
    print("행렬 덧셈 결과:")
    for row in result:
        print(*row)