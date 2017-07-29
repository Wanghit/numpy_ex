import numpy as np
def npSum():
    a=np.array([1,2,3,4,5])
    b=np.array([1,1,1,1,1])
    c=a**2+b**3
    #c=np.array([[1,1,1,1,1],[2,2,2,2,2]])
    print(c)
    print(c.ndim)
    print(c.shape)
    print(c.size)
    print(c.dtype)
    print(c.itemsize)
    #return c
if __name__=="__main__":
    npSum()
    a=[[1,1,1],[2,2],3]
    print(np.ones_like(a))
    print(np.arange(1,10,2))
    print(np.ones((3,2)))
    print(np.eye(5))
    print(np.full(5,5))
    print(np.arange(1,10,3))
    x=np.linspace(start=1,stop=10,num=3,retstep=True)
    print(len(x))
    #a=np.linspace(1,10,4)
    #b=np.linspace(1,10,4,endpoint=False)
    a=[1,2,3]
    b=[4,5,6]
    c=np.concatenate((a,b))#双括号
    print(c)
    print(np.linspace(1,10,num=3,retstep=True))
    x=np.array([1,2,3])
    print(x)
    a=np.ones((2,3,4),dtype=np.int32)
    print(a)
    print(a.reshape((3,8)))
    print(a)
    #b=a.resize((3,8))
    #print(b)#返回空，原数组改变，reshape原数组不改变
    #print(a.resize((3,8)))
    print(a)
    print(a.flatten())#flatten()不改变原数组
    b=a.astype(np.float)
    print(b)
    print(b.astype(b.dtype))
    print(b.tolist())
    a=np.array([1,2,3,4,5,6])
    print(a[-2])
    b=[1,2,3,4,5,6]
    print(b[-1])
    print(a[1:4:2])
    a=np.arange(24).reshape((2,3,4))
    print(a)
    print(a[1,2,3])
    print(a[:,:,::2])
    print(a[:,1:2,:])
    a=np.arange(24).reshape((2,3,4))
    print(a)
    print(a.mean())
    print(a/a.mean())
    print(np.sqrt(a))
    print(np.modf(a))
    b=np.sqrt(a)
    print(a>b)
    a=np.arange(100).reshape((5,20))
    #np.savetxt('D://a.csv',a,fmt='%d',delimiter=',')
    np.savetxt('D://b.csv',a,fmt='%.1f',delimiter=',')
    np.savetxt('D://c.gz',a,fmt='%.1f',delimiter=',')
    b=np.loadtxt('D:/c.gz',delimiter=',')
    print(b)
    d=np.arange(100).reshape(5,10,2)
    d.tofile("D://d.bat",format='%d')
    e=np.fromfile("D://d.bat",dtype=np.int32)
    print(e)
    print(e.reshape(5,10,2))
    np.save("D://f.npy",d)
    f=np.load("D://f.npy")
    print(f)
    print(np.random.rand(3,4,5))
    print(np.random.randn(3,4,5))
    print(np.random.randint(100,200,(3,4)))
    #np.random.seed(10)
    print(np.random.randint(100,200,(3,4)))
    a=np.random.randint(100,200,(3,4))
    print(a)
    print("//")
    np.random.shuffle(a)
    print(a)
    print("//")
    print(np.random.permutation(a))
    print("//")
    print(a)
    a=np.random.randint(100,200,(8,))
    print(">>>>>>>>>")
    print(a)
    print(np.random.choice(a,(3,2)))
    print(np.random.choice(a,(3,2),replace=False))
    print(np.random.choice(a,(3,2),p=a/np.sum(a)))
    print("------------->")
    u=np.random.uniform(0,10,(3,4))
    print(u)
    u=np.random.normal(0,10,(3,4))#正态分布 u,deta
    print(u)
    print("------------------->")
    a=np.arange(15).reshape(3,5)
    print(np.sum(a))
    print(np.mean(a,axis=1))
    print(np.mean(a,axis=0))
    print(np.mean(a))
    print(np.average(a,axis=0,weights=[10,5,1]))
    print(np.std(a))
    print(np.var(a))
    b=np.arange(15,0,-1).reshape(3,5)
    print(np.min(b))
    print(np.max(b))
    print(np.argmin(b))
    print(np.unravel_index(np.argmax(b),b.shape))
    print(np.ptp(b))
    print(np.median(b))
    a=np.random.randint(0,20,(3,5))
    print(a)
    print(np.gradient(a))