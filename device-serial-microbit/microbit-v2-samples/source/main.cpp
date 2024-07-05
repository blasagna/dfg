#include "MicroBit.h"
#include "samples/Tests.h"

MicroBit uBit;

void onButtonA(MicroBitEvent e)
{
    int x = uBit.accelerometer.getX();
    int y = uBit.accelerometer.getY();
    int z = uBit.accelerometer.getZ();
    uBit.display.print("A");
    uBit.serial.send("Button: A\r\n");
    uBit.serial.printf("Accelerometer x:%d y:%d z:%d \r\n",x,y,z);
}

void onButtonB(MicroBitEvent e)
{
    int x = uBit.accelerometer.getX();
    int y = uBit.accelerometer.getY();
    int z = uBit.accelerometer.getZ();
    uBit.display.print("B");
    uBit.serial.send("Button: B\r\n");
    uBit.serial.printf("Accelerometer x:%d y:%d z:%d \r\n",x,y,z);
}

int main()
{
    uBit.init();

    uBit.messageBus.listen(MICROBIT_ID_BUTTON_A, MICROBIT_BUTTON_EVT_CLICK, onButtonA);
    uBit.messageBus.listen(MICROBIT_ID_BUTTON_B, MICROBIT_BUTTON_EVT_CLICK, onButtonB);

    uBit.display.print("S");
    uBit.serial.send("Starting Micro:Bit Program \r\n");

    release_fiber();
}
