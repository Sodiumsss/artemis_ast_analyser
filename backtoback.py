text = input("输入提取后的文件名\n")
doc = input("输入ast文件名\n")
# 将ast中的文本覆盖至提取后文件的JP行
t = open(text, mode="r+", encoding="UTF-8")
f = open(doc, mode="r+", encoding="UTF-8")
ver = None
blockbuf = f.readlines()  # 块缓冲
if blockbuf[0].find("astver = ") != -1:
    ver = blockbuf[0].lstrip("astver = ")
    f.seek(0)
else:
    exit()


def getz(str, lstr, rstr):
    l = str.find(lstr) + len(lstr)
    r = str.find(rstr)
    return str[l:r]


class astblock:
    def __init__(self):
        pass

    code = None
    method = []
    istext = False  # True->japan
    truetext = ""


ct = len(t.readlines()) // 3
t.seek(0)
cnlist = []
for x in range(0, ct):
    code = str(x).zfill(5)
    # print(code)
    t.readline()
    cnstr = t.readline()
    t.readline()
    cnlist.append(getz(cnstr, code + 'CN\t', "\n"))

block = [astblock() for i in range(10000)]  # 偷懒
blockct = 0
isblock = 0
for ct in range(1, len(blockbuf) + 1):  # block开始到结束 ct->行数
    if ct == 1 or ct == 2:
        f.readline()
    else:
        buf = f.readline()
        if buf.count("\t") == 1:
            if buf.find("block") == 1:
                block[blockct].code = buf[7:12]
                isblock = 1
            elif buf.count("\t},") == 1 and isblock == 1:
                blockct = blockct + 1
                isblock = 0
        elif buf.count("\t") == 5 and buf != '\t\t\t\t\t{"rt2"},\n':
            block[blockct].truetext = getz(buf, '"', '",\n')

p = open("./new/" + doc + "E", mode="w+", encoding="UTF-8")
for i in range(blockct):
    mytext = block[i].code + "JP\t" + block[i].truetext + "\n" + block[i].code + "CN\t" + cnlist[i] + "\n\n"
    print(mytext)
    p.writelines(mytext)
f.close()
p.close()
