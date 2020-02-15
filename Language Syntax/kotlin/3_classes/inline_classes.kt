package syntax.`3_classes`

/*
* Sometimes it is necessary for business logic to create a wrapper around some type
* However, it introduces additional runtime overhead due to additional heap allocations
* Moreover, if the wrapper type is primitive, the overhead is terrible, since primitive
* types are heavily optimized by the runtime, to solve such situation, Kotlin (1.3) intruduces
* 'inline' classes. Inline classes must have a single property initialized in its primary contructor
* */

inline class Password(val s: String) {
    val length: Int
        get() = s.length

    fun greet() {
        println("Hey, I am $s")
    }
}

// inline classes are experimental
fun inlineTest() {
    val password = Password("Don't try this in production")
    // instead of creating an object of Password,
    // at runtime, password contains only string
}

// Inline classes can declare properties and member functions
// However, there are some restrictions for inline classes:
/*
* 1) inline classes cannot have init blocks
* 2) inline classes cannot have backing fields
* */
var count_steps = 0
    set(value) {
        if (value >= 0)
            field = value
    }