#!/bin/sh
# chkconfig: 123456 90 10
#

stop() {
    pid=`ps -aef | grep 'mlff'`
    echo $pid
    kill -9 $pid
    sleep 2
    echo "Server killed."
}
start() {
    systemctl start mlff &
    echo "Server started."
}
 
    echo "Usage: systemctl {start|stop|restart} mlff"
    exit 1
esac
exit 0
