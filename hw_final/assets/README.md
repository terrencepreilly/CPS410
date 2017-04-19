# Lazer Blast
"Lazer Blast" is an arcade style shooter (like
[Galaga](https://en.wikipedia.org/wiki/Galaga)), which includes
aspects of color matching and pattern matching.

## Running
To install and run the game, clone this repository and `cd` into
it in a terminal.  Then, run:

```
python3 setup.py install
```

You can then enter the command,

```
lazerblast
```

And the game will start.

## Game-play
The user pilots a small ship against hoards of enemies.  Each enemy
has a given color.  The player must use a similar-colored laser to
destroy that enemy.  For example, an enemy which is green much be
shot with a green laser.  A red laser will have no effect.  Waves of
enemies come in patterns: an astute fighter will be able to predict
the next wave from the previous, and will have a significant
advantage over the enemy.

Since the player cannot be expected to handle the copious masses
of colorful enemies immediately, the difficulty of the game increases
as the player progresses, starting with a single color and slowly
adding other colors and increasing the speed.

## Development

1. Clone the repository.


2. Install the requirements and game:
    ```
    pip install -r requirements.txt
    python3 setup.py develop
    ```
  *NB.* In the future, the requirements should be handled by the
  setup file.

3. Run the game:
    ```
    lazerblast
    ```

*NB.* Using a `virtualenv` would be preferable, but it does not
work (at least, not on a mac.)  See [this](https://bitbucket.org/pygame/pygame/issues/203/window-does-not-get-focus-on-os-x-with)


## Running Tests

Tests are run with the `pytest` runner through the setup utility:

```
python3 setup.py test
```
