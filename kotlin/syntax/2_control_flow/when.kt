package syntax.`2_control_flow`

import kotlin.math.abs

/*
* When replaces the switch operator in C-like languages
* */

fun whenTest() {
    val a = 100
    when (a) {
        1 -> print("one")
        2 -> print("two")
        else -> {
            print("Who knows?")
        }
    }

    // ranges can be used
    when (a) {
        in 80..100 -> print("From 80 to 100")
        1, 2 -> print("1 or 2")
        abs(-30) -> print("30") // not only constants
    }
}

// checking object type with is
fun check(a: Any): Int {
    return when (a) {
        is Int -> a + 100
        is Float -> a.toInt() + 100
        else -> 0
    }
}

// replacement for if-else
fun replaceIfElse() {
    val a = 100
    when {
        a % 2 == 0 -> print("a is even")
        else -> print("a is odd")
    }
}