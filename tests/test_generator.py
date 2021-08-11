import os
import sys
import pytest
from pprint import pprint

# Add relevant ranger module to PATH... there surely is a better way to do this...
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mypalletizer import CommandGenerater

mg: CommandGenerater


@pytest.fixture(scope="module")
def setup():
    global mg
    print("")
    DEBUG = False
    mg = CommandGenerater(debug=DEBUG)
    print("")


def test_generator(setup):
    print("send_coords", end="")
    pprint(mg.send_coords([-160, 160, 160, 0, 0, 0], 7, 2))
    print("power_on", end="")
    pprint(mg.power_on())
    print("power_off", end="")
    pprint(mg.power_off())
    print("release_all_servos", end="")
    pprint(mg.release_all_servos())
    print("is_controller_connected", end="")
    pprint(mg.is_controller_connected())
    print("get_angles", end="")
    pprint(mg.get_angles())
    print("send_angle", end="")
    pprint(mg.send_angle(1, 0, 10))
    print("send_angles", end="")
    pprint(mg.send_angles([0, 0, 0, 0], 5))
    print("get_coords", end="")
    pprint(mg.get_coords())
    print("send_coord", end="")
    pprint(mg.send_coord(1, 110.5, 8))
    print("pause", end="")
    pprint(mg.pause())
    print("is_paused", end="")
    pprint(mg.is_paused())
    print("resume", end="")
    pprint(mg.resume())
    print("stop", end="")
    pprint(mg.stop())
    print("is_in_position", end="")
    pprint(mg.is_in_position([0, 0, 0, 0, 0, 0], 0))
    print("is_moving", end="")
    pprint(mg.is_moving())
    print("jog_angle", end="")
    pprint(mg.jog_angle(1, 0, 1))
    print("jog_coord", end="")
    pprint(mg.jog_coord(2, 1, 3))
    print("jog_stop", end="")
    pprint(mg.jog_stop())
    print("set_encoder", end="")
    pprint(mg.set_encoder(1, 1024))
    print("get_encoder", end="")
    pprint(mg.get_encoder(2))
    print("get_speed", end="")
    pprint(mg.get_speed())
    print("set_speed", end="")
    pprint(mg.set_speed(100))
    print("get_joint_min_angle", end="")
    pprint(mg.get_joint_min_angle(1))
    print("get_joint_max_angle", end="")
    pprint(mg.get_joint_max_angle(2))
    print("is_servo_enable", end="")
    pprint(mg.is_servo_enable(6))
    print("is_all_servo_enable", end="")
    pprint(mg.is_all_servo_enable())
    print("set_servo_data", end="")
    pprint(mg.set_servo_data(0, 1, 2))
    print("get_servo_data", end="")
    pprint(mg.get_servo_data(1, 2))
    print("set_servo_calibration", end="")
    pprint(mg.set_servo_calibration(1))
    print("release_servo", end="")
    pprint(mg.release_servo(1))
    print("focus_servo", end="")
    pprint(mg.focus_servo(1))
    print("set_color", end="")
    pprint(mg.set_color(255, 255, 0))
    print("set_pin_mode", end="")
    pprint(mg.set_pin_mode(1, 0))
    print("set_digital_output", end="")
    pprint(mg.set_digital_output(0, 1))
    pprint(mg)
