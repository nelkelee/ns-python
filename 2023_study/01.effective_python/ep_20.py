# 20 None을 반환하기보다는 예외를 발생시켜라

def careful_divide(a: float, b: float) -> float:
    """
    a를 b로 나눈다.
    :param a:
    :param b:
    :return:
    """
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError("잘못된 입력")

careful_divide(10,2)
careful_divide(0, 0)