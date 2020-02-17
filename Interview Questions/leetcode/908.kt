class Solution {
    fun min(a: Int, b: Int): Int {
        return if (a > b) b else a
    }

    fun max(a: Int, b: Int): Int{
        return if (a > b) a else b
    }

    fun abs(a: Int): Int {
        return if (a < 0) -a else a
    }

    fun smallestRangeI(A: IntArray, K: Int): Int {
        var mn = A[0]
        var mx = A[0]
        for (a in A){
            mn = min(mn, a)
            mx = max(mx, a)
        }
        return max(0, mx - mn - 2*K)
    }
}