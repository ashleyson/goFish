class Card:
    def __init__(self,suit,rank,left = None,right = None,parent = None):
        self.suit = suit.upper()
        self.rank = rank.upper()   
        self.parent = parent
        self.left = left
        self.right = right
        self.count = 1


    def getSuit(self):
        return self.suit
    
    def setSuit(self,suit):
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def setRank(self,rank):
        return self.rank

    def getCount(self):
        return self.count

    def setCount(self,count):
        self.count = count

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self,left):
        self.left = left
    
    def getRight(self):
        return self.right

    def hasBothChildren(self):
        return self.right and self.left

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def replaceNodeData(self,suit,rank,lc,rc):
        self.suit = suit
        self.rank = rank
        self.left = lc
        self.right = rc
        if self.getLeft():
            self.left.parent = self
        if self.getRight():
            self.right = self

    def hasAnyChildren(self):
        #return self.right or self.left
        return self.left != None and self.right != None

    def setRight(self, right):
        self.right = right
    
    def __str__(self):
        return "{} {} | {}\n".format(self.suit,self.rank,self.count)

    def __lt__(self,rhs):
        if self.rank == rhs.rank:
            return self.suit < rhs.suit
        self_rank = self.rank
        rhs_rank = rhs.rank
        #Change face cards into numbers
        if self_rank == "A":
            self_rank = "1"
        elif self_rank == "J":
            self_rank = "11"
        elif self_rank == "Q":
            self_rank = "12"
        elif self_rank == "K":
            self_rank = "13"
        #else:
          #  self_rank = self.rank


        if rhs_rank == "A":
            rhs_rank = "1"
        elif rhs_rank == "J":
            rhs_rank = "11"
        elif rhs_rank == "Q":
            rhs_rank = "12"
        elif rhs_rank == "K":
            rhs_rank = "13"
        return int(self_rank) < int(rhs_rank)

        #return self_rank < rhs_rank

    def __gt__(self,rhs):
        if self.rank == rhs.rank:
            return self.suit > rhs.suit
        self_rank = self.rank
        rhs_rank = rhs.rank
        if self_rank == "A":
            self_rank = "1"
        elif self_rank == "J":
            self_rank = "11"
        elif self_rank == "Q":
            self_rank = "12"
        elif self_rank == "K":
            self_rank = "13"
        #else:
           # self_rank = self.rank
        if rhs_rank == "A":
            rhs_rank = "1"
        elif rhs_rank == "J":
            rhs_rank = "11"
        elif rhs_rank == "Q":
            rhs_rank = "12"
        elif rhs_rank == "K":
            rhs_rank = "13"
      #  else:
       #     rhs_rank = rhs.rank
        return int(self_rank) > int(rhs_rank)

    def __eq__(self,rhs):
        try:
            if rhs!= None:
                if self.rank == rhs.rank and self.suit == rhs.suit:
                    return True
                else:
                    return False
            else:
                return False
        except AttributeError:
            return "{} {} | {}\n".format(self.suit,self.rank,self.count)

    def preOrder(self):
        ret = ''
        ret += str(self)
        if self.getLeft():
            ret += self.getLeft().preOrder()
        if self.getRight():
            ret += self.getRight().preOrder()

        return ret

    def inOrder(self):
        ret = ''
        if self is not None:
            if self.left is not None:
                ret += self.left.inOrder()
            ret += str(self)
            if self.right is not None:
                ret += self.right.inOrder()
        return ret

    def spliceOut(self):
        if not self.hasAnyChildren():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
            
        elif self.hasAnyChildren():
            if self.getRight():
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
