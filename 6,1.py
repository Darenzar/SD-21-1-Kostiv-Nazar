import logging
import time
import os


def record():
    logs_folder = r'D:\WorkArea\ДЗ 3 курс\Loggs'
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    logs_file = os.path.join(logs_folder, 'MainLoggs.log')
    logging.basicConfig(filename=logs_file, filemode="w", level=logging.DEBUG)

    start_time = time.monotonic()
    logging.info("Task started at: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time

        if elapsed_time >= 60:
            logging.error("Task finished")
            break

        logging.info("Elapsed time: {:.2f} seconds, Current time: {}".format(elapsed_time,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
        time.sleep(5)


if __name__ == '__main__':
    record()