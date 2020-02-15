package syntax.`3_classes`

// Using types alieases, we can provide different type names (usualy, shorter ones) to long types:
class ClassNameWithVeryLongName(val id: Long) {
    fun printid() {
        println(id)
    }
}

typealias Jim = ClassNameWithVeryLongName

fun typealiasTest() {
    val c = Jim(1995)
    c.printid()
}

// Type aliases do not introduce new types, they're equivalent to the existing ones