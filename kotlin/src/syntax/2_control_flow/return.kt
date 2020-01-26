package syntax.`2_control_flow`

/*
* By default, returns from the nearest functions
* it can access to labelled functions
* */

fun testReturn() {
    var arr = arrayOf(1, 2, 3, 4)
    arr.forEach inner@{
        if (it == 3)
            return
        print(it)
    }
    // 1 2 4
}