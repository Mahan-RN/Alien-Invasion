# Alien-Invasion :alien: :rocket: :statue_of_liberty:
A Python-based 2D arcade shooter game made with Pygame
# 1- Introduction
Alien Invasion is my first Python project, based on Python Crash Course (3rd Edition)[1], with some minor visual tweaks for more appealing gameplay visuals and (very basic) static type checking using Pyright[2].

## Gameplay :video_game:
Here's a sample gameplay:

![Sample Gameplay](sample_gameplay.gif)

### Controls
- **Movement:** left :arrow_left: and right :arrow_right: arrow keys
- **Shooting:** space key
- **Exit:** `Q` key


# 2- Learning & Reflections
My primary goal from making Alien Invasion was to learn Python and apply the concepts that I learned in a small project. Here's a summary of things I learned and noticed as a computer science student:

## What I Learned and Demonstrated
1. Syntax, Primitives, Functions, Basic Data Structures
2. Object Oriented Python
3. Using External Libraries, and Reading Their Documentation
4. Static Type Checking using Pyright

## Limitations and Improvements
This project was implemented according to Python Crash Course's instructions. Although I really enjoyed it, as a 2nd-year computer science student there were some poor design choices that I noticed:
1. **Tests, Tests, Tests:** this project lacks unit tests. This makes it difficult to maintain, modify, or extend. I am a firm believer in unit tests and I think even the smallest projects should be thoroughly tested.
2. **Separating Game Logic from UI:** cleaner separation of game logic and UI would allow for easier testing, maintenance, and code comprehension. 
3. **Coupling and Cohesion:** this directly ties to my previous point. I think coupling could be reduced by thinking more carefully about the classes making up the game and their relationships with each other. The code related to the game logic and UI are also mixed together in some classes, reducing cohesion. For example, the main class `AlienInvasion` has way too many helpers that could be refactored into other classes that model the game to increase cohesion.
4. **Strict Type Checking:** I used Pyright in the basic mode and only scratched the surface of what it's really capable of. A more rigorous type checking would be better.



# 3- Resources:
[1] Matthes, E. (2023). *Python crash course: a hands-on, project-based introduction to programming*. 3rd edition. No Starch Press.\
[2] https://github.com/microsoft/pyright 

All gameplay art used in this project is copyright-free.
- Spaceship art: https://opengameart.org/content/purple-space-ship
- Bullet art: https://opengameart.org/content/pixel-bullet
- Alien art: https://opengameart.org/content/space-shooter-top-down-2d-pixel-art \
(*Note: directly using the alien image provided in the link above was causing "libpng warning: iCCP: known incorrect sRGB profile" warning when running the game, which I fixed by using https://www.cmyk2rgb.com/ and selecting the sRGB profile*)
- Background art:  https://craftpix.net/freebies/free-sky-with-clouds-background-pixel-art-set/
