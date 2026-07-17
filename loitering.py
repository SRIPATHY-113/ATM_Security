import time

class LoiteringDetector:

    def __init__(self, threshold=30):
        self.start_time = None
        self.threshold = threshold

    def check_loitering(self, person_count):

        if person_count > 0:

            if self.start_time is None:
                self.start_time = time.time()

            duration = time.time() - self.start_time

            if duration > self.threshold:
                return True

        else:
            self.start_time = None

        return False
