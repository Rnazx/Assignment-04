import library as mat
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#Question 1
print("********************************************************************************************************************")
print("Question 1 :-")
print("********************************************************************************************************************")
X=mat.store("Q1.txt",4)
n=len(X)
#Ax=b store A and b in different lists
A=[[X[i][j] for j in range(n)] for i in range(n)]
b=[X[i][n] for i in range(n)]
(L,U,c)=mat.croutLU(A,b)
print("The matrix L is :")
mat.printmatrix(L)
print("The matrix U is :")
mat.printmatrix(U)
print("The product of the two matrices L and U is verified to be A below : ")
mat.printmatrix(mat.matrixmultiply(L,U))
mat.forwardbackward(L,b)
mat.forwardbackward(U,b)
print("The solution to the set of equations is :")
for i in range(1,n+1):
    print("x"+str(i).translate(SUB),end='')
    print(" = ",b[i-1])
print()
#Question 2
print("********************************************************************************************************************")
print("Question 2 :-")
print("********************************************************************************************************************")
X=mat.store("Q2.txt",4)
n=len(X)
I=mat.identity(n)
(L,U,c)=mat.croutLU(X,I)
print("The matrix L is :")
mat.printmatrix(L)
print("The matrix U is :")
mat.printmatrix(U)
print("The permutation matrix (P) is given by :")
mat.printmatrix(I)
print("The product of the two matrices L and U is  :")
mat.printmatrix(mat.matrixmultiply(L,U))
A=mat.store("Q2.txt",4)
print("Which is equal to PxA")
mat.printmatrix(mat.matrixmultiply(I,A))
(Ainv,det)=mat.inverseLU(L,U,I,c)
print("The determinant of the matrix is :",det)
if (det!=0): 
    print("Hence the inverse exists!!\n")
    print("The inverse of the given matrix is :")
    mat.printmatrix(Ainv)
else:
    print("The inverse does not exist")
#Verifying AxAinv=I
print("The product of A and its inverse is given by :")
mat.printmatrix(mat.matrixmultiply(A,Ainv))
print("Which is almost equal to identity. The error is because of decimal approximations in python.")
print("********************************************************************************************************************")
#Output
'''
********************************************************************************************************************
Question 1 :-
********************************************************************************************************************
The matrix L is :

1.0   0.0   0.0   0.0   
0.0   1.0   0.0   0.0   
1.0   2.0   1.0   0.0   
2.0   1.0   1.5   1.0   


The matrix U is :

1.0   0.0   1.0   2.0
0.0   1.0   -2.0   0.0
0.0   0.0   2.0   -2.0
0.0   0.0   0.0   -3.0


The product of the two matrices L and U is verified to be A below :

1.0   0.0   1.0   2.0
0.0   1.0   -2.0   0.0
1.0   2.0   -1.0   0.0
2.0   1.0   3.0   -2.0


The solution to the set of equations is :
x₁ =  1.0
x₂ =  -1.0
x₃ =  1.0
x₄ =  2.0

********************************************************************************************************************
Question 2 :-
********************************************************************************************************************
The matrix L is :

1.0   0.0   0.0   0.0
0.0   1.0   0.0   0.0
0.0   0.0   1.0   0.0
0.0   0.5   -4.0   1.0


The matrix U is :

3.0   7.0   1.0   0.0
0.0   2.0   8.0   6.0
0.0   0.0   1.0   2.0   
0.0   0.0   0.0   6.0   


The permutation matrix (P) is given by :

0   0   0   1
1   0   0   0
0   1   0   0
0   0   1   0


The product of the two matrices L and U is  :

3.0   7.0   1.0   0.0
0.0   2.0   8.0   6.0
0.0   0.0   1.0   2.0
0.0   1.0   0.0   1.0


Which is equal to PxA

3.0   7.0   1.0   0.0
0.0   2.0   8.0   6.0
0.0   0.0   1.0   2.0
0.0   1.0   0.0   1.0


The determinant of the matrix is : -36.0
Hence the inverse exists!!

The inverse of the given matrix is :

-0.25000000000000006   1.6666666666666672   -1.8333333333333333   0.3333333333333333
0.08333333333333337   -0.666666666666667   0.8333333333333333   0.0
0.16666666666666666   -0.33333333333333326   -0.3333333333333333   0.0
-0.08333333333333333   0.6666666666666666   0.16666666666666666   0.0


The product of A and its inverse is given by :

1.0   0.0   0.0   0.0
0.0   1.0   0.0   0.0
4.163336342344337e-17   -3.3306690738754696e-16   0.9999999999999999   0.0
2.7755575615628914e-17   -2.220446049250313e-16   -2.7755575615628914e-16   1.0


Which is almost equal to identity. The error is because of decimal approximations in python.
********************************************************************************************************************
'''