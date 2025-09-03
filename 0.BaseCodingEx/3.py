# 두 수를 입력받아 계산하는 함수

def cal(num1:int, num2:int):
    a = num1 + num2
    b = num1 << num2
    c = num1 * num2
    print(f"{a}\n{b}\n{c}\n")
    print(f"가장 높은 수는 {max(a, b, c)}입니다.")

if __name__ == "__main__":
    n1 = int(input("첫 번째 숫자를 입력하세요: "))
    n2 = int(input("두 번째 숫자를 입력하세요: "))
    cal(n1, n2)