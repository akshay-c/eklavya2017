The hardware comprises of Arduino Uno R3, Lasers(Red,650nm), Stepper Motor, Compact disk and Ply boards. The Stepper Motor allows the platform in which the object to be scanned is placed to be rotated in desired steps and rpm. The laser setup facilitates frame capturing in required steps of rotation.
The circuit diagram for the connection is given as under-
***
1. [Breadboard Connection](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/tree/master/FRITZING)
2. [PCB Connection](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/tree/master/FRITZING)
3. [SCHEMATIC Connection](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/tree/master/FRITZING)
***
[Fritzing Image](http://fritzing.org/projects/scanner-3d)

***
**Command to Arduino via Python GUI using Pyserial**
The Arduino is controlled using Python PyPI Module `pyserial` via Serial Communication.
Installed in Ubuntu using Command line- `pip install pyserial`
Detailed information can be found in documentation/pyserial.rst.
***
**Arduino Code and Explanation**
***    
    #include <Stepper.h>

    const int stepsPerRevolution = 48;  // The motor performs a complete revolution in 48 steps

    Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);//Connections of Stepper End Coils at 8,9,10,11 pins of                       
                                                          Arduino via ULN2003A

    int steps = 0;         // number of steps the motor has taken

    void setup() 
    {//Set pinMode HIGH for each of the pins
    pinMode(8,1);
    pinMode(9,1);
    pinMode(10,1);
    pinMode(11,1);
    Serial.begin(9600);//Serial Communicatoin at a Baud Rate 9600
    myStepper.setSpeed(10);
    }

    void StepCount()
    {
    if (steps<48)
    steps++;
    else if (steps==48)
    steps=0;
    }

    void StepperStep()
    {
    if (Serial.available())
    {
    if (steps<48)
    {
    char data=Serial.read();
    if (data=='1') // The arduino is controlled using Pyserial Command from Python GUI Window using Keypress 1
    {//for each Keypress 1 the stepper moves 1 step
    myStepper.step(1);
    delay(50);
    Serial.print('.');
    StepCount();
    }  
    }
    }  
    }


    void loop() 
    {
    StepperStep();
    }
