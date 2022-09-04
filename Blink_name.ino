//Gaurish Bhatia
//Student ID: 2110994762.
//Task 2.1P.
//SIT 210.
//REMARKS : This is the code file that I have prepared for blinking my name in the form of morsecode.


// global variables for time delay.
int sample_time_delay = 250;
int hyphen_time_delay = 700;
int dot_time_delay = 300;

void setup() {

  Serial.begin(9600);// begin of the serial communication
  pinMode(LED_BUILTIN, OUTPUT);// this is the initialisation of the built-in LED of the arduino nano.
  digitalWrite(LED_BUILTIN, LOW);
}


void loop() {
  if (Serial.available())
  {
    String sample_Input = "input";// sample string for storing the input.

    sample_Input = Serial.readString();// taking the input from the user.

    String useful = filtering(sample_Input);// getting the useful morsecode via filtering function.
    Output_light(useful);// calling the output light  function for blinking the LED.



  }


}


String filtering(String sample)// function for filtering the input to remove any useless characters or spaces.
{
  char filter = 's';// sample character for storing the value of the sring.
  String sample_output;// sample string variable which will store the morse code.

  for (int i = 0; i < sample.length(); i++)// loop for iterating each character in the loop.
  {
    filter = sample[i];

    if (filter == '.' || '-')// checking if the character is '.' or '-'.
    {
      sample_output = sample_output + filter;// adding it to the output.

    }

  }
  return sample_output;// returning the useful morse code.
}




void Output_light(String Sample_morse)// the function for execution of blinking LED.
{
  for (int j = 0; j < Sample_morse.length(); j++)// loop for iterating through the morse code.
  {
    char required = Sample_morse[j];// sample variable.


    // if else blocks for checking the character.
    if (required == '.').
    {
      digitalWrite(LED_BUILTIN, HIGH);// blinking the LED with suitable time delay.
      delay(dot_time_delay);

    }
    else if (required == '-')
    {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(hyphen_time_delay);

    }

    digitalWrite(LED_BUILTIN, LOW);// blinking the lED.

    delay(sample_time_delay);// suitable time delay.

  }
}
