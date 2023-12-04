#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lazer sensörden gelen veriyi kullanma
"""

import rospy 
from sensor_msgs.msg import LaserScan
from ogretici_paket.msg import EsmanurunGeometrisi

class LazerVerisi():
    def __init__(self):
        rospy.init_node("lazer_dugumu")
        self.pub = rospy.Publisher("cmd_vel",EsmanurunGeometrisi,queue_size = 10)
        self.hiz_mesaji = EsmanurunGeometrisi()
        rospy.Subscriber("scan",LaserScan,self.lazerCallback)
        rospy.spin()
        
    def lazerCallback(self,mesaj):
        sol_on = list(mesaj.ranges[0:9])
        sag_on = list(mesaj.ranges[350:359])
        on = sol_on + sag_on
        sol = list(mesaj.ranges[80:100])
        sag = list(mesaj.ranges[260:280])
        arka = list(mesaj.ranges[170:190])
        min_on = min(on)
        min_sol = min(sol)
        min_sag = min(sag)
        min_arka = min(arka)
        print(min_on,min_sol,min_sag,min_arka)
        if min_on < 1.0:
            self.hiz_mesaji.linear.x = 0.0
            self.pub.publish(self.hiz_mesaji)
        else: 
            self.hiz_mesaji.linear.x = 0.25
            self.pub.publish(self.hiz_mesaji)
            
nesne = LazerVerisi()
