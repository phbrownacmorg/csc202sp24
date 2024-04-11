from turtle import Turtle
import math

def draw_triangle(t: Turtle, side: float) -> None:
    """Draws a filled triangle of side SIDE.  Leaves turtle T
    in the same position, same heading as at the beginning."""
    t.begin_fill()
    for i in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()

def sierpinski(t: Turtle, side: float, level: int) -> None:
    """Draw a Sierpinski triangle, recursively.  The function first
    sets the fillcolor according to the level and draws the big
    triangle.  Then, if level > 0, it recursively draws Sierpinski
    triangles in each of its own corners."""
    fillcolors = ['blue', 'red', 'green', 'white', 'yellow', 'pink']
    # Pre:
    assert (0 <= level < len(fillcolors)) and (side > 2**level)
    t.fillcolor(fillcolors[level])
    draw_triangle(t, side)
    if level > 0:
        for i in range(3):
            sierpinski(t, side/2, level-1)
            t.forward(side)
            t.left(120)

def main(args: list[str]) -> int:
    t: Turtle = Turtle()
    t.speed(0)
    t.up()
    t.goto(-200, -150)
    t.down()

    sierpinski(t, 400, 5)

    t.screen.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))