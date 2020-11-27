#include "esphome.h"

class PowerSaverBuzzer : public Component, public FloatOutput
{
public:
  void setup() override
  {
    pinMode(16, OUTPUT);
  }
  void write_state(float state) override
  {
    // state is the amount this output should be on, from 0.0 to 1.0
    // we need to convert it to an integer first
    int value = state * 1024;
    if (value==0) {
      ESP_LOGD("main","Buzzer is off");
      noTone(16);
      return;
    }
    tone (16,value);
    ESP_LOGD("main", "Buzzer set to frquency of %dHz", value);
  }
};

// void loop() override
// {
//   static unsigned long lastChange = 0;
//   unsigned long l = millis() - lastChange;
//   static bool b;
//   if (l < 500)
//   {
//     return;
//   }
//   if (b) {
//     // tone(16,400);
//   } else {
//     noTone(16);
//   }
//   b = !b;
//   lastChange = millis();
// }
