#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2020
# This program is the Towers of Hanoi program


def hanoi(ndisks, startPeg=1, endPeg=3):
    # this is the recursive Towers of Hanoi solution

    if ndisks == 1:
        print("Move disk 1 from peg %d to peg %d" % (startPeg, endPeg))
    else:
        hanoi(ndisks - 1, startPeg, 6 - startPeg - endPeg)
        print("Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg))
        hanoi(ndisks - 1, 6 - startPeg - endPeg, endPeg)

def main():
    # this function solves the Towers of Hanoi problem

    # input
    print("Towers of Hanoi program\n")
    number_of_disks = int(input("How many disks would you like in your tower (1->): "))

    # process
    hanoi(ndisks=number_of_disks)

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
