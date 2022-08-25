# Data classes (classes with all data and no behavior) are meant to short--single use objects
# if a data class becomes used all over the code base, it's likely it's not being designed correctly.

# Data class as scaffolding 
# when imperimenting, it's okay to have a data class which is 
# temporary and it's meant to be expandeded later

# Data Class as Intermediate Representation
# it's also okay to use data class as an intermediate form
# when transfering from one from to another, but data should not be 
# changed while in the intermediate form
