
def maxDiff(arr):
    min, max, pMin = (arr[0],)*3
    for i in arr:
        if i < min and i < pMin:
            pMin = i
        if i > max:
            max = i
            min = pMin
        if max-min < i-pMin:
            min = pMin
            max = i
    print("min: {}, max: {}".format(min, max))
    return max-min

if __name__ == "__main__":
    arr = [3, 2, 7 ,9, 6, 0, 8]
    print(arr)
    print(maxDiff(arr))
