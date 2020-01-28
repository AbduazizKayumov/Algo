package syntax.`3_classes`

// Properties in Kotlin can be either mutable (var) or read-only (val)
// In Kotlin, getter and setters are optional
// they're auto-generated for vars, vals must be initialized in constructor and does not allow setters
class Address(val id: Long) {
    var name = "Sherlock"
    var street = "Baker Street"
    var city = "London"
}


// When custom getters are defined, they're called everytime we access (just like functions)
// it allows to have a computed value
class GiftCollection {
    var size = 0
    val isEmpty: Boolean
        get() = this.size == 0
}

// If we define a custom setter for a property, it wil called everytime we assign a value to the property
class Company {
    var ceo: String
        get() = "CEO name is secret"
        set(value) {
            value.toUpperCase()
        }
}


// Normally, non-null properties must be initialized in the constructor, however, this is not convenient always
// Late initialized properties and variables
// - must be inside class declaration
// - must not be a primitive data type
class Organization {
    lateinit var name: String
    fun setOrgName(s: String) {
        this.name = s.toUpperCase()
    }

    // checking for lateinit property to be initialized
    fun getOrgName(): String {
        if (this::name.isInitialized) {
            return this.name
        }
        return ""
    }
}

// Overriding properties -> see classes and inheritance
