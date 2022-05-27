class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name= str(name)
        self.age= int(age)
        self.tracks = tracks
        self.score= float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print("Name:", change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print("Age:", change_age)

    def add_track(self, add_track):
        self.add_track = add_track
        print("Track:", add_track)

    def get_score(self, get_score):
        self.get_score = get_score
        print("Score:", get_score)

Bob = Student(name= "Bob", age= "26", tracks= ["FE","BE"], score= 20.90)

#Expected methods
Bob.change_name("Chiamaka")
Bob.change_age("24")
Bob.add_track("Fullstack")
Bob.get_score("50")
       
     