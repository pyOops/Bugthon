from typing import Union, Any, Optional


def rectangle_params(p1: tuple[float, float], p2: tuple[float, float]) -> Union[
    str, tuple[Any, Union[float, Any], Union[float, Any]]]:
    """
    Calculate the area and centroid of a specific rectangle

    Parameters
    --------
    p1: tuple(float, float)
        The 1st point of a rectangle
    p2: tuple(float, float)
        The 2nd point of a rectangle

    Examples
    --------
    >>> rectangle_params((2, 1), (2, 2))
    (2.0, 1.0, 1.5)
    >>> rectangle_params((2,1),(3,2))
    This is not a rectangle!

    Returns
    --------
    result: tuple(float, float, float)
        The area, centroid of x, centroid of y, of this rectangle
    """
    width = abs(p1[0] - p2[0])
    height = abs(p1[1] - p2[1])
    area = abs(width * height)
    if area == 0:
        return "This is not a rectangle!"
    x_ = (p1[0] + p2[0]) / 2
    y_ = (p1[1] + p2[1]) / 2
    return area, x_, y_


# print(rectangle_params((2, 1), (2, 2)))

def triangle_params(p1: tuple[float, float], p2: tuple[float, float]) -> Union[
    str, tuple[Any, Union[float, Any], Union[float, Any]]]:
    """
    Calculate the area and centroid of a specific triangle

    Parameters
    --------
    p1: tuple(float, float)
        The 1st point of a rectangle
    p2: tuple(float, float)
        The 2nd point of a rectangle

    Examples
    --------
    >>> tri_data = triangle_params((1,1),(2,2))
    >>> print(tri_data)
    (0.5, 1.3333333333333333, 1.6666666666666665)

    >>> tri_data = triangle_params((2,1),(1,2))
    >>> print(tri_data)
    (0.5, 1.3333333333333333, 1.3333333333333333)

    Returns
    --------
    result: tuple(float, float, float)
        The area, centroid of x, centroid of y, of this triangle
    """
    p3 = (p1[1], p2[0])
    width = abs(p1[0] - p2[0])
    height = abs(p1[1] - p2[1])
    area = abs(width * height / 2)
    x_ = (p1[0] + p2[0] + p3[0]) / 3
    y_ = (p1[1] + p2[1] + p3[1]) / 3
    return area, x_, y_


# print(triangle_params((1, 1), (2, 2)))

def trapezium_params(p1: tuple[float, float], p2: tuple[float, float]) -> Union[
    str, tuple[Any, Union[float, Any], Union[float, Any]]]:
    """
    Calculate the area and centroid of a specific trapezium

    Parameters
    --------
    p1: tuple(float, float)
        The 1st point of a rectangle
    p2: tuple(float, float)
        The 2nd point of a rectangle

    Examples
    --------
    >>> trap_data = trapezium_params((1,1),(2,2))
    >>> print(trap_data)
    (1.5, 0.7777777777777777, 1.5555555555555554)
    >>> trap_data = trapezium_params((2,1),(1,2))
    >>> print(trap_data)
    (1.5, 0.7777777777777777, 1.4444444444444444)

    Returns
    --------
    result: tuple(float, float, float)
        The area, centroid of x, centroid of y, of this trapezium
    """
    p3 = (0, p1[1])
    p4 = (0, p2[1])
    p5 = (p1[0], p2[1])
    top_base = p1[0] - p3[0]
    bottom_base = p2[0] - p4[0]
    height = abs(p3[1] - p4[1])
    area = (abs(top_base) + abs(bottom_base)) * height / 2
    AreaOfTriangle, TriangleCntroidX, TriangleCntroidY = triangle_params(p1, p2)
    AreaOfRectangle, RectangleCntroidX, RectangleCntroidY = rectangle_params(p3, p5)
    x_ = (TriangleCntroidX * AreaOfTriangle + RectangleCntroidX * AreaOfRectangle) / area
    y_ = (TriangleCntroidY * AreaOfTriangle + RectangleCntroidY * AreaOfRectangle) / area
    return area, x_, y_


# print(trapezium_params((1, 1), (2, 2)))


def cumul_list(l: list[float]) -> list[float]:
    """
    Cumulate a list.

    Parameters
    --------
    l : list
        The list expected to be cumulated.

    Examples
    --------
    >>> cumul_list([1, 2, 3, 4, 5])
    [1, 3, 6, 10, 15]
    >>> cumul_list([0, 0, 0, 0, 0])
    [0, 0, 0, 0, 0]

    Returns
    --------
    result : list
        The cumulated list

    """
    result = list()
    for i in range(len(l)):
        result.append(sum(l[0:i + 1]))
    return result


# print(cumul_list([1, 2, 3, 4, 5]))


def bonjean(data: list[tuple]) -> tuple[
    Optional[list[tuple[float, float]]], Optional[list[tuple[float, float]]], Optional[list[tuple[float, float]]]]:
    """
    Calculates the bonjean area and the moments of every section of waterlines.

    Parameters
    --------
    data : list[tuple]
        Contains some points on the bonjean curve.

    Examples
    --------
    >>> a, h, v = bonjean([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
    >>> print(a)
        [(0, 2), (1.5, 3), (4.0, 4), (7.5, 5), (12.0, 6)]
    >>> print(h)
        [(0, 2), (1.3333333333333335, 3), (4.666666666666666, 4), (11.5625, 5), (23.59375, 6)]
    >>> print(v)
        [(0, 2), (3.666666666666667, 3), (12.333333333333332, 4), (29.21875, 5), (57.453125, 6)]

    Returns
    --------
    result: tuple[Optional[list[tuple[float, float]]], Optional[list[tuple[float, float]]], Optional[list[tuple[float, float]]]]
        A tuple of result, with the 1st element of area, 2nd element of horizontal 1st moment, and 3rd element of vertical 1st moment
    """

    def combine(data: list[float], waterline: list[float]) -> Optional[list[tuple[float, float]]]:
        if len(data) != len(waterline):
            return None
        else:
            result = list()
            for index in range(len(data)):
                t = (data[index], waterline[index])
                result.append(t)
            return result

    def getCentroidOfCombinedShape(centroid1: tuple, area1: float, centroid2: tuple, area2: float):
        x1 = centroid1[0]
        x2 = centroid2[0]
        y1 = centroid1[1]
        y2 = centroid2[1]
        x = (x1 * area1 + x2 * area2) / (area1 + area2)
        y = (y1 * area1 + y2 * area2) / (area1 + area2)
        return x, y

    waterline = list()

    # 计算面积
    a0 = [0]
    for i in range(len(data)):
        waterline.append(data[i][1])
    for i in range(len(data) - 1):
        a0.append(trapezium_params(data[i], data[i + 1])[0])
    a = combine(cumul_list(a0), waterline)

    # 计算一阶面积矩
    centroids = []
    for i in range(len(data) - 1):
        centroids.append((trapezium_params(data[i], data[i + 1])[1], trapezium_params(data[i], data[i + 1])[2]))
    for i in range(len(centroids) - 1):
        x, y = getCentroidOfCombinedShape(
            (centroids[i][0], centroids[i][1]),
            a0[i + 1],
            (centroids[i + 1][0], centroids[i + 1][1]),
            a0[i + 2]
        )
        centroids[i + 1] = (x, y)
    horizontalMoments = [0]
    verticalMoments = [0]
    for i in range(len(data) - 1):
        horizontalMoments.append(centroids[i][0] * a[i + 1][0])
        verticalMoments.append(centroids[i][1] * a[i + 1][0])
    horizontalMoments = combine(horizontalMoments, waterline)
    verticalMoments = combine(verticalMoments, waterline)

    return a, horizontalMoments, verticalMoments


# a, h, v = bonjean([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
# print(a)
# print(h)
# print(v)
