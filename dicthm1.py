movies = {}

cast_animal = ["Ranbir Kapoor","Rashmika Mandanna","Bobby Deol","Anil Kapoor"]
cast_pathan = ["Shah Rukh Khan","Deepika Padukone","John Abraham","Salman Khan"]
cast_war2 = ["Hrithik Roshan","Kiara Advani","Jr NTR","Anil Kapoor"]
cast_war = ["Hrithik Roshan","Vaani Kapoor","Tiger Shroff","Aashutosh Rana"]

movies["Animal"] = cast_animal
movies["Pathan"] = cast_pathan
movies["War2"] = cast_war2
movies["War"] = cast_war

count = 0

for cast in movies.values():
    count = count + cast.count("Anil Kapoor")

print("Occurrences of Anil Kapoor:", count)