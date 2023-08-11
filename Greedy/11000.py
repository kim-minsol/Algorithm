import heapq  # 단순 큐가 아닌 우선순위 큐를 사용하여 큐 내에 존재하는 강의 시간을 따로 참조하지 않아도 됨.

n = int(input())
class_ = []

for i in range(n):
    class_.append(list(map(int, input().split())))

class_.sort(key=lambda x: (x[0], x[1]))  # 강의 시작 시간이 빠른 순으로 정렬해야 함
heap = []
heapq.heappush(heap, class_[0][1])

for i in range(1, n):
    if class_[i][0] < heap[0]:  # 새로운 회의실을 사용해야 할 경우
        heapq.heappush(heap, class_[i][1])
    else:  # 강의를 이어서 수강 가능한 경우
        heapq.heappop(heap)  # 기존 강의 종료 시간을 pop한 후, 현재 강의 종료시간을 push
        heapq.heappush(heap, class_[i][1])

print(len(heap))