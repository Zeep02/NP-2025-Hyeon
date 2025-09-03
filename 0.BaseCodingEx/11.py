# 이름, 나이, 전화번호로 구성된 연락처를 반복적으로 입력받아 저장하고 만약 이름이나 나이를 0을 입력하면 입력을 중단하고 입력받은 목록을 반환하는 함수와 
# 입력 받은 연락처 목록을 받아 콘솔에 출력하는 함수 작성한 후 입력받아 출력하는 테스트 코드 작성

def input_contacts():
    contacts = []
    while True:
        name = input("이름을 입력하세요 (종료: 0): ")
        if name == '0':
            break
        age = input("나이를 입력하세요 (종료: 0): ")
        if age == '0':
            break
        phone = input("전화번호를 입력하세요: ")
        contacts.append({'name': name, 'age': age, 'phone': phone})
    return contacts

def print_contacts(contacts):
    print("\n입력된 연락처 목록:")
    for contact in contacts:
        print(f"이름: {contact['name']}, 나이: {contact['age']}, 전화번호: {contact['phone']}")

if __name__ == "__main__":
    contacts = input_contacts()
    print_contacts(contacts)