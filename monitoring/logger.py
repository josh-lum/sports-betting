def log_error(msg):
    # Append error message to a log file
    with open('logs/errors.log', 'a') as f:
        f.write(msg + '\n')
