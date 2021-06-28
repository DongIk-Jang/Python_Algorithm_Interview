def maxDistance(position, m):
    position.sort()
    force = []
    for i in range(len(position)-1):
        force.append(position[i+1]-position[i])

    sum(force) // m
    return force[m-1]



position = [1,2,3,4,7]
maxDistance(position, 3)



    




