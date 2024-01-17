import queue
import threading


def filter_and_write(channel_in, channel_out, _threshold):
    prev_value = None

    while True:
        value = channel_in.get()

        if value is None:
            break

        if prev_value is None or abs(value - prev_value) > _threshold:
            channel_out.put(value)
            prev_value = value


input_queue = queue.Queue()
output_queue = queue.Queue()
threshold = 5

filter_thread = threading.Thread(target=filter_and_write, args=(input_queue, output_queue, threshold))

if __name__ == '__main__':
    filter_thread.start()

    input_queue.put(1)  # т.к. 1 в начале он выведется в любом случае. Т.к. разница с предыдущим NaN
    input_queue.put(6)
    input_queue.put(3)
    input_queue.put(8)
    input_queue.put(None)  # Выход из цикла

    while True:
        result = output_queue.get()

        if result is None:
            break
        print("Exit:", result)

    filter_thread.join()
