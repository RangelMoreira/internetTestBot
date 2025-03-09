from InternetSpeedTwitterBot import InternetSpeedTwitterBot

i = InternetSpeedTwitterBot()
speed_message = i.get_internet_speed()
i.tweet_at_provider(speed_message)
