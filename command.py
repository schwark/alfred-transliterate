# encoding: utf-8

import sys
import re
import argparse
from os import listdir, environ
from workflow.workflow import MATCH_ATOM, MATCH_STARTSWITH, MATCH_SUBSTRING, MATCH_ALL, MATCH_INITIALS, MATCH_CAPITALS, MATCH_INITIALS_STARTSWITH, MATCH_INITIALS_CONTAIN
from workflow import Workflow, ICON_WEB, ICON_NOTE, ICON_BURN, ICON_ERROR, ICON_SWITCH, ICON_HOME, ICON_COLOR, ICON_INFO, ICON_SYNC, web, PasswordNotFound
import subprocess 
import urllib.request
from urllib.error import URLError
from common import languages, input_schemes


log = None

def qnotify(title, text):
    log.debug("notifying..."+text)
    print(text)

def error(text):
    print(text)
    exit(0)

def copy_to_clipboard(text):
    subprocess.run("/usr/bin/pbcopy", text=True, input=text)

def handle_config_commands(wf, args):
    result = False
    # Reinitialize if necessary
    if args.reinit:
        wf.reset()
        qnotify('Transliterate', 'Workflow reinitialized')
        return True

    if args.lang:
        log.debug('saving lang '+args.lang)
        wf.settings['transliterate_lang'] = args.lang
        wf.settings.save()
        qnotify('Transliterate', 'Language set to '+languages[args.lang]['eng'])
        return True

    if args.scheme:
        log.debug('saving scheme '+args.scheme)
        wf.settings['transliterate_scheme'] = args.scheme
        wf.settings.save()
        qnotify('Transliterate', 'Scheme set to '+input_schemes[args.scheme])
        return True
    
def handle_copy_command(wf, args):
    if args.copy:
        text = args.copy
        copy_to_clipboard(text)
        qnotify('Transliterate', text+' on clipboard')
        return True

def main(wf):
    # build argument parser to parse script args and collect their
    # values
    parser = argparse.ArgumentParser()
    # add an optional (nargs='?') --apikey argument and save its
    # value to 'apikey' (dest). This will be called from a separate "Run Script"
    # action with the API key
    parser.add_argument('--lang', dest='lang', nargs='?', default=None)
    parser.add_argument('--scheme', dest='scheme', nargs='?', default=None)
    parser.add_argument('--copy', dest='copy', nargs='?', default=None)
    # reinitialize 
    parser.add_argument('--reinit', dest='reinit', action='store_true', default=False)
    # parse the script's arguments
    args = parser.parse_args(wf.args)
    log.debug("args are "+str(args))

    if(not handle_config_commands(wf, args)):
        # handle copy to clipboard
        handle_copy_command(wf, args)
    return 0


if __name__ == u"__main__":
    wf = Workflow(update_settings={
        'github_slug': 'schwark/alfred-transliterate'
    },libraries=['./lib'])
    log = wf.logger
    sys.exit(wf.run(main))
    