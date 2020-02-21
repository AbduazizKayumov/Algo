// Using a higher order functions imposes certain runtime penalties: each function is an object,
// and it captures a closure -> those variables that are accessed in the body of the function.
// Memory allocations (both for function objects and classes) and virtual calls introduce runtime overhead
// To make the compiler do this, we need to mark a fucntion with the inline modifier:
inline fun <T> lock(lock: Lock, body: () -> T): T {
    ...
}

// The inline modifier affects both the function itself and the lambdas passed to it: all of those will be
// inlined into the call site
// Inlining may cause the generated code to grow, however, if we do it in a reasonable way (ex. avoid inlining large funcs)
// it will pay off in performance, especially at call sites inside loops

// In case, you want only some of the lambdas passed to an inline function to be inlined, 'noinline' modifier is used:
inline fun foo(inlined: () -> Unit, noinline notInlined: () -> Unit)


// Some inline functions may need to call the lambdas passed to them as params not directly from the function body,
// but from another execution context, such as a local object or a nested function, in such cases, the lambda parameter
// must be marked with the crossinline modifier:
inline fun f(crossinline body: () -> Unit){
    val f = object : Runnable {
        override fun run(){
            body()
        }
    }
}
