# START
from queue import Queue

queue = Queue()
# END

# START
# Send message from a thread
# (in Go this will block until someone reads)
queue.put(353)
# END

# START
# Get message to a thread
val = queue.get()
# END

print(val)
