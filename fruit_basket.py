fruit_basket = ['pineapple', 'pear', 'durian', 'lemon', 'grapefruit']

guess = ''

def banner(content, char):
    # a banner method in order to make the output look nicer
    # the options are the content to be shown and the border style
    # border style has to be length of 1
    banner_horizon = str(char * (len(content) + 4))
    # get the current length of the content and add spacing for the side stars
    banner_side = str(char)
    built_banner = str(banner_horizon + '\n' + banner_side + ' ' + content + ' ' + banner_side + '\n' + banner_horizon)
    return built_banner

while guess.lower() not in fruit_basket:
	try:
		guess = str(input('Guess a fruit:\n'))
		print(banner(str(guess.lower() in fruit_basket), '*'))
	except ValueError:
		print('Please enter a text based guest.')