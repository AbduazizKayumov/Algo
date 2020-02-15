package syntax.`3_classes`

// Sealed classes are used to restrict class hierarchies into a single file,
// all subclasses of a sealed class must be declared in the same
sealed class Way(val width: Int) {
}

class Railway : Way(2)

// Sealed class cannot have non-private constructors, by default private
// Sealed class is abstract by itself, so it cannot be instantiated by itself
// and can have abstract members