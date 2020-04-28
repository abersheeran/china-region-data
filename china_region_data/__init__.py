from typing import List
from .datastructures import Region, REGION_DATA

__all__ = ["provinces", "cities", "counties", "Region"]


provinces: List[Region] = [
    Region(*data.values())
    for data in filter(lambda d: d["code"].endswith("0000"), REGION_DATA)
]

cities: List[Region] = [
    Region(*data.values())
    for data in filter(
        lambda d: d["code"].endswith("00") and not d["code"].endswith("0000"),
        REGION_DATA,
    )
]

counties: List[Region] = [
    Region(*data.values())
    for data in filter(lambda d: not d["code"].endswith("00"), REGION_DATA)
]
