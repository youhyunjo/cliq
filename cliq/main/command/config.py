"""config
"""

_setup_ = {
    'version' : '0.0.1',
    'description' : 'Get and set local (workspace) or global (user) options'
}

import sys
from cliq.main.command import SimpleCommand
from cliq.core.config import Config

def init(app):
    return ConfigCommand(app)

class ConfigCommand(SimpleCommand):
    def __init__(self, app, name='config'):
        super().__init__(app, name)

        self.parser.add_argument('-l', '--list', action='store_true', help='list all options')
        #self.parser.add_argument('--unset', action='store_true', help='remove a variable: name')
        self.parser.add_argument('--unset', type=str, nargs= '?', help='remove a variable: name')
        self.parser.add_argument('name', type=str, nargs='?')
        self.parser.add_argument('value', type=str, nargs='?')
        
        location_group = self.parser.add_mutually_exclusive_group()
        location_group.add_argument('--global', action='store_true', help='use global config file')
        location_group.add_argument('--local', action='store_true', help='use local config file')

    def run(self, argv):

        args = self.parser.parse_args(argv)
        
        try:
            config = self.app.config
        except Exception as e:
            sys.exit(str(e))

        if args.list :
            if args.name is not None or args.value is not None:
                print('error: wrong number of arguments, should be 0')
                self.parser.print_help()


            if getattr(args, 'global') :
                config = self.app.config.global_config
            elif args.local:
                config = self.app.config.local_config



            # self.app.config.finder.global_config_filename
            # self.app.config.finder.local_config_filename

            for secname in config.sections():
                for name in config[secname]:
                    print(secname + '.' + name + '=' + config[secname][name])
        elif args.name is not None:
            try:
                section, name = args.name.split('.')
            except ValueError:
                sys.exit('error: key does not contain a section: {}'.format(args.name))
                
            if args.value is None:    
                print(config[section][name])
            else:
                if getattr(args, 'global'):
                    config.set_global(section, name, args.value)
                else:
                    try:
                        config.set_local(section, name, args.value)
                    except OSError:
                        sys.exit('fatal: not in a {} directory'.format(self.app.name))

        else:
            self.parser.print_help()
