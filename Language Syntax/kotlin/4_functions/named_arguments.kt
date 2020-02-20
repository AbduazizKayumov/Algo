// Named arguments
// When a funtion has high number of parameters, a functions call would not readable:
fun reformat(s: String,
             normalizeCase: Boolean = false,
             upperCaseFirstLetter: Boolean = false,
             replaceSpacesWith: Char = ' '){

}

// Simple function call is:
reformat(str, true, true, true, '_')

// However, with named arguments, readability is much better:
reformat(str,
         normalizeCase = true,
         upperCaseFirstLetter = true,
         replaceSpacesWith = '_')


