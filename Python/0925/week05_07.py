i = 0
scores = []
while i<5:
    i+=1
    score = input(f"{i}번째 점수:")
    if not score.strip():
        break
    scores.append(float(score))

if 0<len(scores):
    number=0
    summary=0
    for score in scores:
        number+=1
        summary+=score
        print(f"{number}:{score}")
    print(f"avg:{summary/len(scores)}")
else:
    print("점수가 없어요!")
    
