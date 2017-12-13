import click

@click.command()
@click.option('--action', prompt='Action (login|list-boats|gps-serve)',
              help='login, list-boats or gps-serve')
@click.option('--email', default='', prompt='Your email address',
              help='Enter the email address you registered with Sailaway.')
@click.option('--password', default='', prompt='Your password',
              help='Enter the password you registered with Sailaway.')
def main(action, email, password):
    """Simple program that greets NAME for a total of COUNT times."""
    if action == 'login':
        print(action)

if __name__ == '__main__':
    main()
