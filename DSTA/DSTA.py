import numpy as np

class DSTA():
    # 初始化
    def __init__(self,fun,Range,SE,MaxIter):
        self.fun = fun
        self.Range = Range
        self.SE = SE
        self.MaxIter = MaxIter
        self.Dim = self.Range.shape[1]

    def initialization(self):
        self.Best = np.random.randint(self.Range[0,0],self.Range[1,0],self.Dim)
        self.fBest = self.fun(self.Best)
        self.history = []
        self.history.append(self.fBest)

    # 交换算子，产生候选解
    def op_swap(self):
        State = np.zeros((self.SE,self.Dim),dtype = int)
        for i in range(self.SE):
            temp = self.Best.copy()
            R = np.random.permutation(self.Dim)
            a = R[0]
            b = R[1]
            temp[b],temp[a] =   temp[a],temp[b]
            State[i,:] = temp
        return State

    # 替换算子
    def op_substitute(self):
        State = np.zeros((self.SE, self.Dim), dtype=int)
        for i in range(self.SE):
            temp = self.Best.copy()
            index = np.random.randint(0, self.Dim)  # 如果使用的是random 库中的，是包含后面的上界的，要 n-1，如果你使用numpy 里面的random.randint，则不用减一
            temp[index] = np.random.randint(self.Range[0,index], self.Range[1,index]+1)  # 加一是为了取到上界
            State[i, :] = temp
        return State

    # 对称算子，产生候选解
    def op_symmetry(self):
        State = np.zeros((self.SE,self.Dim),dtype = int)
        for i in range(self.SE):
            temp = self.Best.copy()
            R = np.random.permutation(self.Dim)
            a = R[0]
            b = R[1]
            if a < b:
                temp[list(range(a,b+1))] = temp[list(range(b,a-1,-1))]
            else:
                temp[list(range(b,a+1))] = temp[list(range(a,b-1,-1))]
            State[i,:] = temp
        return State
        
    # 平移算子，产生候选解
    def op_shift(self):
        State = np.zeros((self.SE,self.Dim),dtype = int)
        for i in range(self.SE):
            temp = self.Best.copy()
            R = np.random.permutation(self.Dim)
            a = R[0]
            b = R[1]
            if a < b:
                temp[a:b],temp[b] = temp[a+1:b+1],temp[a]
            else:
                temp[b:a],temp[a] = temp[b+1:a+1],temp[b]
            State[i,:] = temp
        return State
    
    # 选择更新当前最优解
    def selection(self,State):
        fState = np.zeros((self.SE,1))
        for i in range(self.SE):
            fState[i] = self.fun(State[i,:])
        index_newBest = np.argmin(fState)
        newBest = State[index_newBest,:]
        fnewBest = fState[index_newBest,:]
        if fnewBest < self.fBest:
            self.Best = newBest
            self.fBest = fnewBest

    
    # 迭代优化
    def run(self):
        self.initialization()
        for i in range(self.MaxIter):
            State = self.op_swap()
            self.selection(State)
            State = self.op_substitute()
            self.selection(State)
            State = self.op_shift()
            self.selection(State)
            State = self.op_symmetry()
            self.selection(State)

            self.history.append(self.fBest[0])

            """让算法提前停止,如果连续100次都变化不明显"""
            if i>100 and (abs(self.history[i] - self.history[i-100]) < 1e-10):
                break
            
    

        