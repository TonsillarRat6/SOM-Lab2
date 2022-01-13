from typing import List

class Tariefeenheden:

    @staticmethod
    def get_stations() -> List[str]:
        return ["Utrecht Centraal",
                "Gouda",
                "Geldermalsen",
                "Hilversum",
                "Duivendrecht",
                "Weesp"]


#Nested dictionaries, waar de main dictionary [stad] : [dict van de stad met tariefeenheden] 
#Dus: {
#       Utrecht : {Gouda : 32, Geldermalsen : 26}, 
#       Gouda : {Geldermalsen : 58, Hilversum : 50}
#       }
    @staticmethod
    def get_tariefeenheden(frm: str, to: str) -> int:
        TariefeenhedenDict =  { "Utrecht Centraal" : { "Gouda" : 32, "Geldermalsen" : 26, "Hilversum" : 18, "Duivendrecht" : 31, "Weesp" : 33 },
                    "Gouda" : 
                    {"Geldermalsen" : 58, "Hilversum" : 50, "Duivendrecht" : 54, "Weesp" : 57},
                    "Geldermalsen" :
                    {"Hilversum" : 44, "Duivendrecht" : 57, "Weesp" : 59},
                    "Hilversum" : 
                    {"Duivendrecht" : 18, "Weesp" : 15},
                    "Duivendrecht" : 
                    {"Weesp" : 3},
                    "Weesp" : 
                    {}
                }

        if frm == to:
            return 0
        for key, value in TariefeenhedenDict.items():
            if key == frm:
                if to in value.keys():
                    return TariefeenhedenDict.get(frm).get(to)
                else:
                    return Tariefeenheden.get_tariefeenheden(to, frm)