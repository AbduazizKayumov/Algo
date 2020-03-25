##**The Master method for solving recurrences**
### The  master theorem
Let T(n) be defined on the nonnegative integers by the recurrence:  
```
    T(n) = aT(n/b) + f(n)
```
where `a` is # of subproblems each of size `n/b` (`a > 0 and b > 0`) and `f(n)` is the cost 
to divide the problem and combining the results of the subproblems, then `T(n)` has the following
asymptotic bounds:
```
           |  Θ(n^c)  if f(n) = O(n^c) and c < log b of a
    T(n) = |  Θ(n^c * logn) if f(n) = Θ(n^c) and c = log b of a
           |  Θ(f(n))   if f(n) = Ω(n^c) and c > log b of a
```

### Using the master method
To use the master method, simply determine which case of the master method theorem
applies, for ex. consider `T(n) = 9T(n/3) + n`:  
**a = 9, b = 3, f(n) = n**:  
`n^(log b of a) = n^(log 3 of 9) = Θ(n^2)`, since f(n) = O(n^2), we can apply case 1 of the master theorem and conclude that:  
``` 
T(n) = Θ(n^2)
```

Determine which `f(n)` or the dividing subproblem `aT(n/b)` dominates, if `f(n)` is asymptotically tightly bounded by `aT(n/b)`
`T(n) = Θ(n^c * lgn)`, otherwise `T(n)` is the dominating function: `Θ(n^c)` or `Θ(f(n))`
