package leetcode

fun canPlaceFlowers(f: IntArray, n: Int): Boolean {
    var weCanPlant = 0
    for (i in 0 until f.size) {
        if (f[i] == 1) continue
        var left = true
        if (i - 1 >= 0 && f[i - 1] == 1) {
            left = false
        }
        var right = true
        if (i + 1 < f.size && f[i + 1] == 1) {
            right = false
        }
        if (left && right) {
            f[i] = 1
            weCanPlant += 1
        }
    }
    return n <= weCanPlant
}

fun main() {
    val inp = listOf(0, 0, 1, 0, 0)
    val ans = canPlaceFlowers(inp.toIntArray(), 2)
    print(ans)
}