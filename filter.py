# encoding: utf-8

import sys
import argparse
from workflow.workflow import MATCH_ATOM, MATCH_STARTSWITH, MATCH_SUBSTRING, MATCH_ALL, MATCH_INITIALS, MATCH_CAPITALS, MATCH_INITIALS_STARTSWITH, MATCH_INITIALS_CONTAIN
from workflow import Workflow, ICON_WEB, ICON_NOTE, ICON_BURN, ICON_ERROR, ICON_SWITCH, ICON_HOME, ICON_COLOR, ICON_INFO, ICON_SYNC, web, PasswordNotFound
from workflow.background import run_in_background, is_running
from lib.google.transliteration import transliterate_text
from common import languages, input_schemes

log = None

def error(text):
    print(text)
    exit(0)

def add_prereq(wf, args):
    result = False
    word = args.query.lower().split(' ')[0] if args.query else ''
    lang = wf.settings.get('transliterate_lang')
    if not lang:
        wf.add_item('No language found...',
                    'Please use t lang to set your language',
                    valid=False,
                    icon=ICON_ERROR)
        result = True
    if lang and is_chinese(lang):
        scheme = wf.settings.get('transliterate_scheme')
        if not scheme:
            wf.add_item('No scheme found...',
                        'Please use t scheme to set your input scheme for asian languages',
                        valid=False,
                        icon=ICON_ERROR)
            result = True
    # Check for an update and if available add an item to results
    if wf.update_available:
        # Add a notification to top of Script Filter results
        wf.add_item('New version available',
            'Action this item to install the update',
            autocomplete='workflow:update',
            icon=ICON_INFO)
    return result

def add_config_commands(wf, query, config_commands):
    word = query.lower().split(' ')[0] if query else ''
    config_command_list = wf.filter(word, config_commands.keys(), min_score=80)
    if config_command_list:
        if len(config_command_list) > 1:
            for cmd in config_command_list:
                wf.add_item(config_commands[cmd]['title'],
                            config_commands[cmd]['subtitle'],
                            arg=config_commands[cmd]['args'],
                            autocomplete=config_commands[cmd]['autocomplete'],
                            icon=config_commands[cmd]['icon'],
                            valid=config_commands[cmd]['valid'])
        elif config_command_list[0] in config_commands:
            param = query.lower().split(' ')[1] if (query and ' ' in query) else ''
            if 'lang' == config_command_list[0]:
                query = ''
                results = wf.filter(param, languages.values(), key=search_key_for_language, min_score=80)
                if results:
                    for line in results:
                        wf.add_item(line['eng'],
                                    line['lng'],
                                    arg='--lang '+line['code'],
                                    autocomplete=line['eng'],
                                    icon=ICON_COLOR,
                                    valid=True)
            elif 'scheme' == config_command_list[0]:
                query = ''
                lang = wf.stored_data('transliterate_lang')
                if lang:
                    param = query.lower().split(' ')[1] if (query and ' ' in query) else ''
                    results = wf.filter(param, input_schemes.values(), min_score=80)
                    if results:
                        for line in results:
                            wf.add_item(line,
                                        line,
                                        arg='--scheme '+line,
                                        autocomplete=line,
                                        icon=ICON_COLOR,
                                        valid=True)
    return query

def search_key_for_language(language):
    """Generate a string search key for a domain"""
    elements = []
    elements.append(language['eng'])  
    elements.append(language['lng'])  
    elements.append(language['code'])  
    return u' '.join(elements)

def is_chinese(lang):
    return lang.startswith('zh') or lang.startswith('yue')

def main(wf):
    # build argument parser to parse script args and collect their
    # values
    parser = argparse.ArgumentParser()
    # add an optional query and save it to 'query'
    parser.add_argument('query', nargs='?', default=None)
    # parse the script's arguments
    args = parser.parse_args(wf.args)
    log.debug("args are "+str(args))

    # update query post extraction
    query = args.query if args.query else ''
    words = query.split(' ') if query else []

    # list of commands
    config_commands = {
        'lang': {
            'title': 'Set language',
            'subtitle': 'Set the target language',
            'autocomplete': 'lang',
            'args': ' --lang '+(words[1] if len(words)>1 else ''),
            'icon': ICON_WEB,
            'valid': len(words) > 1
        },
        'scheme': {
            'title': 'Set input scheme',
            'subtitle': 'Set the input scheme',
            'autocomplete': 'scheme',
            'args': ' --scheme '+(words[1] if len(words)>1 else ''),
            'icon': ICON_WEB,
            'valid': len(words) > 1
        },
        'reinit': {
            'title': 'Reinitialize the workflow',
            'subtitle': 'CAUTION: this deletes all devices, clients and credentials...',
            'autocomplete': 'reinit',
            'args': ' --reinit',
            'icon': ICON_BURN,
            'valid': True
        },
        'workflow:update': {
            'title': 'Update the workflow',
            'subtitle': 'Updates workflow to latest github version',
            'autocomplete': 'workflow:update',
            'args': '',
            'icon': ICON_SYNC,
            'valid': True
        }
    }
    
    # add config commands to filter
    query = add_config_commands(wf, query, config_commands)
    if(add_prereq(wf, args)):
        wf.send_feedback()
        return 0
 
    if query:
        lang = wf.settings.get('transliterate_lang')
        scheme = wf.settings.get('transliterate_scheme') if is_chinese(lang) else None
        # retrieve cached clients and devices
        # Single client only, no command or not complete command yet so populate with all the commands
        name = transliterate_text(query, lang_code=lang, input_scheme=scheme) if is_chinese(lang) else transliterate_text(query, lang_code=lang)
        wf.add_item(title=name,
                subtitle=languages[lang]['eng'],
                arg=' --copy '+name,
                autocomplete=name,
                valid=True,
                icon=ICON_NOTE)
        # Send the results to Alfred as XML
    wf.send_feedback()
    return 0


if __name__ == u"__main__":
    wf = Workflow(update_settings={
        'github_slug': 'schwark/alfred-transliterate'
    },libraries=['./lib'])
    log = wf.logger
    sys.exit(wf.run(main))
    