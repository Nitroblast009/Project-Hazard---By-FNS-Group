# Project Hazard

*Code by Fazaan, Sarim, and Ninghan.*
*Art by Janna and Nouran.*

- [Introduction](#introduction)
    * [Project Description](#project-description)
    * [Computer Requirements](#computer-requirements)
- [Help Documentation](#help-documentation)
  * [Getting Started](#getting-started)
  * [Main Gameboard](#main-gameboard)
    + [Americas Map](#americas-map)
    + [Afroeurasia Map](#afroeurasia-map)
    + [All Map](#all-map)
  * [Game Phases](#game-phases)
  * [Winning and Miscellaneous](#winning-and-miscellaneous)
- [Installation Instructions](#installation-instructions)
  * [Playing on Itch.io](#playing-on-itchio)
  * [Playing on Local Computer](#playing-on-local-computer)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


---
## Introduction

### Project Description

Our goal is to provide a fun outlet for youth to exercise their strategic planning skills, bond with their peers, and improve their knowledge of game theory through innovating the well-known board game, Risk, into a digital format. In terms of business objectives, we plan on selling this game virtually using an online game store known as itch.io.

![logo](https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group/blob/main/hazard%20logo.png)


### Computer Requirements

An internet connection is required to play our game on itch.io. If downloading project locally from this repository, Python and Pygame must be installed and it is recommended to have at least 4GB of RAM. *(See installation instructions below for more details)*

# Help Documentation

The following serves as an aid for new users with how to play our game. For raw code documentation, please look through our python scripts in this repository (start at `game_board.py`). For any follow-up inquiries or concerns, please feel free to email 736971@pdsb.net. 

> [Video demonstration link](https://drive.google.com/file/d/1e4ZtcCoeQs-86lmj2cSRGgAxtWybpeBF/view?usp=sharing)

## Getting Started

When you first open the game you will be greeted to the following menu screen, where you can move the cursor up and down using the UP and DOWN arrow keys. To select an item hit ENTER.

![menu screen](https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group/blob/main/menu%20screen.png)

If you are selecting the **Start** option, you will need to hit ENTER twice to confirm that you are ready to start the game.

Selecting **Characters** will bring you to a menu where you can select which character each player would like to play as. For the time being, selecting your character is purely for aesthetics, but in the future we plan to add character-specific features. Hit BACKSPACE to return to the main screen.

Selecting **Credits** will take you to our About Us page, where you can read more about the amazing Grade 12 computer science students behind this game! Hit BACKSPACE to return to the main screen.

## Main Gameboard

Upon selecting **Start**, you will be taken to the main gameboard where you will play on your selected map. The current 3 maps available to play on are the *Americas*, *Afroeurasia*, and *All*. Images of our maps below in respective order...

### Americas Map
![americas map](https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group/blob/main/americas%20map.png)
### Afroeurasia Map
![afroeurasia map](https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group/blob/main/afroeurasia%20map.png)
### All Map
![all map](https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group/blob/main/all%20map.png)

> Note: Even though our game is capable of supporting multiple maps, there is no UI option to select which map you want to play on. To change which map the game should be set to, change the `map` variable at the beginning of `main.py` to either "All", "Americas", or "Afroeurasia". 

A couple important details about the gameboard:
- All countries on the map are randomly divided among Player 1 and 2. Red countries belong to Player 1, and blue countries belong to Player 2.
- To select a country you own or are attacking, simply click on it. At the bottom of the screen is text indicating which country is currently selected as well as how many troops it has. The selected country's hue will also darken.
- Each country randomnly has between 1-5 troops, however the odds are more weighted towards giving countries lower amounts of troops.
- On the right of the screen is the gamebar, which states whose turn it currently is, as well as what phase of the game they are in (see game phases section below for more details). When selecting a country, a confirm prompt will also pop up on this gamebar.
- In the case of an emergency, you can exit the game by clicking the X icon in the top right of the screen.

## Game Phases

Each player's turn is divided into three phases in the following order...
1. **Draft Phase:** The player is given 2 troops to add to an ally country. After selecting a country and seeing the confirm prompt, hit ENTER to the add troops and move to next phase.
2. **Attack Phase:** The player has the choice to attack an enemy country. First, select which ally country you want to attack with and hit ENTER after seeing the confirm prompt. Second, choose which neighbouring enemy country you want to attack and hit ENTER after seeing another confirm prompt. **See note below*
3. **Fortify Phase:** The player can choose to take all but 1 troops from an ally country and give them to a neighbouring ally country. First, select which ally country to take troops from and hit ENTER after seeing the confirm prompt. Second, choose the country you want to give the troops to and hit ENTER after seeing another confirm prompt. After completing this phase, the player's turn is over and the next player starts their turn at the **Draft Phase**.

> **Attack Phase Note:*

> Case 1) If the attacking country has more troops than the defending country, the attacking country will be left with 1 troop and the defending country will be left with the difference of both countries' original troops as well as switch player ownership.

> Case 2) If the attacking country has the same or less troops, then either Case 1) will take place in reverse and the attacking country will be taken over by the defending country, or all but 1 of the attacking country's troops will be lost.*

## Winning and Miscellaneous

To win the game, a player must own all countries on the map. This is checked at the end of each **Fortify Phase** and if a winner has been found, the following winning screen will pop up...

![win screen](https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group/blob/main/win%20screen.png)

It is also important to note that once a game has started it cannot end unless a player wins or the game window is forcefully quitted. For the time being, it is also impossible to unselect a country, meaning that if you select a country to attack with that has no neighbouring enemy countries, you have essentially soft-locked yourself. Lastly, all maps in this game are based on real world maps of the Earth, however the geography and nomenclature of countries have been somewhat simplified due to our project's constraints. Below is a hollowed image of the "All" map...

![all map hollow](https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group/blob/main/Project%20Hazard%20World%20Map%20Outline%20-%20CS.G12S1%20(1).png)

# Installation Instructions

## Downloading from Itch.io
Using a web browser, located your way onto the Itch.io website and search for the game called "Hazard" (https://risky-fns.itch.io/hazard). Once located, click on the pink "Download button". This will download a zip file with all the needed component to run the game.

## Playing on Local Computer
After downloading the needed components, extract the files into replit and click the run button. Just like that, you're ready to play :D
