def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{0}]: enter function {1}()".format(level, func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging('INFO')
def say(something):
    print("say {}!".format(something))

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging('DEBUG')
def do(something):
    print("do {}...".format(something))

if __name__ == '__main__':
    say('hello')
    do("my work")