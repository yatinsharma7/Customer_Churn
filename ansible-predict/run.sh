#!/bin/bash


echo "***Configuring Environment, Copying files and installing dependencies ***"
ansible-playbook predict_setup.yaml
echo "***Configuring Environment, Copying files and installing dependencies - done***"

echo "***Running predict application***"
ansible-playbook predict_execute.yaml
echo "***Running predict application - done***"

echo "***Running data analysis application***"
ansible-playbook analysis_execute.yaml
echo "***Running data analysis  application - done***"


echo "Results are stored in /tmp/"
