def announce(f):
    def wrapper():
        print("About to runn the function")
        f()
        print("done running the function")
        return wrapper
    
    @announce
    def hello_func(Egele):
        print (f'Hello {Egele}')
        
    hello_func()