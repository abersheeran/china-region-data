from typing import List

from .datastructures import Region, REGION_DATA
from .exceptions import (
    RegionError,
    RegionNotFoundError,
    RegionNoSuperiorError,
    RegionNoSubordinateError,
)

__all__ = [
    "provinces",
    "cities",
    "counties",
    "Region",
    "RegionError",
    "RegionNotFoundError",
    "RegionNoSuperiorError",
    "RegionNoSubordinateError",
]


provinces: List[Region] = [
    Region(*data)
    for data in filter(lambda d: d[0].endswith("0000"), REGION_DATA.items())
]

cities: List[Region] = [
    Region(*data)
    for data in filter(
        lambda d: d[0].endswith("00") and not d[0].endswith("0000"),
        REGION_DATA.items(),
    )
]

counties: List[Region] = [
    Region(*data)
    for data in filter(lambda d: not d[0].endswith("00"), REGION_DATA.items())
]
