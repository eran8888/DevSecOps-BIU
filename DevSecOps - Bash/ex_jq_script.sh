#!/bin/bash

# checking JQ package is installed and if not requests to install it
command -v jq > /dev/null
if [ "$?" -ne 0 ]
then
  echo 'JQ command does not exists. Please download https://stedolan.github.io/jq/download'
  else echo 'JQ package already exists'
fi

#Checks that the prompted IP is legit and not localhost

if [[ $# -ne 1  || "$1" = "127.0.0.1" ]]; then
  echo 'Failed localhost and 2 IP are not allowed'
  exit 1
fi

if expr "$1" : '[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$' >/dev/null; then
  for i in 1 2 3 4; do
    if [ $(echo "$1" | cut -d. -f$i) -gt 255 ]; then
      echo "fail ($1)"
      exit 1
    fi
  done
  echo "success ($1)"
  Response=$(curl -s http://ip-api.com/json/$1)
  echo $Response
  echo $Response | jq -r '.status'
  echo "exit code is ($?)"

  if [[ "$?" -eq 0 ]]; then
    echo $Response | jq -r '.country , .city , .regionName'
    else
    exit 1
  fi

  exit

else
  echo "fail"
  exit 1

fi

