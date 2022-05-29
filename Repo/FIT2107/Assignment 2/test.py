import json
import requests
from datetime import *
import calendar
import holidays

aus_holidays = holidays.Australia()  # all the holiday date for Australia

date_s = datetime(2020, 3, 3, 5, 0)
date_e = datetime(2020, 3, 3, 7, 10)
print(date_e - date_s)


# date_aus = date(2020, 3, 3)
# print(date_aus in aus_holidays)

# # loc_list = []

# def get_location_id(name, postcode):
#     '''
#     Retrieves the id of a location from the API
#     '''
#     response = requests.get("http://118.138.246.158/api/v1/location?postcode=" + postcode)
#     jsonContent_location = json.loads(response.text)

#     for i in range(len(jsonContent_location)):
#         if jsonContent_location[i]["name"] == name:
#             print(jsonContent_location[i]["name"])
#             return jsonContent_location[i]["id"]
#     raise Exception(f"Argument {name} is wrongly formatted or does not exist")


# # ALG1 EXAMPLE 1
# response = requests.get("http://118.138.246.158/api/v1/location?postcode=7250")
# jsonContent_location = json.loads(response.text)
# # print(jsonContent_location)



# response_weather = requests.get("http://118.138.246.158/api/v1/weather?location=" + "5998b29a-8e3d-4c1e-857c-b5dce80eea6d" + "&date=" + "2020-03-03")
# jsonContent_weather = json.loads(response_weather.text)
# print(" ")
# print(jsonContent_weather)

# # si = jsonContent_weather["sunHours"]
# # print(si)

# # sun_rise = datetime.strptime(jsonContent_weather["sunrise"] + " 2020-12-25", "%H:%M:%S %Y-%m-%d")
# # sun_set = datetime.strptime(jsonContent_weather["sunset"] + " 2020-12-25", "%H:%M:%S %Y-%m-%d")
# # print(sun_rise)
# # print(sun_set)
# # diff = (sun_set - sun_rise).total_seconds() / 60  / 60

# # start_time = 8 # t = 8am
# # duration_charge = 1 # d = 1hr

# # solar = si * duration_charge/diff * 50 * 0.2 # 8.6 *1/14.23 * 1 * 50 * 0.2

# # print(solar)

# # ALG1 EXAMPLE 2
# # response = requests.get("http://118.138.246.158/api/v1/location?postcode=7250")
# # jsonContent_location = json.loads(response.text)
# # string_id = jsonContent_location[0]["id"]

# # response_weather = requests.get("http://118.138.246.158/api/v1/weather?location=" + string_id + "&date=" + "2021-02-22")
# # jsonContent_weather = json.loads(response_weather.text)
# # si = jsonContent_weather["sunHours"]

# # sun_set = datetime.strptime(jsonContent_weather["sunset"], "%H:%M:%S")
# # sun_rise = datetime.strptime(jsonContent_weather["sunrise"], "%H:%M:%S")

# # print(sun_rise)
# # print(sun_set)
# # time_now = datetime.strptime("05:35", "%H:%M")
# # time_now = time_now + timedelta(minutes = 30)
# # only_time = time_now.time()
# # print((sun_set - time_now).total_seconds() / 60 / 60)

# # for i in range(len(jsonContent_location)):
# #     loc_list.append(jsonContent_location[i]["name"])
# # target = loc_list[4]

# # response_2 = requests.get("http://118.138.246.158/api/v1/location?postcode=5000")
# # jsonContent_location_2 = json.loads(response.text)
# # for i in range(len(jsonContent_location_2)):
# #     if jsonContent_location_2[i]["name"] == target:
# #         print(jsonContent_location_2[i]["id"])

# # try:
# #     status_code = jsonContent_weather["statusCode"]
# #     print(status_code)
# # except KeyError:
# #     print("It works!")

# # print(jsonContent_weather["sunHours"])
# # sun_rise = datetime.strptime(jsonContent_weather["sunrise"] + " 2020-02-22", "%H:%M:%S %Y-%m-%d")
# # sun_set = datetime.strptime(jsonContent_weather["sunset"] + " 2020-02-22", "%H:%M:%S %Y-%m-%d")
# # print((sun_set - sun_rise).total_seconds() /60/60)
# # print(sun_rise)
# # print(sun_rise.minute)

# # start = datetime.strptime("06:00", "%H:%M") 
# # finish = datetime.strptime("18:00", "%H:%M")
# # start_now = datetime.strptime("18:00", "%H:%M") + timedelta(minutes=5)
# # print(start <= start_now <= finish)

# # print((finish-start).total_seconds()  /60 /60)

# # def location_exist(location, postcode):   
# #     list_loc = []

# #     response = requests.get("http://118.138.246.158/api/v1/location?postcode=" + postcode)
# #     jsonContent_location = json.loads(response.text)
# #     for i in range(len(jsonContent_location)):
# #         list_loc.append(jsonContent_location[i]["name"])
# #     print(list_loc)

# # location_exist("", "5000")

#     # get id of location
#     # location_url = self.apiURL + self.postcode
#     # json_location = requests.get(location_url)
#     # location_id = json.loads(json_location.text)[0]["id"]

#     # # get sunrise and sunset times
#     # weather_url = self.apiURL + "weather?location=" + location_id + "&date=" + self.start_date
#     # json_weather = requests.get(weather_url)
#     # jsonText_weather = json.loads(json_weather.text)

#     # # sunrise
#     # sun_rise = datetime.strptime(jsonText_weather["sunrise"] + " " + self.start_date, "%H:%M:%S %d/%m/%Y")

#     # # sunset
#     # sun_set = datetime.strptime(jsonText_weather["sunset"] + " " + self.start_date, "%H:%M:%S %d/%m/%Y")

#     # # start_time
#     # start_time_dt = datetime.strptime(self.start_time + " " + self.start_date, "%H:%M %d/%m/%Y")

#     # # duration of charge
#     # charge_duration = self.time_calculation(self.final_charge, self.initial_state) # in minutes

#     # # end_time
#     # end_time = start_time_dt + timedelta(minutes= charge_duration)

#     # #  .st..SR.....et......SS......
#     # if (start_time_dt < sun_rise) and (sun_rise <= end_time <= sun_set):
#     #     print(sun_rise, end_time)
#     # # .....SR...st..et.....SS......
#     # elif (sun_rise <= start_time_dt <= sun_set) and (sun_rise <= end_time <= sun_set):
#     #     print(start_time_dt, end_time)
#     # # .....SR......st......SS..et..
#     # elif (sun_rise <= start_time_dt <= sun_set) and (end_time < sun_set):
#     #     print(start_time_dt, sun_set)
#     # # .st..SR..............SS..et..
#     # elif (start_time_dt < sun_rise) and (end_time > sun_set):
#     #     print(sun_set - sun_rise)
#     # # .....SR..............SS.st.et..
#     # elif (start_time_dt > sun_set) and (end_time > sun_set):
#     #     print(0)
#     # # ..st.et...SR..............SS...
#     # elif (start_time_dt < sun_rise) and (end_time < sun_rise):
#     #     print(0)


# # start = datetime.strptime()

# # def calculate_solar_energy(self, du, hour):
# #     si = self.get_solar_insolation()
# #     cc = self.get_cloud_cover(hour)
    
# #     cal = si*du/dl*(1 - (cc/100))*50*0.2
# #     return cal

# # def cal_cloud_intervals(self):
# #     start_time = self.get_daylight_length_charge()[0]
# #     end_time = self.get_daylight_length_charge()[1]
# #     i = start_time.hour() + 1
# #     length = end_time.hour() - start_time.hour()

#     # if (x):
#     #     for i in range(length):


# # print(datetime.strptime("13:20", "%H:%M"))


# # now_date = datetime.now()

# # print(now_date)
# # now_date = now_date.AddYears(-1)
# # print(now_date)

# # def get_previous_valid_date(date):
# #     """
# #     Helps return previous date of the future date.
# #     :param date: takes in date as a datetime format
# #     :return: returns the date that a year before
# #     """
# #     valid_date = False
# #     first_date = []
# #     date_dt = datetime.strptime(date, "%d/%m/%Y")

# #     while not valid_date:
# #         if calendar.isleap(date_dt.year):
# #             date_dt -= timedelta(days=366)
# #             if date_dt <= datetime.now():
# #                 valid_date = True
# #                 first_date.append(date_dt.strftime("%d/%m/%Y"))
# #         else:
# #             date_dt -= timedelta(days=365)
# #             if date_dt <= datetime.now():
# #                 valid_date = True
# #                 first_date.append(date_dt.strftime("%d/%m/%Y"))

# #     for i in range(2):
# #         first_date.append(get_previous_two_dates(date_dt)[i])

# #     return first_date

# # def get_previous_two_dates(date):
# #     two_dates = []

# #     for _ in range(2):
# #         if calendar.isleap()):
# #             date -= timedelta(days=366)
# #             two_dates.append(date.strftime("%d/%m/%Y"))
# #         else:
# #             date -= timedelta(days=365)
# #             two_dates.append(date.strftime("%d/%m/%Y"))

# #     return two_dates

# # date_t = "29/8/2020"
# # print(get_previous_valid_date(date_t))

