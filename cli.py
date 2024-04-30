import json_manager
import click

@click.group()
def cli():
    pass

@cli.command()
def users():
    data = json_manager.read_json()
    print(data)
    
if __name__ == '__main__':
    cli()