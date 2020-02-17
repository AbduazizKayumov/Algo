/*
* Delegation pattern is a good alternative to implementation inheritance
* A class Derived can implement interface Base by delegating all of its public members to a specific object
* */

interface Base {
    fun print()
}

class BaseImpl(val x: Int) : Base {
    override fun print() {
        print(x)
    }
}

class Derived(b: Base) : Base by b

// same with
class Derived(b: BaseImpl) : Base {
    override fun print() = b.print()
}


fun main() {
    val b = BaseImpl(10)
    Derived(b).print() // 10
}

/*
* The by clause in the supertype list for Derived indicates that b will be stored internally in objects of Derived
* and the compiler will generate all the methods of Base that forward to b
* Overrides work as you may expect: the compiler will use your override in Derived class
* */
