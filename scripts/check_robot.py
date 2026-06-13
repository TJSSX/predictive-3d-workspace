from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig
from p3dwm.robot_state import RobotState

def main() -> None:
    config = SO101FollowerConfig(
        port="COM4",
        id="p3dwm_follower",
    )

    robot = SO101Follower(config)

    try:
        robot.connect()

        observation = robot.get_observation()

        robot_state = RobotState.from_observation(observation)

        print("Robot connected.")
        print("Observation:")

        for key, value in robot_state.to_dict().items():
            print(f"  {key}: {value:.2f}")

    finally:
        robot.disconnect()
        print("Robot disconnected.")


if __name__ == "__main__":
    main()