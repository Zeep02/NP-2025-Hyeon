# 1. 두 정수 n부터 m까지 1씩 증가하면서 숫자를 합한 결과를 출력하는 함수

def sum_range(n, m):
    total = 0
    for i in range(n, m+1):
        total += i
    return total

if __name__ == "__main__":
    n = int(input("첫 번째 정수를 입력하세요: "))
    m = int(input("두 번째 정수를 입력하세요: "))
    result = sum_range(n, m)
    print(f"{n}부터 {m}까지의 합은 {result}입니다.")