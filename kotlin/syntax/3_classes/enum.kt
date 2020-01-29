package syntax.`3_classes`

// The most basic usage of enums
// Each enum constant is an object, enum constants are separated by commas
enum class Direction {
    NORTH, EAST, SOUTH, WEST
}

// Since each enum is an instance of the enum class, they can be initialized as:
enum class Color(val rgb: Int) {
    RED(0xFF0000),
    GREEN(0x00FF00),
    BLUE(0x0000FF)
}

// Enum classes can have abstract methods, and each enum constants are required to implement them
// Enum classes methods are separated using semicolons ';' :
enum class NextMove {
    TO_NORTH {
        override fun move() {
            y += y + 1
        }
    };

    var x = 0
    var y = 0
    open fun move() {}
}

// Enum classes may implement from interfaces
interface Move {
    fun walk() {}
    fun run() {}
    fun fly() {}
}

enum class Robot : Move {
    DOG {
        override fun walk() {

        }

        override fun run() {

        }
    },
    BIRD {
        override fun fly() {

        }

        override fun run() {

        }

        override fun walk() {

        }
    },
    TOURTOISE {
        override fun walk() {

        }
    }
}

// Every enum constant has properties to obtain its name and position
fun enumTest() {
    Direction.EAST.name
    Direction.EAST.ordinal // declaration order
}