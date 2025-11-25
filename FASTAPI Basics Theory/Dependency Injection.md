What is Dependency Injection?

Dependency Injection is instead of creating objects or resources inside a function, we ask FastAPI to give (inject) them to the function automatically.



Why Do We Use Dependency Injection?



1.Code reusability

2.Cleaner functions

3.Automatic handling of shared logic

4.Avoiding repetition

5.Easier testing



Real-Life Example:

Imagine a function needs:



* a database connection
* a token
* a common calculation
* a config value



Instead of writing it inside every endpoint, you create one function for it.

FastAPI will inject it wherever needed automatically.

