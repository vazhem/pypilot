#!/usr/bin/env python

import os, sys
import time, math, multiprocessing, select


class RTIMUsim(object):
    def __init__(self):
        return

    def IMUName(self):
        return 'simulated IMU'

    def IMUInit(self):
        return True

    def setSlerpPower(self, v):
        return

    def setGyroEnable(self, v):
        return

    def setAccelEnable(self, v):
        return

    def setCompassEnable(self, v):
        return

    def IMURead(self):
        return True

    def getIMUData(self):
        data = {
            'accel': (1,1,1),
            'timestamp': time.monotonic(),
            'heading': 10,
            'gyro': (0, 0, 0),
            'compass': (10),
            'fusionQPose': (1,1,1),
        }
        return data

    def getAccelResiduals(self):
        return 'accel.residuals'
