from multiprocessing.pool import ThreadPool
from multiprocessing.context import TimeoutError


class TIMEOUT_EXCEPTION(Exception):
    """function run timeout"""
    pass


def timeout(seconds, exception=TIMEOUT_EXCEPTION):
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

        _.__name__ = func.__name__
        _.__doc__ = func.__doc__
        return _

    return timeout_decorator
