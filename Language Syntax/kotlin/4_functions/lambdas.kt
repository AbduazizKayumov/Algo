/*
* Kotlin functions are first class, which means that they can be stored in variables and data structures,
* passed as arguments to and returned from other higher order functions. You can operate with functions in
* any way that is possible for other non-function values
* */

fun <T, R> Collection<T>.fold(
    initial: R,
    combine: (acc: R, nextElement: T) -> R
): R {
    var accumulator: R = initial
    for (element: T in this)
        accumulator = combine(accumulator, element)
    accumulator
}

val items = listOf(1, 2, 3, 4, 5)

// Lambdas are code blocks enclosed in curly braces
items.fold(0, {
    // When a lambda has params, they go first, followed by '->'
    acc: Int, i: Int ->
    print("acc = $acc, i = $i, ")
    val result = acc + i
    println("result = $result")
    // The last expression in a lambda is considered the return value
    result
})
/*
* acc = 0, i = 1, result = 1
* acc = 1, i = 2, result = 3
* acc = 3, i = 3, result = 6
* acc = 6, i = 4, result = 10
* acc = 10, i = 5, result = 15
* */

// Parameter types are optional if they can be inferred:
val joinedToString = items.fold("Elements:", { acc, nextElement -> acc + " " + nextElement })
// Elements = Elements: 1 2 3 4 5

// Function references can also be used for higher-order function calls:
val product = items.fold(1, Int:times)
// product = 120

// Function types
// Kotlin uses a family of function types like (Int) -> String for declarations that deal with functions:
val onClick: () -> Unit = ...

// These types have a special notation that corresponds to the signatures of the functions: their params and
// return values
// - Parenthesized parameter types list and return type: (A, B) -> C
// - Function type notation can optionally include names for the function parameters: (x: Int, y: Int) -> Point

// You can also give a function type an alternative name by using a type alias:
typealias ClickHandler = (Button, ClickEvent) -> Unit

// Instantiating a function type
// There are several ways to obtain an instance of a function type:
// - Using a code block within a function literal, in one of the forms:
//     - a lambda expression: { a, b -> a + b }
//     - an anon. function: fun(s: String): Int { return s.toIntOrNull() ?: 0 }
// - Using a callable reference to an existing declaration:
//     - a top-level, local, member or extension function: ::isOdd, String::toInt
//     - a top-level, member, or extension property: List<Int>::size
//     - a constructor: ::Regex
// - Using instances of a custom class that implements a function type as an interface

// Invoking a function type instance
// A value of a function type can be invoked by using its invoke(...)operator: f.invoke(x) or just f(x).
// If the value jas a receiver type, the receiver object should be passed as the first argument:
val stringPlus: (String, String) -> String = String::plus
val intPlus: Int.(Int) -> Int = Int::plus

println(stringPlus.invoke("<-", "->"))
println(stringPlus("Hello, ", "World!"))

println(intPlus.invoke(1, 1)) // 2
println(intPlus(1, 2)) // 3
println(1.intPlus(3)) // extension-like call


// Lambda expressions and anonymous functions
// Lambda expression and anon. function are function literals, functions that are not declared, but passed immediately
// as an expression:
max(strings, { a, b -> a.length < b.length })

// max is a higher order function, it takes a function value as the second argument, the second argument is an expression
// that is itself a function

// Lambda expression syntax:
// The full syntactic form of lambda expressions:
fun sum: (Int, Int) -> Int = { x: Int, y: Int -> x + y }

//      func. literal ret.type surrounded by curly braces
// the last expression inside the lambda body is treated as the return value
val sum = { x, y -> x + y }

// Passing trailing lambdas
// In Kotlin, if the last parameter of a function is a function, then a lambda expression passed
// as the corresponding argument can be placed outside the parentheses:
val product = items.fold(1) { acc, nextElement ->
    acc * nextElement
}

// it: implicit name of a single parameter
// it is allowed not to declare the only parameter and omit:
array.filter { it > 0 }

// Underscores for unused variables:
// If the lambda parameter is not used, you can plce an underscore instead of its name:
map.forEach{ _, value -> println(value) }


// Anonymous functions
// An anonymous function looks very much like a regular function declaration, except that its name is omitted
ints.filter(fun(item) = item > 0)
// Anonymous function params are always passed inside the parenthesis


// Lambda expressions or anon. functions can access its closure: the variables declared in the outer scope
// the varibale captured in the closure can be modified in the lambda:
var sum = 0
ints.filter { it > 0 }.forEach{
    sum += it
}
print(sum)