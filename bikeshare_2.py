import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Would you like to see data for Chicago, New York City or Washington? ")
            #print("This is what you entered in lower case: {}".format(city.lower()))
            if CITY_DATA.get(city.lower()) != None:
                #Proceed with next question if the city entered by user is one of the three we are looking for
                #print("Your entered city was found")
                break
            elif CITY_DATA.get(city.lower()) == None and (city.lower() == "nyc" or city.lower() == "new york"):
                #If user enters 'nyc' or 'new york'
                city = "new york city"
                break
            else:
                #For all the other cases i.e. if user enters 'A', '10', 'abscsd' etc.
                print("\nApologies but I couldn\'t understand what you entered. Let\'s try again:")
        except:
            #For all exceptions
            print("\nSomething went wrong - Let\'s try again: \n")
            continue


    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\nWhich month\'s data do you want to see? \nJanuary, February, March, April, May, June or All? ")
            if month.lower() in ["january", "february", "march", "april", "may", "june", "all"]:
                #Proceed with next question if the month entered by user is one from the list
                #print("Your entered month was found")
                break
            elif month.lower() == "jan":
                #If user enters 'jan'
                month = "january"
                break
            elif month.lower() == "feb":
                #If user enters 'feb'
                month = "february"
                break
            elif month.lower() == "mar":
                #If user enters 'mar'
                month = "march"
                break
            elif month.lower() == "apr":
                print("I think you meant \'April\'\n")
                month = "april"
                break
            elif month.lower() == "jun":
                #If user enters 'jun'
                month = "june"
                break
            else:
                #For all other inputs except months e.g. '10', 'abc' etc.
                print("\nApologies but I couldn\'t understand what you entered. Let\'s try again:")
        except:
            #For all exceptions
            print("\nSomething went wrong - Let\'s try again: \n")
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All? ")
            if day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "Saturday", "sunday", "all"]:
                #Proceed with next question if the day entered by user is one from the list
                #print("Your entered day was found")
                break
            elif day.lower() == "mon":
                #If user enters 'mon'
                day = "monday"
                break
            elif day.lower() == "tues" or day.lower() == "tue":
                #If user enters 'Tues' or 'Tue'
                day = "tuesday"
                break
            elif day.lower() == "wed":
                #If user enters 'wed'
                day = "wednesday"
                break
            elif day.lower() == "thu":
                #If user enters 'thu'
                day = "thursday"
                break
            elif day.lower() == "fri":
                #If user enters 'fri'
                day = "friday"
                break
            elif day.lower() == "sat":
                #If user enters 'sat'
                day = "saturday"
                break
            elif day.lower() == "sun":
                #If user enters 'sun'
                day = "sunday"
                break
            else:
                #If user enters anything else e.g. 'A', 'what', '1000' etc.
                print("\nApologies but I couldn\'t understand what you entered. Let\'s try again:")
        except:
            #For all exceptions:
            print("\nSomething went wrong - Let\'s try again: ")
            continue

    print('-'*40)
    #return city, month, day in lower case
    return city.lower(), month.lower(), day.lower()



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    #Fetching month (as number e.g. Jan = 1, June = 6) from start date and adding it as new column 'month' to the dataframe df
    df['month'] = df['Start Time'].dt.month

    #Fetching day's name from start date and adding it as new column 'day_of_week' to the dataframe df
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != "all":
        #converting month entered by user to number
        months = ["january", "february", "march", "april", "may", "june"]
        month_num = months.index(month) + 1

        #filtering dataframe to have data only for the month user entered 
        df = df[df.month == month_num]

    
    if day != "all":
        #filtered DataFrame on day that user entered:
        df = df[df.day_of_week == day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month using mode()
    most_common_month = df['month'].mode()
    
    # get the first row from dataframe i.e. mode value and save in variable, month_num
    month_num = most_common_month.iloc[0]

    # convert the month number to month name
    months = ["january", "february", "march", "april", "may", "june"]
    print("Most common month: {}".format(months[month_num - 1].capitalize()))

    # display the most common day of week using mode()
    most_common_day = df['day_of_week'].mode()
    print("Most common day: {}".format(most_common_day.iloc[0]))

    # display the most common start hour using mode()
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()
    print("Most common start hour: {}".format(most_common_start_hour.iloc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print("Most common start station: {}".format(most_common_start_station.iloc[0]))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print("Most common End station: {}".format(most_common_end_station.iloc[0]))

    # display most frequent combination of start station and end station trip
    
    # Grouping dataframe on Start and End stations, calculating the number of rows as 'counts'
    df_station = df.groupby(['Start Station'])['End Station'].value_counts().reset_index(name='Number of Trips')
    
    # Sorting dataframe in descending order by 'counts' column
    df_station_sorted = df_station.sort_values(by=['Number of Trips'],ascending=False)
    
    print("\nMost frequently used stations:\n{}".format(df_station_sorted.iloc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time and converting seconds to Timedelta object  
    print("Total travel time: {}".format(pd.Timedelta(seconds=df['Trip Duration'].sum())))

    # display mean travel time and converting seconds to Timedelta object
    print("Mean travel time: {}".format(pd.Timedelta(seconds=df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:\n{}".format(df['User Type'].value_counts()))

    # Calculating and displaying counts of gender

    # washington.csv does not have gender column therefore excluding that from calculation and letting user know 
    if(city == 'washington'):
        print("\nNo Gender data available for Washington")
    else:
        print("\nGender count:\n{}".format(df['Gender'].value_counts()))
        

    # Display earliest, most recent, and most common year of birth
    
    # washington.csv does not have Birth year column therefore excluding that from calculation and letting user know 
    if(city == 'washington'):
        print("\nNo Birth year data available for Washington")
    else:
        print("\nBirth year information:\n")
        print("Earliest year: {}".format(int(df['Birth Year'].min())))
        print("Recent year: {}".format(int(df['Birth Year'].max())))
        print("Most common year: {}".format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
      
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        user_stats(df,city)

        trip_detail = input("Would you like to see individual trips data? Enter 'yes' or 'no': ")

        if trip_detail.lower() == 'yes' or trip_detail.lower() == 'y':
            more_trips_detail = ''
            start = 0
            num = 0

            while more_trips_detail.lower() != 'n' or more_trips_detail.lower() == 'no': 
                for i in range(start, len(df)):
                    print(df.iloc[i])
                    num += 1
                    if(num % 5 == 0):
                        break
                    
                more_trips_detail = input("\nEnter 'm' if you want to see more trips or 'n' otherwise: ")
                start = num

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
