package leetcode

fun divisorGame(N: Int): Boolean {
    val dp = BooleanArray(1001)
    for (i in 1 until N + 1) {
        for (x in 1 until i / 2 + 1) {
            if (i % x == 0) {
                dp[i] = dp[i] or !dp[i - x]
            }
        }
    }
    return dp[N]
}

// that fucking one-liner
// fun divisorGame(N: Int) = N % 2 == 0

fun main() {
    println(divisorGame(2))
    println(divisorGame(3))
    println(divisorGame(4))
}