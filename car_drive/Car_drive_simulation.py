# requirement
# 1. A car  (name, speedLimit, start(), stop(), speedUP(), speedDown(), showSpeed())
# 2. user can start the car 
# 3. user can see Speed,
# 4. can change speed (speedUp 10+, speedDown 10-)
# 5. can stop the car.




class Car:
    carBrand = ""
    speedLimit = 0
    currentSpeed = 0
    isStarted = False
  
    def dashboard(self):
        print(f"-->You are in {self.carBrand}<--")
        print(f"-->Speed limit = {self.speedLimit}km/h<---")
        print(f"-->Current speed = {self.currentSpeed}km/h<---")   
    
    def start(self):
        if self.isStarted:
            print(f"{self.carBrand} is already started.")
         
        if not self.isStarted:
            self.isStarted = True
            print(f"{self.carBrand} is started!")
        self.dashboard()   
   
    def speedUp(self):
        if self.isStarted:
            self.currentSpeed += 10
            if self.currentSpeed > self.speedLimit:
                self.currentSpeed -= 10
                print("you are at max speed.")
                
        if not self.isStarted:
            print(f"Start {self.carBrand} car first!")
        self.dashboard()
        
    def speedDown(self):
        if self.isStarted:
            self.currentSpeed -= 10
            if self.currentSpeed < 0:
                self.currentSpeed += 10
                print("you are at min speed.")
                
        if not self.isStarted:
            print(f"Start {self.carBrand} carf first!")
        self.dashboard()

    def stop(self):
        if self.isStarted:
            self.currentSpeed = 0
            self.isStarted = False
            print(f"{self.carBrand} is Stopped!")
        if not self.isStarted:
            print(f"{self.carBrand} is already Stopped!")
        self.dashboard()

        
# prepare a new car.
Toyota = Car()
Toyota.carBrand = "Toyota"
Toyota.speedLimit = 300

Hundayi = Car()
Hundayi.carBrand = "Hundayi"
Hundayi.speedLimit = 100

Hundayi = Car()
Hundayi.carBrand = "Hundayi"
Hundayi.speedLimit = 100


# *********

while True:
    print("---------------")
    print("1. Start ")
    print("2. speedUp by +10")
    print("3. speedDown  by -10")
    print("4. stop ")
    print("5. exit ")
    print("---------------")
    choice = int(input("Choose an option: "))
    print(f"\nYou have choosen {choice}\n")
    
    if choice == 1:
        Hundayi.start()
        
    elif choice == 2:
        Hundayi.speedUp()
        
    elif choice == 3:
         Hundayi.speedDown()
        
    elif choice == 4:
        Hundayi.stop()
    elif choice == 5:
        break