from abc import ABC, abstractmethod


class IDispatcher(ABC):
    @abstractmethod
    def dispatch(self, object):
        ...

class A(IDispatcher):
    def dispatch(self, object):
        ...

class B(IDispatcher):
    def dispatch(self):
        ...

class C(IDispatcher):
    ...

def foo(a: IDispatcher):
    ...

foo(A())
foo(B())
foo(C())
