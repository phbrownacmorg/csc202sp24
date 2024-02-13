import tkinter as tk
from _typeshed import Incomplete
from typing import Any, Callable, Optional

class GraphicsError(Exception): ...

OBJ_ALREADY_DRAWN: str
UNSUPPORTED_METHOD: str
BAD_OPTION: str

def update(rate: float | None = ...) -> None: ...

class GraphWin(tk.Canvas):
    foreground: str
    items: list[GraphicsObject]
    mouseX: Optional[int]
    mouseY: Optional[int]
    height: int
    width: int
    autoflush: bool
    trans: Optional[Transform]
    closed: bool
    lastKey: str
    def __init__(self, title: str = ..., width: int = ..., height: int = ..., autoflush: bool = ...) -> None: ...
    def setBackground(self, color: str) -> None: ...
    def setCoords(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def close(self) -> None: ...
    def isClosed(self) -> bool: ...
    def isOpen(self) -> bool: ...
    def plot(self, x: float, y: float, color: str = ...) -> None: ...
    def plotPixel(self, x: float, y: float, color: str = ...) -> None: ...
    def flush(self) -> None: ...
    def getMouse(self) -> Point: ...
    def checkMouse(self) -> Optional[Point]: ...
    def getKey(self) -> str: ...
    def checkKey(self) -> str: ...
    def getHeight(self) -> int: ...
    def getWidth(self) -> int: ...
    def toScreen(self, x: float, y: float) -> tuple[int, int]: ...
    def toWorld(self, x: int, y: int) -> tuple[int, int]: ...
    def setMouseHandler(self, func: Callable[[tk.Event], None]) -> None: ...
    def addItem(self, item: GraphicsObject) -> None: ...
    def delItem(self, item: GraphicsObject) -> None: ...
    def redraw(self) -> None: ...

class Transform:
    xbase: float
    ybase: float
    xscale: float
    yscale: float
    def __init__(self, w: int, h: int, xlow: float, ylow: float, xhigh: float, yhigh: float) -> None: ...
    def screen(self, x: float, y: float) -> tuple[int, int]: ...
    def world(self, xs: int, ys: int) -> tuple[float, float]: ...

DEFAULT_CONFIG: dict[str, Any]

class GraphicsObject:
    canvas: Optional[GraphWin]
    id: int
    config: dict[str, Any]
    def __init__(self, options: list[str]) -> None: ...
    def setFill(self, color: str) -> None: ...
    def setOutline(self, color: str) -> None: ...
    def setWidth(self, width: float) -> None: ...
    def draw(self, graphwin: GraphWin) -> GraphicsObject: ...
    def undraw(self) -> None: ...
    def move(self, dx: float, dy: float) -> None: ...

class Point(GraphicsObject):
    setFill: Incomplete
    x: float
    y: float
    def __init__(self, x: float, y: float) -> None: ...
    def clone(self) -> Point: ...
    def getX(self) -> float: ...
    def getY(self) -> float: ...

class _BBox(GraphicsObject):
    p1: Point
    p2: Point
    def __init__(self, p1: Point, p2: Point, options: list[str] =...) -> None: ...
    def getP1(self) -> Point: ...
    def getP2(self) -> Point: ...
    def getCenter(self) -> Point: ...

class Rectangle(_BBox):
    def __init__(self, p1: Point, p2: Point) -> None: ...
    def clone(self) -> Rectangle: ...

class Oval(_BBox):
    def __init__(self, p1: Point, p2: Point) -> None: ...
    def clone(self) -> Oval: ...

class Circle(Oval):
    radius: float
    def __init__(self, center: Point, radius: float) -> None: ...
    def clone(self) -> Circle: ...
    def getRadius(self) -> float: ...

class Line(_BBox):
    setOutline: Incomplete
    def __init__(self, p1: Point, p2: Point) -> None: ...
    def clone(self) -> Line: ...
    def setArrow(self, option: str) -> None: ...

class Polygon(GraphicsObject):
    points: list[Point]
    def __init__(self, *points: Incomplete) -> None: ...
    def clone(self) -> Polygon: ...
    def getPoints(self) -> Incomplete: ...

class Text(GraphicsObject):
    anchor: Point
    setOutline: Incomplete
    def __init__(self, p: Point, text: str) -> None: ...
    def clone(self) -> Text: ...
    def setText(self, text: str) -> None: ...
    def getText(self) -> str: ...
    def getAnchor(self) -> Point: ...
    def setFace(self, face: str) -> None: ...
    def setSize(self, size: int) -> None: ...
    def setStyle(self, style: str) -> None: ...
    def setTextColor(self, color: str) -> None: ...

class Entry(GraphicsObject):
    anchor: Point
    width: int
    text: tk.StringVar
    fill: str
    color: str
    font: tuple[str, int, str]
    entry: Optional[tk.Entry]
    def __init__(self, p: Point, width: int) -> None: ...
    def getText(self) -> str: ...
    def getAnchor(self) -> Point: ...
    def clone(self) -> Entry: ...
    def setText(self, t: str) -> None: ...
    def setFill(self, color: str) -> None: ...
    def setFace(self, face: str) -> None: ...
    def setSize(self, size: int) -> None: ...
    def setStyle(self, style: str) -> None: ...
    def setTextColor(self, color: str) -> None: ...

class Image(GraphicsObject):
    idCount: int
    imageCache: dict[int, tk.PhotoImage]
    anchor: Point
    imageId: int
    img: tk.PhotoImage
    def __init__(self, p: Point, *pixmap: str | int) -> None: ...
    def undraw(self) -> None: ...
    def getAnchor(self) -> Point: ...
    def clone(self) -> Image: ...
    def getWidth(self) -> int: ...
    def getHeight(self) -> int: ...
    def getPixel(self, x: int, y: int) -> list[int]: ...
    def setPixel(self, x: int, y: int, color: str) -> None: ...
    def save(self, filename: str) -> None: ...

def color_rgb(r: int, g: int, b: int) -> str: ...
def test() -> None: ...