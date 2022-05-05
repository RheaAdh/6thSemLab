import sys
noOfNodes = int(sys.argv[1])
initiatorNode = int(sys.argv[2])

def bully_algorithm():
    print("----Bully Algorithm----")
    print('Node %s notices the current coordinator %s has failed' % (initiatorNode, noOfNodes))
    if(initiatorNode>=noOfNodes):
        print('INVALID')
    else:
        biggerNodes = []
        if(initiatorNode==noOfNodes-1):
            # no need of election
            biggerNodes.append(initiatorNode+1)
        else:
            for i in range(initiatorNode+1, noOfNodes+1):
                print("%s sends ELECTION message to %s" % (initiatorNode,i))
                biggerNodes.append(i)
            for i in biggerNodes:
                print("%s sends OK message to %s" % (i, initiatorNode))
            while len(biggerNodes) > 1:
                i = biggerNodes[0]
                for j in range(i+1, noOfNodes+1):
                    print("%s sends ELECTION message to %s" % (i, j))
                for k in range(i+1, noOfNodes+1):
                    print("%s sends OK message to %s" % (k, i))
                biggerNodes.remove(i)

        newCoordinatorNode = biggerNodes[0]

        for i in range(1, newCoordinatorNode):
            print("%s sends COORDINATOR message to %s" %
        (newCoordinatorNode, i))

if __name__ == '__main__':
    bully_algorithm()