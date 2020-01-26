package syntax

import java.lang.ArithmeticException
import java.lang.IllegalArgumentException
import java.lang.IllegalStateException
import kotlin.math.pow

/* Data class provides:
* - getters and setters
* - equals()
* - hashCode()
* - toString()
* - copy()
* */

data class Student(val id: Long, val name: String)

/*
* Default values in functions
* */
fun power(a: Int = 2, p: Int = 2): Int {
    return a.toDouble().pow(p).toInt()
}

/*
* Filtering a list
* */
fun filter() {
    val list = arrayOf(-11, 2, -3, 4)
    val positives = list.filter { it >= 0 }
}

/*
* Checking element presence in a list
* */
fun presence() {
    val list = arrayOf(-11, 2, -3, 5)
    val exists = 45 in list // false
}

/*
* String templates
* */
fun template() {
    val name = "Aziz"
    println("My name is $name")
}


/*
* Instance checks
* */
fun instance(a: Any) {
    when (a) {
        is Double -> {
            print("Double")
        }
        is Float -> {
            print("Float")
        }
        else -> {
        }
    }
}


/*
* Traversing a map/list of pairs
* */
fun traverse() {
    val map = hashMapOf<Int, String>()
    map[1995] = "Aziz"
    for ((k, v) in map) {
        println("key = $k, value = $v")
    }
}


/*
* Using ranges
* */
fun ranges() {
    // closed range: includes 100
    for (i in 0..100) {
    }
    // open range: does not include 100
    for (i in 0 until 100) {
    }
    // with step
    for (i in 2 until 10 step 2) {
    } // 2, 4, 6, 8
    // reverse
    for (i in 10 downTo 1) {
    }
    // exists
    if (1 in 0..10) {
    }
}


/*
* Read-only list/map
* */
fun readOnly() {
    val list = listOf("Aziz", "Laziz", "Gulsanam")
    val map = mapOf<Int, String>(1 to "Laziz", 2 to "Gulsanam", 3 to "Aziz")
    // accessing a map
    map.get(1) // String?
}


/*
* Lazy property - iniatializes in the first access
* */
fun lazy() {
    val p: String by lazy {
        // fetch from String
        "Abduaziz"
    }
}


/*
* Extension functions
* */
fun String.clearSpaces() {
    this.replace(" ", "")
}


/*
* Creating a singleton
* */
object Boss {
    val name = "Boss"
}

/*
* If not null and else shorthand
* */
fun ifnotnull() {
    var a: Int? = 12
    println(a?.toString() ?: "not defined")
    val b = a ?: throw IllegalArgumentException("Not defined")
    // execute if not null
    a?.let {
        // smth
    }
}

/*
* Return on when or if statement
* */
fun sum(a: Int, b: Int): String {
    return when (a + b) {
        100 -> "One hundred"
        else -> (a + b).toString()
    }
}

/*
* Try/catch
* */
fun trycatch() {
    val a = try {
        100 + 200
    } catch (e: ArithmeticException) {
        throw IllegalStateException(e)
    }
}


/*
* Single expression methods
* */
fun theAnswer() = 1995


/*
* With statement
* */
fun withTest() {
    val a = 1995
    with(a) {
        print(a)
        print(a + 100)
        for (i in 0 until a) {
            print(i)
        }
    }
}

/*
* Configure changes using apply
* */
fun applyTest() {
    val a = 1995
    a.apply {
        this.dec()
        this.inc()
    }
}


/*
* Swapping twwo variables
* */
fun swap() {
    var a = 1995
    var b = 2000
    a = b.also { b = a }
}
