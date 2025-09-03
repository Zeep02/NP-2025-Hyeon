# 정수 1개를 입력받가 2진수, 8진수, 16진수로 변환

def convert_number(num):
    print(bin(num))  # 2진수
    print(oct(num))  # 8진수
    print(hex(num))  # 16진수

if __name__ == "__main__":
    number = int(input("정수를 입력하세요: "))
    convert_number(number)