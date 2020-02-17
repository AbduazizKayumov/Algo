class Solution {

    fun min(a: Int, b: Int): Int {
        return if (a > b) b else a
    }

    fun abs(a: Int): Int {
        return if (a < 0) -a else a
    }

    fun smallestRangeI(A: IntArray, K: Int): Int {

        // find sum
        var sum = 0
        for (a in A)
            sum += a

        // find the average
        val aver = sum / A.size

        // try to make every A[i] closer to aver
        for (i in 0 until A.size) {
            if (A[i] == aver) continue
            if (A[i] > aver) {
                A[i] += min(-K, aver - A[i])
            } else {
                A[i] += min(K, aver - A[i])
            }
        }
        var ans = 0
        for (i in 0 until A.size) {
            if (abs(A[i]-aver) > ans)
                ans = abs(A[i] - aver)
        }
        return ans
    }
}