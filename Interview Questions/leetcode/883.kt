package leetcode

fun projectionArea(grid: Array<IntArray>): Int {
    var xy = 0
    var xz = 0
    var yz = arrayListOf<Int>()
    for (i in 0 until grid.size) {
        var max = 0
        for (j in 0 until grid[i].size) {
            if (grid[i][j] > max)
                max = grid[i][j]

            if (grid[i][j] != 0)
                xy += 1

            if (j < yz.size) {
                if (yz[j] < grid[i][j])
                    yz[j] = grid[i][j]
            } else {
                yz.add(grid[i][j])
            }
        }
        xz += max
    }

    return xy + xz + yz.sum()
}