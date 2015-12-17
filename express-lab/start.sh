#!/bin/bash

case $1 in
    (test)
    	DEBUG=express:* node app.js
    	;;
    (start)
    	node app.js
        ;;
    (*)
        echo $usage
        exit 1
        ;;
esac