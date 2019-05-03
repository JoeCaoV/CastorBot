Welcome to programm : CASTORBOT

This application is a website locally hosted using Flask, containing a single page.

On this page, you will find a form, where you can ask an address of anything to Castor Bot.

CastorBot will then tell you the address of what you want, display a map and tell a story about the place.

HOW TO USE IT : 

You need to clone this repository and install every module listed in the requirements.txt file

It use Google Map Api, so you will need an API KEY check how to get one here :[Get API KEY](https://cloud.google.com/maps-platform/?__utma=102347093.1697458079.1555141234.1556920707.1556920707.1&__utmb=102347093.0.10.1556920707&__utmc=102347093&__utmx=-&__utmz=102347093.1556920707.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)&__utmv=-&__utmk=125501834&_ga=2.35043297.1518247953.1556381667-1697458079.1555141234#get-started)

Then in the config.py file, please replace "YOUR_API_KEY" by your actual key

To start the program, execute the Run.py file with Python3, then go on http://127.0.0.1:5000/ with your web browser.

DEVELOPER GUIDE:

If you wish to test your code, there is a test.py file in Papybot/tests/

To run the tests, execute "python -m papybot.tests.test" from the root folder