#! /bin/bash

set -e  

for f in days/*/test_day.py; do
  python $f
done
