#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts


def callback(data):
    # Crear publisher
    pub = rospy.Publisher('sum', Int16, queue_size=10)
    
    # Obtener resultado de los numeros leidos y publicar
    result = data.a + data.b
    pub.publish(result)

    # For testing purposes
    print str(data.a) + " + " + str(data.b) + " = " + str(result)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    # Iniciar nodo
    rospy.init_node('listener', anonymous=True)

    # Suscribirse al nodo two_ints (que esta siendo llamado cada
    # 2 segundos, y publica datos de tipo TwoInts
    rospy.Subscriber('two_ints', TwoInts, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

