
def read_file(filename):
    word_list=[]
    fp=open(filename,"r")

    while True:
        tmp=fp.readline()
        if not tmp: break
        if tmp == "\n": continue
        word_list.append(tmp.split("\n")[0])
    fp.close()
    return word_list
    
def count_word_print(target,word_list,start,end):
    count=0
    same_list=[]
    for i in range(start,end+1):
        if word_list[i].split()[0].lower() == target:
            count+=1
            same_list.append(word_list[i])
    print "Found %d items"%count
    for j in range(0,len(same_list)):
        print same_list[j]



## binary search
def find1(target,word_list,start,end):
    if start > end:
        if end<=0:
            print "Not found"
            return -1
        print "Not found"
        print word_list[end].split()[0]+" "+word_list[end].split()[1]
        print "- - -"
        print word_list[start].split()[0]+" "+word_list[start].split()[1] 
        return end
    else:
        middle=(start+end)/2
        word=word_list[middle].split()[0].lower()
        if word == target.lower():
            count_word_print(word,word_list,start,end)
            return middle 
        elif word > target.lower():
            return find1(target,word_list,start,middle-1)
        else:
            return find1(target,word_list,middle+1,end)
        


if __name__ == "__main__":
    args=''
    subcommand=''
    word_list=[]
    while True:
        args=raw_input("$ ")
       
        if len(args.split())==2:
            command=args.split()[0]
            subcommand=args.split()[1]
        else:
            command=args
    
        if command=="find":
            if not len(args.split())==2:
                print "Please, input word"
                continue
            word_index=find1(subcommand,word_list,0,len(word_list)-1)
        if command=="read":
            if not len(args.split())==2:
                print "Please, input filename"
                continue
            word_list=read_file(subcommand)
        if command=="size":
            print len(word_list)
        if command=="exit":
            break

