from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class RobotState:
    shoulder_pan_deg: float
    shoulder_lift_deg: float
    elbow_flex_deg: float
    wrist_flex_deg: float
    wrist_roll_deg: float
    gripper_deg: float

    @classmethod
    def from_observation(cls, observation: dict[str, Any]) -> "RobotState":
        required_keys = (
            "shoulder_pan.pos",
            "shoulder_lift.pos",
            "elbow_flex.pos",
            "wrist_flex.pos",
            "wrist_roll.pos",
            "gripper.pos",
        )

        missing = [key for key in required_keys if key not in observation]
        if missing:
            raise KeyError(f"Missing robot observation fields: {missing}")

        return cls(
            shoulder_pan_deg=float(observation["shoulder_pan.pos"]),
            shoulder_lift_deg=float(observation["shoulder_lift.pos"]),
            elbow_flex_deg=float(observation["elbow_flex.pos"]),
            wrist_flex_deg=float(observation["wrist_flex.pos"]),
            wrist_roll_deg=float(observation["wrist_roll.pos"]),
            gripper_deg=float(observation["gripper.pos"]),
        )

    def to_dict(self) -> dict[str, float]:
        return asdict(self)