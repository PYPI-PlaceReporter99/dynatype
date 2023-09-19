import types
import functools
import inspect
class annotation(object):
    def __init__(self, *conditions: types.FunctionType | types.LambdaType) -> None:
        self.checkfunc = lambda x: all(y(x) for y in conditions)
    @staticmethod
    def typecheckdecor(function: types.FunctionType | types.LambdaType) -> types.FunctionType:
        @functools.wraps(function)
        def inner_function(*args, **kwargs):
            arg_dict = inspect.signature(function).bind(*args, **kwargs).arguments
            arg_annotations = dict((x, function.__annotations__[x] if x in function.__annotations__ else annotation()) for x in arg_dict)
            for x in arg_annotations.values():
                if type(x) is not annotation:
                    raise TypeError("Annotation has to be instance of class 'annotation'. If using a type object, replace with annotation(lambda x: issubclass(type(x), t)) where t is the original type object.") from None
            for x in arg_dict:
                if not arg_annotations[x].checkfunc(arg_dict[x]):
                    raise TypeError(f"Type checking for argument {x!r} failed. Note that annotations for * and ** arguments work differently for mypy.") from None
            return function(*args, **kwargs)
        return inner_function

import __main__

for x in dir(__main__):  # Not using a main guard because this code should run even if it's not the main script.
  f = getattr(__main__, x)
  if type(f) is types.FunctionType:
    setattr(__main__, x, annotation.typecheckdecor(f))
    
