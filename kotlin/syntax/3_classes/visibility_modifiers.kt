package syntax.`3_classes`

// There are 4 visibility modifiers in Kotlin:
// - private // visible in its file or class
// - protected // private + visible to subclasses
// - internal // visible in its module
// - public // visible everywhere

private fun foo() {}

public var counter: Int = 0
    private set // setter is visible in its file

internal val build_version = "v1.0.2"


// In Kotlin, outer class cannot see private members of inner classes
// if you override protected member and do not specify its visibility, it stays as protected
open class Outer {
    private val a = 1
    protected open val b = 2
    internal val c = 3
    val d = 4 // public by default

    // constructor of inner class can be called inside the containing class only
    protected inner class Nested {
        public val e = 5
    }
}

class Subclass : Outer() {
    // a is not visible
    // b is visible because protected
    // c is visible because the same module
    // d is visible because the public by default

    init {
        super.b
        super.c
        super.d
        val n = Nested()
    }

    override var b = 12 // still protected
}

class Unrelated(o: Outer) {
    init {
        // d and c same module
        o.d
        o.c
        // val a = Outer.Nested() ERROR
    }
}

// To specify visibility modifier to constructor
class D private constructor(val name: String) {
    constructor(firstName: String, lastName: String) : this("$firstName $lastName")
}

val d = D("John", "Smith")



