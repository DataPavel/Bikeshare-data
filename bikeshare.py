



# add dictionary of csv files
CITY_DATA = { 'chicago': 'C:\\Users\\averi\\udacity-git-course\\Projects\\bikeshare\\chicago.csv',
              'new york': 'C:\\Users\\averi\\udacity-git-course\\Projects\\bikeshare\\new_york_city.csv',
              'washington': 'C:\\Users\\averi\\udacity-git-course\\Projects\\bikeshare\\washington.csv' }


# main function collects all the functions in the project
def main():
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
