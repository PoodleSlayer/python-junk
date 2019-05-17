import os
import time
import random

# mock input from Raspberry Pi
def GPIOInput():
    return random.uniform(0.0, 3.0)

# the 'duration' parameter is how long to run the script, in seconds
# the 'interval' parameter is how long to wait between each listen, in seconds
def listenToFish(duration, interval):
    start = time.perf_counter()    # get the global start time, agnostic of thread time

    while True:  # better make sure there is a break condition here, haha
        signal = GPIOInput()
        signal = round(signal, 2)  # round to 2 decimal places to map the signal to a response
        print("\tsignal was " + str(signal))
        
        if signal > 0.5 and signal < 1.5:
            print("\tsending a response signal...")
            if signal > 1.25:
                # pretend to play audio file here
                print("> playing response1.wav")
            elif signal > 1.0:
                print("> playing response2.wav")
            elif signal > 0.75:
                print("> playing response3.wav")
            else:  # default case is 0.5 to 0.75
                print("> playing response4.wav")
            time.sleep(2)          # wait while playing back appropriate sound, if needed

        # see how long this has been running
        elapsed = time.perf_counter() - start
        print("elapsed time: " + str(elapsed))

        # if the user-specified script duration was exceeded, go ahead and stop
        if elapsed > duration:
            print("All done!")
            break

        # wait before next "listen" to avoid oversampling the inputs
        time.sleep(interval)
        

# test run for 60 seconds, wait 0.02 seconds between listens
listenToFish(60, 0.02)
