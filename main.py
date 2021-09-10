doc=input("输入文件名\n")
f = open(doc, mode="r+", encoding="UTF-8")
ver = None
blockbuf = f.readlines()  # 块缓冲
#print(blockbuf)
if blockbuf[0].find("astver = ") != -1:
    ver = blockbuf[0].lstrip("astver = ")
    f.seek(0)
else:
    exit()
def getz(str,lstr,rstr):
    l=str.find(lstr)+len(lstr)
    r=str.find(rstr)
    return str[l:r]

class astblock:
    def __init__(self):
        pass
    code=None
    method = []
    istext = False  # True->japan
    truetext = ""


block = [astblock() for i in range(10000)]  # 偷懒
blockct=0
isblock=0
for ct in range(1, len(blockbuf) + 1):  # block开始到结束 ct->行数
    if ct == 1 or ct == 2:
        f.readline()
    else:
        buf = f.readline()
        # print("%d %s"%(ct,buf))
        if buf.count("\t") == 1:
            # 一次为头操作(不一定是block,有可能是label),block结束也在里面
            if buf.find("block") == 1:
                #限定block_xxxxx的情况
                block[blockct].code=buf[7:12]
                isblock=1
            elif buf.count("\t},")==1 and isblock==1:
                #print("%d处" % ct)
                blockct=blockct+1
                #print(ct)
                isblock=0
        elif buf.count("\t")==5 and buf != '\t\t\t\t\t{"rt2"},\n':
            block[blockct].truetext=getz(buf,'"','",\n')






'''
        elif buf.count("\t") == 2:
        # 两次为具体操作,大致两类:带括号的，不带括号的
        #带括号的
            if buf.count('{"')==1 and buf.count('"},')==1:
                #检测逗号，里面没逗号直接放method
                buf=getz(buf,'{','},')
                print(buf)
                if buf.count(",")==0:
                    if buf=='"text"':
                        block[blockct].istext=True
                    else:
                        block[blockct].method.append(buf)

                else:
                    pass

        #不带括号的


        elif buf.count("\t") == 3:
            # 三次是语言

            pass
        elif buf.count("\t") == 4:
            # 四次是文本括号

            pass
'''
p = open(doc+"E", mode="w+", encoding="UTF-8")
for i in range(blockct):
    mytext=block[i].code+"JP\t"+block[i].truetext+"\n"+block[i].code+"CN\t"+block[i].truetext+"\n\n"
    print(mytext)
    p.writelines(mytext)
f.close()
p.close()