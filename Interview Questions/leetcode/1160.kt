package leetcode


fun isSubsequence(a: String, s: String, m: Int, n: Int): Boolean {
    if (n < m)
        return false
    if (n < 0)
        return true
    if (m < 0)
        return true

    if (a[m] == s[n]) {
        return isSubsequence(a, s, m - 1, n - 1)
    }

    return isSubsequence(a, s, m, n - 1)
}


fun countCharacters(words: Array<String>, c: String): Int {
    var ans = 0
    var s = c.toCharArray().sorted().joinToString("")
    for (w in words) {
        if (isSubsequence(w.toCharArray().sorted().joinToString(""), s, w.length - 1, c.length - 1)) {
            ans += w.length
        }
    }
    return ans
}