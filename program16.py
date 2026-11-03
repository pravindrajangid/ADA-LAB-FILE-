import random
from typing import Optional


def strStr(haystack: str, needle: str) -> int:
    """
    Finds the first occurrence of needle in haystack
    using the KMP string matching algorithm.
    """

    if not needle:
        return 0

    m, n = len(haystack), len(needle)

    # Step 1: Compute LPS array
    lps = [0] * n
    prev_lps, i = 0, 1

    while i < n:
        if needle[i] == needle[prev_lps]:
            lps[i] = prev_lps + 1
            prev_lps += 1
            i += 1
        elif prev_lps == 0:
            lps[i] = 0
            i += 1
        else:
            prev_lps = lps[prev_lps - 1]

    # Step 2: Match pattern in haystack
    i = 0
    j = 0

    while i < m:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

        if j == n:
            return i - n

    return -1


class Randomizer:
    """
    Samples a random element from a continuous stream
    using Reservoir Sampling.
    """

    def __init__(self):
        self.count = 0
        self.sampled_element: Optional[int] = None

    def process(self, value: int):
        self.count += 1

        # Keep the new value with probability 1/count
        if random.randint(1, self.count) == 1:
            self.sampled_element = value

    def getRandom(self) -> int:
        if self.count == 0:
            raise ValueError("No stream data has been processed yet.")

        return self.sampled_element


# Example Usage
if __name__ == "__main__":

    # 1. KMP strStr Example
    text = "hello world programming"
    pattern = "world"

    index = strStr(text, pattern)

    print(f"Haystack: '{text}'")
    print(f"Needle: '{pattern}'")
    print(f"Pattern found at index: {index}")

    print("\n" + "-" * 30 + "\n")

    # 2. Stream Sampling Example
    sampler = Randomizer()

    stream_data = [5, 15, 25, 35, 45, 55, 65, 75]

    print(f"Simulating a data stream: {stream_data}")

    # Process stream elements one by one
    for val in stream_data:
        sampler.process(val)

    # Get a random element
    print(
        f"Randomly sampled element from the stream: "
        f"{sampler.getRandom()}"
    )