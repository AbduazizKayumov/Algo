package syntax.`3_classes`

// Kotlin provides the ability to extend from a class without having to inherit from the class
// This is called Extensions: can be methods or properties
fun String.replaceSpacesWith(c: Char): String {
    return this.replace(' ', c)
}

// Nullable receiver
fun Int?.toString(): String {
    if (this == null) return ""
    return this.toString()
}

// Kotlin allows to have extension properties
val String.lowercase_letters: Int
    get() {
        // todo: count lowercase letters
        return 0
    }
// but, extension properties can not be set:
// ERROR: val String.uppercase_letters: Int = 0

// private extension has access to the other private declarations in the same file