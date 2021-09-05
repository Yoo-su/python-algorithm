#(단가, 짐의 무게)
sample=[
    (4,12), (2,1), (10,4), (1,1), (2,2)
]

#한정된 가방에 가치가 최대가 되도록 담게 구현
def solution(data):
    capacity=15
    pack=[]

    for item in data:
        pack.append((item[0]/item[1], item[0], item[1]))
    pack.sort(reverse=True)

    total_value:float=0
    for p in pack:
        if capacity-p[2]>=0:
            capacity-=p[2]
            total_value+=p[1]
        else:
            fraction=capacity/p[2]
            total_value+=p[1]*fraction
            break
    
    return total_value