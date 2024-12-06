
"""Local Variables
Memory Assignment:
Where: Local variables are stored in stack memory.
When: Memory is allocated when a function is called.
How:
The variable is given a reference to an object in heap memory.
The reference itself resides in the stack.
Behavior:
Scope: Local variables are accessible only within the function they are declared in.
Deallocation: When the function exits, the local variable's 
reference is removed from the stack. If no other references exist, the object in the heap is garbage collected."""

"""local variable"""
def example_function():
    local_var = 42  # Reference is stored in stack; object (42) is in the heap
    print(local_var)

example_function()
# local_var is no longer accessible after the function ends

"""Global Variables
Memory Assignment:
Where: Global variables are stored in the global frame, which resides in heap memory.
When: Memory is allocated when the variable is first defined.
How:
The global variable's reference is stored in the global namespace in heap memory.
The reference points to an object also stored in the heap.
Behavior:
Scope: Accessible throughout the program unless shadowed by a local variable.
Deallocation: The global variable remains in memory until the program
ends or the del keyword explicitly removes it."""

global_var = 100  # Stored in the global namespace (heap)

def access_global():
    global global_var
    global_var=101
    print(global_var) 
    # Accessing global variable
access_global()

"""referance Counting"""
x = 10  # Reference count for object 10 increases
y = x   # Reference count for object 10 increases again
del x   # Reference count decreases
del y   # Reference count decreases to 0; object is garbage collected

"""Why is nonlocal Needed?
By default, variables in a nested function are local to that function.
If you need to modify a variable defined in the enclosing scope, you cannot do so directly unless you use the nonlocal keyword.
nonlocal bridges the gap between local variables (function scope) and global variables (module scope)."""

x=100
def outer_function():
    x = 10  # Variable in the enclosing scope

    def inner_function():
        nonlocal x  # Refers to the x in outer_function
        x += 5
        print("Inner x:", x)

    inner_function()
    print("Outer x:", x)

outer_function()
print("Outer x:", x) #global



"""What is an Event Loop?
The event loop is the core of asynchronous programming in Python. It’s a mechanism that manages the execution of multiple tasks (coroutines) by scheduling 
and switching between them, without blocking the main thread.

The event loop is part of the asyncio module and runs as long as there are tasks to be executed.
It enables efficient concurrency by letting tasks yield control when they are waiting (e.g., for I/O), allowing other tasks to run in the meantime."""

"""Key Features of the Event Loop
Manages Coroutines:
Coroutines (async def functions) are added to the event loop for execution.
Non-Blocking:
It suspends tasks during blocking operations (e.g., await asyncio.sleep() or network I/O) and resumes them when ready.
Single Threaded:
All tasks are executed in a single thread but appear to run concurrently by yielding control during waits.
Uses Callbacks:
The event loop schedules tasks and callbacks to run at the appropriate time."""


import asyncio
async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)  # Yields control
    print(f"{name} finished")

async def main():
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 3)
    )

asyncio.run(main())
