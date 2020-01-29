package syntax.`3_classes`

// Classes can be nested in other classes:
class Outer1 {
    var a = 0

    class Inner {
        fun foo() {
            // cannot access a
        }
    }
}

// Inner classes can access outer class properties
// Inner classes carry references to its outer class
class Outer2 {
    private var a = 1

    inner class Inner {
        private var a = 2
        fun foo() {
            print(this@Outer2.a)
            print(this.a)
        }
    }
}

// Anonymous inner classes
// Anon. inner classes are created using object expression:
class AutoTextView {
    private var length = 0
    private var clickListener: ClickListener? = null
    fun addClickListener(clickListener: ClickListener){
        this.clickListener = clickListener
    }
}

interface ClickListener {
    fun onClick()
}

fun anonInnerTest() {
    val atv = AutoTextView()
    atv.addClickListener(object : ClickListener {
        override fun onClick() {

        }
    })
}


