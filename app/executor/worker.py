from app.executor.queue import ExecutionQueue
from app.executor.retry import RetryPolicy
from app.executor.service import ExecutionEngine


class Worker:
    def __init__(self, queue: ExecutionQueue):
        self.queue = queue
        self.executor = ExecutionEngine()
        self.retry = RetryPolicy()

    def process_next(self):
        task = self.queue.dequeue()
        if not task:
            return {"status": "no_tasks"}

        result = self.retry.run(self.executor.execute, task)
        return {
            "status": "processed",
            "result": result
        }
