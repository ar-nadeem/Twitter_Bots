#include <LiquidCrystal.h>
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

void setup()
{
 lcd.begin(16, 2);              
 lcd.setCursor(0,0);
 lcd.print("PC STATUS");
 lcd.setCursor(0,2);
 lcd.print("AbdulRahman");
 lcd.setCursor(0,0);
 Serial.begin(19200);
}
char rec;
void loop(){  

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

}

