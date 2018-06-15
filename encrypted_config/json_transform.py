"""Transforming JSON."""

import typing as t


class JSONTransformer:

    """Transform JSON."""

    def transform(self, data: t.Union[str, list, dict]) -> t.Union[str, list, dict]:
        if isinstance(data, str):
            return self.transform_str(data)
        if isinstance(data, list):
            return self.transform_list(data)
        if isinstance(data, dict):
            return self.transform_dict(data)
        return data

    def transform_dict(self, data: dict) -> dict:
        assert isinstance(data, dict), type(data)
        return data

    def transform_list(self, data: list) -> list:
        assert isinstance(data, dict), type(data)
        return data

    def transform_str(self, data: str) -> str:
        assert isinstance(data, str), type(data)
        return data

    def transform_value(self, data: t.Any) -> t.Any:
        return data
