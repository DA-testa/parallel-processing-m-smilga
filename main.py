# python3

def parallel_processing(n, m, data):
    output = [] 
    thread = [0] * n

    for i in range(0, m):
        minVertiba = min(thread)
        vertiba = thread.index(minVertiba)
        output.append(vertiba)
        output.append(thread[vertiba])
        thread[vertiba] += data[i]

    return output

def main():
    n = 0
    m = 0
    n, m = map(int, input().split())
    data = []
    data = list(map(int, input().split()))
    
    result = parallel_processing(n,m,data)

    for i in range(0, m):
        print(result[i*2], result[i*2 + 1])
    

if __name__ == "__main__":
    main()
