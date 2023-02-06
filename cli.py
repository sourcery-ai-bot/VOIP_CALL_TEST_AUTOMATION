import argparse

"""
goodbye_parser = subparsers.add_parser('goodbye', help='goodbye command')
goodbye_parser.add_argument("name", help="your name")
goodbye_parser.set_defaults(func=goodbye)

args = parser.parse_args()
args.func(args.name)


"""
def p(a):
    print(a)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help="sub-command help")

# Parser Register externsion
register_parser = subparsers.add_parser("Register", help="Register extension")
register_parser.add_argument("-id", "--id", help="ID the account")
register_parser.add_argument("-pwd", "--password", help="Password for register the account")
register_parser.add_argument("-s", "--server", help="Server for register")
register_parser.add_argument("-p", "--port", help="Server for register")
register_parser.add_argument("-e", "--show", help="Show devices register")

# Parser Call

call_parser = subparsers.add_parser("Call", help="Call")
call_parser.add_argument("-P", "--path", help="Path for file with numbers")
call_parser.add_argument("-St", "--Start", help="Start Call for number")
call_parser.add_argument("-C", "--Cancel", help="Cancel call")
call_parser.add_argument("-l", "--log", help="Show call logs")

# Parser Pcap

pcap_parser = subparsers.add_parser("grep", help="grep")
pcap_parser.add_argument("--grep", help="Show pcap in sngrep")

# Parser Create profile 

profile_parser = subparsers.add_parser("profile", help="Pcap")
profile_parser.add_argument("--CreateProfile", help="Create Profile")

args = parser.parse_args()

def main(parser):
    match hasattr(args, id):
        case args.id != None:
            print(args.id)
        case args.pwd != None:
            print(args.pwd)


if __name__ == "__main__":
    main(args)