# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
string = input('请输入：')
d = {}
for ch in string:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
for k,v in d.items():
    print(k,'===', v)
