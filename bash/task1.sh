#!/bin/bash

echo "Hello Aidan"

multiple() {
 echo $(($1 * $2))
 return $(($1 * $2))
}

division() {
 echo $(($1 / $2))
 return $(($1 / $2))
}

addition() {
 echo $(($1 + $2))
 return $(($1 + $2))

}

subtraction() {
 echo $(($1 - $2))
 return $(($1 - $2))
}

calcNums () {

echo "calcNums"
echo "$1"
echo "$2"

clear
loop=y

while [ "$loop" = y ] ;
do

   echo "Enter the first integer :- "
   read int1

   echo "Enter the second integer :-"
   read int2

   echo "Menu"
   echo "===="
   echo "M: Multiply"
   echo "D: Divide"
   echo "A: Add"
   echo "S: Subtract"
   echo "Q: Quit"
   echo
   read choice
   case $choice in
     M | m) multiple $int1 $int2 ;;
     D | d) division $int1 $int2 ;;
     A | a) addition $int1 $int2 ;;
     S | s) subtraction $int1 $int2 ;;
     Q | q) loop=n ; echo "Goodbye" ;;
     *) echo "illegam choice" ;;
   esac
   echo
   done

}



calcNums

### CORRECT SOLUTION

### SCORE = 10 MARKS