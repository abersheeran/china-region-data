class RegionError(Exception):
    """
    异常基类
    """


class RegionNotFoundError(RegionError):
    """
    无此地区
    """


class RegionNoSuperiorError(RegionError):
    """
    此地区无上级
    """


class RegionNoSubordinateError(RegionError):
    """
    此地区无下级
    """
