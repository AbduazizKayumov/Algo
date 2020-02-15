package leetcode

fun numRookCaptures(board: Array<CharArray>): Int {
    val BOARD_SIZE = 8
    var x = 0
    var y = 0
    // find the rook
    outer@ for (i in 0 until BOARD_SIZE) {
        for (j in 0 until board[i].size) {
            if (board[i][j] == 'R') {
                x = i
                y = j
                break@outer
            }
        }
    }
    println(x.toString() + " " + y)
    var ans = 0
    // move left
    for (i in y downTo 0) {
        if (board[x][i] == 'B') break
        if (board[x][i] == 'p') {
            ans += 1
            break
        }
    }
    // move right
    for (i in y until BOARD_SIZE) {
        if (board[x][i] == 'B') break
        if (board[x][i] == 'p') {
            ans += 1
            break
        }
    }
    // move up
    for (i in x downTo 0) {
        if (board[i][y] == 'B') break
        if (board[i][y] == 'p') {
            ans += 1
            break
        }
    }
    // move down
    for (i in x until BOARD_SIZE) {
        if (board[i][y] == 'B') break
        if (board[i][y] == 'p') {
            ans += 1
            break
        }
    }
    return ans
}