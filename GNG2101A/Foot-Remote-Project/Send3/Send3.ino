#include <IRremote.h>
//This code and remote is dedicated to Jorge and God-Emperor Donald Trump.

IRsend irsend;
const int buttonPin0 = 0; // the number of the pushbutton pin
const int buttonPin1 = 1;
const int buttonPin2 = 2;
//Can't use pin 3. Pin 3 is being sent to the LED volcano for sacrifice. <3
const int buttonPin4 = 4; // button placement is for buttons (n-1) from here on.
const int buttonPin5 = 5;
const int buttonPin6 = 6;
const int buttonPin7 = 7;
const int buttonPin8 = 8;
const int buttonPin9 = 9; 
const int buttonPin10 = 10; // Until here lol. Chill, fam
const int pwrButtonPin11 = 11;
const int muteButtonPin12 = 12;

int volUpPin0 = A0;
int volDownPin1 = A1;
int chUpPin2 = A2;
int chDownPin3 = A3;

//Button States for all 0-9 button, starts LOW (0).
int buttonState0 = 0;
int buttonState1 = 0;
int buttonState2 = 0;
int buttonState4 = 0;
int buttonState5 = 0;
int buttonState6 = 0;
int buttonState7 = 0;
int buttonState8 = 0;
int buttonState9 = 0;
int buttonState10 = 0;
int buttonStatePwr = 0;
int buttonStateMute = 0;

int volUpButtonState = 0; 
int volDownButtonState = 0; 
int chUpButtonState = 0; 
int chDownButtonState = 0;

// variable for reading the pushbutton status
void setup()
{
  // pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin0, INPUT);
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  //No Pin 3. The LED Monster ate him. He was a good man, Jim. I'm sorry for your loss.
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
  pinMode(buttonPin6, INPUT);
  pinMode(buttonPin7, INPUT);
  pinMode(buttonPin8, INPUT);
  pinMode(buttonPin9, INPUT);
  pinMode(buttonPin10, INPUT);
  pinMode(powerButtonPin11, INPUT);
  pinMode(powerButtonPin12, INPUT);

  //Vol up
  pinMode(A0, INPUT)
  //Vol down
  pinMode(A1, INPUT)
  //Ch up
  pinMode(A2, INPUT)
  //Ch down
  pinMode(A3, INPUT)
  
  Serial.begin(9600);
}

void loop() {

  //Button States for every pin.
  buttonState0 = digitalRead(buttonPin0);
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState4 = digitalRead(buttonPin4);
  buttonState5 = digitalRead(buttonPin5);
  buttonState6 = digitalRead(buttonPin6);
  buttonState7 = digitalRead(buttonPin7);
  buttonState8 = digitalRead(buttonPin8);
  buttonState9 = digitalRead(buttonPin9);
  buttonState10 = digitalRead(buttonPin10);
  buttonStatePwr = digitalRead(pwrButtonPin11);
  buttonStateMute = digitalRead(muteButtonPin12);

  volUpButtonState=analogRead(volUpPin0);
  volDownButtonState=analogRead(volDownPin1);
  chUpButtonState=analogRead(chUpPin2);
  chDownButtonState=analogRead(chDownPin3);
  
  // check if the pushbutton is pressed.
  // if it is, the buttonState is LOW:
  
  //BUTTON 0
  if (buttonState0 == LOW)
  {
    // turn LED on;
    irsend.sendNEC(0x1CE300FF, 32);
  }
  //BUTTON 1
  if (buttonState1 == LOW)
  {
    //turn LED on;
    irsend.sendNEC(0x1CE3807F);
  }
  //BUTTON 2
  if (buttonState2 == LOW)
  {
    irsend.sendNEC(0x1CE340BF);
  }
  //BUTTON 3
  if (buttonState3 == LOW)
  {
    irsend.sendNEC(0x1CE3C03F);
  }
  //BUTTON 4
  if (buttonState4 == LOW)
  {
    irsend.sendNEC(0x1CE320DF);
  }
  //BUTTON 5
  if (buttonState5 == LOW)
  {
    irsend.sendNEC(0x1CE3A05F);
  }
  //BUTTON 6
  if (buttonState6 == LOW)
  {
    irsend.sendNEC(0x1CE3609F);
  }
  //BUTTON 7
  if (buttonState7 == LOW)
  {
    irsend.sendNEC(0x1CE3E01F);
  }
  //BUTTON 8
  if (buttonState8 == LOW)
  {
    irsend.sendNEC(0x1CE310EF);
  }
  //BUTTON 9
  if (buttonState9 == LOW)
  {
    irsend.sendNEC(0x1CE3906F);
  }

  //Vol up
  if ((volUpButtonState>0) && (volUpButtonState<= 1023))
  // turn LED on:
  irsend.sendNEC(0xFFA05F, 32);

  //Vol down
  if  ((volDownButtonState>0) && (volDownButtonState<= 1023))
  // turn LED on:
  irsend.sendNEC(0x1CE3F00F, 32);

  //Ch up
  if ((chUpButtonState>0) && (chUpButtonState<= 1023)) 
  // turn LED on:
  irsend.sendNEC(0x1CE350AF, 32);

  //Ch down
  if ((chDownButtonState>0) && (chDownButtonState<= 1023))
  // turn LED on:
  irsend.sendNEC(0x1CE3D02F, 32);
}

 // if ((analogState0 > 0) && (analogState <= 1023)) Sample Code. 
 // What? did you think that was actually part of the code? Nice try, amigo.
 // 
 
 
}


