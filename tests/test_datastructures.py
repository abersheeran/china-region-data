from china_region_data.datastructures import (
    Region,
    RegionNoSubordinateError,
    RegionNoSuperiorError,
)


def test_region():
    广东 = Region("广东省")
    深圳 = Region("深圳市")
    南山 = Region("南山区")
    assert 广东.name == "广东省"
    assert 广东.行政级别 == 1
    assert 广东.下级行政区域
    for 广东城市 in 广东.下级行政区域:
        assert 广东城市.行政级别 == 2
    assert 深圳.上级行政地区 == 广东
    assert 南山.上级行政地区.上级行政地区 == 广东
    assert 南山 in 南山.上级行政地区
    assert 南山 in 南山.上级行政地区.上级行政地区
    assert not Region("合肥市") in 广东


def test_municipality_region():
    北京 = Region("北京市")
    assert 北京.下级行政区域
    for 北京市区 in 北京.下级行政区域:
        assert 北京市区.行政级别 == 3


def test_region_error():
    广东 = Region("广东省")
    深圳 = Region("深圳市")
    南山 = Region("南山区")

    try:
        广东.上级行政地区
        assert False
    except RegionNoSuperiorError:
        pass

    try:
        南山.下级行政区域
        assert False
    except RegionNoSubordinateError:
        pass
