# 하나의 십진수 정수가 주어지면 각 자리의 십진수의 합을 반환하는 함수를 작성

def sum_digits(n):
    for i in range(len(n)):
        n[i] = int(n[i])
    return sum(n)

if __name__ == "__main__":
    number = input("정수를 입력하세요: ")
    digits = list(number)
    result = sum_digits(digits)
    print(f"{number}의 각 자리 정수의 합은 {result}입니다.")