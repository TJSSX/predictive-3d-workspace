from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig


def main() -> None:
    config = SO101FollowerConfig(
        port="COM4",
        id="p3dwm_follower",
    )

    robot = SO101Follower(config)

    try:
        robot.connect()

        observation = robot.get_observation()

        print("Robot connected.")
        print("Observation:")

        for key, value in observation.items():
            print(f"  {key}: {value}")

    finally:
        robot.disconnect()
        print("Robot disconnected.")


if __name__ == "__main__":
    main()