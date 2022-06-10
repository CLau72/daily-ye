# The Daily Ye

## Overview

The Daily Ye is fun little tool to text out Kanye West quotes every morning.
This is mostly a little project to practice with API calls to:

- [The Kanye West API](https://kanye.rest)
- [Twilio](https://www.twilio.com/)

## Requirements

- Your own Twilio account for using the API

## Environment Variables

The script allows you to pass in environment variables for API keys using a **.env** file in the root directory. To use this, create your own **.env** file, and add in all the required variables.

|Environment Variable|Required?|Description|
|-|-|-|
|TWILIO_SID| [x] |Twilio Account SID value|
|TWILIO_API| [x] |Twilio API Key|
|FROM_PHONE| [x] |Phone number provided by Twilio to send the text message|
|TO_PHONE| [x] |Phone number of the phone receiving the message|

![Ya boi Yeezy](https://64.media.tumblr.com/dae084312804cbdb256709a5d54e41a3/tumblr_n2x8i2gBxl1toat5eo4_250.gif)
