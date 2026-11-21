def otp_while(correct_otp, inputs):
    attempts = 0
    i = 0
    while attempts < 3 and i < len(inputs):
        otp = inputs[i]
        i += 1
        if otp == "":
            continue
        attempts += 1
        if otp == correct_otp:
            return "Verified"
        if attempts == 3:
            break
    else:
        return "Locked for 30 minutes"
    return "Locked for 30 minutes"

def otp_for(correct_otp, inputs):
    for attempt in range(3):
        otp = inputs[attempt]
        if otp == "":
            continue
        if otp == correct_otp:
            return "Verified"
        if attempt == 2:
            break
    else:
        return "Locked for 30 minutes"
    return "Locked for 30 minutes"
