from Card import Card
class PlayerHand:
    def __init__(self):
        self.root = None
        self.size = 0

    def getTotalCards(self):
        return self.size

    def getMin(self):
        current = self.root
        if self.size == 0:
            return None
        while current.getLeft():
            current = current.getLeft()
        return current

    def get(self,suit,rank):
        curr = self.root
        card = Card(suit,rank)
        while curr is not None:
            if curr < card:
                curr = curr.getRight()

            elif curr > card:
                curr = curr.getLeft()
            else:
                return curr

        return None 
                
    def getSuccessor(self,suit,rank):
        succ = self.get(suit,rank)
        if succ == None:
            return succ
        if succ.right:
            succ = succ.right
            while succ.getLeft():
                succ = succ.getLeft()
            return succ
        elif succ.left:
            succ = succ.left
            while succ.getRight():
                succ = succ.getRight()
            return succ
        #else:
        #    if succ.parent > succ:
        #        return succ.parent
        #    else:
        #        return None

    
    def put(self,suit,rank):
        if self.root:
            self._put(suit,rank,self.root)
        else:
            self.root = Card(suit,rank)

        self.size += 1


    def _put(self,suit,rank,node):
        temp = Card(suit,rank)
        if temp == node:
            node.count += 1
        if temp < node:
            if node.getLeft():
                self._put(suit,rank,node.left)
            else:
                node.left = Card(suit,rank,parent = node)
        if temp > node:
            if node.getRight():
                self._put(suit,rank,node.right)
            else:
                node.right = Card(suit,rank,parent = node)


    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def delete(self,suit,rank):
        temp = Card(suit,rank)
        if self.size >1:
            ToRemove = self.get(suit,rank)
            if ToRemove:
                self.remove(ToRemove)
                self.size -= 1
                return True

            else:
                return False

        elif self.size == 1 and self.root == temp:
            self.root = None
            self.size -= 1
            return True
        else:
            return False

        
    def remove(self,node):
        #Case node is leaf
        if not node.hasAnyChildren():
            if not node.parent == None:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None

        #Case with both children
        elif node.hasBothChildren():
            succ = self.getSuccessor(node.suit,node.rank)
            succ.spliceOut()
            node.suit = succ.suit
            node.rank = succ.rank
            node.count = succ.count
        
        else:
            #Case with one child
            if node.getRight():
                node.right.parent = node.parent
                if node.isLeftChild():
                    node.parent.left = node.right
                elif node.isRightChild():
                    node.parent.right = node.right
            elif node.getLeft():
                node.left.parent = node.parent
                if node.isLeftChild():
                    node.left.parent = node.left
                elif node.isRightChild():
                    node.parent.right = node.left
                else: node.replaceNodeData(node.right.suit,node.left.rank,\
                                           node.left.left,node.left.right)
                
                    
                
            #if node.getLeft():
                #if node.isLeftChild():
                 #   node.left.parent = node.parent
                  #  node.parent.left = node.left

                #elif node.isRightChild():
                   # node.right.parent = node.parent
                    #node.parent.right = node.right
                    
                #else:
                    #node.replaceNodeData(node.right.suit,node.left.rank,\
                        #node.left.left,node.left.right)

            else:
                if node.isLeftChild():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.isRightChild():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replaceNodeData(node.right.suit,node.right.rank,\
                        node.right.left,node.right.right)

    def preOrder(self):
        ret = ""
        if self.root is not None:
            ret += self.root.preOrder()
        return ret

    def inOrder(self):
        ret = ""
        if self.root is not None:
            ret += self.root.inOrder()
        return ret


