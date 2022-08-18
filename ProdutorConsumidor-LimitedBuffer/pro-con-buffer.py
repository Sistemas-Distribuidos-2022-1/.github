import threading

N = 10
buffer = [0] * N

encher = threading.Semaphore(0)
esfaziar = threading.Semaphore(N)

def producer():
    front = 0
    while True:
        print("item produzido")
        esfaziar.acquire()
        buffer[front] = 1
        encher.release()
        front = (front + 1) % N


def consumer():
    rear = 0
    while True:
        encher.acquire()
        y = buffer[rear]
        esfaziar.release()
        print("Item consumido")
        rear = (rear + 1) % N


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()