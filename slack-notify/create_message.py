def console_login_message(iam_name, source_ip, result="Success"):
    message = "The " + iam_name + " login from " + \
        source_ip + " as a result " + result
    return message
