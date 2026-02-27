from datetime import datetime

current_time = datetime.now()
no_microseconds = current_time.replace(microsecond=0)

print("With microseconds:", current_time)
print("Without microseconds:", no_microseconds)