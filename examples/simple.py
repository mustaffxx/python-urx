from math import pi

import urx
import logging

if __name__ == "__main__":
    rob = urx.Robot("192.168.128.120", logLevel=logging.INFO)
    rob.set_tcp((0,0,0,0,0,0))
    rob.set_payload(0.5, (0,0,0))
    try:
        l = 0.05
        v = 0.05
        a = 0.3
        pose = rob.getl()
        print("robot tcp is at: ", pose)
        pose[2] += l
        rob.movel(pose, acc=a, vel=v)
        print("relative move in base coordinate ")
        rob.translate((0, 0, -z), acc=a, vel=v)
        print("relative move in tool coordinate")
        rob.translate_tool((0, 0, -z), acc=a, vel=v)
        rob.translate_tool((0, 0, z), acc=a, vel=v)
    finally:
        rob.cleanup()

