from datetime import datetime
def main():
    props, descs = get_props_from_textfile()
    # save_to_file(props, descs)
    get_and_save_meta_props(props)

def get_props_from_textfile():
    from data_types import DATA_TYPES

    # Variable use to separate values in a row
    sep = '$#$'

    # Open Raw Info
    with open('key_list.txt') as f:
        raw = f.read()

    # Clean the raw text and
    by_line = raw.split('\n')
    corrected_tabs = [line.replace('\t', sep) for line in by_line]

    props = {}
    descriptions = {}
    for line in corrected_tabs:
        entry = {}
        prop, desc, type_, full_desc = line.split(sep)
        entry['prop'] = prop
        entry['desc'] = desc
        entry['data_type'] = DATA_TYPES[type_]
        entry['full_desc'] = full_desc
        props[prop] = entry
        descriptions[desc] = prop

    return props, descriptions

def save_to_file(props, descs, meta):
    from pprint import pformat
    with open('sgf_properties.py', 'w') as f:
        f.write('# Utility Script - SGF Format Properties in a dictionary format\n')
        f.write('from datatime import datetime\n')
        f.write(f'PROPS = {pformat(props)}')
        f.write(f'\n\nDESCRIPTIONS = {pformat(descs)}')


def get_and_save_meta_props(props):
    from pprint import pformat
    meta = []
    game = []
    player_info = []
    review = []
    other = []

    for prop, data in props.items():
        print('*' * 30)
        print(f"[{prop}]{data['desc']}: {data['full_desc']}")
        print('meta - game - player - review')
        user_in = input('>>> ')
        if user_in == 'm':
            meta.append(prop)
        elif user_in == 'g':
            game.append(prop)
        elif user_in == 'r':
            review.append(prop)
        elif user_in == 'p':
            player_info.append(prop)
        else:
            other.append(prop)

    with open('properties_by_category.py', 'w') as f:
        f.write('# Utility Script - SGF Format Meta-info in a dictionary format\n')
        f.write(f'META_PROPS = {pformat(meta)}')
        f.write(f'\nGAME_PROPS = {pformat(game)}')
        f.write(f'\nPLAYER_PROPS = {pformat(player_info)}')
        f.write(f'\nREVIEW_PROPS = {pformat(review)}')
        f.write(f'\nOTHER_PROPS = {pformat(other)}')

# Do not use!
def save_data_types():
    # Variable use to separate values in a row
    sep = '$#$'

    # Open Raw Info
    with open('key_list.txt') as f:
        raw = f.read()

    # Clean the raw text and
    by_line = raw.split('\n')
    corrected_tabs = [line.replace('\t', sep) for line in by_line]

    data_types = set()
    for line in corrected_tabs:
        line = line.split(sep)
        data_types.add(line[2])

    data_types = [f'\t"{type_}": '  for type_ in data_types]

    with open('___data_types.py', 'w') as f:
        f.write('# SGF File data types\n')
        f.write('DATA_TYPES = {\n')
        f.write(',\n'.join(data_types))
        f.write('}')


if __name__ == '__main__':
    main()