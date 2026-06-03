from kginfo import Kginfo

#elementtype = {   #all typings of the pokemon added, basically resistances to damage
    #"lightning": {"malteser": 2.0, "wood" : 0.75, "soft alpha": 1.5},
    #"malteser": {"lightning": 0, "wood": 0.5, "soft alpha": 0.5},
    #"wood": {"lightning": 2.0, "malteser": 1},
    #"soft alpha": {"lightning": 1.5, "malteser": 2.0, "soft beta":2},
    #"soft beta": {"lightning": 1.5, "malteser": 0.5, "soft alpha": 1.5},
    #"son": {}, # only for carlos
    #"invisible": {},
    #"pdf": {}, # for sebastian
    #"peanut butter": {}, # type for me
    #"studyroom":{}, # soham, thomas, abhinav
    #"uchiha life": {} #thierrey

element_type = {
    # Existing types with your current rules balanced out
    "lightning": {
        "malteser": 1.5, 
        "wood": 0.25, 
        "soft alpha": 1.5,
        "invisible": 0.5     # Grounded/Cannot see target clearly
    },
    "malteser": {
        "lightning": 0.25, # for mr hayat
        "wood": 0.5, 
        "soft alpha": 0.5,
        "peanut butter": 1.25  # Melted into the peanut butter
    },
    "wood": {
        "lightning": 2.0, 
        "malteser": 1.25,
        "soft alpha": 1.5,
        "studyroom": 1.75    # Desk/Furniture material advantage
    },
    "soft alpha": {
        "lightning": 1.67, 
        "malteser": 2.25, 
        "soft beta": 2.0,
        "pedf": 0.5           # Bureaucracy slows down the alpha
    },
    "soft beta": {
        "lightning": 1.5, 
        "malteser": 0.5, 
        "soft alpha": 1.5,
        "uchiha life": 2.0   # Genjutsu breaks beta mindset
    },

    # --- NEW TYPES INCORPORATED INTO THE BALANCE ---

    "son": {
        "invisible": 2.0,    # Can sense the unseen
        "pedf": 0.5,          # Homework/Forms hold them back
        "studyroom": 0.5     # Trapped studying
    },
    
    "invisible": {
        "son": 0.0,          # 
        "lightning": 0,    # Surprise electric strike
        "uchiha life": 2   # Sharingan can see right through invisibility
    },

    "pedf": {
        "soft alpha": 2.0,   # Bureaucracy counters the alpha
        "son": 2.0,          # School documents counter the son
        "peanut butter": 0.5 # Physical mess ruins paper/digital files
    },

    "peanut butter": {
        "malteser": 2.0,     # Sticky trap for sweets
        "pedf": 2.0,          # Ruined documents
        "invisible": 0.5,    # Hard to stick to what you can't see
        "studyroom": 0.5     # Not allowed inside the study area
    },

    "studyroom": {
        "son": 0.67,          # 
        "peanut butter": 0, # garbage against me
        "wood": 0.5,         # Already made of wood, no impact
        "uchiha life": 0.5   # Studying can't beat ninja combat experience
    },

    "uchiha life": {
        "studyroom": 2.0,    # Amaterasu burns the room down
        "invisible": 2.0,   
        "soft beta": 0.5,    
        "lightning": 1.25     # genjutsu of that level doesnt work on me
    }
}

all_kgasons = {
    "Hayat": Kginfo("Hayat", 290, "malteser", 59, {
        "not possible": 60, # no extra effect
        "found the three": 150, # 10% of 2x attack
        "2-3 further math and forget": 150, # confuses oppenent and increases crit by 50%
        "habby dere?": 150 # kgamon trapped for next move
    }),
    "Cameron": Kginfo("Cameron", 200, "soft alpha", 152, {
        "lightning eyes": 75, # 50% of paralsying
        "triple t repost": 150, # paralyses all of enemies team however results in immediate death
        "50 euros": 50, # 50% of hitting twice
        "boom boom": 250 # character goes boom boom but always leads to 100% of death, hwoever cannot use once under 50% hp and always goes last
    }),
    "diddi": Kginfo("diddi", 300, "lightning", 221, {
        "lebronjame": 75, # 100% chance of paralsying yourself
        "collitis straight": 150, # results in 0.25x def
        "nooo": 70, # no extra effect
        "thats a good boy": 25 # 100% defense and 100% attack
    }),
    "alexander": Kginfo("alexander", 300, "lightning", 60, {
        "late": 15, # paralyses openent and locks in turn without swap
        "gangwork": 50, # 2x attack and speed in 3 turns
        "lanyard whiplash": 100, # no extra effect
        "friday skipper": 25 # 67% of randomly paralysing 2 of ur pokemon
    }),
    "lameson": Kginfo("lameson", 68, "soft beta", 101, {
        "5 move checkmate": 250, # after 5 moves faints, not possible after using
        "alpha minders": 0, # 2x attack no base attack
        "buffmyshi": 100, # no extra effect
        "thick of it jazz remix": 300 #  insta kill yourself
    }),
    "asamlife": Kginfo("asamlife", 167, "soft alpha", 171, {
        "asamgrinders": 250, # after 5 moves faints, not possible after using
        "table bang": 0, # 2x attack no base attack
        "accounting life": 100, # no extra effect
        "charan put your hand down": 300 #  insta kill
    })
}