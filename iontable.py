from enum import Enum
from elements import PeriodicTable
from ions import Ion

class AnionTable(Enum):
    HYDROXIDE = Ion([{"element": PeriodicTable.HYDROGEN, "quantity": 1},
                     {"element": PeriodicTable.OXYGEN, "quantity": 1}], 'hidróxido', 1)
    OXIDE = Ion([{"element": PeriodicTable.OXYGEN, "quantity": 1}], 'óxido', 2)
    HYDRITE = Ion([{"element": PeriodicTable.HYDROGEN, "quantity": 1}], 'hidreto', 1)

    FLUORIDE = Ion([{"element": PeriodicTable.FLUORINE, "quantity": 1}], 'fluoreto', 1)
    CHLORIDE = Ion([{"element": PeriodicTable.CHLORINE, "quantity": 1}], 'cloreto', 1)
    BROMIDE = Ion([{"element": PeriodicTable.BROMINE, "quantity": 1}], 'brometo', 1)
    IODITE = Ion([{"element": PeriodicTable.IODINE, "quantity": 1}], 'iodeto', 1)
    HYPOCHLORITE = Ion([{"element": PeriodicTable.CHLORINE, "quantity": 1},
                        {"element": PeriodicTable.OXYGEN, "quantity": 1}], 'hipoclorito', 1)
    CHLORITE = Ion([{"element": PeriodicTable.CHLORINE, "quantity": 1},
                    {"element": PeriodicTable.OXYGEN, "quantity": 2}], 'clorito', 1)
    CHLORATE = Ion([{"element": PeriodicTable.CHLORINE, "quantity": 1},
                    {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'clorato', 1)
    PERCHLORATE = Ion([{"element": PeriodicTable.CHLORINE, "quantity": 1},
                       {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'perclorato', 1)
    HYPOBROMITE = Ion([{"element": PeriodicTable.BROMINE, "quantity": 1},
                       {"element": PeriodicTable.OXYGEN, "quantity": 1}], 'hipobromito', 1)
    BROMITE = Ion([{"element": PeriodicTable.BROMINE, "quantity": 1},
                   {"element": PeriodicTable.OXYGEN, "quantity": 2}], 'bromito', 1)
    BROMATE = Ion([{"element": PeriodicTable.BROMINE, "quantity": 1},
                   {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'bromato', 1)
    HYPOIODITE = Ion([{"element": PeriodicTable.IODINE, "quantity": 1}, {"element": PeriodicTable.OXYGEN, "quantity": 1}], 'hipoiodito', 1)
    IODATE = Ion([{"element": PeriodicTable.IODINE, "quantity": 1},
                  {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'iodato', 1)
    PERIODATE = Ion([{"element": PeriodicTable.IODINE, "quantity": 1},
                     {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'periodato', 1)
    CYANIDE = Ion([{"element": PeriodicTable.CARBON, "quantity": 1},
                   {"element": PeriodicTable.NITROGEN, "quantity": 1}], 'cianeto', 1)
    CYANATE = Ion([{"element": PeriodicTable.CARBON, "quantity": 1},
                   {"element": PeriodicTable.NITROGEN, "quantity": 1},
                   {"element": PeriodicTable.OXYGEN, "quantity": 1}], 'cianato', 1)
    THIOCYANATE = Ion([{"element": PeriodicTable.CARBON, "quantity": 1},
                       {"element": PeriodicTable.NITROGEN, "quantity": 1},
                       {"element": PeriodicTable.SULFUR, "quantity": 1}], 'tiocianato', 1)
    ACETATE = Ion([{"element": PeriodicTable.CARBON, "quantity": 2},
                   {"element": PeriodicTable.HYDROGEN, "quantity": 4},
                   {"element": PeriodicTable.OXYGEN, "quantity": 2}], 'acetato', 1)
    CARBONATE = Ion([{"element": PeriodicTable.CARBON, "quantity": 1},
                     {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'carbonato', 2)

    NITRITE = Ion([{"element": PeriodicTable.NITROGEN, "quantity": 1},
                   {"element": PeriodicTable.OXYGEN, "quantity": 2}], 'nitrito', 1)
    NITRATE = Ion([{"element": PeriodicTable.NITROGEN, "quantity": 1},
                   {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'nitrato', 1)
    NITRIDE = Ion([{"element": PeriodicTable.NITROGEN, "quantity": 3}], 'nitreto', 1)
    
    METHAPHOSPHATE = Ion([{"element": PeriodicTable.PHOSPHORUS, "quantity": 1},
                          {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'metafosfato', 1)
    HYPOPHOSPHITE = Ion([{"element": PeriodicTable.HYDROGEN, "quantity": 1},
                         {"element": PeriodicTable.PHOSPHORUS, "quantity": 1},
                         {"element": PeriodicTable.OXYGEN, "quantity": 2}], 'hipofosfito', 1)

    PHOSPHIDE = Ion([{"element": PeriodicTable.PHOSPHORUS, "quantity": 3}], 'fosfeto', 3)
    PHOSPHITE = Ion([{"element": PeriodicTable.HYDROGEN, "quantity": 1},
                     {"element": PeriodicTable.PHOSPHORUS, "quantity": 1},
                     {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'fosfito', 2)
    PHOSPHATE = Ion([{"element": PeriodicTable.PHOSPHORUS, "quantity": 1},
                     {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'fosfato', 3)
    PYROPHOSPHATE = Ion([{"element": PeriodicTable.PHOSPHORUS, "quantity": 2},
                         {"element": PeriodicTable.OXYGEN, "quantity": 7}], 'pirofosfato', 4)

    SULPHIDE = Ion([{"element": PeriodicTable.SULFUR, "quantity": 1}], 'sulfeto', 2)
    SULPHITE = Ion([{"element": PeriodicTable.SULFUR, "quantity": 1},
                    {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'sulfito', 2)
    SULPHATE = Ion([{"element": PeriodicTable.SULFUR, "quantity": 1},
                    {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'sulfato', 2)
    THIOSULPHATE = Ion([{"element": PeriodicTable.SULFUR, "quantity": 2},
                        {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'tiossulfato', 2)
    HYPOSULPHITE = Ion([{"element": PeriodicTable.SULFUR, "quantity": 2},
                        {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'hipossulfito', 2)
    PERSULPHATE = Ion([{"element": PeriodicTable.SULFUR, "quantity": 2},
                       {"element": PeriodicTable.OXYGEN, "quantity": 8}], 'persulfato', 2)
    TETRATHIONATE = Ion([{"element": PeriodicTable.SULFUR, "quantity": 4},
                         {"element": PeriodicTable.OXYGEN, "quantity": 6}], 'tetrationato', 2)

    PERMANGANATE = Ion([{"element": PeriodicTable.MANGANESE, "quantity": 1},
                        {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'permanganato', 1)
    MANGANTATE = Ion([{"element": PeriodicTable.MANGANESE, "quantity": 1},
                      {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'manganato', 2)
    MANGANITE = Ion([{"element": PeriodicTable.MANGANESE, "quantity": 1},
                     {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'manganito', 2)
    CHROMATE = Ion([{"element": PeriodicTable.CHROMIUM, "quantity": 1},
                    {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'cromato', 2)
    DICHROMATE = Ion([{"element": PeriodicTable.CHROMIUM, "quantity": 2},
                      {"element": PeriodicTable.OXYGEN, "quantity": 7}], 'dicromato', 2)

    ARSENIDE = Ion([{"element": PeriodicTable.ARSENIC, "quantity": 1}], 'arseneto', 3)
    ARSENITE = Ion([{"element": PeriodicTable.ARSENIC, "quantity": 1},
                    {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'arsenito', 3)
    ARSENATE = Ion([{"element": PeriodicTable.ARSENIC, "quantity": 1},
                    {"element": PeriodicTable.OXYGEN, "quantity": 4}], 'arsenato', 3)
    
    BORATE = Ion([{"element": PeriodicTable.BORON, "quantity": 1},
                  {"element": PeriodicTable.OXYGEN, "quantity": 3}], 'borato', 3)


class CationTable(Enum):
    LITHIUM = Ion([{"element": PeriodicTable.LITHIUM, "quantity": 1}], PeriodicTable.LITHIUM.get_name(), 1)
    SODIUM = Ion([{"element": PeriodicTable.SODIUM, "quantity": 1}], PeriodicTable.SODIUM.get_name(), 1)
    POTASSIUM = Ion([{"element": PeriodicTable.POTASSIUM, "quantity": 1}], PeriodicTable.POTASSIUM.get_name(), 1)
    RUBIDIUM = Ion([{"element": PeriodicTable.RUBIDIUM, "quantity": 1}], PeriodicTable.RUBIDIUM.get_name(), 1)
    CESIUM = Ion([{"element": PeriodicTable.CESIUM, "quantity": 1}], PeriodicTable.CESIUM.get_name(), 1)
    COPPER1 = Ion([{"element": PeriodicTable.COPPER, "quantity": 1}], PeriodicTable.COPPER.get_name() + ' I', 1)
    
    SILVER = Ion([{"element": PeriodicTable.SILVER, "quantity": 1}], PeriodicTable.SILVER.get_name(), 1)
    GOLD1 = Ion([{"element": PeriodicTable.GOLD, "quantity": 1}], PeriodicTable.GOLD.get_name() + ' I', 1)
    AMMONIUM = Ion([{"element": PeriodicTable.NITROGEN, "quantity": 1},
                    {"element": PeriodicTable.HYDROGEN, "quantity": 4}], 'amônio', 1)

    BERILLIUM = Ion([{"element": PeriodicTable.BERILLIUM, "quantity": 1}], PeriodicTable.BERILLIUM.get_name(), 2)
    MAGNESIUM = Ion([{"element": PeriodicTable.MAGNESIUM, "quantity": 1}], PeriodicTable.MAGNESIUM.get_name(), 2)
    CALCIUM = Ion([{"element": PeriodicTable.CALCIUM, "quantity": 1}], PeriodicTable.CALCIUM.get_name(), 2)
    STRONTIUM = Ion([{"element": PeriodicTable.STRONTIUM, "quantity": 1}], PeriodicTable.STRONTIUM.get_name(), 2)
    BARIUM = Ion([{"element": PeriodicTable.BARIUM, "quantity": 1}], PeriodicTable.BARIUM.get_name(), 2)
    RADIUM = Ion([{"element": PeriodicTable.RADIUM, "quantity": 1}], PeriodicTable.RADIUM.get_name(), 2)
    ZINC = Ion([{"element": PeriodicTable.ZINC, "quantity": 1}], PeriodicTable.ZINC.get_name(), 2)
    CADMIUM = Ion([{"element": PeriodicTable.CADMIUM, "quantity": 1}], PeriodicTable.CADMIUM.get_name(), 2)
    QUICKSILVER2 = Ion([{"element": PeriodicTable.QUICKSILVER, "quantity": 2}], PeriodicTable.QUICKSILVER.get_name(), 2)
    COPPER2 = Ion([{"element": PeriodicTable.COPPER, "quantity": 1}], PeriodicTable.COPPER.get_name() + ' II', 2)
    IRON2 = Ion([{"element": PeriodicTable.IRON, "quantity": 1}], PeriodicTable.IRON.get_name() + ' II', 2)
    COBALT2 = Ion([{"element": PeriodicTable.COBALT, "quantity": 1}], PeriodicTable.COBALT.get_name() + ' II', 2)
    NICKEL2 = Ion([{"element": PeriodicTable.NICKEL, "quantity": 1}], PeriodicTable.NICKEL.get_name() + ' II', 2)
    CHROMIUM2 = Ion([{"element": PeriodicTable.CHROMIUM, "quantity": 1}], PeriodicTable.CHROMIUM.get_name() + ' II', 2)
    MANGANESE2 = Ion([{"element": PeriodicTable.MANGANESE, "quantity": 1}], PeriodicTable.MANGANESE.get_name() + ' II', 2)
    TIN2 = Ion([{"element": PeriodicTable.TIN, "quantity": 1}], PeriodicTable.TIN.get_name() + ' II', 2)
    LEAD2 = Ion([{"element": PeriodicTable.LEAD, "quantity": 1}], PeriodicTable.LEAD.get_name() + ' II', 2)
    TITANIUM2 = Ion([{"element": PeriodicTable.TITANIUM, "quantity": 1}], PeriodicTable.TITANIUM.get_name() + ' II', 2)
    PLATINUM2 = Ion([{"element": PeriodicTable.PLATINUM, "quantity": 1}], PeriodicTable.PLATINUM.get_name() + ' II', 2)
    
    ALUMINIUM = Ion([{"element": PeriodicTable.ALUMINIUM, "quantity": 1}], PeriodicTable.ALUMINIUM.get_name(), 3)
    BISMUTH = Ion([{"element": PeriodicTable.BISMUTH, "quantity": 1}], PeriodicTable.BISMUTH.get_name(), 3)
    GOLD3 = Ion([{"element": PeriodicTable.GOLD, "quantity": 1}], PeriodicTable.GOLD.get_name() + ' III', 3)
    IRON3 = Ion([{"element": PeriodicTable.IRON, "quantity": 1}], PeriodicTable.IRON.get_name() + ' III', 3)
    COBALT3 = Ion([{"element": PeriodicTable.COBALT, "quantity": 1}], PeriodicTable.COBALT.get_name() + ' III', 3)
    NICKEL3 = Ion([{"element": PeriodicTable.NICKEL, "quantity": 1}], PeriodicTable.NICKEL.get_name() + ' III', 3)
    CHROMIUM3 = Ion([{"element": PeriodicTable.CHROMIUM, "quantity": 1}], PeriodicTable.CHROMIUM.get_name() + ' III', 3)
    
    TIN4 = Ion([{"element": PeriodicTable.TIN, "quantity": 1}], PeriodicTable.TIN.get_name() + ' IV', 4)
    TITANIUM4 = Ion([{"element": PeriodicTable.TITANIUM, "quantity": 1}], PeriodicTable.TITANIUM.get_name() + ' IV', 4)
    LEAD4 = Ion([{"element": PeriodicTable.LEAD, "quantity": 1}], PeriodicTable.LEAD.get_name() + ' IV', 4)
    PLATINUM4 = Ion([{"element": PeriodicTable.PLATINUM, "quantity": 1}], PeriodicTable.PLATINUM.get_name() + ' IV', 4)
    MANGANESE4 = Ion([{"element": PeriodicTable.MANGANESE, "quantity": 1}], PeriodicTable.MANGANESE.get_name() + ' IV', 4)
