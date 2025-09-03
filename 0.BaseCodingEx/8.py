# 두 개의 자연수를 입력받아 그 두 수 사이의 홀수만을 더해서 반환하는 함수 (단, 그 두 수도 포함)

def count_odd(x:int, y:int):
    count = 0
    for i in range(x, y+1):
        if i % 2 != 0:
            count += i
    if count != 0:
        return count
    else:
        return -1
    
if __name__ == "__main__":
    x = int(input("첫 번째 정수를 입력하세요: "))
    y = int(input("두 번째 정수를 입력하세요: "))
    count = count_odd(x,y)
    print(f"총 합산 홀수: {count}")