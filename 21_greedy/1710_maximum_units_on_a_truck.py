def maximumUnits(boxTypes,truckSize):
    sorted_box = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    print(sorted_box)
    sum = 0
    answer = 0
    for n, item in sorted_box:
        print(n, item)
        if sum + n > truckSize:
            answer += ((truckSize - sum) * item)
            print("sum :",sum)
            print('answer :', answer)
            break
        else:
            sum += n
            answer += (n * item)
            print("sum :",sum)
            print('answer :', answer)
    return answer
            

print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))

