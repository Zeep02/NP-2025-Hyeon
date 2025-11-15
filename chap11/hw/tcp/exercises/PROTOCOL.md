# TCP 연습문제 프로토콜

## 연습문제 1-1 (telnetlib)
| 구분 | 내용 |
| --- | --- |
| 요청 | `telnetlib.Telnet("localhost", 5000)`으로 TCP 연결 후 `read_all()` 호출. |
| 응답 (정상) | 서버가 현재 시간 문자열을 전송하며 연결 종료 → telnet 클라이언트가 전체 데이터를 수신. |
| 응답 (예외) | 서버가 즉시 닫거나 타임아웃 시 `EOFError`/`socket.timeout` 발생. |
| 오류 조건 | 포트 미오픈 시 `ConnectionRefusedError`, 방화벽 차단 시 `socket.timeout`. |

## 연습문제 1-2 (시간 재포맷)
| 구분 | 내용 |
| --- | --- |
| 요청 | 클라이언트가 `recv()`로 서버 시간 수신. |
| 응답 (정상) | `time.strptime`으로 파싱 후 요청한 포맷(`YYYY Mon DD (Day) HH:MM:SS`)으로 출력. |
| 응답 (예외) | 서버 응답 형식이 다르면 `ValueError` 발생. |
| 오류 조건 | 서버 미기동, 포트 불일치 등으로 `ConnectionRefusedError`. |

## 연습문제 2 (argparse TCP 클라이언트)
| 구분 | 내용 |
| --- | --- |
| 요청 | 명령행 인자로 서버/포트 지정 후 메시지 입력 시마다 `send`. |
| 응답 (정상) | 서버 에코 메시지를 수신 → `print`. |
| 응답 (예외) | 서버가 끊으면 `recv()` 빈 바이트 → 루프 종료. |
| 오류 조건 | 잘못된 IP/포트 → 접속 실패, 연결 중 예외 → `OSError`. |

