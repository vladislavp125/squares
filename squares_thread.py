import threading

nums = [1, 3, 2, 4, 5, 6, 7, 7]


def compute_square(results, num):
    results.append(num * num)


def compute_squares(nums):
    results = []
    threads = []

    for i in nums:
        thread = threading.Thread(target=compute_square, args=(results, i))
        threads.append(thread)
        thread.start()
        print(f'Поток для числа {i} запущен')

    for thread in threads:
        print(f'Принимаем поток {thread}')
        thread.join()

    return results


print(compute_squares(nums))