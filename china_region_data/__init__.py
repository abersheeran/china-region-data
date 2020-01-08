from typing import List
from .datastructures import Region, REGION_DATA

__all__ = ["省级行政区域", "市级行政区域", "县级行政区域", "Region"]


省级行政区域: List[Region] = [
    Region(*data.values())
    for data in filter(lambda d: d["code"].endswith("0000"), REGION_DATA)
]

市级行政区域: List[Region] = [
    Region(*data.values())
    for data in filter(
        lambda d: d["code"].endswith("00") and not d["code"].endswith("0000"),
        REGION_DATA,
    )
]

县级行政区域: List[Region] = [
    Region(*data.values())
    for data in filter(lambda d: not d["code"].endswith("00"), REGION_DATA)
]
