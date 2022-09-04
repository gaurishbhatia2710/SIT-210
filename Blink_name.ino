//Gaurish Bhatia
//Student ID: 2110994762.
//Task 2.1P.
//SIT 210.
//REMARKS : This is the code file that I have prepared for blinking my name in the form of morsecode.

int sample_time_delay = 250;
int hyphen_time_delay = 700;
int dot_time_delay = 300;

void setup() {

  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);// this is the initialisation of the built-in LED of the arduino nano.
  digitalWrite(LED_BUILTIN, LOW);
}


void loop() {
  if (Serial.available())
  {
    String sample_Input = "input";

    sample_Input = Serial.readString();

    String useful = filtering(sample_Input);
    Output_light(useful);



  }


}


String filtering(String sample)
{
  char filter = 's';
  String sample_output;

  for (int i = 0; i < sample.length(); i++)
  {
    filter = sample[i];

    if (filter == '.' || '-')
    {
      sample_output = sample_output + filter;

    }

  }
  return sample_output;
}




void Output_light(String Sample_morse)
{
  for (int j = 0; j < Sample_morse.length(); j++)
  {
    char required = Sample_morse[j];



    if (required == '.')
    {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(dot_time_delay);

    }
    else if (required == '-')
    {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(hyphen_time_delay);

    }

    digitalWrite(LED_BUILTIN, LOW);

    delay(sample_time_delay);

  }
}
