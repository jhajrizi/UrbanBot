# UrbanBot

A Reddit bot programmed in Python that responds to requests to define slang terms.

## Getting Started

### Prerequisites

The program has two dependencies:
   * **BeautifulSoup4** - a library for web scraping
   * **Praw** - a Python / Reddit API Wrapper
   
We can install these two dependencies by writing the following commands in our terminal:

> pip install beautifulsoup4

> pip install praw

**Note:** *You may need to add the* `sudo` *keyword before each command*.

### Installing

1. Clone this github repository onto your local machine.
2. Visit https://www.reddit.com/prefs/apps/ to create an app. Be sure to click script. The ClientID will be under the name of your application and the Client Secret can be found next to the keyword `secret`.
3. Edit the `config.py` file with your credentials.

## Running

### How to run the script

Run the script by writing the following command into your terminal:

> python bot.py

## Built With
* [Praw](https://praw.readthedocs.io/en/latest/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Authors

* **Jon Hajrizi**

## License

This project is licensed undeer the MIT License.
