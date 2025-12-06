import timeit
import gc

def perfTimer(lFxn, iterations):
    """
    Run performance test with percentile analysis.
    
    :param lFxn: Lambda or function to test
    :param iterations: Number of iterations per round
    """
    # Disable garbage collection during timing for consistency
    gc.disable()
    
    times = []
    for _ in range(iterations):
        elapsed = timeit.timeit(lFxn, number=1)
        times.append(elapsed)
    
    gc.enable()
    
    # Sort for percentile calculation
    times.sort()
    
    p0 = times[0]
    p25 = percentile(times, 25)
    p50 = percentile(times, 50)
    p75 = percentile(times, 75)
    p100 = times[-1]
    
    print(f"Performance test: {iterations:,} iterations")
    print(f" > Min (p0):   {secToMicrosec(p0, iterations):.3f} μs/call  ({iterations/p0:,.0f} calls/sec)")
    print(f" > p25:        {secToMicrosec(p25, iterations):.3f} μs/call")
    print(f" > Median:     {secToMicrosec(p50, iterations):.3f} μs/call")
    print(f" > p75:        {secToMicrosec(p75, iterations):.3f} μs/call")
    print(f" > Max (p100): {secToMicrosec(p100, iterations):.3f} μs/call")

def percentile(data, p):
        k = (len(data) - 1) * p / 100
        f = int(k)
        c = f + 1 if f < len(data) - 1 else f
        return data[f] + (k - f) * (data[c] - data[f])
    
def secToMicrosec(seconds, iterations):
    return (seconds / iterations) * 1_000_000