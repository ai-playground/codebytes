import argparse
from codebytes.linkedlist import ListNode, List

if __name__=="__main__":
    print("helloworld")

    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--i1', action='store', type=int, required=True)
    my_parser.add_argument('--i2', action='store', type=int)
    args = my_parser.parse_args()

    f1 = ListNode(args.i1)
    f2 = ListNode(args.i2)
    L1 = List()
    #L1.print()
    L1.insert(args.i1)
    #L1.print()
    L1.insert(args.i2)
    L1.print()
