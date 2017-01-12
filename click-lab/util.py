import click


@click.command()
@click.option('--count', default=5, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(str(x) + name)


@click.group()
def cli():
    pass


@click.command()
def initdb():
    click.echo('Initialized the database')


@click.command()
def dropdb():
    click.echo('Dropped the database')


cli.add_command(initdb)
cli.add_command(dropdb)
