from Card import Card
from PlayerHand import PlayerHand

def test_isEmpty():
    hand = PlayerHand()
    assert hand.isEmpty() == True
    assert hand.getTotalCards() == 0
    hand.put('D','A')
    assert hand.getTotalCards() == 1
    hand.put('C','7')
    hand.put('S','K')
    assert hand.getTotalCards() == 3
    assert hand.isEmpty() == False

def test_getTotalCards():
    hand = PlayerHand()
    hand.put('D', '7') 
    hand.put('D', '4') 
    hand.put('D', '5') 
    hand.put('C', '3')
    assert hand.getTotalCards() == 4
    
def test_deleteRoot():
    hand = PlayerHand()
    hand.put('D', '7') 
    hand.put('D', '4') 
    hand.put('D', '5') 
    hand.put('C', '3') 
    hand.put('C', '2') 
    hand.put('H', '9') 
    hand.put('H', '8') 
    hand.put('S', 'K')
    assert hand.getTotalCards() == 8
    hand.delete('D', '7')
    assert hand.getTotalCards() == 7
    assert hand.isEmpty() == False

def test_deleteLeafNode():
    hand = PlayerHand()
    hand.put('D', '7') 
    hand.put('D', '4') 
    hand.put('D', '5') 
    hand.put('C', '3') 
    hand.put('C', '2') 
    hand.put('H', '9') 
    hand.put('H', '8') 
    hand.put('S', 'K') 
    hand.delete('C', '2')

def test_duplicateCards():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', '7')
    assert hand.getTotalCards() == 2
    assert hand.preOrder() == \
    "D A | 1\n\
S 7 | 1\n"

    
def test_inOrder():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')

    assert hand.inOrder() == \
    "D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"
    hand.delete('D', 'A')
    assert hand.getTotalCards() == 6
    assert hand.isEmpty() == False


def test_getSuccessor():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')

    assert hand.getTotalCards() == 7
    assert hand.isEmpty() == False
    hand.delete('S', '2')
    assert hand.getTotalCards() == 6
    assert hand.getSuccessor('H', '7') == None
    assert hand.getSuccessor('S', 'K') == None
    assert hand.getSuccessor('D', 'A') == 'S K | 2'

def test_delTwoChildren():
    hand = PlayerHand()
    hand.put('D', '8')
    hand.put('D', '6')
    hand.put('D', '5')
    hand.put('D', '7')
    hand.put('D', '9')
    assert hand.inOrder() == \
    "D 5 | 1\n\
D 6 | 1\n\
D 7 | 1\n\
D 8 | 1\n\
D 9 | 1\n"
    hand.delete('D', '6')
    assert hand.inOrder() == \
    "D 5 | 1\n\
D 7 | 1\n\
D 8 | 1\n\
D 9 | 1\n"


    
