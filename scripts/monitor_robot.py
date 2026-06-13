import time

from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig


def main() -> None:
    config = SO101FollowerConfig(
        port="COM4",
        id="p3dwm_follower",
    )
    robot = SO101Follower(config)

    robot.connect()
    print("Robot connected. Press Ctrl+C to stop.\n")

    sample_count = 0
    start_time = time.perf_counter()

    try:
        while True:
            observation = robot.get_observation()
            sample_count += 1

            joint_text = " | ".join(
                f"{name}: {float(value):7.2f}"
                for name, value in observation.items()
            )

            elapsed = time.perf_counter() - start_time
            frequency = sample_count / elapsed if elapsed > 0 else 0.0

            print(
                f"\r{joint_text} | Read rate: {frequency:5.1f} Hz",
                end="",
                flush=True,
            )

            time.sleep(0.02)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

    finally:
        robot.disconnect()
        print("Robot disconnected.")


if __name__ == "__main__":
    main()