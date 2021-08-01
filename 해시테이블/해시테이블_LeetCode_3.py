def sol1(s:str):
    used={}
    maxL=start=0

    for i, c in enumerate(s):
        """중복문자를 발견했을 때, 그냥 
        if문으로 들어가면 카운트되지 않는게 생긴다.
        start가 더 작을 때 if문 입장
        """
        if c in used and start<=used[c]:
            start=used[c]+1
        else:
            maxL=max(maxL, i-start+1)

        used[c]=i

    return maxL


def mysol(s:str):
    used={}
    maxL=start=0

    for index, char in enumerate(s):
        if char not in used:
            #등장한 문자가 아닌경우 등장위치와 함께 삽입
            used[char]=index
            maxL=max(maxL,index-start+1)
        #이미 등장했고, 현재 시작지점보다 뒤의 것이면
        elif used[char]>=start:
            start=used[char]+1
            used[char]=index
        else:
            used[char]=index
            maxL=max(maxL,index-start+1)
    return maxL

testCase='aabaab!bb' 

print(mysol(testCase))