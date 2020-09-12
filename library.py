
#function for storing the augmented matrix matrix(A) from a file
def store(st,rows):
    X=[]
    T=[]
    rows=int(rows)
    with open(st,'r+') as file:
        i=0
        while i<rows:
            s=file.readline()
            p=s.split()
            j=0
            while (j<len(p)):
                T.append(float(p[j]))
                j=j+1
            X.append(T)
            T=[]
            i=i+1 
        return X
#function for partial pivoting
def partialpivot(A,n,b):
    count=0
    for k in range(n-1):
        if A[k][k]==0:
            for l in range(k+1,n):
                if abs(A[l][k])>abs(A[k][k]):
                    A[k],A[l]=A[l],A[k]
                    b[k],b[l]=b[l],b[k]
                    count+=1
                else : continue
        else : continue
    return count
#function for Gauss jordan method
def gaussjordan(Aug):
    n=len(Aug)
    m=len(Aug[1])
    k=0
    flag=True
    while (k<n) and flag:
        partialpivot(Aug,n,[0 for i in range(n)])
        piv = Aug[k][k]
        for l in range(k,m):
            Aug[k][l]/=piv
        for i in range(n):
            if i==k or Aug[i][k]==0: continue
            else: 
                factor=Aug[i][k]
                for j in range(k,m):
                    Aug[i][j]-=factor*Aug[k][j]
        k+=1
        #to check if unique solution exists
        l=0
        for i in range(n):
            if Aug[n-1][i]==0:
                l+=1
        if (l==n):
            flag=False
            if (Aug[n-1][n]!=0): print("The system has no solution")
            else: 
                print("The system has no unique solution")
                print("One of the infinite solutions is")
#function for matrix multiplication
def matrixmultiply(A,B):
    n=len(A)
    prod=[[] for x in range(n)]
    t=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                t+=A[i][k]*B[k][j]
            prod[i].append(t)
            t=0
        j=0
    return prod
#function for identity matrix of order n 
def identity(n):
    I=[[int(x==y) for x in range(n)] for y in range(n)]
    return I
#function for augmenting a matrix upon the other
def augment(A,B):
    n=len(A)
    for i in range(n):
        A[i]+=B[i]
#function to print matrix
def printmatrix(A):
    n=len(A)
    m=len(A[0])
    for i in range(n):
        print()
        for j in range(m):
            print(A[i][j],end="   ")
    print('\n\n')
#function for Crout's L, U decomposition
def croutLU(A,b):
    n=len(A)
    c=0
    augment(A,A)#this will be a 3x6 matrix with LHS as L and RHS as U
    for j in range(n):
        c+=partialpivot(A,n,b)
        for i in range(n):
            l=k=0
            while k<i and i<=j:
                A[i][n+j] -= A[i][k]*A[k][n+j]
                k+=1 
            while l<j and i>j:
                A[i][j] -= A[i][l]*A[l][n+j]
                l+=1
            if (i>j): 
                A[i][j]/=A[j][n+j]
                A[i][j+n]=0.0 #lower triangular entries in U to be 0
            else : A[i][j]=float(i==j)  #setting upper triangular entries in U to be 0 and diagnol entriesto be 1
    L=[[A[i][j]for j in range(n)] for i in range(n)]
    U=[[A[i][j+n]for j in range(n)] for i in range(n)]
    return L,U,c
#Function for forward backward substitution Ax=b
def forwardbackward(A,b):
    n=len(A)
    sum=0
    #to check if lower or upper triangular
    for l in range(n):
        for m in range(n):
            if (l<m):
                sum+=A[l][m]
    if(sum==0):
        p=1 #it is lower triangular
    else: 
        p=-1 #it is upper triangular
        n+=1
    s=int(sum!=0)
    #substitution
    for i in range(s,n):
        for j in range(s,i):
            b[p*i]-=A[p*i][p*j]*b[p*j]
        b[p*i]/=A[p*i][p*i]
#function for finding the inverse of a decomposed matrix
def inverseLU(L,U,P,c):
    n=len(L)
    det=1
    for i in range(n):
        det*=U[i][i]
    det*=(-1)**c
    if (det!=0):
        X=fbm(U,fbm(L,P))
    return X,det
#forward backward for matrices LUxAinv=P
def fbm(A,P):
    n=len(A)
    sum=0
    y=list(P)
    #to check if lower or upper triangular
    for l in range(n):
        for m in range(n):
            if (l<m):
                sum+=A[l][m]
    if(sum==0):
        p=1 #it is lower triangular
    else: 
        p=-1 #it is upper triangular
        n+=1
    s=int(sum!=0)
    #substitution
    for i in range(s,n):
        for k in range(s,n):
            for j in range(s,i):
                y[p*i][p*k]-=A[p*i][p*j]*P[p*j][p*k]
            y[p*i][p*k]/=A[p*i][p*i]
    return y