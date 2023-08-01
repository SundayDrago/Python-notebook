# Context Manager-> is an object that defines the methods '__enter__' and '__exit__, which  allows it to be used with the
# 'with' statement. context managers are used to set up and tear down resources such as opening and closing files or acquiring 
# and releasing locks in a clean and efficient manner

# 'with' statement provides a convenient way to manage resources by automatically calling the context manager's '__enter__'
#at the beginning of the block and its '__exit__ method at the end of the block


# Example 1:
# import time
class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")

with Timer():
    time.sleep(2)
    print("Finished executing the code block")
print("============================================================")

# Example 2:
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileHandler('example.txt', 'w') as file:
    file.write('Hello, Content Manager')

print("---------------Multithreading--------------------")
# Program that is used to run several threads concurrently with a single process
# Also provides built-in  module called 'threading' for working with threads
import threading
import time
def thread_function(name):
    print(f"Thread {name} started:")
    time.sleep(3)
    print(f"Thread {name} finished:")

threads = []
for i in range(3):
    t = threading.Thread(target=thread_function, args=(i,))
    threads.append(t)
    t.start()

# Wait for threads to finish 
for t in threads:
    t.join()
print ("Threads finished successfully")

print ("*************Multiprocessing*******************************")
# Whereas multithreading refers to the execution of of multiple threads concurrently in a single process
# therefore, multiprocessing refers to the execution of multiple processes concurrently. However, multiprocessing allows for 
# parallel execution of tasks.
# Python provides built-in module  called 'multiprocessing' for working with multiple processes concurrently.

# Example 1:
import multiprocessing
import time


# Function to be executed in a separate process
def process_function(name):
    print(f"Process {name} started")
    time.sleep(3)
    print(f"Process {name} finished")

# Create and start multiple processes
processes = []
for i in range(3):
    p = multiprocessing.Process(target=process_function, args=(i,))
    processes.append(p)
    p.start()

# Wait for all the processes to finish
for p in processes:
    p.join()

print("All processes finished successfully")

