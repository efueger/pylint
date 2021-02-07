"""Test PEP 604 - Alternative Union syntax
without postponed evaluation of annotations.

For Python 3.7 - 3.9: Everything should fail.
Testing only 3.8/3.9 to support TypedDict.
"""
# pylint: disable=missing-function-docstring,unused-argument,invalid-name,missing-class-docstring,inherit-non-class,too-few-public-methods,line-too-long
import dataclasses
import typing
from dataclasses import dataclass
from typing import NamedTuple, TypedDict


Alias = str | typing.List[int]  # [unsupported-binary-operation]
lst = [typing.Dict[str, int] | None,]  # [unsupported-binary-operation]

cast_var = 1
cast_var = typing.cast(str | int, cast_var)  # [unsupported-binary-operation]

T = typing.TypeVar("T", int | str, bool)  # [unsupported-binary-operation]

(lambda x: 2)(int | str)  # [unsupported-binary-operation]

var: str | int  # [unsupported-binary-operation]

def func(arg: int | str):  # [unsupported-binary-operation]
    pass

def func2() -> int | str:  # [unsupported-binary-operation]
    pass

class CustomCls(int):
    pass

Alias2 = CustomCls |  str  # [unsupported-binary-operation]

var2 = CustomCls(1) | int(2)


# Check typing.NamedTuple
CustomNamedTuple = typing.NamedTuple(
    "CustomNamedTuple", [("my_var", int | str)])  # [unsupported-binary-operation]

class CustomNamedTuple2(NamedTuple):
    my_var: int | str  # [unsupported-binary-operation]

class CustomNamedTuple3(typing.NamedTuple):
    my_var: int | str  # [unsupported-binary-operation]


# Check typing.TypedDict
CustomTypedDict = TypedDict("CustomTypedDict", my_var=int | str)  # [unsupported-binary-operation]

CustomTypedDict2 = TypedDict("CustomTypedDict2", {"my_var": int | str})  # [unsupported-binary-operation]

class CustomTypedDict3(TypedDict):
    my_var: int | str  # [unsupported-binary-operation]

class CustomTypedDict4(typing.TypedDict):
    my_var: int | str  # [unsupported-binary-operation]


# Check dataclasses
def my_decorator(*args, **kwargs):
    def wraps(*args, **kwargs):
        pass
    return wraps

@dataclass
class CustomDataClass:
    my_var: int | str  # [unsupported-binary-operation]

@dataclasses.dataclass
class CustomDataClass2:
    my_var: int | str  # [unsupported-binary-operation]

@dataclass()
class CustomDataClass3:
    my_var: int | str  # [unsupported-binary-operation]

@my_decorator
@dataclasses.dataclass
class CustomDataClass4:
    my_var: int | str  # [unsupported-binary-operation]