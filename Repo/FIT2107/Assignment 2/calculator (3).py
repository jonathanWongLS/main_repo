import holidays
from datetime import *
import json
import requests
import calendar
import re

aus_holidays = holidays.Australia()  # all the holiday date for Australia


class Calculator():
    def __init__(self, initial, final, cap, charger, dates, times, postcodes, location):
        self.initial_state = initial
        self.final_charge = final
        self.capacity = cap
        self.charger_config = charger
        self.start_date = dates
        self.start_time = times
        self.postcode = postcodes
        self.location = location.upper()
        self.apiURL = "http://118.138.246.158/api/v1/"
        self.location_id = ""

    def get_api_location(self):
        """
        A function that helps concat the url with location and postode
        :return: the jsonContent of the location
        """
        self.test_valid_postcode()

        response = requests.get(self.apiURL + "location?postcode=" + self.postcode)
        jsonContent_location = json.loads(response.text)
        return jsonContent_location

    def get_location_id(self):
        """
        Retrieves the id of a location from the API
        :return: the jsonContent of the location that matches.
        """
        self.test_valid_location()

        jsonContent_location = self.get_api_location()

        for i in range(len(jsonContent_location)):
            if jsonContent_location[i]["name"] == self.location:
                self.location_id = jsonContent_location[i]["id"]
                return self.location_id
        raise Exception(f"Argument {self.location} is wrongly formatted or does not exist")

    def get_weather_api(self, dates):
        """
        Retrieve the current api for the date and location.
        :param dates: input a date format as a string
        :return:
        """
        location_id = self.get_location_id()

        str_date = str(datetime.strptime(dates, '%d/%m/%Y').strftime('%Y-%m-%d'))

        # get sunrise and sunset times
        weather_api = self.apiURL + "weather?location=" + location_id + "&date=" + str_date
        return weather_api

    def get_json_content(self, api):
        try:
            # Try to request from API
            r = requests.get(api)

            # if API can be obtained with requests then change the self variable json_content
            if r.ok:
                self.json_content = r.json()
                return self.json_content
            else:
                return None
        except requests.exceptions.Timeout:
            return "Bad Response"

    def cost_calculation(self):
        """
        Calculating cost value with initial state and final charge
        :return: a value of cost
        """
        self.test_valid_start_date()
        self.test_valid_start_time()
        self.test_valid_initial()
        self.test_valid_final()

        date_time = self.start_date + " " + self.start_time + ":00"
        if self.is_surcharged(date_time):
            surcharge_factor = 1.1
            if self.is_surcharged_to_not():
                cost = self.cost_par(int(self.initial_state), int(self.final_charge), 0.5, surcharge_factor)
                return cost

        else:
            surcharge_factor = 1
            if self.is_not_to_surcharged():
                cost = self.cost_par(int(self.initial_state), int(self.final_charge), 0.5, surcharge_factor)
                return cost

        if self.is_peak(self.start_time + ":00"):
            if self.is_peak_to_off():
                mid = self.middle_charge()
                first = self.cost_par(int(self.initial_state), mid, 1, surcharge_factor)
                second = self.cost_par(mid, int(self.final_charge), 0.5, surcharge_factor)
                cost = first + second
            else:
                cost = self.cost_par(int(self.initial_state), int(self.final_charge), 1, surcharge_factor)

        else:
            if self.is_off_to_peak():
                mid = self.middle_charge()
                first = self.cost_par(int(self.initial_state), mid, 0.5, surcharge_factor)
                second = self.cost_par(mid, int(self.final_charge), 1, surcharge_factor)
                cost = first + second
            else:
                cost = self.cost_par(int(self.initial_state), int(self.final_charge), 0.5, surcharge_factor)

        return cost

    def cost_par(self, initial_state, final_state, base_price, surcharge_factor):
        """
        A partial function that calculate the cost using the formula given.
        :param initial_state: takes in an integer value ranging from 1-100 but less than final_state
        :param final_state: takes in an integer value ranging from 1-100 but more than initial_state
        :param base_price: takes in either 0.5 or 1
        :param surcharge_factor: takes in either 1 or 1.1
        :return: a value of cost
        """

        if int(initial_state) > int(final_state):
            raise ValueError("Initial charge must be lesser than final charge")
        elif int(initial_state) < 0:
            raise ValueError("Initial charge cannot be lesser than 0")
        elif int(initial_state) > 99:
            raise ValueError("Initial charge cannot be more than 99")

        if int(final_state) < int(initial_state):
            raise ValueError("Final charge must be more than initial charge")
        elif int(final_state) > 100:
            raise ValueError("Final charge cannot be more than 100")
        elif int(final_state) < 1:
            raise ValueError("Final charge cannot be less than 1")

        if base_price != 0.5 and base_price != 1:
            raise ValueError("Base price can only be 1 or 0.5 in numerical form.")
        elif surcharge_factor != 1 and surcharge_factor != 1.1:
            raise ValueError("Surcharge can only be 1 or 1.1 in numerical form.")

        cost = (final_state - initial_state) / 100 * int(self.capacity) * base_price * self.get_charger_val()[1] / 100 \
               * surcharge_factor

        return cost

    def time_calculation(self, final_charge, initial_state):
        """
        A function that calculates the time from initial_state to final_charge
        :param final_charge: takes in an integer value ranging from 1-100 but more than initial_state
        :param initial_state: takes in an integer value ranging from 1-100 but less than final_state
        :return: the time after calculation by minutes
        """
        if int(initial_state) > int(final_charge):
            raise ValueError("Initial charge must be lesser than final charge")
        elif int(initial_state) < 0:
            raise ValueError("Initial charge cannot be lesser than 0")
        elif int(initial_state) > 99:
            raise ValueError("Initial charge cannot be more than 99")

        if int(final_charge) < int(initial_state):
            raise ValueError("Final charge must be more than initial charge")
        elif int(final_charge) > 100:
            raise ValueError("Final charge cannot be more than 100")
        elif int(final_charge) < 1:
            raise ValueError("Final charge cannot be less than 1")

        times = (int(final_charge) - int(initial_state)) / 100 * int(self.capacity) / self.get_charger_val()[0]

        return times * 60  # in hours then times 60 to make it minutes

    def middle_charge(self):
        """
        A function that finds the middle value of the state after going through the given time.
        :return: a float value of mid_charge.
        """
        self.test_valid_start_time()
        self.test_valid_capacity()
        self.test_valid_initial()

        mid_charge = (100 * self.time_diff(self.start_time) / int(self.capacity) * self.get_charger_val()[0]) + int(
            self.initial_state)

        return mid_charge

    def time_diff(self, start_time):
        """
        To find the time difference from the start_time and the start/end of peak
        :param start_time: a string value of time format ..:..
        :return: either a float or int value of the time difference calculated
        """
        if type(start_time) != str:
            raise ValueError("Input should be in String format")
        datetime.strptime(start_time,"%H:%M")

        if self.is_off_to_peak() and not self.is_peak(start_time + ":00"):
            start_peak = datetime.strptime("06:00", "%H:%M")
            now = datetime.strptime(start_time, "%H:%M")
            diff = (start_peak - now).total_seconds() / 60 / 60
            return diff  # in hours

        elif self.is_peak_to_off() and self.is_peak(start_time + ":00"):
            end_peak = datetime.strptime("18:00", "%H:%M")
            now = datetime.strptime(start_time, "%H:%M")
            diff = (end_peak - now).total_seconds() / 60 / 60
            return diff  # in hours

        # if it isn't both peak to off peak and vice versa it will just return minute of 0
        else:
            return 0

    def is_peak(self, start_time):
        """
        Takes time and checks if it is in peak hour
        :param start_time: the start_time needs to be in H:M:S format
        :return: returns a boolean
        """

        start_peak = datetime.strptime("06:00", "%H:%M")
        end_peak = datetime.strptime("18:00", "%H:%M")
        now = datetime.strptime(start_time, "%H:%M:%S")
        return start_peak <= now <= end_peak

    def is_peak_to_off(self):
        """
        Checks if it is still on peak hour after adding the time to the start_time.
        :return: a boolean
        """
        self.test_valid_start_time()
        self.test_valid_final()
        self.test_valid_initial()

        end_times = datetime.strptime(self.start_time, "%H:%M") \
                    + timedelta(minutes=self.time_calculation(int(self.final_charge), int(self.initial_state)))
        end_time1 = str(end_times.time()).split(".", 1)[0]
        return not self.is_peak(end_time1)

    def is_off_to_peak(self):
        """
        Checks if it is still on off peak hours after adding the time to the start_time.
        :return: a boolean
        """
        self.test_valid_start_time()
        self.test_valid_final()
        self.test_valid_initial()

        end_times = datetime.strptime(self.start_time, "%H:%M") \
                    + timedelta(minutes=self.time_calculation(int(self.final_charge), int(self.initial_state)))
        end_time1 = str(end_times.time()).split(".", 1)[0]
        return self.is_peak(end_time1)

    def is_surcharged(self, dates):
        """
        Takes dates and checks if it is surcharged or not
        :param dates: the dates needs to be in %d/%m/%Y %H:%M:%S format
        :return: returns a boolean
        """
        self.test_valid_surchaged(dates)

        weekno = datetime.strptime(dates, "%d/%m/%Y %H:%M:%S").weekday()
        if weekno < 5:
            d = "Weekday"
        else:  # 5 Sat, 6 Sun
            d = "Weekend"

        return dates in aus_holidays or d == "Weekday"

    def is_surcharged_to_not(self):
        """
        Checks if it still on surcharged date after adding the time to the start_date
        :return: returns a boolean
        """
        self.test_valid_start_time()
        self.test_valid_start_date()
        self.test_valid_initial()
        self.test_valid_final()

        start_date = self.start_date + " " + self.start_time
        end_date = datetime.strptime(start_date, "%d/%m/%Y %H:%M") \
                   + timedelta(minutes=self.time_calculation(self.final_charge, self.initial_state))

        end_date1 = end_date.strftime('%d/%m/%Y %H:%M:%S')

        return not self.is_surcharged(end_date1)

    def is_not_to_surcharged(self):
        """
        Checks if it still on a non surcharged date after adding the time to the start_date
        :return: returns a boolean
        """
        self.test_valid_start_time()
        self.test_valid_start_date()
        self.test_valid_initial()
        self.test_valid_final()

        start_date = self.start_date + " " + self.start_time
        end_date = datetime.strptime(start_date, "%d/%m/%Y %H:%M") \
                   + timedelta(minutes=self.time_calculation(self.final_charge, self.initial_state))
        end_date1 = end_date.strftime('%d/%m/%Y %H:%M:%S')
        return self.is_surcharged(end_date1)

    def get_charger_val(self):
        """
        Getter method that gets the power or the base value of the current configuration.
        :return: a tuple of int/float values
        """
        self.test_valid_charger_config()

        if self.charger_config == "1":
            return 2, 5
        elif self.charger_config == "2":
            return 3.6, 7.5
        elif self.charger_config == "3":
            return 7.2, 10
        elif self.charger_config == "4":
            return 11, 12.5
        elif self.charger_config == "5":
            return 22, 15
        elif self.charger_config == "6":
            return 36, 20
        elif self.charger_config == "7":
            return 90, 30
        elif self.charger_config == "8":
            return 350, 50

    def get_daylight_length_charge(self):
        """
        This method helps returns start time and end time for the solar energy calculation
        :return: a tuple with datetime format of the start time and end time to calculate solar energy
        """
        self.test_valid_start_time()
        self.test_valid_initial()
        self.test_valid_final()

        # sunrise
        sun_rise = datetime.strptime(self.get_sunrise_sunset()[0], "%H:%M:%S")

        # sunset
        sun_set = datetime.strptime(self.get_sunrise_sunset()[1], "%H:%M:%S")

        # start_time
        start_time_dt = datetime.strptime(self.start_time, "%H:%M")

        # duration of charge
        charge_duration = self.time_calculation(self.final_charge, self.initial_state)  # in minutes

        # end_time
        end_time = start_time_dt + timedelta(minutes=charge_duration)

        #  .st..SR.....et......SS......
        if (start_time_dt < sun_rise) and (sun_rise <= end_time <= sun_set):
            return sun_rise, end_time
        # .....SR...st..et.....SS......
        elif (sun_rise <= start_time_dt <= sun_set) and (sun_rise <= end_time <= sun_set):
            return start_time_dt, end_time
        # .....SR......st......SS..et..
        elif (sun_rise <= start_time_dt <= sun_set) and (end_time > sun_set):
            return start_time_dt, sun_set
        # .st..SR..............SS..et..
        elif (start_time_dt < sun_rise) and (end_time > sun_set):
            return sun_rise, sun_set
        # .....SR..............SS.st.et..
        elif (start_time_dt > sun_set) and (end_time > sun_set):
            return None
        # ..st.et...SR..............SS...
        elif (start_time_dt < sun_rise) and (end_time < sun_rise):
            return None
        else:
            return None

    # to be acquired through API
    def get_sunrise_sunset(self):
        """
        Get the time when sunrise and sunset in a tuple
        :return: tuple with datetime format
        """
        start_time = self.json_content["sunrise"]
        end_time = self.json_content["sunset"]

        # mock_api.return_value = MagicMock(sunrise= "05:44", sunset= "19:23")

        return start_time, end_time

    # to be acquired through API
    def get_day_light_length(self):
        """
        Get the time duration from sunrise and sunset in hours (dl)
        :return: a value of duration in hours
        """

        start_time = self.json_content["sunrise"]
        end_time = self.json_content["sunset"]

        # convert date from string to datetime format
        start = datetime.strptime(start_time, "%H:%M:%S")
        end = datetime.strptime(end_time, "%H:%M:%S")

        # duration in hours
        duration = (end - start).total_seconds() / 60 / 60

        return duration

    # to be acquired through API
    def get_solar_insolation(self):
        """
        Get sun hours (si) from API given the date.
        :return: returns the si value
        """
        sun_hours = self.json_content["sunHours"]

        return sun_hours

    # to be acquired through API
    def get_cloud_cover(self, hour):
        """
        Get cloud cover percentage given a specific hour
        :param hour: takes in an int ranging from 0-23
        :return: the cc % of the current date and hour
        """
        if type(hour) != int:
            raise ValueError("Hour should be in Integer format")
        elif hour < 0 or hour > 23:
            raise ValueError("Hour must be in between 0 and 23")

        cloud_cover = self.json_content["hourlyWeatherHistory"][hour]["cloudCoverPct"]

        return cloud_cover

    def check_future_date(self, dates):
        """
        Checks if the date input is in the future or not
        :param dates: takes in date as a string format
        :return: a boolean
        """
        self.test_valid_dates(dates)

        now_date = datetime.now()
        date1 = datetime.strptime(dates, "%d/%m/%Y")
        if date1 > now_date:
            return True
        else:
            return False

    def get_previous_valid_date(self, dates):
        """
        Helps return previous date of the future date.
        :param dates: takes in date as a string format
        :return: returns the date that a year before
        """
        self.test_valid_dates(dates)

        valid_date = False
        first_date = []
        date_dt = datetime.strptime(dates, "%d/%m/%Y")

        while not valid_date:
            if calendar.isleap(date_dt.year):
                date_dt -= timedelta(days=366)
                if date_dt <= datetime.now():
                    valid_date = True
                    first_date.append(date_dt.strftime("%d/%m/%Y"))
            else:
                date_dt -= timedelta(days=365)
                if date_dt <= datetime.now():
                    valid_date = True
                    first_date.append(date_dt.strftime("%d/%m/%Y"))

        for i in range(2):
            first_date.append(self.get_previous_two_dates(date_dt)[i])

        return first_date

    def get_previous_two_dates(self, dates):
        """
        get 2 previous date from the valid date.
        :param dates: takes in as a string of date format
        :return: returns a string of date
        """

        two_dates = []

        for _ in range(2):
            if calendar.isleap(dates.year - 1):
                dates -= timedelta(days=366)
                two_dates.append(dates.strftime("%d/%m/%Y"))
            else:
                dates -= timedelta(days=365)
                two_dates.append(dates.strftime("%d/%m/%Y"))

        return two_dates

    def calculate_solar_energy(self, du, hour):
        """
        takes in parameters and calculate the solar energy
        :param du: takes in as a float
        :param hour: takes in as a int
        :return: returns a value of cal
        """
        if type(du) != float:
            raise ValueError("du should be in float or int format")
        if type(hour) != int:
            raise ValueError("Hour should be in Integer format")
        elif hour < 0 or hour > 23:
            raise ValueError("Hour must be in between 0 and 23")

        si = float(self.get_solar_insolation())
        cc = float(self.get_cloud_cover(hour))
        dl = float(self.get_day_light_length())

        cal = si * du / dl * (1 - (cc / 100)) * 50 * 0.2

        return cal

    def cal_is_peak(self, net, surcharged, times):
        """
        checking if the current hour is peak and calculating the cost at the current hour
        :param net: takes in a value of net
        :param surcharged: takes in a value of surcharged
        :param times: inputs time that is in string
        :return: return a value of cost
        """

        if self.is_peak(times):
            cost = 0.1 * net * surcharged
        else:
            cost = 0.1 * net * surcharged * 0.5

        return abs(cost)

    def cal_solar_energy_cost(self):
        """
        Firstly it checks if the start date is surcharged. It will then check if the time duration
        is 0 then it will just return the cost. If it is more than 1 then it will loop through
        different hour and calculate the solar energy calculation and returns in cost.
        :param: dates in a string value.
        :return: cost value.
        """

        if self.get_daylight_length_charge() is None:
            return 0

        # Sets the start time, end tim and current configuration value from methods called below.
        daylight_charge = self.get_daylight_length_charge()
        start_time = daylight_charge[0]
        end_time = daylight_charge[1]
        curr_config = self.get_charger_val()[0]

        # taking end_time value without decimal places in seconds.
        end_time1 = str(end_time).split(".", 1)[0]

        # changing the format of dates in string to datetime format
        str_start_time = datetime.strptime(str(start_time), "%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S')
        str_end_time = datetime.strptime(end_time1, "%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S')

        solar_energy_sum = 0  # to accumulate calculation
        cost = 0
        length = end_time.hour - start_time.hour  # complete hours in between start and finish
        surcharged_val = 1  # default surcharged value is 1

        # If the date input is surcharged then it the surcharged value will be 1.1
        if self.is_surcharged(start_time.strftime('%d/%m/%Y %H:%M:%S')):
            surcharged_val = 1.1

        # When difference of length is 0 where start time is 15:15 and end time is 15:45
        if length == 0:
            solar_energy_sum += self.calculate_solar_energy((end_time.minute - start_time.minute) / 60,
                                                            start_time.hour)

            net = (curr_config * (end_time.minute - start_time.minute) / 60) - solar_energy_sum

            cost = self.cal_is_peak(net, surcharged_val, str_start_time)

        # When difference of length is more than 1 where start time is 15:15 and end time is 16:45
        elif length >= 1:
            solar_energy_sum = self.calculate_solar_energy((60 - start_time.minute) / 60, start_time.hour)

            net = (curr_config * (60 - start_time.minute) / 60) - solar_energy_sum

            cost += self.cal_is_peak(net, surcharged_val, str_start_time)

            # When difference of length is more than 1 where start time is 15:15 and end time is 17:45
            if length >= 2:
                for i in range(start_time.hour + 1, end_time.hour):
                    solar_energy_sum = self.calculate_solar_energy(1.0, i)

                    net = curr_config - solar_energy_sum

                    cost += self.cal_is_peak(net, surcharged_val, str(i) + ":00:00")

            solar_energy_sum += self.calculate_solar_energy(end_time.minute / 60, end_time.hour)

            net = (curr_config * end_time.minute / 60) - solar_energy_sum

            cost += self.cal_is_peak(net, surcharged_val, str_end_time)

        return cost

    def final_cost_calculation(self):
        """
        This function first checks if it is a future date, if it is then it will find the 3 preceeding dates
        if it isn't then it will return the current date.
        It first calculate the cost calculation and the solar energy cost and the difference between
        both of the value.
        :return: it returns the final cost value
        """
        self.test_valid_start_date()

        # use cost_calculation method to find the cost charging without the solar cost.
        cost_charging = self.cost_calculation()

        if self.check_future_date(self.start_date):
            previous_dates = self.get_previous_valid_date(self.start_date)
            x1 = previous_dates[0]
            # assign the self.json_content to the current date needed.
            self.get_json_content(self.get_weather_api(x1))
            x = self.cal_solar_energy_cost()

            y1 = previous_dates[1]
            # assign the self.json_content to the current date needed.
            self.get_json_content(self.get_weather_api(y1))
            y = self.cal_solar_energy_cost()

            z1 = previous_dates[2]
            # assign the self.json_content to the current date needed.
            self.get_json_content(self.get_weather_api(z1))
            z = self.cal_solar_energy_cost()

            # Calculate the average of all 3 preceding dates solar cost value.
            solar_cost = (x + y + z) / 3

        else:
            self.get_json_content(self.get_weather_api(self.start_date))
            solar_cost = self.cal_solar_energy_cost()

        final_cost = cost_charging - solar_cost
        if final_cost < 0:
            final_cost = 0

        return final_cost

    """
    The test functions below does a check for every instance variables which is inputted from the webpage
    to be called in the methods to raise the corresponding errors.
    """
    def test_valid_initial(self):
        if self.initial_state is None:
            raise AssertionError('Field cannot be empty')
        elif self.initial_state == '':
            raise ValueError("Field cannot be empty")
        elif type(self.initial_state) != str:
            raise ValueError("Input should be in String format")
        elif not self.initial_state.isnumeric():
            raise ValueError("Initial charge must be of numerical values only")
        elif int(self.initial_state) > int(self.final_charge):
            raise ValueError("Initial charge must be lesser than final charge")
        elif int(self.initial_state) < 0:
            raise ValueError("Initial charge cannot be lesser than 0")
        elif int(self.initial_state) > 99:
            raise ValueError("Initial charge cannot be more than 99")

    def test_valid_final(self):
        if self.final_charge is None:
            raise AssertionError('Field cannot be empty')
        elif self.final_charge == '':
            raise ValueError("Field cannot be empty")
        elif type(self.final_charge) != str:
            raise ValueError("Input should be in String format")
        elif not self.final_charge.isnumeric():
            raise ValueError("Final charge must be of numerical values only")
        elif int(self.final_charge) < int(self.initial_state):
            raise ValueError("Final charge must be more than initial charge")
        elif int(self.final_charge) > 100:
            raise ValueError("Final charge cannot be more than 100")
        elif int(self.final_charge) < 1:
            raise ValueError("Final charge cannot be less than 1")

    def test_valid_capacity(self):
        if self.capacity is None:
            raise AssertionError('Field cannot be empty')
        elif self.capacity == '':
            raise ValueError("Field cannot be empty")
        elif type(self.capacity) != str:
            raise ValueError("Input should be in String format")
        elif not self.capacity.isnumeric():
            raise ValueError("Battery pack capacity must be of numerical values only")
        elif int(self.capacity) <= 0:
            raise ValueError("Battery pack capacity cannot be empty or negative")

    def test_valid_charger_config(self):
        if self.charger_config is None:
            raise AssertionError('Field cannot be empty')
        elif self.charger_config == '':
            raise ValueError('Field cannot be empty')
        elif type(self.charger_config) != str:
            raise ValueError("Input should be in String format")
        elif not self.charger_config.isnumeric():
            raise ValueError("Charger configuration must be of numerical values only")
        elif int(self.charger_config) < 1 or int(self.charger_config) > 8:
            raise ValueError("Charger configuration is only between 1 to 8")

    def test_valid_start_date(self):
        if datetime.strptime(self.start_date, "%d/%m/%Y") < datetime.strptime("01/07/2008", "%d/%m/%Y"):
            raise ValueError("Invalid")

    def test_valid_start_time(self):
        if self.start_time is None:
            raise AssertionError('Field cannot be empty')
        elif self.start_time == '':
            raise ValueError("Field cannot be empty")
        elif type(self.start_time) != str:
            raise ValueError("Input should be in String format")
        datetime.strptime(self.start_time,"%H:%M")

    def test_valid_postcode(self):
        if self.postcode is None:
            raise AssertionError('Field cannot be empty')
        elif self.postcode == '':
            raise ValueError('Field cannot be empty')
        elif type(self.postcode) != str:
            raise ValueError("Input should be in String format")
        elif not self.postcode.isnumeric():
            raise ValueError("Post code must be of numerical values only")
        elif len(self.postcode) != 4:
            raise ValueError("Post code must have 4 digits only")

    def test_valid_location(self):
        if self.location is None:
            raise AssertionError('Field cannot be empty')
        elif self.location == '':
            raise ValueError('Field cannot be empty')
        elif type(self.location) != str:
            raise ValueError("Input should be in String format")
        elif has_numbers(self.location):
            raise ValueError("Location should not contain numerical values")
        elif not location_exist(str(self.location).upper(), self.postcode):
            raise ValueError("Location provided is not in the post code area")

    def test_valid_surchaged(self, dates):
        if type(dates) != str:
            raise ValueError("Input should be in String format")

        datetime.strptime(dates, "%d/%m/%Y %H:%M:%S")

    def test_valid_dates(self, dates):
        if datetime.strptime(dates, "%d/%m/%Y") < datetime.strptime("01/07/2008", "%d/%m/%Y"):
            raise ValueError("Invalid Date")


# helper function to check if a string has numbers in it
def has_numbers(instr):
    return any(char.isdigit() for char in instr)

#helper function to check if the provided location is in the post code
def location_exist(location , postcode):
    if has_numbers(location) or not postcode.isnumeric():
        return False

    list_loc = []
    response = requests.get("http://118.138.246.158/api/v1/location?postcode=" + postcode)
    jsonContent_location = json.loads(response.text)
    for i in range(len(jsonContent_location)):
        list_loc.append(jsonContent_location[i]["name"])

    if location in list_loc:
        return True
    else:
        return False

if __name__ == "__main__":
    calc = Calculator("15", "74", "65", "7", "27/11/2021", "04:24", "7250", "LAUNCESTON")
    print(calc.final_cost_calculation())
    print(calc.get_sunrise_sunset())