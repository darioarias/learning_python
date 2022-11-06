# Spinner with Threads
"""The idea of the next few examples is simple: start a function that blocks for 3 seconds 
while animating characters in the terminal to let the user know that the program is “thinking” and not stalled."""

import itertools
import time
from threading import Event, Thread


def spin(msg: str, done: Event) -> None:
    # print("starting spinner")
    status = ""
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


def slow() -> int:
    # print("starting slow")
    time.sleep(6)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=("thinking!", done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f"Answer: {result}")


main()
