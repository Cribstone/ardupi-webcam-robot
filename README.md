ardupi-webcam-robot
===================

A web controllable tracked robotic chassis with pan/tilt webcam controlled by Arduino, Raspberry Pi and node.js

 As of writing (3/1/13) this is still very much a work in progress, but most of the hardware construction has been completed. This robot will provide a remotely controlled, mobile platform for a pan/tilt webcam. It is based on the excellent Tamiya Tracked Chassis Kit with the Dual DC Motors connected to the Arduino Motor Shield R3 via the Screw Terminal. The Pan/Tilt function is provided by two Tinkerkit Servos which also allows them to be connected to the Motor Shield without taking up additional pins. The webcam is connected via USB to the Raspberry Pi and streamed to an online server using MJPG-Streamer and an Edimax wifi dongle. Control for the Arduino can be provided via Bluetooth Bee, or XBee but the eventual goal is to connect and control the Arduino from the Raspberry Pi. As the RPi USB ports will be filled up with the webcam and wifi, connection will likely be achieved via GPIO.
This repository will contain Sketches for the Arduino, Programs on the Raspberry Pi for webcam streaming and various methods of controlling the hardware via web-based interface, bluetooth or XBee
Follow or contribute to project development via the project wiki-https://github.com/Cribstone/ardupi-webcam-robot/wiki
Visit the Project Profile on "Let's Build Robot's"- http://letsmakerobots.com/node/36345

