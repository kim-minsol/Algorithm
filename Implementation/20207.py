n = int(input())

calender = []
arr = []
min_ = 100000
max_ = -1
for i in range(n):
    s, e = map(int, input().split())
    calender.append([s, e])
    if s < min_:
        min_ = s
    if e > max_ :
        max_ = e

arr = [0] * (max_ + 1)
calender.sort(key=lambda x: (x[0], -x[1]))


for i in range(n):
    s, e = calender[i]
    for i in range(s, e+1):
        arr[i] += 1


cnt = 0
ans = 0
range_ = 0
for k in arr:
    if k == 0:
        ans += (cnt * range_)
        cnt = 0
        range_ = 0
    else:
        if cnt < k:
            cnt = k
        range_ += 1
ans += (cnt * range_)
print(ans)




# 연속된 날짜 합치기
# for i in range(n):
#     if i >= len(calender):
#         break
#     s, e = calender[i]
#     flag = 0
#     for idx, (cal_s, cal_e) in enumerate(calender):
#         if cal_e + 1 == s:
#             calender[idx][1] = e
#             flag = 1
#             break
#         elif cal_s == e + 1:
#             calender[idx][0] = s
#             flag = 1
#             break
#     if flag == 1:
#         calender.pop(i)

# print(calender)
# # 직사각형 만들기
# calender.sort(key=lambda x: (x[0], -x[1]))

# min_ = calender[0][0]
# max_ = calender[0][1]
# cnt = 1
# ans = 0
# print(calender)
# for i in range(1, len(calender)):
#     if min_ <= calender[i][0] and max_ >= calender[i][0] and max_ >= calender[i][1]:
#         cnt += 1
#     else:
#         ans += cnt * (max_ - min_ + 1)
#         min_ = calender[i][0]
#         max_ = calender[i][1]
#         cnt = 1
# ans += cnt * (max_ - min_ + 1)
# print(ans)



## 코드 이해 및 정리는 내일 작업할 예정입니다  !!!