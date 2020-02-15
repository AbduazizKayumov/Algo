package leetcode

fun relativeSortArray(arr1: IntArray, arr2: IntArray): IntArray {
    val d = mutableMapOf<Int, Int>()
    for (a in arr1) {
        if (d.containsKey(a))
            d.put(a, d.getOrDefault(a, 0) + 1)
        else
            d.put(a, 1)
    }
    val ans = arrayListOf<Int>()

    var i = 0
    for (a in arr2) {
        for (j in 0 until d.getOrDefault(a, 0)) {
            ans.add(a)
        }
        d.remove(a)
    }

    val keys = d.keys.sorted()
    for (k in keys){
        for (i in 0 until d.getOrDefault(k,0))
            ans.add(k)
    }

    return ans.toIntArray()
}

fun main() {
    val lis1 = listOf(2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19).toIntArray()
    val lis2 = listOf(2, 1, 4, 3, 9, 6).toIntArray()
    val ans = relativeSortArray(lis1, lis2)
}