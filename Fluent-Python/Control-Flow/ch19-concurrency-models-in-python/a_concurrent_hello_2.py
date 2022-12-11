import itertools
import time
from multiprocessing import Event, Process, synchronize


def spin(msg: str, done: synchronize.Event) -> None:
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
    spinner = Process(target=spin, args=("thinking!", done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
