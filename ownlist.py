import ctypes

class ownlist:
    def __init__(self):
        self.size=1
        self.n=0
        self.A=self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self):
        result='' 
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '['+result[:-1]+']'
    def __getitem__(self,index):
        if 0<= index <=self.n:
            return self.A[index]
        else:
            return 'IndexError'
    def __delitem__(self,pos):
        if 0<=pos<self.n:
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n-=1
    def append(self,item):
        if self.n==self.size:
            self.__resize(self.size*2)
        self.A[self.n]=item 
        self.n+=1
    
    def __resize(self,new_cap):
        B= self.__make_array(new_cap)
        self.size=new_cap
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B
    def pop(self):
        if self.n==0:
            return 'Empty list'
        print(self.A[self.n-1])
        self.n=self.n-1
    def __make_array(self,capacity):
        #create a referential static array
        return (capacity*ctypes.py_object)()
    def clear(self):
        self.n=0
        self.size=1
    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return 'ValueError'
    def insert(self,pos,item):
        if self.n==self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i]=self.A[i-1]
        self.A[pos]=item
        self.n+=1
    def remove(self,item):
        pos = self.find(item)
        if type(pos)==int:
            self. __delitem__(pos)
        else:
            return pos
    def remove_index(self,index):
        item=self.__getitem__(index)
        self.remove(item)

            
L=ownlist()
L.append(23)
L.append('hello')
L.append(3.4)
L.append(23)
L.append(90)
print(L)
L.remove(23)
print(L)
print(L[1])
L.remove_index(2)
print(L)
