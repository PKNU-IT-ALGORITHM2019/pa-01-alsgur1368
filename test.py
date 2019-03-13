def read_file(filename):
    size=0
    word_list=[]
    try:
        fp=open(filename,"r")

        while True:
            tmp=fp.readline()
            if not tmp: break
            if tmp == "\n": continue
            word_list.append(tmp.split("\n")[0])
            size+=1

        fp.close()
        return word_list
    except IOError:
        print "Error"
        

wlist=["dictdd.txt",]
word_list=read_file(wlist[0])
print len(word_list)
print word_list[1]
