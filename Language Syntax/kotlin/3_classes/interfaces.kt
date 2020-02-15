package syntax.`3_classes`

// Interfaces in Kotlin can have declarations of abstract methods, as well as method implementations
interface Shiny {
    fun bar()
    fun shine(s: String) {
        println("**$s**")
    }
}

// A class or object can implement one or more interfaces
class Sun : Shiny {
    override fun bar() {
        shine("sun")
    }

    override fun shine(s: String) {
        println("*****")
        super.shine(s)
        println("*****")
    }
}


// Properties in interface can either be abstract or provide implementations
interface Planet {
    val radius: Long
    val diameter: Long
        get() = this.radius * 2
}


// val property can be changed to var
class FlexPlanet : Planet {
    override var radius = 100L
}

// Interface can implement other interfaces, naturally, derived interfaces provide their own implementations
// so that base class only have to implement methods without implementation
interface Named {
    val name: String
}

interface Human : Named {
    val firstName: String
    val lastName: String
    override val name: String
        get() = "$firstName $lastName"
}

data class Employee(
        override val firstName: String,
        override val lastName: String,
        var position: String
) : Human


// Resolving overriding conflicts
interface A {
    fun foo() = println("foo A")
    fun bar()
}

interface B {
    fun foo() = println("foo B")
    fun bar() = println("bar B")
}

class C : A, B {
    override fun foo() {
        super<A>.foo()
        super<B>.foo()
    }

    override fun bar() {
        super<B>.bar()
    }
}
