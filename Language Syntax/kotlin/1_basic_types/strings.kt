package syntax.`1_basic_types`

import kotlin.math.abs

// Strings are represented by the type String, Strings are immutable e.g. s[0] = '1' does not work
fun stringTest() {
    var s = "hello"
    // s[0] = '12' ERROR
    s = "asdas"

    for (c in s)
        print(c)

    s = "hello" + 1


    // raw strings
    val t = """
        for (c in "hello")
            println(c)
    """.trimIndent()


    // string templates
    val a = 1995
    println("I was born in $a")
    println("I was born in ${abs(a)}")
}