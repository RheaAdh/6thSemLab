import sys
noOfNodes = int(sys.argv[1])
initiatorNode = int(sys.argv[2])

def ring_algorithm():
    print('Node: ' + str(initiatorNode) +' notices the coordinator: ' + str(noOfNodes)+' has failed')
    biggerNodes = []
    init = initiatorNode
    biggerNodes.append(init)
    print(biggerNodes)
    for i in range(0, noOfNodes):
        biggerNodes.append((i+init)%noOfNodes)
        print(str((i+init)%noOfNodes) +' sent ELECTION message to: ' + str((i+1+init)%noOfNodes))
        largest = biggerNodes[0]
    for i in biggerNodes:
        if largest < biggerNodes[i]:
            largest = biggerNodes[i]
    for i in range(0, noOfNodes):
        if i != initiatorNode:
            print(str(initiatorNode)+' sends COORDINATOR message to '+str(i) + ' that ' + str(largest) + ' is the coordinator node')



if __name__ == '__main__':
    ring_algorithm()