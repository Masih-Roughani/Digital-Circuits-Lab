#include <mega16.h>
#include <delay.h>
#include <alcd.h>

// Declare your global variables here

// External Interrupt 0 service routine
interrupt [EXT_INT0] void ext_int0_isr(void)
{
    lcd_puts("00");                                                                                                            
}

// External Interrupt 1 service routine
interrupt [EXT_INT1] void ext_int1_isr(void)
{
    lcd_puts("11");
}

void main(void)
{

PORTD=(0<<PORTD7) | (0<<PORTD6) | (0<<PORTD5) | (0<<PORTD4) | (1<<PORTD3) | (1<<PORTD2) | (0<<PORTD1) | (0<<PORTD0);

GICR|=(1<<INT1) | (1<<INT0) | (0<<INT2);
MCUCR=(1<<ISC11) | (0<<ISC10) | (1<<ISC01) | (0<<ISC00);
MCUCSR=(0<<ISC2);
GIFR=(1<<INTF1) | (1<<INTF0) | (0<<INTF2);


lcd_init(16);


#asm("sei")

while (1)
      {
      lcd_putchar('*');
      delay_ms(500);
      }
}
