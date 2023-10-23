
    
   
def new_function(function):
    def internal_funciton():
        print("hi")
        function()
        print("bye")
    return internal_funciton()

#lol = new_function(lol)


@new_function
def lol():
    print("middle")

lol()