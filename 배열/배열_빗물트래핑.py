#투 포인터 이용 방식
def sol(height:list):
    if not height:
        return 0

    #빗물 양 변수
    volume=0

    left, right=0,len(height)-1
    left_max, right_max=height[left], height[right]

    while left<right:
        left_max,right_max=max(height[left], left_max), max(height[right],right_max)

        if left_max<=right_max:
            print(left_max, height[left])
            volume+=left_max-height[left]
            left+=1
        else:
            print(right_max, height[right])
            volume+=right_max-height[right]
            right-=1

    return volume


#스택을 이용한 방식
def sol2(height:list):
    stack=[]
    volume=0

    for i in range(len(height)):
        #이 while 조건을 잘 이해해야 함. 물이 차려면 스택에 일단 
        #높이가 있는 기둥의 인덱스가 들어있어야 하고, 
        #현재 보고있는 기둥이 스택의 마지막 기둥높이보다 높아야 함
        while stack and height[i] > height[stack[-1]]:
            top=stack.pop()

            #스택에서 하나 팝했는데 스택이 비면
            #물이 차는게 성립되지 않음 --> break로 나감
            if not len(stack):
                break

            distance=i-stack[-1]-1

            #물의 양은 더 짧은 기둥에 맞춰짐
            waters=min(height[i],height[stack[-1]])-height[top]

            volume+=distance*waters
        stack.append(i)
         
    return volume


height=[3,1,2,1,2,5]
height2=[3,1,1,1,4]
print(sol(height))
