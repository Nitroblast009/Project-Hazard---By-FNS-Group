from country import Country
import random


# Americas Countries/Provinces
Greenland = Country("Greenland", ((240, 90), (240, 10), (310, 10), (310, 90)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

Nuvuk = Country("Nuvuk", ((20, 20), (10, 50), (50, 40)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

Alaska = Country("Alaska", ((10, 50), (30, 120), (50, 40)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Northwest = Country("Northwest", ((50, 40), (20, 170), (150, 50)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
BritishColumbia = Country("BC", ((80, 120), (20, 170), (70, 240)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Nunavut = Country("Nunavut", ((150, 50), (80, 120), (160, 110)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Alberta = Country("Alberta", ((80, 120), (70, 240), (160, 110)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Ontario = Country("Ontario", ((160, 110), (70, 240), (160, 230)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Quebec = Country("Quebec", ((160, 110), (160, 230), (230, 190)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
PEI = Country("PEI", ((160, 110), (230, 190), (250, 140)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Newfoundland = Country("Newfoundland", ((220, 80), (190, 120), (250, 140)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

Mexico = Country("Mexico", ((70, 240), (150, 330), (140, 230)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Caribbeans = Country("Caribbeans", ((160, 290), (180, 310), (190, 270)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

Ecuador = Country("Ecuador", ((150, 330), (100, 380), (150, 380)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Columbia = Country("Columbia", ((150, 330), (150, 380), (190, 340)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Venezuela = Country("Venezuela", ((190, 340), (150, 380), (220, 380)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Peru = Country("Peru", ((100, 380), (90, 420), (180, 490)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Brazil = Country("Brazil", ((100, 380), (180, 490), (220, 380)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Chile = Country("Chile", ((110, 440), (80, 530), (180, 490)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Argentina = Country("Argentina", ((180, 490), (80, 530), (150, 550)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

# Afroeurasia Countries

UK = Country("UK", ((280, 190), (280, 120), (320, 120), (320, 190)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
France = Country("France", ((310, 200), (290, 300), (380, 270)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Germany = Country("Germany", ((360, 180), (310, 200), (380, 270)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Scandinavia = Country("Scandinavia", ((450, 80), (350, 120), (380, 270)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

Turkey = Country("Turkey", ((410, 190), (380, 270), (460, 250)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Egypt = Country("Egypt", ((290, 300), (330, 310), (380, 270)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Nigeria = Country("Nigeria", ((380, 270), (330, 310), (360, 420)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Ethiopia = Country("Ethiopia", ((380, 270), (360, 420), (410, 380)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
SaudiArabia = Country("Saudi Arabia", ((380, 270), (400, 350), (460, 250)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Madagascar = Country("Madagascar", ((420, 430), (420, 370), (450, 370), (450, 430)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

Ukraine = Country("Ukraine", ((450, 80), (410, 190), (500, 150)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Siberia = Country("Siberia", ((450, 80), (500, 150), (510, 90)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
FarEast = Country("Far East", ((510, 90), (500, 150), (620, 110)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
China = Country("China", ((560, 130), (410, 190), (540, 210)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Korea = Country("Korea", ((560, 130), (540, 210), (570, 200)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
India = Country("India", ((410, 190), (500, 300), (540, 210)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Japan = Country("Japan", ((580, 260), (580, 180), (610, 180), (610, 260)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

Indonesia = Country(
    "Indonesia", ((490, 330), (490, 310), (510, 310), (510, 330)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Philippines = Country(
    "Philippines", ((550, 350), (550, 330), (620, 330), (620, 350)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
Australia = Country(
    "Australia", ((500, 430), (500, 370), (600, 370), (600, 430)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))
NewZealand = Country(
    "New Zealand", ((570, 470), (570, 440), (620, 440), (620, 470)), random.choice(["p1", "p2"]), random.choice([1,2,2,3,4,5]))

#Attack list




