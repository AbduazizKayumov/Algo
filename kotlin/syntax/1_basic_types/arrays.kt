package syntax.`1_basic_types`

/*
* Arrays are represented by the Arrays class, has getter and setter functions ([] by oper. overloading) and size
* To create an array, we can use arrayOf() library function and pass the item values to it
* */
val a = arrayOf(1, 2, 3)

// arrayOfNulls(size) function can be used to create an array with size and filled with null values
val bb = arrayOfNulls<Int>(10)

// alternatively, use Array constructor:
val c = Array(5) { i -> (i * i).toString() } // ["0","1","4","9","16"]

// primitive type arrays
val int_arr = intArrayOf(2, 3, 4, 5)
val flo_arr = floatArrayOf(3F, 4F, 5F, 6F)
val sho_arr = shortArrayOf(1, 2, 3, 4)
val lon_arr = longArrayOf(1L, 2L, 3L, 4L, 5L)
