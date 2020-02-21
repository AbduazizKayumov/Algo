package syntax.`3_classes`

// As in Java, classes in Kotlin may have type parameters
class Box<T>(val t: T) {
    fun printT() {
        println(t)
    }
}

// we need to provide the type to create an instance of such class
val b1: Box<Int> = Box(12)
val b2 = Box(32) // if the type can be inferred from the constructor, no need to include the type


// In and Out  = CONSUMER IN, PRODUCER OUT
// Classes having <in T> modifier can only consume T type objects
// Classes having <out T> modifier can produce T type objects
interface Consumer<in T> {
    fun nextT(): T // ERROR, can only consume
    fun nextT(a: T) // OK
}

interface Source<out T> {
    fun nextT(): T // OK
    fun nextT(a: T) // ERROR, can only produce
}
