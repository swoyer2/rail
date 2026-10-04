from manim import VMobject, VGroup, Polyhedron, Prism, OUT, LEFT, RIGHT, DOWN
import numpy as np


class Profile(VMobject):
    def __init__(self) -> None:
        super().__init__()
        self._add_vectors()

    def _add_vectors(self) -> None:
        points = np.array([
            [ 0.00,  0.45, 0],
            [-0.17,  0.45, 0],
            [-0.23,  0.40, 0],
            [-0.23,  0.28, 0],
            [-0.19,  0.28, 0],
            [-0.06,  0.17, 0],
            [-0.06, -0.25, 0],
            [-0.10, -0.34, 0],
            [-0.50, -0.43, 0],
            [-0.50, -0.50, 0],
            [ 0.50, -0.50, 0],
            [ 0.50, -0.43, 0],
            [ 0.10, -0.34, 0],
            [ 0.06, -0.25, 0],
            [ 0.06,  0.17, 0],
            [ 0.19,  0.28, 0],
            [ 0.23,  0.28, 0],
            [ 0.23,  0.40, 0],
            [ 0.17,  0.45, 0],
            [ 0.00,  0.45, 0],
        ])

        self.set_points_as_corners(points)


class Rail(Polyhedron):
    def __init__(self, length: float = 10.0) -> None:
        begin = Profile().get_anchors()[:-1]
        end = Profile().shift(OUT * length).get_anchors()[:-1]
        n = len(begin)

        faces = [
            list(range(n)),          # start cap
            list(range(n, 2 * n)),   # end cap
        ]
        for i in range(n):           # side quads along the length
            j = (i + 1) % n
            faces.append([i, j, n + j, n + i])

        super().__init__(
            [*begin, *end],
            faces,
            graph_config={"vertex_config": {"radius": 0.0, "stroke_opacity": 0}},
            faces_config={"stroke_width": 0}
        )
        self.remove(*self.graph.vertices.values())

class Track(VGroup):
    def __init__(self, length: float = 10.0, width: float = 4.0) -> None:
        super().__init__()

        self.left_rail = Rail(length=length).shift(LEFT * width / 2)
        self.right_rail = Rail(length=length).shift(RIGHT * width / 2)

        self.ties = [Prism(dimensions=np.array([width + 2, 0.5, 1.0])).shift(OUT * 2 * (i) + DOWN * 0.8) for i in range(int(length // 2))]
        self.add(self.left_rail, self.right_rail, self.ties)