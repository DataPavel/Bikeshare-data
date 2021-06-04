import time
import pandas as pd
import numpy as np
import calendar



# add dictionary of csv files
CITY_DATA = { 'chicago': 'C:\\Users\\averi\\udacity-git-course\\Projects\\bikeshare\\chicago.csv',
              'new york': 'C:\\Users\\averi\\udacity-git-course\\Projects\\bikeshare\\new_york_city.csv',
              'washington': 'C:\\Users\\averi\\udacity-git-course\\Projects\\bikeshare\\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    city = input('What city do you want to explore Washington, New York or Chicago?').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('What month do you want to select? January, February, March, April, May, June or all? ').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('What day of the week do you want to select? Monday, Tuesday, Wednesday, Thursday, '
                'Friday, Saturday, Sunday or all? ').lower()


    return city, month, day

def load_data(city, month, day):
 #   """
 #  Loads data for the specified city and filters by month and day if applicable.

 # Args:
 #    (str) city - name of the city to analyze
 #   (str) month - name of the month to filter by, or "all" to apply no month filter
 #  (str) day - name of the day of week to filter by, or "all" to apply no day filter
 #Returns:
 #   df - pandas DataFrame containing city data filtered by month and day
 # """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
# Adding new columns to dataframe "month" and "day_of_week"
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
#filtering by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = int(months.index(month)) + 1
        df = df[df['month'] == month]
#filtering by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        #displaying five rows of data
    rows = input('Do you want to see the first five rows?')
    x = 0
    y = 5

    while rows == 'yes':
        print(df.iloc[x:y])
        rows = input('Do you want to see the next five rows?')
        x = x + 5
        y = y + 5
    print('-' * 40)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = calendar.month_name[df['month'].mode()[0]]
    print('The most frequent month of travel is {}'.format(common_month))
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most frequent day of travel is {}'.format(common_day))
    # display the most common start hour
    df['Start hour'] = df['Start Time'].dt.hour
    common_start = df['Start hour'].mode()[0]
    print('The most frequent start hour of Travel is {}'.format(common_start))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station =df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(common_start_station))

    # display most commonly used end station
    common_end_station =df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' and ' + df['End Station']

    common_combination = df['Trip'].mode()[0]
    print('The most commonly used combination is {}'.format(common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sec = float(df['Trip Duration'].sum())
    days = int(sec // (24*3600))
    sec = sec % (24*3600)
    hours = int(sec // 3600)
    sec = sec % 3600
    mins = int(sec // 60)
    sec = int(sec % 60)

    print('Total travel time is {} days, {} hours, {} minutes and {} seconds'.format(days,hours,mins,sec))

    # display mean travel time
    sec = float(df['Trip Duration'].mean())
    days = int(sec // (24*3600))
    sec = sec % (24*3600)
    hours = int(sec // 3600)
    sec = sec % 3600
    mins = int(sec // 60)
    sec = int(sec % 60)

    print('Total mean travel time is {} days, {} hours, {} minutes and {} seconds'.format(days, hours, mins, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usertype = df.groupby(df['User Type'])['User Type'].count()
    print('Below are counts of user types: \n\n{}'.format(usertype))
    # Display counts of gender
    while True:
        try:
            gender = df.groupby(df['Gender'])['Gender'].count()
            print('\nBelow are counts by gender:\n{}'.format(gender))
            break
        except:
            print('No information on Gender is available for Washington')
            break
    # Display earliest, most recent, and most common year of birth
    while True:
        try:
            earliest = int(df['Birth Year'].min())
            recent = int(df['Birth Year'].max())
            common = int(df['Birth Year'].mode()[0])
            print('\nThe earliest year of birth is {}\nThe most recent year of birth is {}\nThe most common'
                ' year of birth is {}'.format(earliest,recent,common))
            break
        except:
            print('No information on Birth is available for Washington')
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# main function collects all the functions in the project
def main():
    while True:
        while True:
            city, month, day = get_filters()
            if city in CITY_DATA and \
                    month in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and \
                    day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturdays', 'sunday', 'all']:
                break
            else:
                print('Please correct the entries')
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
