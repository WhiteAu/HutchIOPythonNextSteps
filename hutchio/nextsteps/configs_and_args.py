import argparse
import yaml

cmd_arg_parser = argparse.ArgumentParser("A example script that combines config files and command line arguments to show how they can be used.")
cmd_arg_parser.add_argument('-t', action="store_true", default=False,
                            dest="is_test",
                            help="Set mode to test. There will be additional debug information and no computationally expensive functions will be run.")
cmd_arg_parser.add_argument('--b1',
                            action="store_true",
                            default=True,
                            dest="is_branch_one",
                            help="Set mode to Branch one")
cmd_arg_parser.add_argument('--b2', action="store_true",
                            default=False,
                            dest="is_branch_two",
                            help="Set mode to Branch two")
cmd_arg_parser.add_argument('--load',
                            action="store",
                            dest="model_dir",
                            help="Load model(s) from directory to restart model learning from a saved checkpoint. This is false by default")
cmd_arg_parser.add_argument('-a',
                            action="store_true",
                            default=False,
                            dest="allnums",
                            help="A flag to run all of our numbers!")
cmd_arg_parser.add_argument('--nums',
                            nargs='+',
                            type=int,
                            default=[],
                            dest="numlist",
                            help="A flag to supply an optional list of 1+ numbers")

cmd_args = cmd_arg_parser.parse_args()

print("We can conditionally set variables based on whether a command line argument is supplied!")
if cmd_args.is_test == True:
    print("We are running n test mode!")
    exe_mode = "Test"
else:
    print("We are running in production mode!")
    exe_mode = "Production"
print("In this case, we have set the variable exe_mode to be {} based on a command line arg".format(exe_mode))

print("If we have a more static set of parameters that we want to persist between sessions, we can store these in a config file.")
with open('../config.yaml') as f:
    # use safe_load instead load
    config = yaml.safe_load(f)

print("Python-YAML reads a text file in as a dictionary, which can be used to store parameters")
print("Our config file looks like: {}".format(config))


src_dir = None
data_dir = None
input_dir = None
if cmd_args.is_branch_one:
    cfg_branch = config['treeroot']['branch1']
elif cmd_args.is_branch_two:
    cfg_branch = config['treeroot']['branch2']
else:
    raise(Exception())

cfg_name = cfg_branch['name']
cfg_branch = cfg_branch['inner_branch']

if cmd_args.model_dir != None:
    model_directory = cmd_args.model_dir

'''
below we use some basic if/else logic to condense two possible cmd line arguments to a single variable
'''
nums=[]

if cmd_args.allnums and cmd_args.numlist != []:
    raise(Exception("These are mutually exclusive!"))
elif cmd_args.allnums:
    nums = list(range(1,23))
elif cmd_args.numlist != []:
    nums = cmd_args.numlist
else:
    print("neither --nums or -a were provided on the command line. Provided args were {}".format(cmd_args))
    raise(Exception("Either specify all nums using -a or specific nums using --nums <space separated list eg: 1 2 3...>"))

def num_param_parser(all_flag, nums_flag):
    logic_fails = False
    print("do some complex logic here!")
    if logic_fails:
        raise(Exception())
    else:
        return None


print("our chosen cfg_name: {} our chosen cfg_branch: {}".format(cfg_name, cfg_branch))
print("from our allnums/num-list split, we got: {}".format(nums))
print("our supplied model directory from the command line is: {}".format(cmd_args.model_dir))
print("all our command line arguments were: {}".format(cmd_args))