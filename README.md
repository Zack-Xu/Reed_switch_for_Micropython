# Reed_switch_for_Micropython
this is a switch demo for people who want to learn how to use mircopython on ESP8266<BR> 

�ṩ�����ּ�ⷽʽ<BR>
���ַ�ʽ����Ч����<BR>
### A����ѯʽ<BR>
����⵽�˴���ʱ��GPIO2�ϵ�LED������ͬʱrepl�л���ʾ������������<BR> 
���򱣳�Ϩ��ͬʱrepl�л���ʾ��δ��⡱<BR>
��ѯʽ���������������repl�ϻ�һֱ�з���<BR>
### B���ж�ʽ<BR>
����⵽�˴���ʱ��GPIO2�ϵ�LED������ͬʱrepl�л���ʾ�������ӽ���<BR>
���򱣳�Ϩ��ͬʱrepl�л���ʾ������Զ�롱<BR>
�ж�ʽ�����������������repl��ֻ�б�Ҫ����<BR>
ʵ���ϸɻɹ��൱��һ�����������Կ���ֱ��ʹ�ð������滻��<BR>



Two ways of detection are provided.<BR>
Two ways of running:<BR>
### A: polling type<BR>
When the magnet is detected, the LED on the GPIO2 will light up, and in the repl, the "��������" will be displayed.<BR>
Otherwise the LED will remain off, and repl will show "δ���".<BR>
Polling will continue to trigger, so there will always be feedback on repl.<BR>
### B: interrupt type<BR>
When the magnet is detected, the LED on the GPIO2 will light up, and the repl will display "magnet approaching".<BR>
Otherwise the LED will remain off, and repl will show "magnet away".<BR>
Interrupt mode will not trigger continuously, so there is only necessary feedback on repl.<BR>

In fact, the reed switch is equivalent to a button, so it can be replaced directly by a button.<BR>