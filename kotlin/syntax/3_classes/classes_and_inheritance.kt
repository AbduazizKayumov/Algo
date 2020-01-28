package syntax.`3_classes`

// Classes are declared using 'class' keyword
class Person {}

/* The class declaration consists of:
* - the class name
* - the class header (type params, primary constructor)
* - the class body surrounded by curly braces {}
* */
class Empty

/*
* Constructors
* A class in Kotlin can have a primary constructor and several other secondary constructors
* The primary constructor is part of the class header, it goes after the class name
* */
class Student constructor(val name: String)

// constructor keyword can be omitted:
class PHDStudent(val name: String)

/*
* The primary constructor cannot contain any code, initializations can be places in init blocks
* The properties in primary constuctor can be mutable(var) or immutable(val)
* */
class MSStudent(val name: String) {
    val grade: Int

    init {
        grade = 5
    }
}

/*
* If the constructor has annotations or visibility modifiers, constructor keyword is required
* */
class Customer public constructor(val name: String)


/*
* Secondary constructors
* If a class has secondary constructor, each secondary constructor need to delegate to the primary constructor
* */
open class Node(val value: Int) {
    var children = mutableListOf<Node>()

    constructor(value: Int, parent: Node) : this(value) {
        parent.children.add(this)
    }
}

/*
* Creating instances of classes
* Note that Kotlin does not have 'new' keyword
* */
val customer = Customer("Aziz")


/*
* Class members
* Classes can contain:
* - constructors and init blocks
* - functions
* - properties
* - nested and inner classes
* - object declarations
* */

/*
* Inheritance
* All classes in Kotlin have a common superclass Any, that is a default superclass for a class with
* no super type declared
* */
class Example // extends Any

/*
* If the superclass has a primary constructor, the base-class must be initialized right there, using the params
* of the primary constructor
* */
open class Base(p: Int)

class Derived(p: Int) : Base(p)

/*
* If the base class has no primary constructor, each secondary constructor must initialize
* the base type with super() keyword
* */
open class View {
    constructor(ctx: Int)
    constructor(ctx: Int, attr: String)
}

class TextView : View {
    constructor(ctx: Int) : super(ctx)
    constructor(ctx: Int, attr: String) : super(ctx, attr)
}

/*
* Overriding functions
* The base class must declare which of its functions can be overridden
* */
open class Shape {
    open fun draw(x: Int) {}
    fun fill() {}
}

class Circle : Shape() {
    override fun draw(x: Int) {
        super.draw(x)
        print("Circle")
    }
}

/*
* The override keyword is open itself, if you want to restrict it to be overridden, make it final
* */
open class Rectangle : Shape() {
    final override fun draw(x: Int) {
        super.draw(x)
        print("Rect")
    }

    fun drawPlz() {}
}

/*
* Overriding properties works the same way as functions
* You can also override val properties and change its modifier to var, but not vice-versa
* */

/*
* Inside an inner class, accessing the superclass of the outer class with super@outer
* */
class FilledRectangle : Rectangle() {
    fun draw() {}
    inner class Filler {
        fun fill() {}
        fun drawAndFill() {
            super@FilledRectangle.drawPlz()
            fill()
        }
    }
}


/*
* If the derived class extends multiple classes, calling super class functions is done with:
* */
open class Rect {
    open fun draw() {}
}

interface Polygon {
    open fun draw() {}
}

class Square : Rect(), Polygon {
    override fun draw() {
        super<Rect>.draw()
        super<Polygon>.draw()
    }
}

/*
* Abstract classes
* A class or some of its members can be declared abstract, an abstract member does not have implementation
* */
open class Animal {
    open fun run() {}
}

abstract class Dog : Animal() {
    override abstract fun run()
}
