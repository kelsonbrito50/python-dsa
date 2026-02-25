from src.queues.queue import Queue

def test_fifo():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

def test_empty():
    q = Queue()
    assert q.dequeue() is None
    assert q.is_empty() is True
