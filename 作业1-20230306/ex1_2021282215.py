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
    width = abs(p1[0] - p2[0])  # 计算矩形的宽度
    height = abs(p1[1] - p2[1]) # 计算矩形的高度
    area = abs(width * height) # 计算矩形的面积
    if area == 0: # 如果面积为0，说明在两个方向上至少有一个方向上不构成矩形，输出相关信息，并停止函数
        return "This is not a rectangle!"
    x_ = (p1[0] + p2[0]) / 2 # 形心横坐标
    y_ = (p1[1] + p2[1]) / 2 # 形心纵坐标
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
    p3 = (p1[1], p2[0]) # 向左上角取点，构成直角三角形
    width = abs(p1[0] - p2[0])
    height = abs(p1[1] - p2[1])
    area = abs(width * height / 2)
    x_ = (p1[0] + p2[0] + p3[0]) / 3 # 形心横坐标
    y_ = (p1[1] + p2[1] + p3[1]) / 3 # 形心纵坐标
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
    p3 = (0, p1[1]) # 向z轴投影
    p4 = (0, p2[1]) # 向z轴投影
    p5 = (p1[0], p2[1]) # 选取p5点，使得该梯形可以被分为一个矩形和一个直角三角形
    top_base = p1[0] - p3[0]
    bottom_base = p2[0] - p4[0]
    height = abs(p3[1] - p4[1])
    area = (abs(top_base) + abs(bottom_base)) * height / 2
    AreaOfTriangle, TriangleCntroidX, TriangleCntroidY = triangle_params(p1, p2)
    AreaOfRectangle, RectangleCntroidX, RectangleCntroidY = rectangle_params(p3, p5)
    x_ = (TriangleCntroidX * AreaOfTriangle + RectangleCntroidX * AreaOfRectangle) / area # 使用组合形心公式进行计算
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
        '''
        从第一个数累加到当前index的数，因此，是从0到i+1，不必担心i+1超过，因为超出不影响结果（最后还是取到最后一个元素）
        '''
        result.append(sum(l[0:i + 1]))
    return result


# print(cumul_list([1, 2, 3, 4, 5]))


def bonjean(data: list[tuple]):
    def combine(a: list[float], b: list[float]) -> Optional[list[tuple[float, float]]]:
        return [(a[x], b[x]) for x in range(len(data))] if len(a) == len(b) else None
    waterline = [(data[i][1]) for i in range(len(data))]
    a = cumul_list([(trapezium_params(data[i], data[i + 1])[0]) for i in range(len(data) - 1)])
    a.insert(0, 0)
    h = cumul_list([(trapezium_params(data[i], data[i + 1])[1] * trapezium_params(data[i], data[i + 1])[0]) for i in range(len(data) - 1)])
    h.insert(0, 0)
    v = cumul_list([(trapezium_params(data[i], data[i + 1])[2] * trapezium_params(data[i], data[i + 1])[0]) for i in range(len(data) - 1)])
    v.insert(0, 0)
    return combine(a, waterline), combine(h, waterline) ,combine(v, waterline)


# a, h, v = bonjean([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
# print(a)
# print(h)
# print(v)
