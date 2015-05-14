def static_var(varname,value):
    print('defining wrapper')
    def decorate(func):
        print('calling wrapper')
        setattr(func,varname,value)
        return func
    return decorate

@static_var('counter',0)
def fact(n):
    fact.counter += 1
    if n<1:
        return 1
    else:
        return n * fact(n-1)

#print(fact(10))
#print(fact.counter)
