package syntax.`3_classes`

// Sometimes we need to create an object of some class without declaring it as subclass
// Kotlin handes this using object expressions
object Retrofit {
    fun connect(url: String) {}
}

// The code in object expressions can access variables from the enclosing scope
fun bindData() {
    var counter = 0
    object : ClickListener {
        override fun onClick() {
            counter += 1
        }
    }
}

// Singleton may be useful in several cases:
object RetrofitProvider {

    var retrofit: C? = null
    fun provideRetrofit(): C {
        if (retrofit == null) {
            retrofit = C()
        }
        return retrofit!!
    }
}

// Object declaration in inside a class can be marked with companion keyword:
class SettingsFragment {
    companion object {
        fun nightTheme(): SettingsFragment {
            return SettingsFragment().apply {
                themeId = 0L
            }
        }
    }

    var themeId = 0L
}