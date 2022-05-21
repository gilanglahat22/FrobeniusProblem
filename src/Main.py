# Nama : Muhammad Gilang Ramadhan
# NIM  : 13520137
# MainProgram

from Algorithm import *
import time

print("Frobenius Problem Solver")
print()
n = int(input("Please input n : "))
print()
A = [0 for i in range(n)]
for i in range(n):
    A[i] = int(input("input a_" + str(i+1)+" : "))
print()
start = time.time()
print("Solution of "+str(A)+" is", GreedyDijkstra(A))
end = time.time()
print()
print("Execution time : ",(end-start))
