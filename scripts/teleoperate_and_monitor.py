import time

from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig
from lerobot.teleoperators.so_leader import SO101Leader, SO101LeaderConfig

from p3dwm.robot_state import RobotState


TARGET_HZ = 30.0


def main() -> None:
    robot_config = SO101FollowerConfig(
        port="COM4",
        id="p3dwm_follower",
    )

    leader_config = SO101LeaderConfig(
        port="COM5",
        id="p3dwm_leader",
    )

    robot = SO101Follower(robot_config)
    leader = SO101Leader(leader_config)

    robot.connect()
    leader.connect()

    print("Leader and follower connected.")
    print("Move the leader arm. Press Ctrl+C to stop.\n")

    loop_count = 0
    start_time = time.perf_counter()

    try:
        while True:
            loop_start = time.perf_counter()

            # 读取主臂目标关节位置
            action = leader.get_action()

            # 将目标发送给从臂
            robot.send_action(action)

            # 读取从臂实际关节状态
            observation = robot.get_observation()
            state = RobotState.from_observation(observation)

            loop_count += 1
            elapsed = time.perf_counter() - start_time
            loop_hz = loop_count / elapsed if elapsed > 0 else 0.0

            state_text = " | ".join(
                f"{key}: {value:7.2f}"
                for key, value in state.to_dict().items()
            )

            print(
                f"\r{state_text} | Loop: {loop_hz:5.1f} Hz",
                end="",
                flush=True,
            )

            remaining_time = (1.0 / TARGET_HZ) - (
                time.perf_counter() - loop_start
            )

            if remaining_time > 0:
                time.sleep(remaining_time)

    except KeyboardInterrupt:
        print("\nTeleoperation stopped.")

    finally:
        leader.disconnect()
        robot.disconnect()
        print("Leader and follower disconnected.")


if __name__ == "__main__":
    main()