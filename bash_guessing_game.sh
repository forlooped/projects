#!/bin/bash

echo
# Welcome your player :)
echo "Hi there! What is your name?"
read name
echo
echo "Welcome to the game, $name!"

# Choose the number for players to guess
x=5
echo

# function to run game
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
        echo "OK, Thanks for playing, $name!"
        echo
        exit 1
fi
}

rerun
