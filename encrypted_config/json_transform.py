"""Transforming JSON."""

import abc
import functools
import typing as t


def json_coordinate(
        data: t.Union[str, list, dict], coordinate: str, parent: bool = False) -> t.Tuple[
            t.Callable[[], t.Any], t.Callable[[t.Any], None]]:
    assert coordinate
    parts = coordinate.split('.')

    def getter(container, key) -> t.Any:
        if key is None:
            return container
        return container[key]
    getter_ = functools.partial(getter, container=data, key=None)

    def setter(value, container, key) -> None:
        container[key] = value
    setter_ = functools.partial(setter, container=data, key=None)

    if parent:
        last_part = parts[-1]
        try:
            last_part = int(last_part)
        except ValueError:
            pass
        parts = parts[:-1]

    for part in parts:
        try:
            part = int(part)
        except ValueError:
            pass
        getter_ = functools.partial(getter, container=data, key=part)
        setter_ = functools.partial(setter, container=data, key=part)
        data = data[part]

    if parent:
        setter_ = last_part

    return getter_, setter_


class JSONTransformer(metaclass=abc.ABCMeta):

    """Transform JSON."""

    def __init__(self):
        pass

    def transform(self, data: t.Any) -> t.Any:
        transformed_data = self.transform_value(data)
        return transformed_data

    def transform_value(self, data: t.Union[str, list, dict]) -> t.Union[str, list, dict]:
        if isinstance(data, str):
            return self.transform_str(data)
        if isinstance(data, list):
            return self.transform_list(data)
        if isinstance(data, dict):
            return self.transform_dict(data)
        return data

    @abc.abstractmethod
    def transform_dict(self, data: dict) -> dict:
        assert isinstance(data, dict), type(data)
        return data

    # @abc.abstractmethod
    def transform_list(self, data: list) -> list:
        assert isinstance(data, list), type(data)
        # return data
        # data = super().transform_list(data)
        transformed = type(data)()
        for value in data:
            transformed.append(self.transform_value(value))
        return transformed

    @abc.abstractmethod
    def transform_str(self, data: str) -> str:
        assert isinstance(data, str), type(data)
        return data
