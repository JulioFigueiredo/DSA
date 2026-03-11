class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length+=1
        return self.length 

    def pop(self):
        lastItem = self.data[self.length-1] 
        del self.data[self.length-1]
        self.length-=1
        return lastItem
    
    def delete(self,index):
        deleteditem = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]

        del self.data[self.length-1]
        self.length-=1
        return deleteditem

arr = Array()
arr.push('hi')
arr.push('you')
arr.push('!')
arr.pop()
# arr.delete(1)
print(arr)