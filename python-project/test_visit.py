from visit import createGraph



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_createGraph():
    try:
        #assert count1 == 5, "Running count_all_stars([2, 3])... Expected 5, got {}".format(count1)
        success()

    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    test_count_all_stars()
