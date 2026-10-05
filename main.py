from manim import ThreeDScene, DEGREES, ORIGIN, RIGHT
from rail import Track


class Test(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES, zoom=0.8)
        obj = Track(length=10, width=3)
        obj.rotate(90 * DEGREES, axis=RIGHT, about_point=ORIGIN)
        obj.move_to(ORIGIN)
        self.add(obj)
        # self.play(Rotate(obj, angle=TAU, axis=OUT, about_point=ORIGIN), run_time=6)
