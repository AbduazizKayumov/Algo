// In Kotlin, we don't need to create a class to hold a function
// Functions can be declared at top level
fun add(a: Int, b: Int) {...}
class A{
    fun foo(){
        add(12, 15)
    }
}

// Local functions
// Function can have local functions -> a function inside another function
// Local functions can access local variables of outer function
fun dfs(graph: Graph){
    val visited = HashSet<Vertex>()
    fun dfs(current: Vertex){
        if (!visited.add(current)) return
        for (v in current.neighbors){
            dfs(v)
        }
    }
    dfs(graph.vertices[0])
}


