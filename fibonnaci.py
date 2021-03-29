def fibonacci_recursive(n):
    if n== 0 or n==1:
        return 1
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dynamic(n, memo = {} ):
    if n==1 or n==0:
        return 1
    try:
        return memo[n]
    except KeyError:
        result =  fibonacci_dynamic(n-1, memo) + fibonacci_dynamic(n-2, memo)
        memo[n] = result
    
    return result



if __name__ == '__main__':

    n = int(input("Write a number: "))

    result = fibonacci_dynamic(n)

    print(result)