# cliq: creating command line interface quickly

cliq is a lightweight framework for creating a command line application or
writing a libary powered with command line tools. 

- supports nested subcommands
- equiped with init and config system
- supports multiple command line tools in a single library
- only depends on the standard library


## Quick Start

Install cliq:

```
$ pip install cliq
```

Create your project:

``` 
$ cliq create project ./myapp
$ pip install -e ./myapp
$ myapp
```

Create a new command:

```
$ cliq create command do.py
$ python do.py -h
```

Add the command to your project:

```
$ mv do.py ./myapp/myapp/main/command/
$ myapp do -h
```

Edit your command:

- It's just an argparse.ArgumentParser
- See <https://docs.python.org/3/library/argparse.html>
- Add arguments to the `self.parser`
- Write the `run` method

```python
class Command(SimpleCommand):
    def __init__(self, app = None, name = __name__):
        super().__init__(app, name)

        # self.parser is an argparse.ArumentParser
        # see https://docs.python.org/3/library/argparse.html       
        #
        # add arguments. for example:
        #
        # self.parser.add_argument('input', type=str, help='input filename')
        # self.parser.add_argument('-v', '--verbose', action='store_true', help='verbose')
        # self.parser.add_argument('-o', '--output', type=str, help='output filename')

    def run(self, argv):
        args = self.parser.parse_args(argv)

        # implement command line functionalities
        print(args)
 
```

Remove `help`, `init`, `config` commands if you don't need them:

```
$ cd ./myapp/myapp/main/command
$ rm help.py init.py config.py
```

## Commands

- A command is standalone and complete by itself. 
- You can run it as an independent script. 
- Just copy a command script into your project.
- There is nothing to be configured.

Try toy sample commands:

```
$ cliq say hello
hello
$ cliq please say hello
hello
$ cliq please sum 1 2 3 4 5
15.0
```

Download a command script file:

```
$ wget https://raw.githubusercontent.com/youhyunjo/cliq/main/cliq/main/command/please.py
$ python please.py sum 1 2 3 4 5
15.0
```

Add it into your project:


```
$ mv please.py ./myapp/myapp/main/command/
$ myapp please sum 1 2 3 4 5
15.0
```




## Tutorials
### Simple command

Generate a simple command template script file:

```
$ cliq create command say.py  
$ python say.py -h
usage: __main__ [-h]

options:
  -h, --help  show this help message and exit
```

Add arguments to `self.parser` and implement `run` method:

```python
class Command(SimpleCommand):
    def __init__(self, app = None, name = __name__):
        super().__init__(app, name)
        
        self.parser.add_argument('something', type=str, help='something')
        
    def run(self, argv):
        args = self.parser.parse_args(argv)
        print(args.something)
```

Use it:

```
$ python say.py hello
hello
```


### Complex command with nested subcommands

Create a command script file with the subcommands option:

```
$ cliq create command do.py --with-subcommands something,anything,nothing 
```

Test it:

```
$ python do.py
usage: __main__ [-h] {something,anything,nothing} ...

options:
  -h, --help            show this help message and exit

subcommands:
  {something,anything,nothing}
                        command help
    something           something
    anything            anything
    nothing             nothing

```

Edit it and put it into the command directory:

```
$ mv do.py myapp/myapp/main/command/
```

### Project with multiple command line modules

You can create a project with multiple command line interface modules.

```
$ cliq create project ./holy --with-cli graham,terry 
$ pip install -e ./holy
```

Directory strucutre:

```
holy/
└── holy
    ├── graham
    │   └── main
    │       └── command
    └── terry
        └── main
            └── command
```

Test cli modules:

```
$ graham -h 
...

$ terry -h 
...
```

Add commands:

```
$ cliq create command holy/holy/graham/main/command/play.py
$ graham play -h
```


