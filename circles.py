from turtle import Turtle
import random

def draw_archery_ring(t: Turtle, radius: float, width: float) -> None:
    """Draw an archery target of radius RADIUS with ring width WIDTH."""
    # Base case: draw the circle
    pencolors = ['black', 'black', 'black', 'white', 'black']
    fillcolors = ['yellow', 'red', 'blue', 'black', 'white']
    t.pencolor(pencolors[(radius - width) // (2*width)])
    t.fillcolor(fillcolors[(radius - width) // (2*width)])
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    if radius > width: # Recursive case
        # Move the turtle upwards by the width
        t.up()
        t.left(90)
        t.forward(width)
        t.right(90)
        t.down()

        draw_archery_ring(t, radius - width, width)

def draw_ring(t: Turtle, radius: float, width: float, 
              color: str, altcolor: str) -> None:
    """Draw concentric circles of radius RADIUS down to radius WIDTH, using 
    alternatig colors COLOR and ALTCOLOR."""
    # Draw the circle (done in all cases)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    if radius > width: # Recursive case
        # Move the turtle upwards by the width
        t.up()
        t.left(90)
        t.forward(width)
        t.right(90)
        t.down()

        draw_ring(t, radius - width, width, altcolor, color)


def draw_double_circle(t: Turtle, radius: float, min_size: float, 
                       color: str, altcolor: str) -> None:
    """Draw a circle of radius RADIUS with two circles of radius RADIUS/2
    inscribed in it, recursively until RADIUS <= MIN_SIZE.  Alternate fill
    colors between COLOR and ALTCOLOR."""
    # Draw the circle (base case and recursive case)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    if radius > min_size: # Recursive case
        draw_double_circle(t, radius/2, min_size, altcolor, color)
        # Move the turtle up by half a radius
        t.up()
        t.left(90)
        t.forward(radius)
        t.right(90)
        t.down()
        draw_double_circle(t, radius/2, min_size, altcolor, color)
        # Put the turtle back to the bottom
        t.up()
        t.left(90)
        t.backward(radius)
        t.right(90)
        t.down()



def main(args: list[str]) -> int:
    t: Turtle = Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.right(90)

    #draw_archery_ring(t, 300, 30)
    #draw_ring(t, 300, 10, 'purple', 'gold')
    draw_double_circle(t, 300, 3, 'purple', 'gold')

    t.screen.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))