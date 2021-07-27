class LRU:
    l=[]
    def __init__(self,memory):
        self.memory=memory
    def put(self,ele):
        if(len(self.l)>=self.memory):
            if ele in self.l:
                ind=self.l.index(ele)
                self.l.pop(ind)
                self.l.append(ele)
            else:
                self.l.pop(0)
                self.l.append(ele)
        else:
            self.l.append(ele)

    def get(self):

        return self.l[0]



    def get_cache(self):

        return self.l

