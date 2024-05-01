import copy
from AbstractCard import AbstractCard
from PlayingCard import PlayingCard

def check_aliasing(name1: str, name2: str, 
                  val1: list[list[AbstractCard]], 
                  val2: list[list[AbstractCard]]) -> None:
    print(f'{name1} aliases {name2}?', val1 is val2)
    print(f'{name1} equals {name2}?', val1 == val2)
    print(f'{name1}[0] aliases {name2}[0]?', val1[0] is val2[0])
    print(f'{name1}[0] equals {name2}[0]?', val1[0] == val2[0])
    print(f'{name1}[0][0] aliases {name2}[0][0]?', val1[0][0] is val2[0][0])
    print(f'{name1}[0][0] equals {name2}[0][0]?', val1[0][0] == val2[0][0])
    print()

def main(args: list[str]) -> int:
    list1: list[list[AbstractCard]] = \
        [[PlayingCard.makeCard('king', 'hearts')]] 

    list2 = list1 # Direct alias
    check_aliasing('list1', 'list2', list1, list2)
    list3 = list1[:] # Shallow copy
    check_aliasing('list1', 'list3', list1, list3)
    list4 = copy.deepcopy(list1)
    check_aliasing('list1', 'list4', list1, list4)

    print('Call a method on list2[0]...')
    print('list2[0][0]:', list2[0][0])
    list1[0].insert(0, PlayingCard.makeCard('7','diamonds'))
    print('list2[0][0]:', list2[0][0])
    check_aliasing('list1', 'list2', list1, list2)
    print('list3[0][0]:', list3[0][0])
    check_aliasing('list1', 'list3', list1, list3)
    print('list4[0][0]:', list4[0][0])
    check_aliasing('list1', 'list4', list1, list4)

    print(list1[0][0])
    print('Insert into list1...')
    list1.insert(0,[PlayingCard.makeCard('ace', 'spades')])
    print('list2[0][0]:', list2[0][0])
    check_aliasing('list1', 'list2', list1, list2)
    print('list3[0][0]:', list3[0][0])
    check_aliasing('list1', 'list3', list1, list3)
    print('list4[0][0]:', list4[0][0])
    check_aliasing('list1', 'list4', list1, list4)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))