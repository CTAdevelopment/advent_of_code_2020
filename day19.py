import pandas as pd
regels_data = open('day19cond.txt').read().splitlines()
zinnen_data = open('day19zinnen.txt').read().splitlines()
regels_data = {str(i).split(':')[0] : [str(i).split(':')[0].strip(), str(i).split(':')[1].strip()] for i in regels_data }

frame = pd.DataFrame.from_dict(regels_data, orient='index', columns=['nummers', 'regels'])
frame.nummers = frame.nummers.astype('int32')
frame.sort_values(by=['nummers'], inplace=True)


for zin in zinnen_data:

    def regel_na_regel():

    return mogelijke_letters

    current_condition = 0
    error_not_found = True
    counter = 0
    letters = zin[current_condition]

    while error_not_found and counter != len(zin):
        huidige_regel = frame.at[current_condition, 'regels']

        if huidige_regel != 'a' and huidige_regel != 'b':
            mogelijkheden = regel_na_regel(huidige_regel)
            if huidige_regel in mogelijkheden:
                counter += 1


        else:
            if letters == huidige_regel:
                print('condition met, ')
                print('next condition loop here .. right?')
