#!/bin/bash
ansible all -m ping -u root 
ansible all -m shell -a "echo test>t.py" 
ansible all -m shell -a 'echo ${HOME}' 
ansible all -m copy -a 'src=~/Documents/workspace/adesk/adesk-webapp-template/js/adesk-webapp-template.js   dest=~/workspace/picasso-server'
ansible all -m shell -a "cd ~/workspace/picasso-server && git status"
ansible all -m apt -a "name=python state=present" --ask-become-pass
