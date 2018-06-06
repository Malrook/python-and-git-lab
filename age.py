import datetime

# declare variables
today = datetime.date.today()
current_age = 0

def age_calc(age):
    # return a string of saying the users current age and the age they will be in 2035
    return str("If you are " + str(age) + " in  "+ str(today.year) + " then you will be " + str(2035 - today.year + age) + " in 2035")

def banner(content, char):
    # a banner method in order to make the output look nicer
    # the options are the content to be shown and the border style
    # border style has to be length of 1
    banner_horizon = str(char * (len(content) + 4))
    # get the current length of the content and add spacing for the side stars
    banner_side = str(char)
    built_banner = str(banner_horizon + '\n' + banner_side + ' ' + content + ' ' + banner_side + '\n' + banner_horizon)
    return built_banner

while current_age <= 99 and current_age >= 0:
    # keep checking asking until the user enters 100 or more
    try:
        # the input is as expected and can continue
        current_age = int(input('What is you age? '))
        print(banner(age_calc(current_age), '*'))
    except ValueError:
        # the input is not as expected and must be collected again
        if(current_age != int):
            print('please input an integer')