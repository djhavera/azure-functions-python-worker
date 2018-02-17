import abc
import typing


class Out(abc.ABC):

    @abc.abstractmethod
    def set(self):
        pass


class Context(abc.ABC):

    @property
    @abc.abstractmethod
    def invocation_id(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def function_name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def function_directory(self) -> str:
        pass


class TypedData(abc.ABC):
    pass


class HttpRequest(TypedData):

    @property
    @abc.abstractmethod
    def method(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def url(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def headers(self) -> typing.Mapping[str, str]:
        pass

    @property
    @abc.abstractmethod
    def params(self) -> typing.Mapping[str, str]:
        pass

    def get_body(self) -> TypedData:
        pass


class HttpResponse(TypedData):

    @property
    @abc.abstractmethod
    def status_code(self):
        pass

    @property
    @abc.abstractmethod
    def headers(self):
        pass

    def set_body(self, body: TypedData):
        pass