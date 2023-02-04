from flask import Flask
import random
import itertools
import math
random.seed(10)


def heavy_compute():
    list1=[random.randint(1, 100) for i in range(10000)]
    list2=[random.randint(1, 10) for i in range(100)]

    two_lists=[list1,list2]
    permutation = itertools.product(*two_lists) # I obtain the permutation ty Cyttorak
    result=[math.factorial(x[0]+x[1]) for x in permutation] # The complex operation (factorial of the sum)
    return result

app = Flask(__name__)

@app.route("/")
def hello():
    file_name = "/tmp/test.txt"
    try:
        with open(file_name, "w+") as f:
            import time
            start_time = time.time()
            heavy_compute()
            time_spent = time.time() - start_time
            response = f"Time spent in compute() function: {time_spent} seconds"
            f.write(response)
            return response + "\n"
    except Exception as e:
        return "open file failed"

       