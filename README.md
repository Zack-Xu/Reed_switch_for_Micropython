# Reed_switch_for_Micropython
this is a switch demo for people who want to learn how to use mircopython on ESP8266 

提供了两种检测方式
两种方式运行效果：
A：轮询式
当检测到了磁铁时候，GPIO2上的LED会亮起，同时repl中会显示“检测出磁铁”
反则保持熄灭，同时repl中会显示“未检测”
轮询式会持续触发，所以repl上会一直有反馈
B：中断式
当检测到了磁铁时候，GPIO2上的LED会亮起，同时repl中会显示“磁铁接近”
反则保持熄灭，同时repl中会显示“磁铁远离”
中断式不会持续触发，所以repl上只有必要反馈
实际上干簧管相当于一个按键，所以可以直接使用按键来替换。



Two ways of detection are provided.
Two ways of running:
A: polling type
When the magnet is detected, the LED on the GPIO2 will light up, and in the repl, the "检测出磁铁" will be displayed.
Otherwise the LED will remain off, and repl will show "未检测".
Polling will continue to trigger, so there will always be feedback on repl.
B: interrupt type
When the magnet is detected, the LED on the GPIO2 will light up, and the repl will display "magnet approaching".
Otherwise the LED will remain off, and repl will show "magnet away".
Interrupt mode will not trigger continuously, so there is only necessary feedback on repl.

In fact, the reed switch is equivalent to a button, so it can be replaced directly by a button.