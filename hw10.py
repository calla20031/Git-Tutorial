import pickle
import os

def save_scores(scores):
    with open('score.bin', 'wb') as file:
        pickle.dump(scores, file)

def load_scores():
    if os.path.exists('score.bin'):
        with open('score.bin', 'rb') as file:
            scores = pickle.load(file)
            return scores
    else:
        return None

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f"#{i}?"))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=" ")
    print()

scores = load_scores()
if scores is None:
    print("[점수 입력]")
    scores = input_scores()
    save_scores(scores)

print("\n[점수 출력]")
print("개인 점수 :", end="")
show_scores(scores)
avg = get_average(scores)
print(f"평균 : {avg:.1f}")
print("[파일 읽기]")
