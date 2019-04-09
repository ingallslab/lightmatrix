
/*************************************************** 
  This is an example for our Adafruit 16-channel PWM & Servo driver
  GPIO test - this will set a pin high/low

  Pick one up today in the adafruit shop!
  ------> http://www.adafruit.com/products/815

  These drivers use I2C to communicate, 2 pins are required to  
  interface.

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver pwm2 = Adafruit_PWMServoDriver(0x41);
Adafruit_PWMServoDriver pwm3 = Adafruit_PWMServoDriver(0x42);
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);
// you can also call it with a different address and I2C interface
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(&Wire, 0x40);
int incomingByte = 0;
int pinRead = -1;
int pinValue = -1;
//void setup() {
//  Serial.begin(9600);
//  Serial.println("GPIO test!");
// 
//  pwm.begin();
//  pwm.setPWMFreq(1000);  // Set to whatever you like, we don't use it in this demo!
//
//  // if you want to really speed stuff up, you can go into 'fast 400khz I2C' mode
//  // some i2c devices dont like this so much so if you're sharing the bus, watch
//  // out for this!
//  Wire.setClock(400000);
//}
//
//void loop() {
//  if (Serial.available() ){
//    incomingByte = Serial.read();
//    if (pinRead == -1){
//        pinRead = incomingByte;
//      } else  if (pinValue == -1) {
//        pinValue = incomingByte;
//        }
//    if (pinRead > 0 && pinValue > 0){
//      Serial.print("Pin: ");
//      Serial.println(pinRead, DEC);
//      Serial.print("Value");
//      Serial.println(pinValue, DEC);
//      pinRead = -1;
//      pinValue = -1;
//    }
//    }
//    
//  // Drive each pin in a 'wave'
//    pwm.setPWM(15, 4096, 0);       // turns pin fully on
//    delay(100);
//    pwm.setPWM(15, 0, 4096);       // turns pin fully off
// 
//}

const byte numChars = 32;
char receivedChars[numChars];

boolean newData = false;

void setup() {
    Serial.begin(9600);
    Serial.println("<Arduino is ready>");

    pwm1.begin();
    pwm1.setPWMFreq(1000);  // Set to whatever you like, we don't use it in this demo!
    pwm2.begin();
    pwm2.setPWMFreq(1000);
    pwm3.begin();
    pwm3.setPWMFreq(1000);
    // if you want to really speed stuff up, you can go into 'fast 400khz I2C' mode
    // some i2c devices dont like this so much so if you're sharing the bus, watch
    // out for this!
    Wire.setClock(400000);
}

void loop() {
    recvWithStartEndMarkers();
    showNewData();
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
 // if (Serial.available() > 0) {
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
                parseData();
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
        Serial.print("This just in ... ");
        Serial.println(receivedChars);
        newData = false;
    }
}



void parseData() {

    // split the data into its parts
  char * strtokIndx; // this is used by strtok() as an index
  strtokIndx = strtok(receivedChars,",");      // get the first part - the string
  int pin = atoi(strtokIndx) % 16;     // convert this part to an integer
  strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
  int v1 = atoi(strtokIndx);     // convert this part to an integer
  strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
  int v2 = atoi(strtokIndx);     // convert this part to an integer
  strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
  int v3 = atoi(strtokIndx);     // convert this part to an integer

  // check what board to use based on these values
  for (int i = pin; i < pin+3; ++i){
    int val = 0;
    if (i == pin) val = v1;
    if (i == pin + 1) val = v2;
    if (i == pin + 2) val = v3;
    if (pin / 16 == 0){
      // do something to board 1
      pwm1.setPWM(pin % 16, 0, val);
     }else if (pin / 16 == 1){
      pwm2.setPWM(pin % 16, 0, val); 
     }else if (pin / 16 == 2) {
      pwm3.setPWM(pin % 16, 0, val);
     }else {
      // throw err
      }
    }
  
}

