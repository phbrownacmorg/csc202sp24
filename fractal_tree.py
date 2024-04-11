from turtle import Turtle
import random

def draw_tree(t: Turtle, length: float) -> None:
    diff: float = 15
    angle: float = 20
    if length > 0:
        oldwidth = t.width()
        t.width(max(length // diff, 1))
        oldcolor = t.pencolor()
        if length < 2 * diff:
            t.pencolor('green')
        else:
            t.pencolor('brown')
        
        t.forward(length)
        angle_R = random.uniform(0.5 * angle, 1.5 * angle)
        t.right(angle_R)
        draw_tree(t, (length - diff) * (1 + random.uniform(-0.1, 0.1)))
        angle_L = random.uniform(angle * 0.5, angle * 1.5)
        t.left(angle_R + angle_L)
        draw_tree(t, (length - diff) * (1 + random.uniform(-0.1, 0.1)))

        # Restore original turtle condition
        t.right(angle_L) # Return to original heading
        t.backward(length) # Back to original position
        t.pencolor(oldcolor) # Restore original color
        t.width(oldwidth)

def main(args: list[str]) -> int:
    t: Turtle = Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()

    draw_tree(t, 100)

    t.screen.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))