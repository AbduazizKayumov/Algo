package syntax.`4_functions`

// Functions
// A function having two input ints with Int return type
fun sum_ab(a: Int, b: Int): Int {
    return a + b
}

// A function with expression body and infered return type
fun sum_ab_inferred(a: Int, b: Int) = a + b

// A function tha return nothing
fun just_print(s: String): Unit {
    println(s)
}

// Unit return type can be omitted
fun just_print2(s: String) {
    println(s)
}

// or
fun just_print3(s: String) = println(s)

// A function with default parameters
fun printSum(a: Int = 0, b: Int = 0) {
    println("Sum of $a and $b is ${a + b}")
}

// If default value is used, other parameters must be passed with named arguments
// printSum(b = 23) // a is 0 by default

