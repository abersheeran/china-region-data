import pytest

from china_region_data import (
    Region,
    RegionNotFoundError,
    RegionNoSubordinateError,
    RegionNoSuperiorError,
)


def test_region():
    广东 = Region("广东省")
    深圳 = Region("广东省深圳市")
    南山 = Region("广东省深圳市南山区")
    assert 广东.name == "广东省"
    assert 广东.level == 1
    assert 广东.subordinate
    for 广东城市 in 广东.subordinate:
        assert 广东城市.level == 2
    assert 深圳.superior == 广东
    assert 南山.superior.superior == 广东
    assert 南山 in 南山.superior
    assert 南山 in 南山.superior.superior

    北京 = Region("110000")
    assert 北京.name == 北京.fullname == "北京市"
    assert 北京 not in 广东


def test_full_name():
    广东 = Region("广东省")
    深圳 = Region("广东省深圳市")
    南山 = Region("广东省深圳市南山区")

    assert 广东.fullname == "广东省"
    assert 深圳.fullname == "广东省深圳市"
    assert 南山.fullname == "广东省深圳市南山区"


def test_municipality_region():
    北京 = Region("北京市")
    东城 = Region("北京市东城区")
    assert 北京.subordinate
    assert 东城.superior == 北京
    for 北京市区 in 北京.subordinate:
        assert 北京市区.level == 3
    assert 北京.fullname == "北京市"
    assert 东城.fullname == "北京市东城区"


def test_region_error():
    广东 = Region("广东省")
    南山 = Region("广东省深圳市南山区")

    with pytest.raises(RegionNoSuperiorError):
        广东.superior

    with pytest.raises(RegionNoSubordinateError):
        南山.subordinate

    with pytest.raises(RegionNotFoundError, match='不存在此地区"深圳市"，可使用城市全称尝试查找'):
        Region("深圳市")

    with pytest.raises(RegionNotFoundError, match='不存在此地区"10000"'):
        Region("10000")
