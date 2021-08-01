#로그의 가장 앞 부분은 식별자
#문자로 구성된 로그가 숫자로 구성된 로그보다 앞에
#식별자는 순서에 영향x, 문자가 동일할 경우에만 식별자순 정렬
#숫자 로그는 입력 순서대로

logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def solution(logs:list):
    words, nums=[],[]

    for i in range(len(logs)):
        if logs[i].split()[1].isdigit():
            nums.append(logs[i])
        else:
            words.append(logs[i])

    #이부분이 핵심
    words.sort(key=lambda x: (x.split()[1], x.split()[0]))

    return words+nums

sol=solution(logs)
print(sol)
