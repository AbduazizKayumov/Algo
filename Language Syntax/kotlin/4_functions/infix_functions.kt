// Infix notation
// Function marked with infix notation can be called without the parentheses and omitting the dot
infix fun Int.shl(x: Int): Int { ... }
10 shl 2
// Infix functions must satisfy:
// 1. Must be member functions or extension functions
// 2. They must have a single parameter
// 3. Must accept variable number of arguments
// 4. Parameter must have no default value
// Infix functions have lower precendence than the arithmetic operations, type casts and rangeTo operator
10 shl 2 + 3 = 10 shl (2 + 3)