import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
                'new york city': 'new_york_city.csv',
                'washington': 'washington.csv' }

def get_filters():
    day, month = 'all', 'all'
    print('\nHello! Let\'s explore some US bikeshare data!')
    
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease choose one state from: \n1-Chicago\n2-New York City\n3-Washington\n-').lower()
#User input validation
        while city not in CITY_DATA.keys():
            print("That's invalid input! choose the correct city name,please...")
            city = input('\nPlease choose one state from: \n1-Chicago\n2-New York City\n3-Washington\n-').lower()


        #Filter types for user input..
        filter_type = input('Would you like to filter the data by month, day or both\n-').lower()
        while filter_type not in (['month', 'day', 'both']):
            print('Type a valid filter type...')
            filter_type = input('Would you like to filter the data by month, day or both? ').lower()
            
        #break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    #while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        if filter_type == 'month' or filter_type == 'all':
            month = input('\n\nTo filter {}\'s date by a particular month, please type the month or all for not filtering by month : \n1-January \n2-February \n3-March \n4-April \n5-May \n6-June \n7-All\n-'.format(city.title())).lower()
            #while month != 'all' and month not in months:
            while month not in months:
                
                print('That\'s invalid choice, please type a valid month name or all\n-')
                month = input('\n\nTo filter {}\'s date by a particular month, please type the month or all for not filtering by month : \n1-January \n2-February \n3-March \n4-April \n5-May \n6-June \n7-All\n-'.format(city.title())).lower()

            

            else:
                month = 'all'
 
        break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['sat', 'sun', 'mon', 'tues', 'wed', 'thru', 'fri','all']
        if filter_type == 'day' or filter_type == 'all':
            day = input("\n\nTo filter data by particular day, kindly type the appreviated week name from:\n \n1-Sat \n2-Sun \n3-Mon \n4-Tues \n5-Wed \n6-Thru \n7-Fri \n8-All \n- ").lower()
            while day not in days:
                print('That\'s invalid choice, please type a valid day name or all.')

                #day = input('\n\nTo filter data by particular day, kindly type the appreviated name such as (Sat, Sun, Mon, Tues, Wed, Thru, Fri) or all for not filtering by day : \n\n ').lower()
        

            else:
                day = 'all'


        break
    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    
    #read data
    
    df = pd.read_csv(CITY_DATA[city])
    
    #Conver Start Time Col. to Datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time col. to new col.
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #Filtering by month if it available
    if month != 'all':
        



        #Use index of month list to get corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1



        #Filter by month to create new dataframe
        df = df[df['month'].str.startwith(month.title)()]


    #Filter by day of week
    if day != 'all':
        df = df[df['day_of_week'].str.startswith(day.title())]



    return df

def display_raw_data(df):
    print('\nRaw data is available to check... \n')
    #The fuction takes the name of the city produced by the get_filters fuction as input and returns the raw data of that city as chunks of 5 rows based upon user input.
#Display by user answer..

    display_raw = input('Would you like to display the first 5 rows of data? type: Yes for agree and No for disagree \n').lower()
    if display_raw.lower() == 'yes':
        x = 0
        while True:
            print(df.iloc[x: x+5])
            x+=5
            another_rows = input('Do you want to show another 5 rows?\n')
            if another_rows.lower() != 'yes':
                break



                  

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is: ', most_common_day)

    # TO DO: display the most common start hour
    #Convert Start Time to datetime
    df['hour'] = df['Start Time'].dt.hour

    #Extract hour from Start Time col. to create an hour col
    
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is: ' , most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    


    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly start station is: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly end station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    #The two columns are grouped by(['Start Station'], ['End Station'])

    most_frequent_start_end = (df['Start Station'] + '|' + df['End Station']).mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time =df['Trip Duration'][0]
    print('\nThe total trip duration by seconds:\n', total_travel_time, 'seconds')
    print('\nThe total trip duration by minutes:\n', total_travel_time/60, 'minutes')
    print('\nThe total trip duration by hours:\n', total_travel_time/3600, 'hours')
          
    # TO DO: display mean travel time
    average_of_time = df['Trip Duration'].mean()
    print('\nAverage travel time by seconds:\n', average_of_time, 'seconds')
    print('\nAverage travel time by minutes:\n', average_of_time/60, 'minutes')
    print('\nAverage travel time by hours:\n', average_of_time/3600, 'hours')

                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_users = df['User Type'].value_counts().to_frame()
    print('\nCounts of user types is:\n ',count_of_users)
    try:
        count_of_gender = df['Gender'].value_counts().to_frame()
        print('\nCount of gender split:\n',count_of_gender)

        
        earlist_by = int(df['Birth Year'].min())
        print('\nThe earlist birth year is:\n ', earlist_by)

        recent_by = int(df['Birth Year'].max())
        print('\nThe most recent birth year is:\n ', recent_by)

        common_year = int(df['Birth Year'].mode()[0])
        print('\nThe most common birth year is:\n ', common_year)

        #Dealing with Washington
    except KeyError:
        print('This data is not available for Washintgon')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break





