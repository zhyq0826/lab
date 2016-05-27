import functools
import inspect


def action(func):
    @functools.wraps
    def wrapper(*args, **kwargs):
        return func()

    return wrapper


def register(state):
    def outwrapper(func):
        state.register(func)
        @functools.wraps
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    return outwrapper


class CallFuncAsAttr(object):

    class __CallObject(object):

        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)

    def __init__(self):
        setattr(self, self.__name, {})

    @property
    def __get_func(self):
        return getattr(self, self.__name)

    @property
    def __name(self):
        return 'state_%s'%id(self)        

    def register(self, func):
        if not inspect.isfunction(func):
            raise TypeError("argument expect function, now is '%s'"%func)

        name = func.func_name
        if name == (lambda x:x).func_name:
            raise TypeError('lambda is not allowed')

        self.__get_func[name] = self.__CallObject(func)

    def __getattr__(self, name):
        if name not in self.__get_func:
            raise AttributeError("state object has no attribute '%s'"%name)

        return self.__get_func[name]


class State(CallFuncAsAttr):
    pass


class Mutation(CallFuncAsAttr):
    pass


if __name__ == '__main__':
    import random
    state = State()

    @register(state)
    def order_status(_id):
        return random.choice(['0', '1'])

    print state.order_status('asd')

