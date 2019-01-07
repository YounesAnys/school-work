// This sketch will send out a Nikon D50 trigger signal (probably works with most Nikons)
// See the full tutorial at http://www.ladyada.net/learn/sensors/ir.html
// this code is public domain, please enjoy!

const int buttonPin = 2; //Button set to pin 2.
const int IRledPin =  13;    // LED connected to digital pin 13.
int buttonState = LOW; //Binary Status of Button.
int lastButtonState = LOW; //Last Known Status of Button.
 
// The setup() method runs once, when the sketch starts
 
void setup()   {                
  // initialize the IR digital pin as an output:
  pinMode(buttonPin, INPUT);
  pinMode(IRledPin, OUTPUT);      
 
  Serial.begin(9600);
}
 
void loop()                     
{
  Serial.println("Sending IR signal");

  buttonState = digitalRead(buttonPin);
  if (buttonState != lastButtonState)
  {
    SendChannelUpCode();    
  }
}
 
// This procedure sends a 38KHz pulse to the IRledPin 
// for a certain # of microseconds. We'll use this whenever we need to send codes
void pulseIR(long microsecs) {
  // we'll count down from the number of microseconds we are told to wait
 
  cli();  // this turns off any background interrupts
 
  while (microsecs > 0) {
    // 38 kHz is about 13 microseconds high and 13 microseconds low
   digitalWrite(IRledPin, HIGH);  // this takes about 3 microseconds to happen
   delayMicroseconds(10);         // hang out for 10 microseconds
   digitalWrite(IRledPin, LOW);   // this also takes about 3 microseconds
   delayMicroseconds(10);         // hang out for 10 microseconds
 
   // so 26 microseconds altogether
   microsecs -= 26;
  }
 
  sei();  // this turns them back on
}
 
void SendChannelUpCode() 
{
  //Read the binary status of button 2. Expected result: the number "2" is read by TV.
  //buttonState = digitalRead(buttonPin);
  
  //Check if button is pushed down, and act accordingly.
    //delayMicroseconds(30668);
    //pulseIR(9420);
    buttonState = LOW;
    delayMicroseconds(21312);
    pulseIR(9280);
    delayMicroseconds(4600);
    pulseIR(560);
    delayMicroseconds(580);
    pulseIR(580);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(1740);
    pulseIR(560);
    delayMicroseconds(1740);
    pulseIR(560);
    delayMicroseconds(1720);
    pulseIR(580);
    delayMicroseconds(580);
    pulseIR(580);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(1760);
    pulseIR(540);
    delayMicroseconds(1740);
    pulseIR(560);
    delayMicroseconds(1740);
    pulseIR(560);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(1720);
    pulseIR(580);
    delayMicroseconds(1720);
    pulseIR(580);
    delayMicroseconds(600);
    pulseIR(580);
    delayMicroseconds(1700);
    pulseIR(600);
    delayMicroseconds(580);
    pulseIR(560);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(620);
    pulseIR(560);
    delayMicroseconds(620);
    pulseIR(540);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(560);
    pulseIR(600);
    delayMicroseconds(1740);
    pulseIR(560);
    delayMicroseconds(600);
    pulseIR(560);
    delayMicroseconds(1700);
    pulseIR(600);
    delayMicroseconds(1700);
    pulseIR(600);
    delayMicroseconds(1740);
    pulseIR(560);
    delayMicroseconds(1720);
    pulseIR(580);
    delayMicroseconds(1720);
    pulseIR(580);
    delayMicroseconds(1700);
    pulseIR(600);
    delayMicroseconds(41020);
    pulseIR(9260);
    delayMicroseconds(2280);
    pulseIR(580);
    delayMicroseconds(33244);
    pulseIR(9300);
    delayMicroseconds(2260);
    pulseIR(600);
}

