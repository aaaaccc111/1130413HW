num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_even_squares(num_list: list[int]) -> list[int]:
    """
    回傳列表中所有偶數的平方。
    """
    return [x**2 for x in num_list if x % 2 == 0]


def get_odd_cubes(num_list: list[int]) -> list[int]:
    """
    回傳列表中所有奇數的立方。
    """
    cube = []
    for num in num_list:
        if num % 2 != 0:
            cube.append(num ** 3)
    return cube


def sliced_list(num_list: list[int]) -> list[int]:
    """
    回傳列表的第五個到第九個元素。
    """
    return num_list[4:9]


def format_numbers(numbers: list[int]) -> str:
    """
    將數字列表格式化為一個字符串，每個數字都被格式化為靠右對齊，並且用逗號分隔。
    """
    formatted_numbers = ','.join(f"{num: >8}" for num in numbers)
    return formatted_numbers


square = get_even_squares(num_list)
cube = get_odd_cubes(num_list)
sliced = sliced_list(num_list)


print("\n".join([format_numbers(square),
                 format_numbers(cube),
                 format_numbers(sliced)]))
