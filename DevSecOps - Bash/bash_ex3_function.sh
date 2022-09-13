#!/bin/bash

#function string_contains {
#  echo $1
#  echo $2
#  if [[ "$1" == *"$2"* ]]; then
#    echo 'true'
#    RETURN=0
#    echo $RETURN
#    else
#      echo 'false'
#      RETURN=1
#      echo $RETURN
#  fi
#}

function empty_null {
  if [[ $1 == " " || $1 == "null" ]]; then
    echo 'true'
    RETURN=0
    echo $RETURN
    else
      echo 'false'
      RETURN=1
      echo $RETURN
    fi

}

#string_contains "abcefgd" "abcefg"

# Given a string $str, return the substring beginning at index $start and ending at index $end.
# Use ${str:4:10} to the get substring of $str from index 4 to 10
# Example:
#
# string_substr "hello world" 0 5
#   Returns "hello"

empty_null "null"

STR=$1
START=$2
END=$3

function hello_world {

  if [[ $STR=" " || $(); then
    echo 'Not a good string'
  }

