import argparse
import sys


def parseopts():
    argumentparser = argparse.ArgumentParser(usage='''
    binsget <command> [options]''')

    subparsers = argumentparser.add_subparsers(title='commands', dest='command')

    install_parser = subparsers.add_parser('install', help='Install packages.')

    install_parser.add_argument('-r', '--requirement', action='store',
                                required=True, help='Install from the given requirements file.',
                                metavar='<file>')

    install_parser.add_argument('-s', '--server', action='store',
                                required=True, help='Install from remote binsget server.',
                                metavar='<ip:port>')

    uninstall_parser = subparsers.add_parser('uninstall', help='Uninstall packages.')

    list_parser = subparsers.add_parser('list', help='List installed packages.')

    options = argumentparser.parse_args()

    print(options)


def main():
    options = parseopts()


if __name__ == '__main__':
    sys.exit(main())
