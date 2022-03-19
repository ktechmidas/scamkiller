from mnemonic import Mnemonic

import requests
import random
import click
import time

mnemo = Mnemonic("english")

@click.command()
@click.option('--address', prompt='address to hit with the POST request')
@click.option('--seedname', default='seed')
def generate(address,seedname):

    while True:
        words = mnemo.generate(strength=256)
        r = requests.post(address, data={"phrase_name": "Trust", seedname: words, "phrase_btn": ""})
        print(r.text)
        time.sleep(30)

def main():

    generate()

main()