# Knapsack problem
# 
# A thief robbing a store finds n items. The ith item is worth v[i] dollars and weighs w[i] kilos.
# The thief wants to take as valuable a load as possible, but he can carry at most W kilos in his
# backpack. Which items should he take? 
# 
# 			0-1 Knapsack problem 				 Fractional knapsack problem
#     	   You CANNOT divide items					You CAN divide items
# 					|										 |
#					v 										 V
#			Dynamic programming						  Greedy approach
#
#
#			 Why not Greedy?							Why not DP?
# 					|										 |
#					v 										 V
#	Does not guarantee an optimal solution				 Overkill!


# 0-1 Knapsack problem
v = [60, 100, 120, 140, 200]
w = [1,  2,  3,  4,  5]
W = 5

n = len(v)
dp = [[0] * (W+1) for _ in range(n+1)]

for i in range(1, n+1):
	for  j in range(1, W+1):
		weight, value = w[i-1], v[i-1]
		if weight <= j:
			dp[i][j] = max(value + dp[i-1][j - weight], dp[i-1][j])
		else:
			dp[i][j] = dp[i-1][j]

# Pick 2nd and 3rd items with overall value = 210
for d in dp:
	print(d)


# Fractional knapsack problem
# Compute value per kilo, take most valuable items until exhausted
f = [0] * n
for i in range(n):
	value_per_kilo, weight = v[i] / w[i], w[i]
	f[i] = [value_per_kilo, weight]
# Sort by value per kilo
f.sort(reverse=True)
print()

res = 0
val = 0
for i in range(n):
	value_per_kilo, weight = f[i][0], f[i][1]
	available = W - res
	if available > 0:
		res += min(weight, available)
		val += value_per_kilo * min(weight, available)
print(res, "kilos gold ($", val, ")")






