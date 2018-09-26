#!/bin/bash
echo "Welcome"
echo "Cloning data from git"
git clone https://github.com/sangeeta2306/projectB.git
echo "Inside the application"
cd projectB
npm install
if [ $? -ne 0 ]; then
echo "CRITICAL: node modules could not be downloaded. Aborting"
exit 1
fi 
exit 0

