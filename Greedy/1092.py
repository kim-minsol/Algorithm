n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

box.sort(reverse=True)
crain.sort(reverse=True)

if crain[0] < box[0]:  # 배로 옮길 수 없는 경우는 박스의 무게가 크레인이 들 수 있는 최대 무게보다 큰 경우임.
    print(-1)
else:
    cost = 0
    while box:
        for c in crain:
            for i in range(len(box)):  # 옮긴 박스는 제거하였으므로, 반복문으로 참조 시에 len함수를 통해 box 범위를 맞춰야 함.
                if c - box[i] >= 0:  # 크레인이 박스를 들 수 있는 경우
                    c -= box.pop(i)  # 박스 제거 + 값 가져오기
                    break
        cost += 1
    print(cost)
