import re
def change(res,dict):
     n=int(res[2])
     start=int(res[1])
     destination=int(res[0])
     for i in range(n):
         dict[start+i]=destination+i
     return dict
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input5.txt", "r") as f:
    input=f.read().strip().split("\n\n")

seeds_to_soil_dict={}
soil_to_fertilizer_dict={}
fertilizer_to_water_dict={}
water_to_light_dict={}
light_to_temperature_dict={}
temperature_to_humidity_dict={}
humidity_to_location_dict={}

seeds=re.findall("\d+",input[0])
seeds=[int(x) for x in seeds]
seeds_to_soil=input[1].split("\n")
soil_to_fertilizer=input[2].split("\n")
fertilizer_to_water=input[3].split("\n")
water_to_light=input[4].split("\n")
light_to_temperature=input[5].split("\n")
temperature_to_humidity=input[6].split("\n")
humidity_to_location=input[7].split("\n")


for item in seeds_to_soil:
    res=re.findall("\d+",item)
    if res!=[]:
        seeds_to_soil_dict=change(res,seeds_to_soil_dict)

for item in soil_to_fertilizer:
    res=re.findall("\d+",item)
    if res!=[]:
        soil_to_fertilizer_dict=change(res,soil_to_fertilizer_dict)

for item in fertilizer_to_water:
    res=re.findall("\d+",item)
    if res!=[]:
        fertilizer_to_water_dict=change(res,fertilizer_to_water_dict)

for item in water_to_light:
    res=re.findall("\d+",item)
    if res!=[]:
        water_to_light_dict=change(res,water_to_light_dict)

for item in light_to_temperature:
    res=re.findall("\d+",item)
    if res!=[]:
        light_to_temperature_dict=change(res,light_to_temperature_dict)

for item in temperature_to_humidity:
    res=re.findall("\d+",item)
    if res!=[]:
        temperature_to_humidity_dict=change(res,temperature_to_humidity_dict)

for item in humidity_to_location:
    res=re.findall("\d+",item)
    if res!=[]:
       humidity_to_location_dict=change(res,humidity_to_location_dict)

garden={}
for seed in seeds: 
   soil=seed if seed not in seeds_to_soil_dict else seeds_to_soil_dict[seed]
   fertilizer=soil if soil not in soil_to_fertilizer_dict else soil_to_fertilizer_dict[soil]
   water=fertilizer if fertilizer not in fertilizer_to_water_dict else fertilizer_to_water_dict[fertilizer] 
   light=water if water not in  water_to_light_dict else water_to_light_dict[water]
   temperature=light if light not in  light_to_temperature_dict else light_to_temperature_dict[light]
   humidity= temperature if temperature not in temperature_to_humidity_dict else temperature_to_humidity_dict[temperature]
   location= humidity if humidity not in  humidity_to_location_dict else humidity_to_location_dict[humidity]
   garden[seed]=location
lowest_location=10000000000
for key in garden:
   lowest_location=min(location,garden[key])
print(lowest_location)