from multiprocessing.pool import ThreadPool
from multiprocessing.context import TimeoutError
from secreepy.exceptions import TooLongException
import time


def timeout(seconds, exception=TooLongException):
    def timeout_decorator(func):
        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        def _(*args, **kwargs):
            result = []

            pool = ThreadPool(1)
            try:
                pool.apply_async(_new_func, args=(func, result, args, kwargs)).get(timeout=seconds)
            except TimeoutError:
                raise exception('function run too long, timeout %d seconds.' % seconds)

            return result[0]

        return _

    return timeout_decorator


def repeat(exception=Exception, attempts=1, action=None, pass_self=False):
    def repeat_decorator(func):
        def _(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    if i + 1 == attempts:
                        raise e
                    if action is not None:
                        if pass_self:
                            self = args[0]
                            action(self)
                        else:
                            action()

        return _

    return repeat_decorator
