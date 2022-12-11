import heapq
import queue
from collections import deque


def main():
    # creating different queue
    priority_queue = queue.PriorityQueue(10)
    normal_queue = queue.Queue(maxsize=10)
    stack = queue.LifoQueue(10)

    # Adding to queue of different
    stack.put(2)
    stack.put(1)
    stack.put(3)

    normal_queue.put(2)
    normal_queue.put(1)
    normal_queue.put(3)

    priority_queue.put(2)
    priority_queue.put(1)
    priority_queue.put(3)

    # removing from different queues
    # print("Stack", stack.get())
    # print("Queue", normal_queue.get())
    # print("Priority Queue", priority_queue.get())

    # # viewing the current queue *note: may not be reliable
    # print("Priority Queue", priority_queue.queue)
    # print("Normal Queue", normal_queue.queue)
    # print("Stack", stack.queue)

    # Monkey patching a queue
    items = [10, 5, 4, 2, 5, 5]
    que = deque(items)
    monkey_patched_queue = queue.PriorityQueue()
    print(monkey_patched_queue.queue)  # shows that the queue is empty

    heapq.heapify(
        items
    )  # converts the list into a min-heap so that Priority Queue would be correct
    monkey_patched_queue.queue = items  # Patches the new inner-queue (i.e replaces the inner min-heap for the new min-heap)

    print(monkey_patched_queue.queue)  # shows that the queue is no longer empty
    print(monkey_patched_queue.get())  # access a value
    # Monkey patching a queue


main()
