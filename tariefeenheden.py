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

        # if frm == "Utrecht Centraal":
        #     if to == "Utrecht Centraal":
        #         return 0
        #     elif to == "Gouda":
        #         return 32
        #     elif to == "Geldermalsen":
        #         return 26
        #     elif to == "Hilversum":
        #         return 18
        #     elif to == "Duivendrecht":
        #         return 31
        #     elif to == "Weesp":
        #         return 33
        #     else:
        #         raise Exception("Unknown stations")

        # elif frm == "Gouda":
        #     if to == "Gouda":
        #         return 0
        #     elif to == "Geldermalsen":
        #         return 58
        #     elif to == "Hilversum":
        #         return 50
        #     elif to == "Duivendrecht":
        #         return 54
        #     elif to == "Weesp":
        #         return 57
        #     else:
        #         return Tariefeenheden.get_tariefeenheden(to, frm)

        # elif frm == "Geldermalsen":
        #     if to == "Geldermalsen":
        #         return 0
        #     elif to == "Hilversum":
        #         return 44
        #     elif to == "Duivendrecht":
        #         return 57
        #     elif to == "Weesp":
        #         return 59
        #     else:
        #         return Tariefeenheden.get_tariefeenheden(to, frm)

        # elif frm == "Hilversum":
        #     if to == "Hilversum":
        #         return 0
        #     elif to == "Duivendrecht":
        #         return 18
        #     elif to == "Weesp":
        #         return 15
        #     else:
        #         return Tariefeenheden.get_tariefeenheden(to, frm)

        # elif frm == "Duivendrecht":
        #     if to == "Duivendrecht":
        #         return 0
        #     elif to == "Weesp":
        #         return 3
        #     else:
        #         return Tariefeenheden.get_tariefeenheden(to, frm)

        # elif frm == "Weesp":
        #     if to == "Weesp":
        #         return 0
        #     else:
        #         return Tariefeenheden.get_tariefeenheden(to, frm)
        
        # else:
        #     raise Exception("Unknown stations")