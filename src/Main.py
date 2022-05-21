# Nama : Muhammad Gilang Ramadhan
# NIM  : 13520137
# MainProgram

from Algorithm import *
import time

print("Frobenius Problem Solver")
print()
n = int(input("Masukkan n : "))
print()
A = [0 for i in range(n)]
for i in range(n):
    A[i] = int(input("Masukkan a_" + str(i+1)+" : "))
print()
start = time.time()
print("Solusi dari "+str(A)+" is", GreedyDijkstra(A))
end = time.time()
print()
print("Execution time : ",(end-start))