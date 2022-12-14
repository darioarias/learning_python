# quote by Go co-inventor Rob Pike
# Concurrency is about dealing with lots of things at once.
# Parallelism is about doing lots of things at once.


# A Bit of Jargon

# Concurrency
## The ability to handle multiple pending tasks, making progress one at a time or in parallel
## (if possible) so that each of them eventually succeeds or fails.
## A single-core CPU is capable of concurrency if it runs an OS scheduler
## that interleaves the execution of the pending tasks. Also known as multitasking.

# Execution unit
## General term for objects that execute code concurrently, each with independent state and call stack.
## Python natively supports three kinds of execution units: processes, threads, and coroutines.


# Process
## An instance of a computer program while it is running, using memory and a slice of the CPU time.
## Modern desktop operating systems routinely manage hundreds of processes concurrently, with
## each process isolated in its own private memory space.
## Processes communicate via pipes, sockets, or memory mapped files—all of which can only carry raw bytes.
## Python objects must be serialized (converted) into raw bytes to pass from one process to another.
## This is costly, and not all Python objects are serializable. A process can spawn subprocesses, each called a child process.
## These are also isolated from each other and from the parent.
## Processes allow preemptive multitasking: the OS scheduler preempts—i.e.,
## suspends —each running process periodically to allow other processes to run.
## This means that a frozen process can’t freeze the whole system—in theory.

# Thread
## An execution unit within a single process. When a process starts, it uses a single thread: the main thread.
## A process can create more threads to operate concur‐ rently by calling operating system APIs.
## Threads within a process share the same memory space, which holds live Python objects.
## This allows easy data sharing between threads, but can also lead to corrupted data when more
## than one thread updates the same object concurrently.
## Like processes, threads also enable preemptive multitasking under the supervision of the OS scheduler.
## A thread con‐ sumes less resources than a process doing the same job.

# Coroutine
## A function that can suspend itself and resume later.
## In Python, classic coroutines are built from generator functions, and native coroutines are defined with async def.
## “Classic Coroutines” on page 641 introduced the concept, and Chapter 21 covers the use of native coroutines.
## Python coroutines usually run within a single thread under the supervision of an event loop, also in the same thread.
## Asynchronous programming frameworks such as asyncio, Curio, or Trio provide an event loop and supporting libraries
## for nonblocking, coroutine-based I/O. Coroutines support cooperative multitasking: each coroutine must explicitly cede
## control with the yield or await keyword, so that another may proceed concurrently (but not in parallel).
## This means that any blocking code in a coroutine blocks the execution of the event loop and all other coroutines—in
## contrast with the preemptive multitasking supported by processes and threads.
## On the other hand, each coroutine consumes less resources than a thread or process doing the same job.

# Queue
## A data structure that lets us put and get items, usually in FIFO order: first in, first out.
## Queues allow separate execution units to exchange application data and control messages,
## such as error codes and signals to terminate.
## The implementation of a queue varies according to the underlying concurrency model:
## the queue package in Python’s standard library provides queue classes to support threads,
## while the multiprocessing and asyncio packages implement their own queue classes.
## The queue and asyncio packages also include queues that are not FIFO: LifoQueue and PriorityQueue.

# Lock
## An object that execution units can use to synchronize their actions and avoid corrupting data.
## While updating a shared data structure, the running code should hold an associated lock.
## This signals other parts of the program to wait until the lock is released before accessing the same data structure.
## The simplest type of lock is also known as a mutex (for mutual exclusion).
## The implementation of a lock depends on the underlying concurrency model.

# Contention
## Dispute over a limited asset.
## Resource contention happens when multiple execution units try to access a shared resource—such as a lock or storage.
## There’s also CPU contention, when compute-intensive processes or threads must wait
## for the OS scheduler to give them a share of the CPU time.
