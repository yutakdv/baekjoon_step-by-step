# 1110
tmp = input()
if int(tmp) < 10:
    tmp = "0" + tmp

num = list(tmp)

st_num = "".join(num)
new_ls = []

while True:
    a = list(str(int(num[0]) + int(num[1])))
    num = num[1] + str(a[-1])
    new_ls.append(num)
    num = list(num)
    if st_num in new_ls:
        break

print(len(new_ls))
    