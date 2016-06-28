//Sample using LiquidCrystal library
#include <LiquidCrystal.h>

/*******************************************************

This program will test the LCD panel and the buttons
Mark Bramwell, July 2010

********************************************************/

// select the pins used on the LCD panel
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);
String x = ("NONE")  ;    
// define some values used by the panel and buttons
int lcd_key     = 0;
int serial      = 0;
int adc_key_in  = 0;
#define btnRIGHT  0
#define btnUP     1
#define btnDOWN   2
#define btnLEFT   3
#define btnSELECT 4
#define btnNONE   5

int read_LCD_buttons()
{
 adc_key_in = analogRead(0);
// if (adc_key_in > 1000) return btnNONE;
// if (adc_key_in < 50)   return btnRIGHT;  
// if (adc_key_in < 195)  return btnUP; 
// if (adc_key_in < 380)  return btnDOWN; 
// if (adc_key_in < 555)  return btnLEFT; 
// if (adc_key_in < 790)  return btnSELECT;   


 return btnNONE;
}

void setup()
{
 lcd.begin(16, 2);              
 lcd.setCursor(0,0);
 lcd.print("Raspberry PI");
 Serial.begin(9600);
}
char rec;
void loop(){
  
  lcd_key = read_LCD_buttons();
  if (Serial.available()) {
    while (Serial.available() > 0) {
      rec = Serial.read();
      if(rec == '\n'){
        lcd.setCursor(0,1);
      }else if(rec == '\r'){
        lcd.clear();
      }else{
        lcd.write(rec);
      }
      
    }
    
  }
  /* 
  if (adc_key_in < 380){
   Serial.println("S1");
   x="S1" ;
  }
  if (adc_key_in < 195){
    Serial.println("S2");
    x="S2" ;
  }

  if (adc_key_in >1000){
    
  Serial.println(x); 
  } 
  */
}

