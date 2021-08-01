import collections
import re

def solution(paragraph:str, banned:list):
    #먼저 문자열에서 단어만 솎아냄
    words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]

    counter=collections.Counter(words)

    result=counter.most_common(1)[0][0]
    
    return result



paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
banned=['hit']
