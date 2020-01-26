package syntax.`1_basic_types`

/*
* Double - 64 bit real number
* Float - 32 bit real number
* Long - 64 bit integer
* Int - 32 bit integer
* Short - 16 bit integer
* Byte - 8 bit integer
* Chars are not assumed to be numbers in Kotlin
* */

// Double
val d = 129319823.19283798123

// Float
val f = 12312.1232F

// Long: L is added
val l = 1231128391231911124L

// Int
val i = 123123123

// Hexadecimal
val h = 0x0F

// Binary
val b = 0b00001

// You may use _ to beatify number representations:
val one_million = 1_000_000
val creditCardNumber = 1234_5678_9012_3456L

// Operations on numbers
fun operations() {
    val a = 1250
    // shift left
    val left = a shl 2
    // shift right
    val right = a shr 2
    // unsigned shr
    val uright = a ushr 2
    // and
    val and = a and 2
    // or
    val or = a or 2
    // xor
    val xor = a xor 2
    // invert
    val inv = a.inv()
}
