package syntax.`3_classes`

// The main purpose of creating classes is to hold data, in Kotlin, data classes provides with
// standard functionality and utility functions that are automatically derived
data class User(val id: Long, var name: String)
// The compiler automatically derives the following functions:
// - equals() and hashCode()
// - toString() "User(id=32,name=Aziz)"
// - copy() functions
// - componentN() functions corresponding to their order of declarations in the primary constructor

// To ensure consistency, data class have to fulfill the following requirements:
// - the primary constructor with at least one parameter with val or var
// - cannot be abstract, open, sealed or inner

// it is often the case that we need t change some properties of an object and copy:
fun copyTest() {
    val u1 = User(1, "Aziz")
    val u2 = u1.copy(id = 2)
}