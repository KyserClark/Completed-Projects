glossary = {
    'list': 'mutable ordered objects grouped together inside brackets',
    'tuple': 'immutable ordered objects grouped together inside parenthesis',
    'boolean': 'can be labeled as True or False',
    'dictionary': 'unordered key value pairs inside curly braces',
    'string': 'variable defined by programmer in-between quotation marks',
    'set': 'unordered and unique objects grouped together inside curly braces',
    'variable': 'object that is defined by programmer',
    'if statement': 'checks to see if something is true or false, \n'
                    '\tthen performs an action based on the result',

    'while loop': 'while something is true, perform an action \n' 
                  '\tuntil it is not true',

    'comment': 'code not read by computers, intended for humans to read in \n'
               '\torder to understand the code around it'
    }

for key, value in glossary.items():
    print(f"{key} - {value}\n")

