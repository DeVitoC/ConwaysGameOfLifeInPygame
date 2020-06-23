# ConwaysGameOfLifeInPygame

Conways's game of life is a zero player game, used widely across many technical fields to simulate the
emergence of patterns. The earliest form of the Game of Life was developed by John Neumann in 1940.
At that time, this was just a theoretical concept, although he and others attempted to create this
Game of life using the technology of their time with little success. Then after the development of
computers, John Conway began developing this idea for computers. Starting work on it in 1968, he
successfully completed his first version of this in 1970.

This game follows several simple rules, including:
    1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    2. Any live cell with two or three live neighbors lives to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

In my implementation of Conway's Game of Life, I have implemented several of the common structures and
patterns discovered over the years in the Game of Life. These include:
    1. In the first option, a randomized screen which over time should settle on some stable pattern based
        on the random start
    2. In the second option, this app demonstrates a Gosper Glider Gun, which will perpetually generate
        gliders
    3. In the third option, this demonstrates a constructor
    4. In the fourth option, this shows many different stable patterns, including:
        Top to bottom on the left: Block, Bee-hive, Loaf, Boat, Tub
        Tob to bottom on the right: *Period 2 Oscillators* Blinker, Toad, Beacon
                                    *Period 3 Oscillator* Pulsar
    5. In the fifth option, this shows a few more spacechips (the glider in the Gosper Glider Gun is
        considered a spaceship)
        Top to bottom both directions: Light-weight spaceship, Middle-weight spaceship, and Heavy-weight spaceship

Key Commands in Conway's Game of Life:
    1.  'p' - Toggles between play and pause
    2.  '1' - Starts over with preset one (Random)
    3.  '2' - Starts over with preset two (Gosper's Glider Gun)
    4.  '3' - Starts over with preset three (Constructor)
    5.  '4' - Starts over with preset four (Stable Shapes)
    6.  '5' - Starts over with preset five (Spaceships)
    7.  '-' - Decreases the speed of the game
    8.  '=' - Increases the speed of the game
    9.  'q' - Quits to the main screen
