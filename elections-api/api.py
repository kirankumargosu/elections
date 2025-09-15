from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
app = FastAPI()
origins = [
    os.environ.get("FRONTEND_URL", "http://localhost:3000"),
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:5173/",
    "http://192.168.1.181:3000",
    "192.168.1.181:3000",
    "192.168.0.252:3000",
    "http://86.1.96.160:3000",
    "*"
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

tn_alliances = [
    {'alliance_id': -1, 'alliance_name': 'Unknown', 'colorcode': "#D8DAD8"},
    {'alliance_id': 1, 'alliance_name': 'DMK+', 'colorcode': '#FF0000'},
    {'alliance_id': 2, 'alliance_name': 'NDA', 'colorcode': '#F97D09'},
    {'alliance_id': 3, 'alliance_name': 'TVK', 'colorcode': '#FFFF00'},
    {'alliance_id': 4, 'alliance_name': 'NTK', 'colorcode': "#621515"},
    {'alliance_id': 5, 'alliance_name': 'Others', 'colorcode': "#493D1C"},
]

tn_districts = [
    {'district_id' : 1, 'district_name' : 'Thiruvallur'},
    {'district_id' : 2, 'district_name' : 'Chennai'},
    {'district_id' : 3, 'district_name' : 'Kancheepuram'},
    {'district_id' : 4, 'district_name' : 'Chengalpattu'},
    {'district_id' : 5, 'district_name' : 'Ranipet'},
    {'district_id' : 6, 'district_name' : 'Vellore'},
    {'district_id' : 7, 'district_name' : 'Tirupathur'},
    {'district_id' : 8, 'district_name' : 'Krishnagiri'},
    {'district_id' : 9, 'district_name' : 'Dharmapuri'},
    {'district_id' : 10 , 'district_name' : 'Tiruvannamalai'},
    {'district_id' : 11 , 'district_name' : 'Villupuram'},
    {'district_id' : 12 , 'district_name' : 'Kallakurichi'},
    {'district_id' : 13 , 'district_name' : 'Salem'},
    {'district_id' : 14 , 'district_name' : 'Namakkal'},
    {'district_id' : 15 , 'district_name' : 'Erode'},
    {'district_id' : 16 , 'district_name' : 'Tiruppur'},
    {'district_id' : 17 , 'district_name' : 'Nilgiris'},
    {'district_id' : 18 , 'district_name' : 'Coimbatore'},
    {'district_id' : 19 , 'district_name' : 'Dindigul'},
    {'district_id' : 20 , 'district_name' : 'Karur'},
    {'district_id' : 21 , 'district_name' : 'Tiruchirappalli'},
    {'district_id' : 22 , 'district_name' : 'Perambalur'},
    {'district_id' : 23 , 'district_name' : 'Ariyalur'},
    {'district_id' : 24 , 'district_name' : 'Cuddalore'},
    {'district_id' : 25 , 'district_name' : 'Mayiladuthurai'},
    {'district_id' : 26 , 'district_name' : 'Nagapattinam'},
    {'district_id' : 27 , 'district_name' : 'Tiruvarur'},
    {'district_id' : 28 , 'district_name' : 'Thanjavur'},
    {'district_id' : 29 , 'district_name' : 'Pudukottai'},
    {'district_id' : 30 , 'district_name' : 'Sivagangai'},
    {'district_id' : 31 , 'district_name' : 'Madurai'},
    {'district_id' : 32 , 'district_name' : 'Theni'},
    {'district_id' : 33 , 'district_name' : 'Virudhunagar'},
    {'district_id' : 34 , 'district_name' : 'Ramanathapuram'},
    {'district_id' : 35 , 'district_name' : 'Thoothukudi'},
    {'district_id' : 36 , 'district_name' : 'Tenkasi'},
    {'district_id' : 37 , 'district_name' : 'Tirunelveli'},
    {'district_id' : 38 , 'district_name' : 'Kanniyakumari'}
]

tn_constituencies = {
                        1: 'Gummidipoondi',
                        2: 'Ponneri(SC)',
                        3: 'Tiruttani',
                        4: 'Thiruvallur',
                        5: 'Poonamallee(SC)',
                        6: 'Avadi',
                        7: 'Maduravoyal',
                        8: 'Ambattur',
                        9: 'Madavaram',
                        10: 'Thiruvottiyur',
                        11: 'Dr. Radhakrishnan Nagar',
                        12: 'Perambur',
                        13: 'Kolathur',
                        14: 'Villivakkam',
                        15: 'Thiru-Vi-Ka-Nagar(SC)',
                        16: 'Egmore(SC)',
                        17: 'Royapuram',
                        18: 'Harbour',
                        19: 'Chepauk-Thiruvallikeni',
                        20: 'Thousand Lights',
                        21: 'Anna Nagar',
                        22: 'Virugampakkam',
                        23: 'Saidapet',
                        24: 'Thiyagaraya Nagar',
                        25: 'Mylapore',
                        26: 'Velachery',
                        27: 'Shozhinganallur',
                        28: 'Alandur',
                        29: 'Sriperumbudur(SC)',
                        30: 'Uthiramerur',
                        31: 'Kancheepuram',
                        32: 'Pallavaram',
                        33: 'Tambaram',
                        34: 'Chengalpattu',
                        35: 'Thiruporur',
                        36: 'Cheyyur(SC)',
                        37: 'Maduranthakam(SC)',
                        38: 'Arakkonam(SC)',
                        39: 'Sholingur',
                        40: 'Ranipet',
                        41: 'Arcot',
                        42: 'Katpadi',
                        43: 'Vellore',
                        44: 'Anaikattu',
                        45: 'Kilvaithinankuppam(SC)',
                        46: 'Gudiyattam(SC)',
                        47: 'Vaniyambadi',
                        48: 'Ambur', 
                        49: 'Jolarpet',
                        50: 'Tirupattur',
                        51: 'Uthangarai(SC)',
                        52: 'Bargur',
                        53: 'Krishnagiri',
                        54: 'Veppanahalli',
                        55: 'Hosur',
                        56: 'Thalli', 
                        57: 'Palacode',
                        58: 'Pennagaram',
                        59: 'Dharmapuri',
                        60: 'Pappireddippatti',
                        61: 'Harur(SC)',
                        62: 'Chengam(SC)',
                        63: 'Tiruvannamalai',
                        64: 'Kilpennathur',
                        65: 'Kalasapakkam',
                        66: 'Polur',
                        67: 'Arani', 
                        68: 'Cheyyar',
                        69: 'Vandavasi(SC)',
                        70: 'Gingee',
                        71: 'Mailam',
                        72: 'Tindivanam',
                        73: 'Vanur(SC)',
                        74: 'Villupuram',
                        75: 'Vikravandi',
                        76: 'Tirukkoyilur',
                        77: 'Ulundurpettai',
                        78: 'Rishivandiyam',
                        79: 'Sankarapuram',
                        80: 'Kallakurichi(SC)',
                        81: 'Gangavalli(SC)',
                        82: 'Attur(SC)',
                        83: 'Yercaud(ST)',
                        84: 'Omalur',
                        85: 'Mettur',
                        86: 'Edappadi',
                        87: 'Sankari',
                        88: 'Salem (West)',
                        89: 'Salem (North)',
                        90: 'Salem (South)',
                        91: 'Veerapandi',
                        92: 'Rasipuram(SC)',
                        93: 'Senthamangalam(ST)',
                        94: 'Namakkal',
                        95: 'Paramathi-Velur',
                        96: 'Tiruchengode',
                        97: 'Kumarapalayam',
                        98: 'Erode (East)',
                        99: 'Erode (West)',
                        100: 'Modakkurichi',
                        101: 'Perundurai',
                        102: 'Bhavani',
                        103: 'Anthiyur',
                        104: 'Gobichettipalayam',
                        105: 'Bhavanisagar(SC)',
                        106: 'Dharapuram(SC)',
                        107: 'Kangayam',
                        108: 'Avanashi(SC)',
                        109: 'Tiruppur (North)',
                        110: 'Tiruppur (South)',
                        111: 'Palladam',
                        112: 'Udumalaipettai',
                        113: 'Madathukulam',
                        114: 'Udhagamandalam',
                        115: 'Gudalur(SC)',
                        116: 'Coonoor',
                        117: 'Mettupalayam',
                        118: 'Sulur',
                        119: 'Kavundampalayam',
                        120: 'Coimbatore (North)',
                        121: 'Thondamuthur',
                        122: 'Coimbatore (South)',
                        123: 'Singanallur',
                        124: 'Kinathukadavu',
                        125: 'Pollachi',
                        126: 'Valparai(SC)',
                        127: 'Palani',
                        128: 'Oddanchatram',
                        129: 'Athoor',
                        130: 'Nilakottai(SC)',
                        131: 'Natham',
                        132: 'Dindigul',
                        133: 'Vedasandur',
                        134: 'Aravakurichi',
                        135: 'Karur',
                        136: 'Krishnarayapuram(SC)',
                        137: 'Kulithalai',
                        138: 'Manapaarai',
                        139: 'Srirangam',
                        140: 'Tiruchirappalli (West)',
                        141: 'Tiruchirappalli (East)',
                        142: 'Thiruverumbur',
                        143: 'Lalgudi',
                        144: 'Manachanallur',
                        145: 'Musiri',
                        146: 'Thuraiyur(SC)',
                        147: 'Perambalur(SC)',
                        148: 'Kunnam',
                        149: 'Ariyalur',
                        150: 'Jayankondam',
                        151: 'Tittakudi(SC)',
                        152: 'Vriddhachalam',
                        153: 'Neyveli',
                        154: 'Panruti',
                        155: 'Cuddalore',
                        156: 'Kurinjipadi',
                        157: 'Bhuvanagiri',
                        158: 'Chidambaram',
                        159: 'Kattumannarkoil(SC)',
                        160: 'Sirkazhi(SC)',
                        161: 'Mayiladuthurai',
                        162: 'Poompuhar',
                        163: 'Nagapattinam',
                        164: 'Kilvelur(SC)',
                        165: 'Vedaranyam',
                        166: 'Thiruthuraipoondi(SC)',
                        167: 'Mannargudi',
                        168: 'Thiruvarur',
                        169: 'Nannilam',
                        170: 'Thiruvidaimarudur(SC)',
                        171: 'Kumbakonam',
                        172: 'Papanasam',
                        173: 'Thiruvaiyaru',
                        174: 'Thanjavur',
                        175: 'Orathanadu',
                        176: 'Pattukkottai',
                        177: 'Peravurani',
                        178: 'Gandharvakottai(SC)',
                        179: 'Viralimalai',
                        180: 'Pudukkottai',
                        181: 'Thirumayam',
                        182: 'Alangudi',
                        183: 'Aranthangi',
                        184: 'Karaikudi',
                        185: 'Tiruppattur',
                        186: 'Sivaganga',
                        187: 'Manamadurai(SC)',
                        188: 'Melur',
                        189: 'Madurai East',
                        190: 'Sholavandan(SC)',
                        191: 'Madurai North',
                        192: 'Madurai South',
                        193: 'Madurai Central',
                        194: 'Madurai West',
                        195: 'Thiruparankundram',
                        196: 'Tirumangalam',
                        197: 'Usilampatti',
                        198: 'Andipatti',
                        199: 'Periyakulam(SC)',
                        200: 'Bodinayakanur',
                        201: 'Cumbum',
                        202: 'Rajapalayam',
                        203: 'Srivilliputhur(SC)',
                        204: 'Sattur',
                        205: 'Sivakasi',
                        206: 'Virudhunagar',
                        207: 'Aruppukkottai',
                        208: 'Tiruchuli',
                        209: 'Paramakudi(SC)',
                        210: 'Tiruvadanai',
                        211: 'Ramanathapuram',
                        212: 'Mudhukulathur',
                        213: 'Vilathikulam',
                        214: 'Thoothukkudi',
                        215: 'Tiruchendur',
                        216: 'Srivaikuntam',
                        217: 'Ottapidaram(SC)',
                        218: 'Kovilpatti',
                        219: 'Sankarankovil(SC)',
                        220: 'Vasudevanallur(SC)',
                        221: 'Kadayanallur',
                        222: 'Tenkasi',
                        223: 'Alangulam',
                        224: 'Tirunelveli',
                        225: 'Ambasamudram',
                        226: 'Palayamkottai',
                        227: 'Nanguneri',
                        228: 'Radhapuram',
                        229: 'Kanniyakumari',
                        230: 'Nagercoil',
                        231: 'Colachel',
                        232: 'Padmanabhapuram',
                        233: 'Vilavancode',
                        234: 'Killiyoor'
                        }

tn_parties = [
    {'party_id': 1, 'party_name': 'DMK', 'colorcode': '#FF0000'},
    {'party_id': 2, 'party_name': 'INC', 'colorcode': "#2D09F9"},
    {'party_id': 3, 'party_name': 'VCK', 'colorcode': "#196ED0"},
    {'party_id': 4, 'party_name': 'AIADMK', 'colorcode': "#199C19"},
    {'party_id': 5, 'party_name': 'CPI', 'colorcode': '#DE0000'},
    {'party_id': 6, 'party_name': 'PMK', 'colorcode': '#FFFF00'},
    {'party_id': 7, 'party_name': 'KMDK', 'colorcode': '#17560A'},
    {'party_id': 8, 'party_name': 'BJP', 'colorcode': '#F97D09'},
    {'party_id': 9, 'party_name': 'MMK', 'colorcode': ''},
    {'party_id': 10, 'party_name': 'CPI(M)', 'colorcode': '#cc0d0d'},
    {'party_id': 11, 'party_name': 'NTK', 'colorcode': '#621515'},
    {'party_id': 12, 'party_name': 'TVK', 'colorcode': '#FFFF00'},
    {'party_id': 13, 'party_name': 'MDMK', 'colorcode': '#FC0000'},
    {'party_id': 14, 'party_name': 'DMDK', 'colorcode': '#FFFF00'},
    {'party_id': 15, 'party_name': 'Others', 'colorcode': '#5B5C5B'},
    {'party_id': 16, 'party_name': 'IUML', 'colorcode': '#006600'},
    {'party_id': 17, 'party_name': 'DMK+ Others', 'colorcode': '#FF0000'},
    {'party_id': 18, 'party_name': 'AIADMKTUMK', 'colorcode': '#199C19'},
    {'party_id': 19, 'party_name': 'AMMK', 'colorcode': '#228B22'},
    {'party_id': 20, 'party_name': 'TMC(M)', 'colorcode': '#FFA500'},
    {'party_id': 21, 'party_name': 'PTMK', 'colorcode': ''},
    {'party_id': 22, 'party_name': 'RPI', 'colorcode': '#0000FF'},
    {'party_id': 23, 'party_name': 'IJK', 'colorcode': '#F08080'},
    {'party_id': 24, 'party_name': 'PT', 'colorcode': '#CF0922'},
    {'party_id': 25, 'party_name': 'TMMK', 'colorcode': '#FF0000'},
    {'party_id': 26, 'party_name': 'PBK', 'colorcode': '#0000FF'},
    {'party_id': 27, 'party_name': 'PNK', 'colorcode': '#FF8C00'},
    {'party_id': 28, 'party_name': 'NDA Others', 'colorcode': '#F97D09'},
    {'party_id': 29, 'party_name': 'MNM', 'colorcode': '#FF0000'}
        
]

tn_alliance_map = {
    1: [1, 2, 13, 3, 16, 5, 10, 29, 7, 9, 17, ], # DMK+
    2: [4, 8, 6, 14, 20, 19, 21, 27, 26, 25, 22, 23, 24, 18, 28,  ], # NDA
    3: [12, ], # TVK+
    4: [11, ], # NTK+
    5: [15, ], # Others
}

tn_static = [
        {'district_id': 1, 'constituency_id': 1, 'constituency_name': 'Gummidipoondi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 1, 'constituency_id': 2, 'constituency_name': 'Ponneri(SC)', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 1, 'constituency_id': 3, 'constituency_name': 'Tiruttani', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 1, 'constituency_id': 4, 'constituency_name': 'Thiruvallur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 1, 'constituency_id': 5, 'constituency_name': 'Poonamallee(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 1, 'constituency_id': 6, 'constituency_name': 'Avadi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 2, 'constituency_id': 7, 'constituency_name': 'Maduravoyal', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 8, 'constituency_name': 'Ambattur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 9, 'constituency_name': 'Madavaram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 10, 'constituency_name': 'Thiruvottiyur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 11, 'constituency_name': 'Dr. Radhakrishnan Nagar', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 12, 'constituency_name': 'Perambur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 13, 'constituency_name': 'Kolathur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 14, 'constituency_name': 'Villivakkam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 15, 'constituency_name': 'Thiru-Vi-Ka-Nagar(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 16, 'constituency_name': 'Egmore(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 17, 'constituency_name': 'Royapuram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 18, 'constituency_name': 'Harbour', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 19, 'constituency_name': 'Chepauk-Thiruvallikeni', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 20, 'constituency_name': 'Thousand Lights', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 21, 'constituency_name': 'Anna Nagar', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 22, 'constituency_name': 'Virugampakkam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 23, 'constituency_name': 'Saidapet', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 24, 'constituency_name': 'Thiyagaraya Nagar', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 25, 'constituency_name': 'Mylapore', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 26, 'constituency_name': 'Velachery', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 27, 'constituency_name': 'Shozhinganallur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 2, 'constituency_id': 28, 'constituency_name': 'Alandur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 3, 'constituency_id': 29, 'constituency_name': 'Sriperumbudur(SC)', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 3, 'constituency_id': 30, 'constituency_name': 'Uthiramerur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 3, 'constituency_id': 31, 'constituency_name': 'Kancheepuram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 4, 'constituency_id': 32, 'constituency_name': 'Pallavaram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 4, 'constituency_id': 33, 'constituency_name': 'Tambaram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 4, 'constituency_id': 34, 'constituency_name': 'Chengalpattu', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 4, 'constituency_id': 35, 'constituency_name': 'Thiruporur', 'winner_party_id_prev': 3, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 4, 'constituency_id': 36, 'constituency_name': 'Cheyyur(SC)', 'winner_party_id_prev': 3, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 4, 'constituency_id': 37, 'constituency_name': 'Maduranthakam(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 5, 'constituency_id': 38, 'constituency_name': 'Arakkonam(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 5, 'constituency_id': 39, 'constituency_name': 'Sholingur', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 5, 'constituency_id': 40, 'constituency_name': 'Ranipet', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 5, 'constituency_id': 41, 'constituency_name': 'Arcot', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 6, 'constituency_id': 42, 'constituency_name': 'Katpadi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 6, 'constituency_id': 43, 'constituency_name': 'Vellore', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 6, 'constituency_id': 44, 'constituency_name': 'Anaikattu', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 6, 'constituency_id': 45, 'constituency_name': 'Kilvaithinankuppam(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 6, 'constituency_id': 46, 'constituency_name': 'Gudiyattam(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 7, 'constituency_id': 47, 'constituency_name': 'Vaniyambadi', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 7, 'constituency_id': 48, 'constituency_name': 'Ambur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 7, 'constituency_id': 49, 'constituency_name': 'Jolarpet', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 7, 'constituency_id': 50, 'constituency_name': 'Tirupattur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 8, 'constituency_id': 51, 'constituency_name': 'Uthangarai(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 8, 'constituency_id': 52, 'constituency_name': 'Bargur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 8, 'constituency_id': 53, 'constituency_name': 'Krishnagiri', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 8, 'constituency_id': 54, 'constituency_name': 'Veppanahalli', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 8, 'constituency_id': 55, 'constituency_name': 'Hosur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 8, 'constituency_id': 56, 'constituency_name': 'Thalli', 'winner_party_id_prev': 5, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 9, 'constituency_id': 57, 'constituency_name': 'Palacode', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 9, 'constituency_id': 58, 'constituency_name': 'Pennagaram', 'winner_party_id_prev': 6, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 9, 'constituency_id': 59, 'constituency_name': 'Dharmapuri', 'winner_party_id_prev': 6, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 9, 'constituency_id': 60, 'constituency_name': 'Pappireddippatti', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 9, 'constituency_id': 61, 'constituency_name': 'Harur(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 10, 'constituency_id': 62, 'constituency_name': 'Chengam(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 10, 'constituency_id': 63, 'constituency_name': 'Tiruvannamalai', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 10, 'constituency_id': 64, 'constituency_name': 'Kilpennathur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 10, 'constituency_id': 65, 'constituency_name': 'Kalasapakkam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 10, 'constituency_id': 66, 'constituency_name': 'Polur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 10, 'constituency_id': 67, 'constituency_name': 'Arani', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 10, 'constituency_id': 68, 'constituency_name': 'Cheyyar', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 10, 'constituency_id': 69, 'constituency_name': 'Vandavasi(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 11, 'constituency_id': 70, 'constituency_name': 'Gingee', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 11, 'constituency_id': 71, 'constituency_name': 'Mailam', 'winner_party_id_prev': 6, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 11, 'constituency_id': 72, 'constituency_name': 'Tindivanam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 11, 'constituency_id': 73, 'constituency_name': 'Vanur(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 11, 'constituency_id': 74, 'constituency_name': 'Villupuram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 11, 'constituency_id': 75, 'constituency_name': 'Vikravandi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 11, 'constituency_id': 76, 'constituency_name': 'Tirukkoyilur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 12, 'constituency_id': 77, 'constituency_name': 'Ulundurpettai', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 12, 'constituency_id': 78, 'constituency_name': 'Rishivandiyam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 12, 'constituency_id': 79, 'constituency_name': 'Sankarapuram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 12, 'constituency_id': 80, 'constituency_name': 'Kallakurichi(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 13, 'constituency_id': 81, 'constituency_name': 'Gangavalli(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 82, 'constituency_name': 'Attur(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 83, 'constituency_name': 'Yercaud(ST)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 84, 'constituency_name': 'Omalur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 85, 'constituency_name': 'Mettur', 'winner_party_id_prev': 6, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 86, 'constituency_name': 'Edappadi', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 87, 'constituency_name': 'Sankari', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 88, 'constituency_name': 'Salem (West)', 'winner_party_id_prev': 6, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 89, 'constituency_name': 'Salem (North)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 90, 'constituency_name': 'Salem (South)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 13, 'constituency_id': 91, 'constituency_name': 'Veerapandi', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 14, 'constituency_id': 92, 'constituency_name': 'Rasipuram(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 14, 'constituency_id': 93, 'constituency_name': 'Senthamangalam(ST)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 14, 'constituency_id': 94, 'constituency_name': 'Namakkal', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 14, 'constituency_id': 95, 'constituency_name': 'Paramathi-Velur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 14, 'constituency_id': 96, 'constituency_name': 'Tiruchengode', 'winner_party_id_prev': 7, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 14, 'constituency_id': 97, 'constituency_name': 'Kumarapalayam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 15, 'constituency_id': 98, 'constituency_name': 'Erode (East)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 15, 'constituency_id': 99, 'constituency_name': 'Erode (West)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 15, 'constituency_id': 100, 'constituency_name': 'Modakkurichi', 'winner_party_id_prev': 8, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 15, 'constituency_id': 101, 'constituency_name': 'Perundurai', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 15, 'constituency_id': 102, 'constituency_name': 'Bhavani', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 15, 'constituency_id': 103, 'constituency_name': 'Anthiyur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 15, 'constituency_id': 104, 'constituency_name': 'Gobichettipalayam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 15, 'constituency_id': 105, 'constituency_name': 'Bhavanisagar(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 16, 'constituency_id': 106, 'constituency_name': 'Dharapuram(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 16, 'constituency_id': 107, 'constituency_name': 'Kangayam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 16, 'constituency_id': 108, 'constituency_name': 'Avanashi(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 16, 'constituency_id': 109, 'constituency_name': 'Tiruppur (North)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 16, 'constituency_id': 110, 'constituency_name': 'Tiruppur (South)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 16, 'constituency_id': 111, 'constituency_name': 'Palladam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 16, 'constituency_id': 112, 'constituency_name': 'Udumalaipettai', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 16, 'constituency_id': 113, 'constituency_name': 'Madathukulam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        
        {'district_id': 17, 'constituency_id': 114, 'constituency_name': 'Udhagamandalam', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 17, 'constituency_id': 115, 'constituency_name': 'Gudalur(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 17, 'constituency_id': 116, 'constituency_name': 'Coonoor', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 18, 'constituency_id': 117, 'constituency_name': 'Mettupalayam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 118, 'constituency_name': 'Sulur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 119, 'constituency_name': 'Kavundampalayam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 120, 'constituency_name': 'Coimbatore (North)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 121, 'constituency_name': 'Thondamuthur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 122, 'constituency_name': 'Coimbatore (South)', 'winner_party_id_prev': 8, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 123, 'constituency_name': 'Singanallur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 124, 'constituency_name': 'Kinathukadavu', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 125, 'constituency_name': 'Pollachi', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 18, 'constituency_id': 126, 'constituency_name': 'Valparai(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 19, 'constituency_id': 127, 'constituency_name': 'Palani', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 19, 'constituency_id': 128, 'constituency_name': 'Oddanchatram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 19, 'constituency_id': 129, 'constituency_name': 'Athoor', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 19, 'constituency_id': 130, 'constituency_name': 'Nilakottai(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 19, 'constituency_id': 131, 'constituency_name': 'Natham', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 19, 'constituency_id': 132, 'constituency_name': 'Dindigul', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 19, 'constituency_id': 133, 'constituency_name': 'Vedasandur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 20, 'constituency_id': 134, 'constituency_name': 'Aravakurichi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 20, 'constituency_id': 135, 'constituency_name': 'Karur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 20, 'constituency_id': 136, 'constituency_name': 'Krishnarayapuram(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 20, 'constituency_id': 137, 'constituency_name': 'Kulithalai', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 21, 'constituency_id': 138, 'constituency_name': 'Manapaarai', 'winner_party_id_prev': 9, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 21, 'constituency_id': 139, 'constituency_name': 'Srirangam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 21, 'constituency_id': 140, 'constituency_name': 'Tiruchirappalli (West)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 21, 'constituency_id': 141, 'constituency_name': 'Tiruchirappalli (East)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 21, 'constituency_id': 142, 'constituency_name': 'Thiruverumbur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 21, 'constituency_id': 143, 'constituency_name': 'Lalgudi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 21, 'constituency_id': 144, 'constituency_name': 'Manachanallur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 21, 'constituency_id': 145, 'constituency_name': 'Musiri', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 21, 'constituency_id': 146, 'constituency_name': 'Thuraiyur(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 22, 'constituency_id': 147, 'constituency_name': 'Perambalur(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 22, 'constituency_id': 148, 'constituency_name': 'Kunnam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 23, 'constituency_id': 149, 'constituency_name': 'Ariyalur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 23, 'constituency_id': 150, 'constituency_name': 'Jayankondam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 24, 'constituency_id': 151, 'constituency_name': 'Tittakudi(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 24, 'constituency_id': 152, 'constituency_name': 'Vriddhachalam', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 24, 'constituency_id': 153, 'constituency_name': 'Neyveli', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 24, 'constituency_id': 154, 'constituency_name': 'Panruti', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 24, 'constituency_id': 155, 'constituency_name': 'Cuddalore', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 24, 'constituency_id': 156, 'constituency_name': 'Kurinjipadi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 24, 'constituency_id': 157, 'constituency_name': 'Bhuvanagiri', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 24, 'constituency_id': 158, 'constituency_name': 'Chidambaram', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 24, 'constituency_id': 159, 'constituency_name': 'Kattumannarkoil(SC)', 'winner_party_id_prev': 3, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 25, 'constituency_id': 160, 'constituency_name': 'Sirkazhi(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 25, 'constituency_id': 161, 'constituency_name': 'Mayiladuthurai', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 25, 'constituency_id': 162, 'constituency_name': 'Poompuhar', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 26, 'constituency_id': 163, 'constituency_name': 'Nagapattinam', 'winner_party_id_prev': 3, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 26, 'constituency_id': 164, 'constituency_name': 'Kilvelur(SC)', 'winner_party_id_prev': 10, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 26, 'constituency_id': 165, 'constituency_name': 'Vedaranyam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 27, 'constituency_id': 166, 'constituency_name': 'Thiruthuraipoondi(SC)', 'winner_party_id_prev': 5, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 27, 'constituency_id': 167, 'constituency_name': 'Mannargudi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 27, 'constituency_id': 168, 'constituency_name': 'Thiruvarur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 27, 'constituency_id': 169, 'constituency_name': 'Nannilam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 28, 'constituency_id': 170, 'constituency_name': 'Thiruvidaimarudur(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 28, 'constituency_id': 171, 'constituency_name': 'Kumbakonam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 28, 'constituency_id': 172, 'constituency_name': 'Papanasam', 'winner_party_id_prev': 9, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 28, 'constituency_id': 173, 'constituency_name': 'Thiruvaiyaru', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 28, 'constituency_id': 174, 'constituency_name': 'Thanjavur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 28, 'constituency_id': 175, 'constituency_name': 'Orathanadu', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 28, 'constituency_id': 176, 'constituency_name': 'Pattukkottai', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 28, 'constituency_id': 177, 'constituency_name': 'Peravurani', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 29, 'constituency_id': 178, 'constituency_name': 'Gandharvakottai(SC)', 'winner_party_id_prev': 10, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 29, 'constituency_id': 179, 'constituency_name': 'Viralimalai', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 29, 'constituency_id': 180, 'constituency_name': 'Pudukkottai', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 29, 'constituency_id': 181, 'constituency_name': 'Thirumayam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 29, 'constituency_id': 182, 'constituency_name': 'Alangudi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 29, 'constituency_id': 183, 'constituency_name': 'Aranthangi', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 30, 'constituency_id': 184, 'constituency_name': 'Karaikudi', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 30, 'constituency_id': 185, 'constituency_name': 'Tiruppattur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 30, 'constituency_id': 186, 'constituency_name': 'Sivaganga', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 30, 'constituency_id': 187, 'constituency_name': 'Manamadurai(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 31, 'constituency_id': 188, 'constituency_name': 'Melur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 189, 'constituency_name': 'Madurai East', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 190, 'constituency_name': 'Sholavandan(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 191, 'constituency_name': 'Madurai North', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 192, 'constituency_name': 'Madurai South', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 193, 'constituency_name': 'Madurai Central', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 194, 'constituency_name': 'Madurai West', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 195, 'constituency_name': 'Thiruparankundram', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 196, 'constituency_name': 'Tirumangalam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 31, 'constituency_id': 197, 'constituency_name': 'Usilampatti', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 32, 'constituency_id': 198, 'constituency_name': 'Andipatti', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 32, 'constituency_id': 199, 'constituency_name': 'Periyakulam(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 32, 'constituency_id': 200, 'constituency_name': 'Bodinayakanur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 32, 'constituency_id': 201, 'constituency_name': 'Cumbum', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 33, 'constituency_id': 202, 'constituency_name': 'Rajapalayam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 33, 'constituency_id': 203, 'constituency_name': 'Srivilliputhur(SC)', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 33, 'constituency_id': 204, 'constituency_name': 'Sattur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 33, 'constituency_id': 205, 'constituency_name': 'Sivakasi', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 33, 'constituency_id': 206, 'constituency_name': 'Virudhunagar', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 33, 'constituency_id': 207, 'constituency_name': 'Aruppukkottai', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 33, 'constituency_id': 208, 'constituency_name': 'Tiruchuli', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 34, 'constituency_id': 209, 'constituency_name': 'Paramakudi(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 34, 'constituency_id': 210, 'constituency_name': 'Tiruvadanai', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 34, 'constituency_id': 211, 'constituency_name': 'Ramanathapuram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 34, 'constituency_id': 212, 'constituency_name': 'Mudhukulathur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 35, 'constituency_id': 213, 'constituency_name': 'Vilathikulam', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 35, 'constituency_id': 214, 'constituency_name': 'Thoothukkudi', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 35, 'constituency_id': 215, 'constituency_name': 'Tiruchendur', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 35, 'constituency_id': 216, 'constituency_name': 'Srivaikuntam', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 35, 'constituency_id': 217, 'constituency_name': 'Ottapidaram(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 35, 'constituency_id': 218, 'constituency_name': 'Kovilpatti', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 36, 'constituency_id': 219, 'constituency_name': 'Sankarankovil(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 36, 'constituency_id': 220, 'constituency_name': 'Vasudevanallur(SC)', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 36, 'constituency_id': 221, 'constituency_name': 'Kadayanallur', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 36, 'constituency_id': 222, 'constituency_name': 'Tenkasi', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 36, 'constituency_id': 223, 'constituency_name': 'Alangulam', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},

        {'district_id': 37, 'constituency_id': 224, 'constituency_name': 'Tirunelveli', 'winner_party_id_prev': 8, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 37, 'constituency_id': 225, 'constituency_name': 'Ambasamudram', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 37, 'constituency_id': 226, 'constituency_name': 'Palayamkottai', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 37, 'constituency_id': 227, 'constituency_name': 'Nanguneri', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 37, 'constituency_id': 228, 'constituency_name': 'Radhapuram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},

        {'district_id': 38, 'constituency_id': 229, 'constituency_name': 'Kanniyakumari', 'winner_party_id_prev': 4, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 38, 'constituency_id': 230, 'constituency_name': 'Nagercoil', 'winner_party_id_prev': 8, 'winner_alliance_id_prev': 2, 'prediction_alliance_id_next': -1},
        {'district_id': 38, 'constituency_id': 231, 'constituency_name': 'Colachel', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 38, 'constituency_id': 232, 'constituency_name': 'Padmanabhapuram', 'winner_party_id_prev': 1, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 38, 'constituency_id': 233, 'constituency_name': 'Vilavancode', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1},
        {'district_id': 38, 'constituency_id': 234, 'constituency_name': 'Killiyoor', 'winner_party_id_prev': 2, 'winner_alliance_id_prev': 1, 'prediction_alliance_id_next': -1}
    ]

tn_data = []
@app.get("/", tags=["root"])
async def read_root() -> dict:
    print("root called")
    print("returning >>>> ", "Elections-Root.")
    return {"message": "Elections-Root."}

@app.get("/tamilnadu/districts", tags=["districts"])
async def get_tnDistricts() -> dict:
    print("districts called")
    print("returning >>>> ", tn_districts)
    return {"data": tn_districts}

@app.get("/tamilnadu/static/{district_id}", tags=["staticForDistrict"])
async def get_tnStaticForDistrict(district_id) -> dict:
    print("district id called for ", district_id)
    data = []
    global tn_data
    tn_data = []
    print(district_id)
    for item in tn_static:
        alliance_name = ''
        party_name = ''
        district_name = ''
        if (item["district_id"] == int(district_id)):
            for d in tn_districts:
                if (d['district_id'] == item['district_id']):
                    district_name = d['district_name']
                    break
            for a in tn_alliances:
                if (a['alliance_id'] == item['winner_alliance_id_prev']):
                    alliance_name = a['alliance_name']
                    break
            
            for p in tn_parties:
                if (p['party_id'] == item['winner_party_id_prev']):
                    party_name = p['party_name']
                    break

            tn_data.append(
                {'district_id': item['district_id'],
                'district': district_name,
                'constituency_id': item['constituency_id'],
                'constituency_name': tn_constituencies[item['constituency_id']],
                'winner_alliance_prev': alliance_name,
                'winner_party_prev': party_name,
                "prediction_alliance_id_next": item['prediction_alliance_id_next']
                }
            )
        # print("tn data >>>>", tn_data)
    print("returning >>>>", tn_data)
    return {"data": tn_data}
# @app.get("/tamilnadu/alliancePartyData/{alliance_id}", tags=["alliancePartyData"])



@app.get("/tamilnadu/static", tags=["tnstatic"])
async def get_tnStatic() -> dict:
    print("static called")
    # data = []
    global tn_data
    tn_data = []
    for item in tn_static:
        alliance_name = ''
        party_name = ''
        district_name = ''

        for d in tn_districts:
            if (d['district_id'] == item['district_id']):
                district_name = d['district_name']
                break
        for a in tn_alliances:
            if (a['alliance_id'] == item['winner_alliance_id_prev']):
                alliance_name = a['alliance_name']
                break
        
        for p in tn_parties:
            if (p['party_id'] == item['winner_party_id_prev']):
                party_name = p['party_name']
                break

        tn_data.append(
            {'district_id': item['district_id'],
             'district': district_name,
             'constituency_id': item['constituency_id'],
             'constituency_name': tn_constituencies[item['constituency_id']],
             'winner_alliance_prev': alliance_name,
             'winner_party_prev': party_name,
             "prediction_alliance_id_next": item['prediction_alliance_id_next']
               }
        )
        # print("tn data >>>>", tn_data)
    print("returning >>>> ", tn_data)
    return {"data": tn_data}

@app.get("/tamilnadu/prevResults", tags=["prevResults"])
async def get_tnPrevResults() -> dict:
    print("prevResults called")

    # data = []
    global tn_data
    tn_data = []
    for item in tn_static:
        alliance_name = ''
        party_name = ''
        district_name = ''

        for d in tn_districts:
            if (d['district_id'] == item['district_id']):
                district_name = d['district_name']
                break
        for a in tn_alliances:
            if (a['alliance_id'] == item['winner_alliance_id_prev']):
                alliance_name = a['alliance_name']
                break
        
        for p in tn_parties:
            if (p['party_id'] == item['winner_party_id_prev']):
                party_name = p['party_name']
                break

        tn_data.append(
            {'district_id': item['district_id'],
             'district': district_name,
             'constituency_id': item['constituency_id'],
             'constituency_name': tn_constituencies[item['constituency_id']],
             'winner_alliance_prev': alliance_name,
             'winner_party_prev': party_name,
             "prediction_alliance_id_next": item['winner_alliance_id_prev']
               }
        )
        # print("tn data >>>>", tn_data)
    print("returning >>>> ", tn_data)
    return {"data": tn_data}

@app.post("/tamilnadu/updatePrediction", tags=["updatePrediction"])
async def update_prediction(data: dict) -> dict:
    # print("updatePrediction called")
    # print("to update >>>>", data)
    for item in tn_data:
        if item['constituency_id'] == data['constituency_id']:
            item['prediction_alliance_id_next'] = data['prediction_alliance_id_next']
            # print("updated >>>> ", item)
            break
    
    print("returning >>>> ", tn_data)
    return{ "data" : tn_data
    }

@app.get("/tamilnadu/allianceColorCode", tags=["tnAllianceColorCode"])
async def get_tnAllianceColorCode() -> dict:
    print("allianceColorCode called")
    data = {}
    # print(tn_alliances)
    for alliance in tn_alliances:
        data[alliance['alliance_id']] = alliance['colorcode']
        
    # print(data)
    print("returning >>>> ", data)
    return {"data": data}

@app.get("/tamilnadu/alliances", tags=["allianceData"])
async def get_tnAlliances() -> dict:
    print("alliances called")
    # print(tn_alliances)
    data = []
    for a in tn_alliances:
        if (a['alliance_id'] != -1):
            data.append( {'alliance_id': a['alliance_id'], 'alliance_name': a['alliance_name'], 'colorcode': a['colorcode']})
    
    print("returning >>>> ", data)
    return {"data": data}

@app.get("/tamilnadu/alliancePartyData/{alliance_id}", tags=["alliancePartyData"])
async def get_tnAlliancePartyData(alliance_id) -> dict:
    print("alliancePartyData called for ", alliance_id)
    data = []
    for alliancePartyId in tn_alliance_map[int(alliance_id)]:
        for p in tn_parties:
            if p['party_id'] == alliancePartyId:
                data.append(p)
    return {"data": data}

@app.get("/tamilnadu/predictedData", tags=["tnPredictedData"])
async def get_tnPredictedData() -> dict:
    print("predictedData called")
    data = []
    dataDict = {}
    # print(len(tn_data))
    for item in tn_data:
        # print("predictedData " , item)
        alliance_name = ''
        for a in tn_alliances:
            if (a['alliance_id'] == item['prediction_alliance_id_next']):
                alliance_name = a['alliance_name']
                break
        dataDict[alliance_name] = dataDict.get(alliance_name, 0) + 1
    # print(dataDict)

    for d in dataDict:
        colorcode = [a for a in tn_alliances if a['alliance_name'] == d][0]['colorcode']
        data.append({
            'label': d,
            'value': dataDict[d],
            'color': colorcode
        })

    print("returning >>>> ", data)
    return {"data": data}

@app.post("/tamilnadu/resetPrediction", tags=["resetPrediction"])
async def reset_prediction() -> dict:
    print("resetPrediction called")
    for item in tn_data:
        item['prediction_alliance_id_next'] = -1
    
    print("returning >>>> ", tn_data)
    return{ "data" : tn_data}
