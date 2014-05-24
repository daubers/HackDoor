void setup(){
  Serial.begin(9600);
}

void loop(){
  delay(10000);
  Serial.write("hello\n"); 
}
