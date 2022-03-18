/* Student Information 
 *  IBEHS 3P04 - T05
 *  Sheridan Fong 
 *  400240385 - fongs7
*/


#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

// making this the delay time between collecting samples
#define BNO055_SAMPLERATE_DELAY_MS (1000)

// initializing the sensor
Adafruit_BNO055 bno = Adafruit_BNO055(55);

// Declaring this as a global variable
/* Setting up the counting variable */ 
long count = 4;
float euler_x_array[1000];
float euler_y_array[1000];
float euler_z_array[1000];

// ---------------------------- creating functions to call in set-up and loop ---------
void displaySensorDetails(void)
{
  sensor_t sensor;
  bno.getSensor(&sensor);
  Serial.println("------------------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" xxx");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" xxx");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" xxx");
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}

void displaySensorStatus(void)
{
  /* Get the system status values (mostly for debugging purposes) */
  uint8_t system_status, self_test_results, system_error;
  system_status = self_test_results = system_error = 0;
  bno.getSystemStatus(&system_status, &self_test_results, &system_error);

  /* Display the results in the Serial Monitor */
  Serial.println("");
  Serial.print("System Status: 0x");
  Serial.println(system_status, HEX);
  Serial.print("Self Test:     0x");
  Serial.println(self_test_results, HEX);
  Serial.print("System Error:  0x");
  Serial.println(system_error, HEX);
  Serial.println("");
  delay(100);
}

// Calculates the average of the last five values
float average (float * array, int count){ // input is an array of floats and a count
  long sum = 0L; // initializing sum 
  for(int i = count ; i > count - 5; i--){
    sum += array[i];
  }
  return((float)sum)/5; 
}


// ----------------------------- Setting up the sensor this runs once -------------------------

// Setting up the sensor 
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200); // baud rate
Serial.println("Orientation Sensor Test"); Serial.println("");
Wire.begin(); 



if(!bno.begin())
{
  /* There was a problem detecting the BNO055 ... check your connections */
  Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
  while(1);
}
  delay(1000);

  /* Display some basic information on this sensor */
  displaySensorDetails(); // calling the other functions

  /* Optional: Display current status */
  displaySensorStatus(); // calling the other functions

  /* Populating the arrays with first four values */

  for(int i = 0; i < 4; i ++){
    euler_x_array[i] = 0;
    euler_y_array[i] = 0;
    euler_z_array[i] = 0;
  }

  bno.setExtCrystalUse(true);
}

// ------------------- creating the looping structure this repeats infinitely ------------
void loop() {
  // Possible vector values can be:
  // - VECTOR_ACCELEROMETER - m/s^2
  // - VECTOR_MAGNETOMETER  - uT
  // - VECTOR_GYROSCOPE     - rad/s
  // - VECTOR_EULER         - degrees
  // - VECTOR_LINEARACCEL   - m/s^2
  // - VECTOR_GRAVITY       - m/s^2

  // getting the euler values using the .getVector function
  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
  imu::Vector<3> accel_value = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);

  /* Display calibration status for each sensor. */
  uint8_t system, gyro, accel, mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);
  Serial.print("CALIBRATION: Sys=");
  Serial.print(system, DEC); // what does DEC mean? 
  Serial.print(" Gyro=");
  int gyro_value = (gyro, DEC);
  //Serial.print(gyro_value);
  Serial.print(gyro, DEC);
  Serial.print(" Accel=");
  Serial.print(accel, DEC);
  Serial.print(" Mag=");
  Serial.println(mag, DEC);


  // the below code should only run if Gyro is callibrated so when gyro = 3 callibrated

  if(gyro == 3){

      /* Display the floating point data for the Euler angles
      The floating point data is the average of the last five
      */
      
      Serial.println("IMU Gyro Data:"); 
    
      // Gathering euler data 
      float euler_x = euler.x(); 
      float euler_y = euler.y(); 
      float euler_z = euler.z(); 
    
      // Adding the euler values to the appropriate array 
      euler_x_array[count] = euler_x; 
      euler_y_array[count] = euler_y; 
      euler_z_array[count] = euler_z; 
    
      // Printing the average of last five values
      Serial.print("X:");
      Serial.print(average(euler_x_array, count));
      Serial.print(" Y: ");
      Serial.print(average(euler_y_array, count)); 
      Serial.print(" Z: ");
      Serial.println(average(euler_z_array,count)); 
    
    
      // printing acceleratometer data out to the screen
      Serial.println("IMU Accelerometer Data:");
      Serial.print("X: ");
      Serial.print(accel_value.x());
      Serial.print(" Y: ");
      Serial.print(accel_value.y());
      Serial.print(" Z: ");
      Serial.println(accel_value.z());

      // increasing the counter for inserting values into the appropriate arrays
      count += 1;
    
  }else{
    Serial.println("Sensor is not callibrated, values will be collected when the sensor's gyroscope is calibrated. Please wait a second :)");
  }

  
  Serial.println("-----------------------------------------------------------");
  

  delay(BNO055_SAMPLERATE_DELAY_MS);
}
