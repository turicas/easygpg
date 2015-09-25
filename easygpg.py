# coding: utf-8

# Copyright 2015 Álvaro Justen <https://github.com/turicas/rows/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import shlex
import subprocess
import sys

import click


__version__ = '0.1.0-dev'


def echo(message):
    click.echo('[easygpg] {}'.format(message))


def gpg(command, verbose=False):
    command = 'gpg {}'.format(command)
    if verbose:
        echo('Executing: {}'.format(command))
    subprocess.call(shlex.split(command))


@click.group()
@click.version_option(version=__version__, prog_name='easygpg')
@click.option('-v', '--verbose', count=True)
@click.pass_context
def cli(context, verbose):
    context.obj = {'verbose': verbose, }


@cli.group()
@click.pass_context
def key(context):
    pass


@cli.group()
@click.pass_context
def certificate(context):
    pass


@certificate.command(help='Receive a public key certificate from a key server')
@click.option('--key-server', default='pgp.mit.edu')
@click.argument('key_id')
@click.pass_context
def get(context, key_server, key_id):
    gpg('--keyserver {} --recv-key {}'.format(key_server, key_id),
        verbose=context.obj['verbose'])


@certificate.command(help='Send a public key certificate to a server')
@click.option('--key-server', default='pgp.mit.edu')
@click.argument('key_id')
@click.pass_context
def send(context, key_server, key_id):
    gpg('--keyserver {} --send-key {}'.format(key_server, key_id),
        verbose=context.obj['verbose'])


@key.command(help='Create a new PGP key pair')
@click.pass_context
def create(context):
    gpg('--gen-key', verbose=context.obj['verbose'])


@key.command(name='list', help='List available keys')
@click.pass_context
def list_(context):
    # TODO: list-key, list-keys, list-secret-keys
    gpg('--list-keys', verbose=context.obj['verbose'])


@key.command(help='Delete keys from local trusted base')
@click.pass_context
def delete(context):
    # TODO: delete-keys, delete-secret-keys, delete-secret-and-public-keys
    gpg('--delete-keys', verbose=context.obj['verbose'])


@key.command(help='Print the fingerprint for a key')
@click.argument('key_id')
@click.pass_context
def fingerprint(context, key_id):
    gpg('--fingerprint {}'.format(key_id), verbose=context.obj['verbose'])


@cli.group(help='Sign a file or key with your private key')
@click.pass_context
def sign(context):
    pass


@sign.command(help='Sign a public key')
@click.argument('key_id')
@click.pass_context
def key(context, key_id):
    gpg('--sign-key {}'.format(key_id), verbose=context.obj['verbose'])


if __name__ == '__main__':
    cli()
