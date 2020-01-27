package leetcode

fun numUniqueEmails(emails: Array<String>): Int {
    val set = HashSet<String>()
    var ans = 0
    for (email in emails) {
        val splits = email.split('@')
        val domain = splits[1]
        val local = splits[0]

        var loc = ""
        for (c in local) {
            if (c == '+') {
                break
            }
            if (c != '.') {
                loc += c
            }
        }

        val res = loc + "@" + domain
        if (!set.contains(res)) {
            ans++
            set.add(res)
        }
    }
    return ans
}


fun main() {
    numUniqueEmails(arrayOf(
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"))
}