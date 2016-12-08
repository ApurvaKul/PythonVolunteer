def sleep_in(weekday, vacation):
    Holiday = False
    if (not weekday or vacation):
        Holiday = True
    print(Holiday)
    return Holiday;

sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)
