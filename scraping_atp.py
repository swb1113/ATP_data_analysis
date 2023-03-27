from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

from atp_scrape_function import atp_scraper

atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=11433&tab=profile", "halys.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=6200&tab=profile", "otte.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=11553&tab=profile", "mmoh.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=5902&tab=profile", "fucsovics.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=25608&tab=profile", "ivashka.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=6317&tab=profile", "oconnell.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=11415&tab=profile", "thompson.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=4921&tab=profile", "fognini.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=23588&tab=profile", "riveros.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=6031&tab=profile", "kudla.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=6051&tab=profile", "cecchinato.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=5863&tab=profile", "gomez.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=11164&tab=profile", "zhang.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=6409&tab=profile", "kokkinakis.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=26647&tab=profile", "purcell.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=5476&tab=profile", "bagnis.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=6412&tab=profile", "garin.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=26959&tab=profile", "altmaier.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=6184&tab=profile", "dellien.csv")
atp_scraper("https://www.ultimatetennisstatistics.com/playerProfile?playerId=4526&tab=profile", "wawrinka.csv")