text = input("输入提取后的文件名\n")
doc = input("输入ast文件名\n")
# 打开doc寻找在astE中JP行的文字，将其替换为CN行的文字即可
d = open(doc, mode="r+", encoding="UTF-8")
t = open(text, mode="r+", encoding="UTF-8")


def getz(str, lstr, rstr):
    l = str.find(lstr) + len(lstr)
    r = str.find(rstr)
    return str[l:r]


ct = len(t.readlines()) // 3
t.seek(0)
a = int(input("共有%d行要替换，确认输入1\n" % ct))

if a == 1:
    mainbuf = d.read()
    jplist = []
    cnlist = []
    for x in range(0, ct):
        code = str(x).zfill(5)
        #print(code)
        jpstr = t.readline()
        cnstr = t.readline()
        t.readline()
        jplist.append(getz(jpstr, code + 'JP\t', "\n"))
        cnlist.append(getz(cnstr, code + 'CN\t', "\n"))
    print(mainbuf)
    nd = open("./new/" + doc, mode="w", encoding="UTF-8")
    for x in range(len(jplist)):
        mainbuf = mainbuf.replace(jplist[x], cnlist[x])
    nd.write(mainbuf)
else:
    exit()


d.close()
t.close()
