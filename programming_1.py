

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
def find1(search_word,word,start,end):
    if start > end:
        if end<0:
            return -1
        return end,start
    
        

        
        
        




def get_word(word_list):
    word=[]
    for i in range(0,len(word_list)):
        word.append(word_list[i].split()[0])
    return word







if __name__ == "__main__":
    args=''
    subcommand=''
    word_list=[]
    word_index=[]
    word=[]
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
            word=get_word(word_list)
            word_index=find1(subcommand,word,0,len(word_list)-1)
        if command=="read":
            if not len(args.split())==2:
                print "Please, input filename"
                continue
            word_list=read_file(subcommand)
        if command=="size":
            print len(word_list)
        if command=="exit":
            break

