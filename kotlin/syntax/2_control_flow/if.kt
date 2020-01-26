package syntax.`2_control_flow`

/*
* In Kotlin, if is an expression, it returns a value, so there is no need for ternary operator,
* since ordinary if+else works fine in this role
* */
fun max(a: Int, b: Int): Int {
    return if (a > b) {
        print(a)
        a
    } else {
        print(b)
        b
    }
}