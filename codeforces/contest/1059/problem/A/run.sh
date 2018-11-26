#!/bin/bash -eo pipefail

url=https://codeforces.com/contest/1059/problem/A

cd "$(dirname "${BASH_SOURCE[0]}")"

printf "\n${url}\n\n"

for i in $(seq 1 4); do
  printf "input #${i}\n"
  cat "example${i}.txt"
  printf "\n\noutput #${i}\n"
  cat "example${i}.txt" | python3 cashier.py
  printf "\n"
done

printf "input #6\n"
cat "example6.txt"
printf "\n\noutput #6\n"
cat "example6.txt" | python3 cashier.py
printf "\n"
