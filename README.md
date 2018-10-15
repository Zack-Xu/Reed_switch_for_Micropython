# Reed_switch_for_Micropython
this is a switch demo for people who want to learn how to use mircopython on ESP8266<BR> 

提供了两种检测方式<BR>
两种方式运行效果：<BR>
### A：轮询式<BR>
当检测到了磁铁时候，GPIO2上的LED会亮起，同时repl中会显示“检测出磁铁”<BR> 
反则保持熄灭，同时repl中会显示“未检测”<BR>
轮询式会持续触发，所以repl上会一直有反馈<BR>
### B：中断式<BR>
当检测到了磁铁时候，GPIO2上的LED会亮起，同时repl中会显示“磁铁接近”<BR>
反则保持熄灭，同时repl中会显示“磁铁远离”<BR>
中断式不会持续触发，所以repl上只有必要反馈<BR>
实际上干簧管相当于一个按键，所以可以直接使用按键来替换。<BR>



Two ways of detection are provided.<BR>
Two ways of running:<BR>
### A: polling type<BR>
When the magnet is detected, the LED on the GPIO2 will light up, and in the repl, the "检测出磁铁" will be displayed.<BR>
Otherwise the LED will remain off, and repl will show "未检测".<BR>
Polling will continue to trigger, so there will always be feedback on repl.<BR>
### B: interrupt type<BR>
When the magnet is detected, the LED on the GPIO2 will light up, and the repl will display "magnet approaching".<BR>
Otherwise the LED will remain off, and repl will show "magnet away".<BR>
Interrupt mode will not trigger continuously, so there is only necessary feedback on repl.<BR>

In fact, the reed switch is equivalent to a button, so it can be replaced directly by a button.<BR>