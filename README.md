# Reed_switch_for_Micropython
this is a switch demo for people who want to learn how to use mircopython on ESP8266 

�ṩ�����ּ�ⷽʽ
���ַ�ʽ����Ч����
A����ѯʽ
����⵽�˴���ʱ��GPIO2�ϵ�LED������ͬʱrepl�л���ʾ������������
���򱣳�Ϩ��ͬʱrepl�л���ʾ��δ��⡱
��ѯʽ���������������repl�ϻ�һֱ�з���
B���ж�ʽ
����⵽�˴���ʱ��GPIO2�ϵ�LED������ͬʱrepl�л���ʾ�������ӽ���
���򱣳�Ϩ��ͬʱrepl�л���ʾ������Զ�롱
�ж�ʽ�����������������repl��ֻ�б�Ҫ����
ʵ���ϸɻɹ��൱��һ�����������Կ���ֱ��ʹ�ð������滻��



Two ways of detection are provided.
Two ways of running:
A: polling type
When the magnet is detected, the LED on the GPIO2 will light up, and in the repl, the "��������" will be displayed.
Otherwise the LED will remain off, and repl will show "δ���".
Polling will continue to trigger, so there will always be feedback on repl.
B: interrupt type
When the magnet is detected, the LED on the GPIO2 will light up, and the repl will display "magnet approaching".
Otherwise the LED will remain off, and repl will show "magnet away".
Interrupt mode will not trigger continuously, so there is only necessary feedback on repl.

In fact, the reed switch is equivalent to a button, so it can be replaced directly by a button.