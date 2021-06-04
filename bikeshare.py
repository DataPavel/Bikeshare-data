



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
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
