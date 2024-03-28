import logging
import time
import os


def record():
    logs = r'D:\logs'
    if not os.path.exists(logs):
        os.makedirs(logs)

    logs_file = os.path.join(logs, 'Logs.log')
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