package leetcode

import kotlin.math.abs

fun shortestToChar(S: String, C: Char): IntArray {
    val ans = IntArray(S.length)
    for (i in 0 until S.length)
        ans[i] = if (S[i] == C) 0 else 10001

    for (i in 0 until S.length) {
        if (S[i] == C) {
            // walk right & left as much as possible
            // until ans[i - l] < l
            for (l in i - 1 downTo 0) {
                if (ans[l] < i - l)
                    break
                ans[l] = i - l
            }
            for (r in i + 1 until S.length){
                if (ans[r] < r - i)
                    break
                ans[r] = r - i
            }
        }
    }
    return ans
}