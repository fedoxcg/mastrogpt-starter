#--kind python:default
#--web true
#--param OLLAMA_HOST $OLLAMA_HOST
#--param AUTH $AUTH
#END TODO

import stateless
import os

def main(args):
  return { "body": stateless.stateless(args) }
