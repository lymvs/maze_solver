from gui import Window, Point, Line


def main() -> None:
    win = Window(800, 600)

    point1 = Point(50, 50)
    point2 = Point(200, 100)
    l = Line(point1, point2)
    
    win.draw_line(l, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()
