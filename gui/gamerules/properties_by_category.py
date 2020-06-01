# Utility Script - SGF Format Meta-info in a dictionary format
META_PROPS = ['AN',
 'AP',
 'CA',
 'CP',
 'DT',
 'EV',
 'FF',
 'GC',
 'GM',
 'GN',
 'JD',
 'PC',
 'RO',
 'SO',
 'US']
GAME_PROPS = ['HA', 'KM', 'LC', 'LT', 'OT', 'RU', 'SZ']
PLAYER_PROPS = ['BC', 'BR', 'BT', 'PB', 'PW', 'WC', 'WR', 'WT']
REVIEW_PROPS = ['CR', 'MA', 'N', 'SL', 'SQ', 'TR']
OTHER_PROPS = ['AB',
 'AE',
 'AW',
 'B',
 'BL',
 'C',
 'LB',
 'MN',
 'OB',
 'OH',
 'OW',
 'PL',
 'RE',
 'TB',
 'TM',
 'TW',
 'VW',
 'W',
 'WL']

def main():
    from sgf_properties import PROPS

    def print_it(prop):
        print('\t-', end='')
        print(PROPS[prop]['prop'], PROPS[prop]['desc'])


    print('META:')
    for prop in META_PROPS:
        print_it(prop)

    print('GAME:')
    for prop in GAME_PROPS:
        print_it(prop)

    print('PLAYER:')
    for prop in PLAYER_PROPS:
        print_it(prop)

    print('REVIEW:')
    for prop in REVIEW_PROPS:
        print_it(prop)

    print('OTHER:')
    for prop in OTHER_PROPS:
        print_it(prop)

if __name__ == '__main__':
    main()