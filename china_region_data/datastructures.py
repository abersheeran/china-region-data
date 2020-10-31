import os
import re
import json
from typing import List, Dict, Tuple, Any

from .utils import cached_property
from .exceptions import (
    RegionNotFoundError,
    RegionNoSuperiorError,
    RegionNoSubordinateError,
)

__all__ = ["Region"]


CODE_PATTERN = re.compile(r"^\d+")

with open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json"),
    encoding="utf8",
) as file:
    # 地区数据
    REGION_DATA: Dict[str, str] = json.load(file)


class SingletonRegion(type):
    def __init__(
        cls,
        name: str,
        bases: Tuple[type],
        namespace: Dict[str, Any],
    ) -> None:
        cls.instances: Dict[str, Region] = {}
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs) -> Any:
        if kwargs:
            raise TypeError("Keyword arguments not allowed.")

        code = args[0]
        if code not in cls.instances:
            if code not in REGION_DATA:
                msg = f'不存在此地区"{code}"'
                if not CODE_PATTERN.match(code):
                    msg += "，可使用城市全称尝试查找"
                raise RegionNotFoundError(msg)
            # 创建 Region 类的实例对象
            instance = super().__call__(code, REGION_DATA[code])
            cls.instances[code] = instance
            cls.instances[instance.fullname] = instance
        return cls.instances[code]


class Region(metaclass=SingletonRegion):
    def __init__(self, code: str = "", name: str = "", **kwargs) -> None:
        assert name and isinstance(name, str)
        assert code and isinstance(code, str)

        self.code = code
        self.name = name

    def __repr__(self) -> str:
        return self.fullname

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Region):
            return NotImplemented
        return self.code == other.code

    def __contains__(self, other: object) -> bool:
        if not isinstance(other, Region):
            return NotImplemented
        if self.level == 2:
            return other.code.startswith(self.code[:4])
        elif self.level == 1:
            return other.code.startswith(self.code[:2])
        else:
            return False

    @cached_property
    def fullname(self) -> str:
        try:
            name = self.superior.fullname + self.name
        except RegionNoSuperiorError:
            name = self.name
        return name

    @cached_property
    def level(self) -> int:
        """
        行政级别

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

    @cached_property
    def superior(self) -> "Region":
        """
        上级行政地区
        """

        if self.level == 2:
            return Region(self.code[:-4] + "0000")

        if self.level == 3:
            try:
                return Region(self.code[:-2] + "00")
            except RegionNotFoundError:  # 直辖市区
                return Region(self.code[:-4] + "0000")

        raise RegionNoSuperiorError(f"{self.name}不存在上级地区")

    @cached_property
    def subordinate(self) -> List["Region"]:
        """
        下级行政地区列表
        """
        if self.level == 2:
            return [
                Region(d[0])
                for d in filter(
                    lambda d: d[0].startswith(self.code[:-2]) and d[0] != self.code,
                    REGION_DATA.items(),
                )
            ]

        if self.level == 1:
            subo = [
                Region(d[0])
                for d in filter(
                    lambda d: d[0].startswith(self.code[:-4]) and d[0] != self.code,
                    REGION_DATA.items(),
                )
            ]
            return list(filter(lambda d: d.code.endswith("00"), subo)) or subo

        raise RegionNoSubordinateError(f"{self.name}不存在下级地区")


list(map(lambda t: Region(*t), REGION_DATA.items()))
