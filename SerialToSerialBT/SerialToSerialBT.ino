//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial

#define BNO055_SAMPLERATE_DELAY_MS (100)
#include "BluetoothSerial.h" //includes the blue tooth serial library 
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);
BluetoothSerial SerialBT; //an instance of bluetoothserial called SerialBT

//
//checks if bluetooth is properly enabled
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif


void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Wire.begin(); 
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
    delay(1000);
  Serial.println("The device started, now you can pair it with bluetooth!");
}

// sends and receives data via bluetooth serial 
// SerialBT.write() sends data using bluetooth serial 
// Serial.read() returns the data received in the serial port

void loop() {
  if (SerialBT.available()) {
    imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
    SerialBT.print(euler.x());
    SerialBT.print(" , ");
    SerialBT.println(euler.z()); // getting z-value and printing to serial monitor
    delay(600);
//    SerialBT.write(Serial.read()); //checks to see if there are bytes being received in the serial port. If there are, send that information via Bluetooth to the connected device
  }
}

//
//#include "BluetoothSerial.h"
//#define BNO055_SAMPLERATE_DELAY_MS (100)
//#include <Adafruit_Sensor.h>
//#include <Adafruit_BNO055.h>
//#include <utility/imumaths.h>
//
//Adafruit_BNO055 bno = Adafruit_BNO055(55);
//BluetoothSerial SerialBT;
//
//void setup() {
//  Serial.begin(115200);
//  SerialBT.begin("Team32_foot_ESP32");
//  Wire.begin(); 
//  if(!bno.begin())
//  {
//    /* There was a problem detecting the BNO055 ... check your connections */
//    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
//    while(1);
//  }
//    delay(1000);
//}
//
//
//void loop(){
//
//  if (SerialBT.available()){
//    imu::Vector<3> foot_accel = bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL);
//    imu::Vector<3> foot_angle = bno.getVector(Adafruit_BNO055::VECTOR_EULER); 
//    SerialBT.print(foot_accel.y());
//    SerialBT.print(",");
//    SerialBT.println(foot_angle.z());
//    delay(600);
//  }
//}
