# 문자열과 하나의 문자를 받아 문자열에서 그 문자가 위치를 모두 찾아 콘솔에 출력하고 그 갯수를 반환하는 함수

def count_str(x:str, y:str):
    count = 0
    list = []
    for i in range(len(x)):
        if x[i] == y:
            count += 1
            list.append(i)
    if count != 0:
        return list, count
    else:
        return -1
    
if __name__ == "__main__":
    x = input("문자열을 입력하세요: ")
    y = input("문자를 입력하세요: ")

list, count = count_str(x,y)
print("위치:", *list, "\n개수:", count)
    