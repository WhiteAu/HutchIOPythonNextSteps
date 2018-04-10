import argparse

cmd_arg_parser = argparse.ArgumentParser("Hello World: a script for our first steps into Python!")
cmd_arg_parser.add_argument('-u',
                            action="store",
                            dest="user",
                            help="The User to greet! Defaults to None.")


cmd_args = cmd_arg_parser.parse_args()

if cmd_args.user != None:
    print("Hello {}!".format(cmd_args.user))
else:
    print("Hello World!")