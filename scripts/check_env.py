import sys

import cv2
import numpy as np
import open3d as o3d
import pyrealsense2 as rs


def main() -> None:
    print("Python:", sys.version)
    print("OpenCV:", cv2.__version__)
    print("NumPy:", np.__version__)
    print("Open3D: OK")
    print("RealSense: OK")


if __name__ == "__main__":
    main()