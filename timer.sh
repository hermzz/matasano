#!/bin/env bash

REPS=10

for script in e*.py; do
	echo -n "$script: "
	CMD="for i in {1..$REPS}; do time ./$script; done 2>&1 | grep ^real | sed -e s/.*m// | awk '{sum += \$1} END {print sum / NR}'"
	eval "$CMD"
done