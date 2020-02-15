package syntax.`2_control_flow`

/*
* While and do-while works as usual
* */
fun testWhile() {
    var a = 10
    while (a > 0) {
        print(a)
        a--
    }

    a = 10
    do {
        print(a)
        a--
    } while (a > 0)
}