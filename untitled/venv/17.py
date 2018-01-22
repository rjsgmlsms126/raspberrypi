def print_args(argc, *argv):

    for i in range(argc):
        print(argv[i])


print_args(3,'arg1','argv2','argv3')