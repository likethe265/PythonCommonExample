class Sample:
    def __enter__(self):
        return self #return value will be passed to variable after 'as' keyword

    def __exit__(self, type, value, trace): # will catch every error even an exception happen in the mid-way
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        bar = 1 / 0
        print('after the error')
        return bar + 10


with Sample() as sample:
    sample.do_something()
print("I'll not going to be shown because of error")

# 'with as' statement is used to do some init and post processing for a class to simplify the code
# 'with as' can catch exception init __exit__ but the programe will stop. This is quite different with try catch.