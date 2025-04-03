#include <mega16.h>
#include <delay.h>
// Alphanumeric LCD functions
#include <alcd.h>

// Declare your global variables here

void main(void)
{
char name[16] = {"Masih Roughani "};
char num[16] = {"   4023623016  "};
char i =0;
char side = 1;
lcd_init(16);
while (1)
      {
            lcd_clear();
            lcd_gotoxy(i,0);
            if(i == 2){side = -1;}
            if(i == 0){side = 1;}
            i = i+side;
            lcd_puts(name);  
            lcd_puts(num);
            delay_ms(250);
      }
}
