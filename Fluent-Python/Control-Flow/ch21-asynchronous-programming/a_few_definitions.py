# Native coroutine
## A coroutine function defined with async def.
## You can delegate from a native coroutine to another native coroutine using the await keyword,
## similar to how classic coroutines use yield from.
## The async def statement always defines a native coroutine, even if the await keyword is not used in its body.
## The await keyword cannot be used outside of a native coroutine.

# Classic coroutine
## A generator function that consumes data sent to it via my_coro.send(data) calls,
## and reads that data by using yield in an expression. Classic coroutines can delegate
## to other classic coroutines using yield from.
## Classic coroutines cannot be driven by await, and are no longer supported by asyncio.

# Generator-based coroutine
## A generator function decorated with @types.coroutine—introduced in Python 3.5.
## That decorator makes the generator compatible with the new await keyword.

# Asynchronous generator
## A generator function defined with async def and using yield in its body.
## It returns an asynchronous generator object that provides __anext__, a coroutine method to retrieve the next item.
