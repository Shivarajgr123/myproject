''''''
'''
REQ: Employee joined in a company. Give hike to employee based on 
      Rating: 5 
        : 5 - 30% Hike
        : 3-4 - 20% Hike
        : 2-3 - 10% Hike
         1-2 - 0% Hike
        < 1  - Termination
'''
class Employee:
    # STATE
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # BEHAVIOR
    def get_einfo(self):
        print("Employee information: ", self.eid, self.name, self.sal)

    def apply_hike(self, score):
        if score > 5 or score < 0:
            print("Invalid Data")
        else:
            esal = self.sal
            if score == 5:
                esal += esal*30/100
            elif score == 3 or score == 4:
                esal += esal*20/100
            elif score == 2:
                esal += esal * 10 / 100
            elif score == 1:
                print("No salary hike")
            else:
                print("Sorry. You got terminated")
                return
            self.sal = esal
            #print("After hike : ", self.eid, self.name, self.sal)

madhu = Employee(100,'Madhu Nettem', 8000)
madhu.get_einfo()

# Apply hike: Rating: Manager
rating = int(input("Enter rating : "))
madhu.apply_hike(rating)
madhu.get_einfo()