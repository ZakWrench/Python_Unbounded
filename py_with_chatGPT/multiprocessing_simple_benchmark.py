import multiprocessing
import time

start_time = time.perf_counter()  # start_time = time.time()

num_iterations_outer = 5000
num_iterations_inner = 1000


def nested_loop(x):
    for i in range(num_iterations_inner):
        # random computation
        result = x ** 2 + i ** 2


# Pool with 4 worker processes
with multiprocessing.Pool(4) as p:
    for x in range(num_iterations_outer):
        # Execute the nested_loop fct in a worker process
        p.apply_async(nested_loop, args=(x,))
        #p.apply_async(nested_loop, (0, 30)) (30,60)(60,90)(90,120)
# Wait for all worker processes to finish
p.close()
p.join()

end_time = time.perf_counter()  # end_time = time.time()
elapsed_time = time.perf_counter() - start_time

print(f'Execution time: {time.perf_counter() - start_time:.2f} seconds')
#print("Execution time: ", end_time - start_time)

###############
start_time = time.perf_counter()

for i in range(num_iterations_outer):
    for j in range(num_iterations_inner):
        result1 = i + j

    for k in range(num_iterations_inner):
        result2 = i + k

    for l in range(num_iterations_inner):
        result3 = i + l

    for m in range(num_iterations_inner):
        result4 = i + m

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f'Execution time: {elapsed_time:.2f} seconds')
