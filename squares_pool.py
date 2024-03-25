from multiprocessing import Pool


nums = [1, 3, 2, 4, 5, 6, 7, 7]


def square(x):
    return x * x


def compute_squares(nums):
    for i in range(len(nums)):
        with Pool() as p:
            squares = p.map(square, nums)
            print(squares)


if __name__ == '__main__':
    compute_squares(nums)
