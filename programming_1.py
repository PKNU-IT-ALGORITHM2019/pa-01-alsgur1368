
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
    


## binary search
def find1(target,word_list,start,end,count):
    if start > end:
        if count != 0:
            return 0
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
            return middle 
        elif word > target.lower():
            return find1(target,word_list,start,middle-1,count)
        else:
            return find1(target,word_list,middle+1,end,count)
        


if __name__ == "__main__":
    args=''
    subcommand=''
    word_list=[]
    word_index=[]
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
            copy_list=word_list[:]
            find_items=[]
            count=0
            word_index=find1(subcommand,copy_list,0,len(copy_list)-1,count)
            while copy_list[word_index].split()[0].lower()==subcommand.lower():
                find_items.append(copy_list[word_index])
                del copy_list[word_index]
                count+=1
                word_index=find1(subcommand,copy_list,0,len(copy_list)-1,count)
            if not count==0:
                print "Found %d items"%count
                for i in range(0,len(find_items)):
                    print find_items[i]                
        if command=="read":
            if not len(args.split())==2:
                print "Please, input filename"
                continue
            word_list=read_file(subcommand)
        if command=="size":
            print len(word_list)
        if command=="exit":
            break

