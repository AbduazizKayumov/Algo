/*
* Delegation standards
* */

/*
* lazy()
* lazy is a function that takes a lambda and returns an instance of Lazy<T> which can serve as a delegate
* for implementing a lazy property: the first call to get() needs to be computed and remembered, the next calls to get()
* will return the remembered property
* */

val lazyString: String by lazy {
    println("Computed")
    "Hello, lazy!"
}

println(lazyString) // Computed and "Hello, Lazy!"
println(lazyString) // Hello, Lazy!