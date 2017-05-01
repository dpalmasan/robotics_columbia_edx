# Project 1

The goal of this project was getting familiar with the Robot Operating System (ROS).


## Project Description
This assignment is meant to make sure that you are familiar with the most basic functions of ROS. Please make sure that you have completed (or at least read through) the tutorials 1-6 & 11-13.

In this assignment you are tasked with writing a node that subscribes to a topic and publishes to another. Your code will subscribe to a topic called 'two_ints', on which a custom message containing two integers can be broadcast. Make sure to familiarize yourself with the message format of this topic (have a look at the TwoInts.msg in the msg directory). Those two integers are to be added and the result published to topic 'sum' as an Int16 from std_msgs.

## Setup

* Start by running source setup_project1.sh  in the command line terminal. You should do this first every time you load or reload your workspace. You must run this command before trying to invoke any ROS commands (catkin_make, roscd, etc.). This will also start a roscore for your session. **Please do not start your own roscore.**

* Once you have sourced this script, there will be a ROS package publishing random integers to the 'two_ints' topic every two seconds.

## Implementation

You must implement your code in the file ~/catkin_ws/src/project1_solution/scripts/solution.py . This file has already been created for you and any starter code has been placed inside.


## To execute the code:
```sh
$ source setup_project1.sh
$ rosrun project1_solution solution.py
```
