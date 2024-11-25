# Blink.sh

No arquivo 'blink.sh' foi feito um programa que pisca um LED na saida GPIO 18 com uma frequência de 5 Hz  

```shell
echo 18 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio18/direction

while [ 1 ]
	do
		echo 1 > /sys/class/gpio/gpio18/value
		sleep 0.2s
		echo 0 > /sys/class/gpio/gpio18/value
		sleep 0.2s
	done

```

# Blink.service 

Neste arquivo foi criado para que o programa Blink.sh fosse executado logo após o Boot do raspberry pi conforme foi descrito pelo professor

```shell
[Unit]
Description= Blink LED
After=multi-user.target

[Service]
ExecStart=/home/sel/5277/git5277/SEL0630/blink.sh
#ExecStop=
user=SEL

[Install]
WantedBy=multi-user.target
```

# Videos

## Blink.mp4

No video 'blink.mp4' é o funcionamento do codigo 'blink.sh'

## BootBlink.mp4 

No video mostra a inicialização do raspberry pi com o blink.sh sendo ativado no boot

# PWM 

Esse programa foi upado somente como teste para entender o funcionamento do git 