def greet(fx):
    def mfx():
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")


hello()