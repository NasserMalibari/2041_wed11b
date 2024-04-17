import sys

def chomp(line):
    if line[-1] == "\n":
        line = line[0:-1]
    return line

def qw(line):
    return line.split(' ')

def die(message, exit_status):
    """ prints message and exits with exit_status
        exit_status: int
        message: string 
    """
    print(message ,file=sys.stderr)
    sys.exit(exit_status)


def main():
    print(qw("hello world foo bar"))
    die("error!", 42)
if __name__ == "__main__":
    main()