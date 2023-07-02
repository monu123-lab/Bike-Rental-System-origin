import datetime


class BikeRental:

    def __init__(self, stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """

        self.stock = stock

    def display_stock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """

        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

    def rent_bike_on_hourly_basis(self, n):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rent_bike_on_daily_basis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rent_bike_on_weekly_basis(self, n):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n

            return now

    def return_bike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replenishes the inventory
        3. Return a bill
        """
        rental_time, rental_basis, num_of_bikes = request
        bill = 0

        if rental_time and rental_basis and num_of_bikes:
            self.stock += num_of_bikes
            now = datetime.datetime.now()
            rental_period = now - rental_time

            # hourly bill calculation
            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * num_of_bikes

            # daily bill calculation
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * num_of_bikes

            # weekly bill calculation
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * num_of_bikes

            if 3 <= num_of_bikes <= 5:
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """

        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def request_bike(self):
        """
        Takes a request from the customer for the number of bikes.
        """

        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def return_bike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0
