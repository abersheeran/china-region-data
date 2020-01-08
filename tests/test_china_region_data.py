from china_region_data import 省级行政区域, 市级行政区域, 县级行政区域


def test_area():
    for 省级行政地区 in 省级行政区域:
        assert 省级行政地区.行政级别 == 1
        for 市级行政地区 in 省级行政地区.下级行政区域:
            assert 市级行政地区.行政级别 == 2
            assert 市级行政地区.上级行政地区 == 省级行政地区
            for 县级行政地区 in 市级行政地区.下级行政区域:
                assert 县级行政地区.行政级别 == 3
                assert 县级行政地区.上级行政地区 == 市级行政地区
