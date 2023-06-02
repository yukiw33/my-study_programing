import sys

input = sys.stdin.readline

def main(N, K, M, words, logs):
    valid_people = list(range(1, N+1))
    used_words = set()
    last_word = ''

    for idx, log in enumerate(logs, start=1):
        person = ((idx-1) % N) + 1

        if person not in valid_people:
            continue

        if log not in words or log in used_words:
            valid_people.remove(person)
            last_word = ''
            continue

        if last_word and last_word[-1] != log[0]:
            valid_people.remove(person)
            last_word = ''
            continue

        if log[-1] == 'z':
            valid_people.remove(person)
            last_word = ''
            continue

        used_words.add(log)
        last_word = log

    print(len(valid_people))
    for person in valid_people:
        print(person)

if __name__ == '__main__':
    # 入力を受け取る
    N, K, M = map(int, input().split())
    words = [input().rstrip('\r\n') for _ in range(K)]
    logs = [input().rstrip('\r\n') for _ in range(M)]

    # 出力
    main(N, K, M, words, logs)