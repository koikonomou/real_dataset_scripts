#!/bin/bash
for i in {1..225}
do
	python json_to_dataset.py "$i/rgb0.json"
	python json_to_dataset.py "$i/rgb1.json"
done