import click

from four_devs.four_requests import FourDevsRequests
from four_devs.four_selenium import FourDevsSelenium


def use_requests():
    fd = FourDevsRequests()
    option_events = fd.get_options()
    return fd, option_events


def show_options(fd, option_events):
    fd.show_options(options=option_events)


def use_selenium(_option, option_events):
    fs = FourDevsSelenium(option_events=option_events)
    fs.execute(_option)


# @click.command()
# @click.option('--options', '-O', is_flag=True, help='Retorna os opções de evento')
# @click.option("--option", '-o', type=int, default=None)
def start(options, option):
    option_events = None

    if options:
        fd, option_events = use_requests()
        show_options(fd=fd, option_events=option_events)
        option = int(input("\nDigite o número da sua opção:\n"))

    if option:
        if not option_events:
            option_events = use_requests()
        use_selenium(_option=option, option_events=option_events)


if __name__ == '__main__':
    start(options=True, option=None)
