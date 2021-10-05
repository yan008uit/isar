from models.geometry.frame import Frame
from models.geometry.orientation import Orientation
from models.geometry.pose import Pose
from models.geometry.position import Position
from models.planning.step import (
    DriveToPose,
    TakeImage,
)


class MockStep:
    @staticmethod
    def drive_to(
        position: Position = Position(x=1, y=1, z=1, frame=Frame.Robot),
        orientation: Orientation = Orientation(
            x=0, y=0, z=0.7071068, w=0.7071068, frame=Frame.Robot
        ),
    ) -> DriveToPose:
        return DriveToPose(
            pose=Pose(position=position, orientation=orientation, frame=Frame.Robot)
        )

    @staticmethod
    def take_image_in_coordinate_direction(
        target: Position = Position(x=1, y=1, z=1, frame=Frame.Robot)
    ) -> TakeImage:
        return TakeImage(target=target)
