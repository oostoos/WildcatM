import timeit

def perf_timer(lFxn, iterations):
    
    elapsed = timeit.timeit(
        lFxn,
        number=iterations
    )
    
    per_call_us = (elapsed / iterations) * 1_000_000

    print(f"Performance test: {iterations:,} iterations")
    print(f" > Total seconds: {elapsed:.2f} s")
    print(f" > Microseconds per call: {per_call_us:.3f} μs")
