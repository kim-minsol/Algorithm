sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

max_w, max_h = 0, 0


for w, h in sizes:
    tmp_w1 = max(w, max_w)
    tmp_h1 = max(h, max_h)
    
    change_w, change_h = h, w
    tmp_w2 = max(change_w, max_w)
    tmp_h2 = max(change_h, max_h)
    
    if tmp_w1*tmp_h1 <= tmp_w2*tmp_h2:
        max_w, max_h = tmp_w1, tmp_h1
    else:
        max_w, max_h = tmp_w2, tmp_h2

answer = max_w * max_h
print(answer)