package syntax.`2_control_flow`

/*
* By default:
* - break terminates the nearest enclosing loop
* - continue skips the nearest enclosing loop
* Besides, they can be labeled to access the labelled
* */

fun testBreakContinue() {
    for (i in 0 until 10) {
        print(i)
        if (i % 2 == 0)
            continue
        if (i == 5)
            break
    }


    outer@ for (i in 0 until 100) {
        inner@ for (j in 0 until 100) {
            print(j)
            if (j == 50)
                break@outer
        }
    }
}