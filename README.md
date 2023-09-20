# dynatype
A dynamic type checker.
## What happens?
When you import the module, it silently decorates all your functions with a type checker.
## How do I use it?
Type annotate it like you would in regular Python except using the annotation object (e.g. `def f(a: dynatype.annotation(lambda x: type(x) is float or type(x) is int, lambda x: x < 0.5))`). That annotation only allows numbers less than 0.5 to be passed into the function.
## What happens when an innapropriate value is passed?
A `TypeError` is raised, allowing you to catch the error if you don't want the program to stop.
