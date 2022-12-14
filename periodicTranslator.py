def errorMessage(unableSymbol):
    print("Sorry! Unfortunately your text cannot be translated.")
    print(f"There's no element for {unableSymbol}")
    quit()

# dictionary of every element and symbol
translations = {
    "Actinium": 'Ac',
    "Aluminum": 'Al',
    "Americium": 'Am',
    "Antimony": 'Sb',
    "Argon": 'Ar',
    "Arsenic": 'As',
    "Astatine": 'At',
    "Barium": 'Ba',
    "Berkelium": 'Bk',
    "Beryllium": 'Be',
    "Bismuth": 'Bi',
    "Bohrium": 'Bh',
    "Boron": 'B',
    "Bromine": 'Br',
    "Cadmium": 'Cd',
    "Calcium": 'Ca',
    "Californium": 'Cf',
    "Carbon": 'C',
    "Cerium": 'Ce',
    "Cesium": 'Cs',
    "Chlorine": 'Cl',
    "Chromium": 'Cr',
    "Cobalt": 'Co',
    "Copper": 'Cu',
    "Curium": 'Cm',
    "Darmstadtium": 'Ds',
    "Dubnium": 'Db',
    "Dysprosium": 'Dy',
    "Einsteinium": 'Es',
    "Erbium": 'Er',
    "Europium": 'Eu',
    "Fermium": 'Fm',
    "Fluorine": 'F',
    "Francium": 'Fr',
    "Gadolinium": 'Gd',
    "Gallium": 'Ga',
    "Germanium": 'Ge',
    "Gold":	'Au',
    "Hafnium": 'Hf',
    "Hassium": 'Hs',
    "Helium": 'He',
    "Holmium": 'Ho',
    "Hydrogen": 'H',
    "Indium": 'In',
    "Iodine": 'I',
    "Iridium": 'Ir',
    "Iron": 'Fe',
    "Krypton": 'Kr',
    "Lanthanum": 'La',
    "Lawrencium": 'Lr',
    "Lead": 'Pb',
    "Lithium": 'Li',
    "Lutetium": 'Lu',
    "Magnesium": 'Mg',
    "Manganese": 'Mn',
    "Meitnerium": 'Mt',
    "Mendelevium": 'Md',
    "Mercury": 'Hg',
    "Molybdenum": 'Mo',
    "Neodymium": 'Nd',
    "Neon": 'Ne',
    "Neptunium": 'Np',
    "Nickel": 'Ni',
    "Niobium": 'Nb',
    "Nitrogen": 'N',
    "Nobelium": 'No',
    "Oganesson": 'Uuo',
    "Osmium": 'Os',
    "Oxygen": 'O',
    "Palladium": 'Pd',
    "Phosphorus": 'P',
    "Platinum": 'Pt',
    "Plutonium": 'Pu',
    "Polonium": 'Po',
    "Potassium": 'K',
    "Praseodymium": 'Pr',
    "Promethium": 'Pm',
    "Protactinium": 'Pa',
    "Radium": 'Ra',
    "Radon": 'Rn',
    "Rhenium": 'Re',
    "Rhodium": 'Rh',
    "Roentgenium": 'Rg',
    "Rubidium": 'Rb',
    "Ruthenium": 'Ru',
    "Rutherfordium": 'Rf',
    "Samarium": 'Sm',
    "Scandium": 'Sc',
    "Seaborgium": 'Sg',
    "Selenium": 'Se',
    "Silicon": 'Si',
    "Silver": 'Ag',
    "Sodium": 'Na',
    "Strontium": 'Sr',
    "Sulfur": 'S',
    "Tantalum": 'Ta',
    "Technetium": 'Tc',
    "Tellurium": 'Te',
    "Terbium": 'Tb',
    "Thallium": 'Tl',
    "Thorium": 'Th',
    "Thulium": 'Tm',
    "Tin": 'Sn',
    "Titanium": 'Ti',
    "Tungsten": 'W',
    "Ununbium": 'Uub',
    "Ununhexium": 'Uuh',
    "Ununpentium": 'Uup',
    "Ununquadium": 'Uuq',
    "Ununseptium": 'Uus',
    "Ununtrium": 'Uut',
    "Uranium": 'U',
    "Vanadium": 'V',
    "Xenon": 'Xe',
    "Ytterbium": 'Yb',
    "Yttrium": 'Y',
    "Zinc": 'Zn',
    "Zirconium": 'Zr'
}
elements = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 'Californium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copper', 'Curium', 'Darmstadtium', 'Dubnium', 'Dysprosium', 'Einsteinium', 'Erbium', 'Europium', 'Fermium', 'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Hassium', 'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iridium', 'Iron', 'Krypton', 'Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 'Lutetium', 'Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury', 'Molybdenum', 'Neodymium', 'Neon', 'Neptunium', 'Nickel', 'Niobium', 'Nitrogen', 'Nobelium', 'Oganesson', 'Osmium', 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Plutonium', 'Polonium', 'Potassium', 'Praseodymium', 'Promethium', 'Protactinium', 'Radium', 'Radon', 'Rhenium', 'Rhodium', 'Roentgenium', 'Rubidium', 'Ruthenium', 'Rutherfordium', 'Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 'Silver', 'Sodium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 'Ununbium', 'Ununhexium', 'Ununpentium', 'Ununquadium', 'Ununseptium', 'Ununtrium', 'Uranium', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']
symbols = ['Ac', 'Al', 'Am', 'Sb', 'Ar', 'As', 'At', 'Ba', 'Bk', 'Be', 'Bi', 'Bh', 'B', 'Br', 'Cd', 'Ca', 'Cf', 'C', 'Ce', 'Cs', 'Cl', 'Cr', 'Co', 'Cu', 'Cm', 'Ds', 'Db', 'Dy', 'Es', 'Er', 'Eu', 'Fm', 'F', 'Fr', 'Gd', 'Ga', 'Ge', 'Au', 'Hf', 'Hs', 'He', 'Ho', 'H', 'In', 'I', 'Ir', 'Fe', 'Kr', 'La', 'Lr', 'Pb', 'Li', 'Lu', 'Mg', 'Mn', 'Mt', 'Md', 'Hg', 'Mo', 'Nd', 'Ne', 'Np', 'Ni', 'Nb', 'N', 'No', 'Uuo', 'Os', 'O', 'Pd', 'P', 'Pt', 'Pu', 'Po', 'K', 'Pr', 'Pm', 'Pa', 'Ra', 'Rn', 'Re', 'Rh', 'Rg', 'Rb', 'Ru', 'Rf', 'Sm', 'Sc', 'Sg', 'Se', 'Si', 'Ag', 'Na', 'Sr', 'S', 'Ta', 'Tc', 'Te', 'Tb', 'Tl', 'Th', 'Tm', 'Sn', 'Ti', 'W', 'Uub', 'Uuh', 'Uup', 'Uuq', 'Uus', 'Uut', 'U', 'V', 'Xe', 'Yb', 'Y', 'Zn', 'Zr']
finalElements = []

userText = list(input("Input the text you would like to translate\n>"))

workingString = ""
for i in userText:
    # skip spaces
    if i == " ":
        continue

    # if last iteration we added to finalElements
    if len(workingString) == 0:
        workingString = i.upper()
        if workingString in symbols:
            finalElements.append(elements[symbols.index(workingString)])
            workingString = ""
        continue
    
    # if last iteration we didn't match to a single length symbol
    if len(workingString) == 1:
        workingString += i.lower()
        if workingString in symbols:
            finalElements.append(elements[symbols.index(workingString)])
            workingString = ""
        else:
            errorMessage(workingString)
        continue


abrieviations = []
for element in finalElements:
    abrieviations.append(symbols[elements.index(element)])

print(f"Your text can be translated to: {' '.join(abrieviations)}")
print(f"Which is {' '.join(finalElements)}")