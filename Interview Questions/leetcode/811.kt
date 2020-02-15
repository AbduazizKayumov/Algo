package leetcode

fun subdomainVisits(cpdomains: Array<String>): List<String> {
    val map = mutableMapOf<String, Int>()
    for (domain in cpdomains) {
        val splits = domain.split(" ")
        val count = splits[0].toInt()

        if (map.containsKey(splits[1])) {
            map.put(splits[1],  map.getOrDefault(splits[1],0) + count)
        } else {
            map.put(splits[1], count)
        }

        for (i in 0 until splits[1].length) {
            if (splits[1][i] == '.') {
                val current = splits[1].substring(i + 1)
                if (map.containsKey(current)) {
                    map.put(current, map.getOrDefault(current,0) + count)
                } else {
                    map.put(current, count)
                }
            }
        }
    }
    val ans = mutableListOf<String>()
    for ((k, v) in map) {
        ans.add("$v $k")
    }
    return ans
}

fun main() {
    print(subdomainVisits(arrayOf("900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org")))
}