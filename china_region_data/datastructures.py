import os
import json
from typing import List, Dict, Tuple, Any, Optional, Union, NoReturn

__all__ = ["Region"]


class RegionError(Exception):
    pass


class RegionNotFoundError(RegionError):
    pass


class RegionNoSuperiorError(RegionError):
    pass


class RegionNoSubordinateError(RegionError):
    pass


with open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
) as file:
    # 地区数据
    REGION_DATA: List[Dict[str, str]] = json.load(file)


class SingletonRegion(type):
    def __init__(
        cls, name: str, bases: Tuple[type], namespace: Dict[str, Any],
    ) -> None:
        cls.instances: Dict[str, Region] = {}
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs) -> Any:
        if kwargs:
            raise TypeError("Keyword argument not allowed.")

        key = args[0]
        if key not in cls.instances:
            try:
                instance = super().__call__(*args, **kwargs)
            except AssertionError:
                raise RegionNotFoundError("No such region.") from None
            for _key in args:
                cls.instances[_key] = instance
        return cls.instances[key]


class Region(metaclass=SingletonRegion):
    def __init__(self, code: str = "", name: str = "", **kwargs) -> None:
        assert name and isinstance(name, str)
        assert code and isinstance(code, str)

        self.code = code
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Region):
            return NotImplemented
        return self.code == other.code

    def __contains__(self, other: object) -> bool:
        if not isinstance(other, Region):
            return NotImplemented
        return other in self.下级行政区域

    @property
    def 行政级别(self) -> int:
        """
        1. 省、直辖市、自治区
        2. 市、省直辖县
        3. 县、县级市、直辖市区
        """
        if self.code.endswith("00"):
            if self.code.endswith("0000"):
                return 1
            return 2
        else:
            return 3

    @property
    def 上级行政地区(self) -> "Region":
        """
        上级行政地区
        """

        if self.行政级别 == 2:
            return Region(self.code[:-4] + "0000")

        if self.行政级别 == 3:
            return Region(self.code[:-2] + "00")

        raise RegionNoSuperiorError("不存在上级地区")

    @property
    def 下级行政区域(self) -> List["Region"]:
        """
        下级行政地区列表
        """
        if self.行政级别 == 2:
            return [
                Region(d["code"])
                for d in filter(
                    lambda d: d["code"].startswith(self.code[:-2])
                    and d["code"] != self.code,
                    REGION_DATA,
                )
            ]

        if self.行政级别 == 1:
            return [
                Region(d["code"])
                for d in filter(
                    lambda d: d["code"].startswith(self.code[:-4] + "00")
                    and d["code"] != self.code,
                    REGION_DATA,
                )
            ]

        raise RegionNoSubordinateError("不存在下级地区")


list(map(lambda d: Region(*d.values()), REGION_DATA))
