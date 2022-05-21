# FrobeniusProblem
## Compute Solution of Frobenius Problem

The Frobenius problem, also known as the postage-stamp problem or the money changing problem, is an integer programming problem that seeks nonnegative integer solutions to x_1 * a_1 + ··· + x_n * a_n = M, where a_i and M are positive integers. In particular, the Frobenius number f(A), where A = {a_i}, is the largest M so that
this equation fails to have a solution

To Solve this problem we can use Dijkstra Algorithm which transform the problem to a shortest-path problem as a directed weighted graph to using Dijkstra's Algorithm. And then, we also can optimize this aproach by Greedy Algorithm. for the details, you can read my paper in this repository at the doc folder.

## requirement
- python3

## How to use This Program

clone this repository 
```
  git clone https://github.com/gilanglahat22/FrobeniusProblem.git
```

and then run this command in your terminal
```
 python src/main.py
```

## Copyright by Muhammad Gilang Ramadhan
