from concurrent.futures import ThreadPoolExecutor


def double_minutes(minutes):
    return minutes * 2


with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(double_minutes, [15, 0, 10]))
print(results)

import time
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(10):
            print(f'Thread name {self.name}, number {i}')
            time.sleep(1)


def main():
    print("main start")
    threads = [MyThread() for _ in range(3)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("main end")


if __name__ == '__main__':
    main()
