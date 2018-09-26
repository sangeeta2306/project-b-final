#!/bin/bash
echo "Inside the application"
cd projectB
ng build
echo "Application build successfully. Starting Node server."
node server


