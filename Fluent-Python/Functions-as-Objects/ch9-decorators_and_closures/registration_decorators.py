# how are decorators used in real code
## The decorator function is defined in the same module as the 
## decorated functions. A real decorator is usually defined in 
## one module and applied to functions in other modules.
## The register decorator returns the same function passed as an 
## argument. In practice, most decorators define an inner function 
## and return it.