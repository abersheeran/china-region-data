from china_region_data import provinces, cities, counties


def test_area():
    for province in provinces:
        assert province.level == 1
    for city in cities:
        assert city.level == 2
    for county in counties:
        assert county.level == 3
