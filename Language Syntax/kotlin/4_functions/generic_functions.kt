// Functions can have generic types
// They're specified using angle brackets <> before the function name:
fun <T> makeList(a: T, b: T): List<T> {
    return listOf(a, b)
}