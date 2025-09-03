# 학번이 문자열로 주어지면 입학년도를 정수로 반환하는 함수

def get_admission_year(id):
    return int(id[:4])

if __name__ == "__main__":
    id = input("학번을 입력하세요: ")
    year = get_admission_year(id)
    print(f"입학년도: {year}년")