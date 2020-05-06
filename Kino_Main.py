from flask import Flask, jsonify, request
import requests
import config

def movieApi():
    # set the domain for the api, and give the api key
    key = '&apikey=' + config.key
    search = '?t=' + input('please give a movie to pull info for: ')
    domain = 'http://www.omdbapi.com/' + search + key
    source = requests.get(domain)

    print(source.url)

if __name__ == "__main__":
    movieApi()