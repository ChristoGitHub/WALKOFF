from functools import wraps

from walkoff.core.actionresult import ActionResult
from walkoff.helpers import get_function_arg_names
from walkoff.appgateway.walkofftag import WalkoffTag


def format_result(result):
    if not isinstance(result, tuple):
        return ActionResult(result, None)
    else:
        return ActionResult(*result)


def tag(func, tag_name):
    setattr(func, tag_name, True)


def action(func):
    """
    Decorator used to tag a method or function as an action

    Args:
        func (func): Function to tag
    Returns:
        (func) Tagged function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return format_result(func(*args, **kwargs))
    WalkoffTag.action.tag(wrapper)
    wrapper.__arg_names = get_function_arg_names(func)
    return wrapper


def condition(func):
    """
    Decorator used to tag a method or function as a condition

    Args:
        func (func): Function to tag
    Returns:
        (func) Tagged function
    """
    WalkoffTag.condition.tag(func)
    return func


def transform(func):
    """
    Decorator used to tag a method or function as a transform

    Args:
        func (func): Function to tag
    Returns:
        (func) Tagged function
    """
    WalkoffTag.transform.tag(func)
    return func
