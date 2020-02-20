// Variable number of args can passed using keyword 'vararg':
fun foo(vararg ids: Long){
    ids // is a LongArray
}


// Only one parameter can marked with vararg(usually the last one),
// if there are other parameters, values can be passed using the named argument syntax
fun foo(a: Int, b: String, vararg ids: Long){ ... }
foo(a = 1, b = "Aziz", *arrayOf(1L, 2L, 3L))