import time


class TokenBucketRateLimiter:
    def __init__(
        self,
        number_of_token,
        refill_rate,
        forward_callback,
        drop_callback,
    ) -> None:
        self.bucket = number_of_token
        self.tokens = number_of_token
        self.refill_rate = refill_rate
        self.last_check = time.time()
        self.drop_callback = drop_callback
        self.forward_callback = forward_callback

    def refill(self):
        current_time = time.time()
        time_passed = current_time - self.last_check
        print(time_passed)
        self.last_check = current_time
        self.bucket += time_passed * (self.tokens / self.refill_rate)
        self.bucket = min(self.tokens, self.bucket)

    def handle(self, request):
        self.refill()
        if self.bucket < 1:
            self.drop_callback(request)
        else:
            self.bucket -= 1
            self.forward_callback(request)


def forward(packet):
    print("Packet Forwarded: " + str(packet))


def drop(packet):
    print("Packet Dropped: " + str(packet))


throttle = TokenBucketRateLimiter(
    number_of_token=2, refill_rate=1, forward_callback=forward, drop_callback=drop
)

packet = 0

while True:
    throttle.handle(packet)
    packet += 1
    time.sleep(0.2)
