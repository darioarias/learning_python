### auxiliary functions for display only ###


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split(".")[-1]


def disply(obj):
    cls = type(obj)

    if cls is type:
        return f"<class {obj.__name__}>"
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return f"<{cls_name(obj)} object>"


def print_args(name, *args):
    pseudo_args = ", ".join(disply(x) for x in args)
    print(f"-> {cls_name(args[0])}__.{name}__({pseudo_args})")
