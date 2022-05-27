from pprint import pprint

import click

from four_devs.four_requests import FourDevsRequests
from four_devs.four_selenium import FourDevsSelenium


def use_requests():
    fd = FourDevsRequests()
    option_events = fd.get_options()
    return fd, option_events


def show_options(fd, option_events):
    fd.show_options(options=option_events)


def use_selenium(_option, option_events, _response):
    fs = FourDevsSelenium(option_events=option_events)
    return fs.execute(_option, _response)


@click.command()
@click.option('--options', '-O', is_flag=True, help='Retorna os opções de evento')
@click.option("--option", '-o', type=int, default=None, help='Número da opção desejada')
def start(options, option):
    option_events = None
    _continue = "S"
    response = {}
    while "S" in _continue:
        if options:
            fd, option_events = use_requests()
            show_options(fd=fd, option_events=option_events)
            option = int(input("\nDigite o número da sua opção:\n"))

        if option:
            if not option_events:
                _, option_events = use_requests()
            response = use_selenium(_option=option, option_events=option_events, _response=response)
            print("\nResultado:")
            pprint(response, indent=4)
            _continue = input("\nDeseja Continuar? (S)im ou (N)ão\n").upper()
            options, option = True, None


# if __name__ == '__main__':
#     start(options=False, option=None)
