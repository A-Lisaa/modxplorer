from typing import Protocol


class DispatcherProtocol(Protocol):
    def dispatch(self, object):
        ...

class A:
    def dispatch(self, object):
        ...

class B:
    def dispatch(self):
        ...

class C:
    ...

def foo(a: DispatcherProtocol):
    ...

foo(A())
foo(B())
foo(C())

