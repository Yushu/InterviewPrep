def solution(img):
    temp = [[0 for i in range(len(img[0]))] for j in range(len(img))]
    img_row = len(img)
    img_col = len(img[0])
    for i in range(img_row):
        for j in range(img_col):
            cell = 0
            e = -1
            for k in range(-1,2):
                for l in range(-1,2):
                    if 0 <= k + i < img_row and 0 <= l + j < img_col:
                        cell += img[k+i][l+j]
                        e += 1
            temp[i][j] = (cell - img[i][j]) / e
    return temp