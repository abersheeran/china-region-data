from china_region_data import 省级行政区域, 市级行政区域, 县级行政区域


def test_area():
    for 省级行政地区 in 省级行政区域:
        assert 省级行政地区.行政级别 == 1
    for 市级行政地区 in 市级行政区域:
        assert 市级行政地区.行政级别 == 2
    for 县级行政地区 in 县级行政区域:
        assert 县级行政地区.行政级别 == 3
