package leetcode

import kotlin.math.abs

fun shortestToChar(S: String, C: Char): IntArray {
    val ans = IntArray(S.length)
    val ci = C.toInt()
    for (i in 0 until S.length) {
        ans[i] = abs(S[i].toInt() - ci)
    }
    return ans
}