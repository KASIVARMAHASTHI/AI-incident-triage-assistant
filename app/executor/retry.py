class RetryPolicy:
    def __init__(self, retries=3):
        self.retries = retries

    def run(self, func, *args, **kwargs):
        for _ in range(self.retries):
            try:
                return func(*args, **kwargs)
            except Exception:
                continue
        raise Exception("Execution failed after retries")