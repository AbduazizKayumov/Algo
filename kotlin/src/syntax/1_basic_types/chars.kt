package syntax.`1_basic_types`

import java.lang.IllegalArgumentException

/* Chars are represented by the type Char, they can't be treated directly as numbers
* Chars literals go in a single quotes: 'a', '1'
* Special chars can be escaped using a backslash: '\n', '\t' '\b'
* */

fun decimalDigitValue(c: Char): Int {
    if (c !in '0'..'9')
        throw IllegalArgumentException("Out of range")
    return c.toInt()
}