#!/bin/bash

x=5

echo

rerun () {
        echo
echo "Guess the number: "
read y

echo

if [ "$x" -ne "$y" ]
then
        echo "Sorry, the number is not $y"
else
        echo "You guessed it! The number is $x"
fi

echo

echo "Do you want to play again? (yes or no)"
read answer

if [ "$answer" == "yes" ]
then
        echo
        echo "Ok, here we go!"
        rerun
else
        echo
        echo "OK, Thanks for playing!"
        echo
        exit 1
fi

}

rerun
