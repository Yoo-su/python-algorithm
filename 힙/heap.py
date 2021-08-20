#최대힙을 구현해보자

class BinaryHeap(object):
    def __init__(self) -> None:
        #0번 인덱스 미사용
        self.items=[None]

    def __len__(self):
        return len(self.items)-1

    def up(self):
        #현재 힙 길이
        i=len(self)

        #삽입할 요소의 Parent 인덱스
        parent=i//2
        while parent>0:
            if self.items[parent]<self.items[i]:
                self.items[parent],self.items[i]=self.items[i],self.items[parent]
            
            i=parent
            parent=parent//2

    def insert(self,num):
        self.items.append(num)
        self.up()

    def down(self,idx):
        left,right=idx*2,idx*2+1
        biggest=idx

        if left<=len(self) and self.items[left]>self.items[biggest]:
            biggest=left

        if right<=len(self) and self.items[right]>self.items[biggest]:
            biggest=right

        #왼쪽 오른쪽 중 값이 더 큰 자리와 교체
        if biggest !=idx:
            self.items[idx], self.items[biggest]=self.items[biggest],self.items[idx]
            self.down(biggest)

    def pop(self):
        extracted=self.items[1]
        self.items[1]=self.items[len(self)]
        self.items.pop()
        self.down(1)
        return extracted

arr=[3,2,3,1,2,4,5,5,6]
test=BinaryHeap()
for i in arr:
    test.insert(i)

print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())


    