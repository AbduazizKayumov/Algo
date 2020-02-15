package syntax.`2_control_flow`

/*
* For loop iterates through everything that provides iterator
* */

fun forLoopTest(){
    val arr = arrayOf(1, 2, 3)
    for (a in arr)
        print(a)

    // to iterate over a range of numbers, use range expression:
    for (i in 0 until 10) // 10 is excluded
        print(i) // 0 1 2 3 4 .. 9
    for (i in 0..10) // 10 is included
        print(i) // 0 1 2 3 4 .. 9 10

    // reverse for loop
    for (i in 10 downTo 0)
        print(i) // 10, 9, 8 .. 0
}