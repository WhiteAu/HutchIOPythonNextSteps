import argparse
import yaml

cmd_arg_parser = argparse.ArgumentParser("A example script that combines config files and command line arguments to show how they can be used.")
cmd_arg_parser.add_argument('-t', action="store_true", default=False,
                            dest="is_test",
                            help="Set mode to test. There will be additional debug information and no computationally expensive functions will be run.")
cmd_arg_parser.add_argument('-g',
                            action="store_true",
                            default=True,
                            dest="is_branch_one",
                            help="Set mode to Branch one")
cmd_arg_parser.add_argument('-c', action="store_true",
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
                            dest="all_chromosomes",
                            help="Run PCA over all Chromosomes. WARNING: This is computationally expensive!")
cmd_arg_parser.add_argument('--chromosomes',
                            nargs='+',
                            type=int,
                            default=[],
                            dest="chromosome_num",
                            help="Run PCA over specific chromosomes. WARNING: This is computationally expensive!")

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
    cfg_name = cfg_branch['name']
    cfg_branch = cfg_branch['branch1-1']


elif cmd_args.is_branch_two:
    cfg_branch = config['treeroot']['branch2']
    cfg_name = cfg_branch['name']
    cfg_branch = cfg_branch['branch2-1']

else:
    raise(Exception())

if cmd_args.model_dir != None:
    model_directory = cmd_args.model_dir

chromosomes=[]
if cmd_args.all_chromosomes:
    chromosomes = list(range(1,23))
elif cmd_args.chromosome_num != []:
    chromosomes = cmd_args.chromosome_num
else:
    print("neither --chromosomes or -a were provided on the command line. Provided args were {}".format(cmd_args))
    raise(Exception("Either specify all chromosomes using -a or specific chromosomes using --chromosomes <space separated list eg: 1 2 3...>"))

print("our chosen cfg_name: {} our chosen cfg_branch: {}".format(cfg_name, cfg_branch))