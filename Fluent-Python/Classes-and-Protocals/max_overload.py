# sometimes annotating functions that use dynamic features is hard/impossible
# take a look at the max native method in python

# mymax.py: Python rewrite of max function
MISSING = object()
EMPTY_MSG = "max() arg is an empty sequence"


def max(first, *args, key=None, default=MISSING):
    if args:
        series = args
        candidate = first
    else:
        series = iter(first)
        try:
            candidate = next(series)
        except StopIteration:
            if default is not MISSING:
                return default
            raise ValueError(EMPTY_MSG) from None
        if key is None:
            for current in series:
                if candidate < current:
                    candidate = current
        else:
            candidate_key = key(candidate)
            for current in series:
                current_key = key(current)
                if candidate_key < current_key:
                    candidate = current
                    candidate_key = current_key
    return candidate


def volwes_count(str):
    total = 0
    for char in str:
        if char in ("a", "e", "i", "o", " u"):
            total += 1
    return total


print(max(["Go", "Python", "Rust"], key=volwes_count))
