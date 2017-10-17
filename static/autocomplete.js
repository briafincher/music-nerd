$( function() {
    var tags = [
        "pop",
        "dance pop",
        "pop rap",
        "rap",
        "post-teen pop",
        "tropical house",
        "rock",
        "modern rock",
        "trap music",
        "edm",
        "latin",
        "hip hop",
        "southern hip hop",
        "pop rock",
        "neo mellow",
        "alternative rock",
        "r&b",
        "dwn trap",
        "classic rock",
        "alternative metal",
        "latin pop",
        "album rock",
        "mellow gold",
        "post-grunge",
        "indie r&b",
        "indie rock",
        "indie pop",
        "viral pop",
        "reggaeton",
        "soft rock",
        "nu metal",
        "pop punk",
        "electro house",
        "singer-songwriter",
        "indie folk",
        "indietronica",
        "tropical",
        "folk-pop",
        "urban contemporary",
        "permanent wave",
        "contemporary country",
        "gangster rap",
        "hard rock",
        "indie poptimism",
        "rap metal",
        "country road",
        "canadian pop",
        "big room",
        "country",
        "hip pop",
        "house",
        "folk rock",
        "latin hip hop",
        "dirty south rap",
        "underground hip hop",
        "garage rock",
        "rock en espanol",
        "chamber pop",
        "grupera",
        "stomp and holler",
        "funk rock",
        "roots rock",
        "regional mexican",
        "europop",
        "blues-rock",
        "trap latino",
        "modern country rock",
        "progressive house",
        "dance rock",
        "alternative dance",
        "new wave pop",
        "synthpop",
        "new wave",
        "adult standards",
        "latin alternative",
        "neo soul",
        "neo-psychedelic",
        "banda",
        "classic funk rock",
        "soul",
        "emo",
        "deep indie r&b",
        "quiet storm",
        "psychedelic rock",
        "deep pop r&b",
        "rap rock",
        "norteno",
        "art rock",
        "spanish pop",
        "progressive electro house",
        "new rave",
        "motown",
        "metal",
        "electronic",
        "brostep",
        "shimmer pop",
        "regional mexican pop",
        "screamo",
        "latin arena pop",
        "escape room",
        "reggaeton flow",
        "crunk",
        "teen pop",
        "indie anthem-folk",
        "funk",
        "deep big room",
        "disco",
        "pop reggaeton",
        "new romantic",
        "vapor soul",
        "deep tropical house",
        "punk",
        "trap francais",
        "electronic trap",
        "deep german hip hop",
        "deep funk carioca",
        "acoustic pop",
        "metropopolis",
        "metalcore",
        "west coast rap",
        "hardcore hip hop",
        "folk",
        "new americana",
        "francoton",
        "focus",
        "brill building pop",
        "sertanejo universitario",
        "southern rock",
        "east coast hip hop",
        "german hip hop",
        "ranchera",
        "freak folk",
        "groove metal",
        "jazz blues",
        "swedish pop",
        "talent show",
        "piano rock",
        "worship",
        "christian alternative rock",
        "boy band",
        "chillwave",
        "argentine rock",
        "vocal jazz",
        "christian music",
        "g funk",
        "modern blues",
        "vegas indie",
        "redneck",
        "new jack swing",
        "british blues",
        "ccm",
        "mpb",
        "country rock",
        "deep underground hip hop",
        "soundtrack",
        "memphis soul",
        "compositional ambient",
        "bass trap",
        "swedish idol pop",
        "dance-punk",
        "indie psych-rock",
        "lo-fi",
        "soul blues",
        "rock-and-roll",
        "moombahton",
        "noise pop",
        "k-pop",
        "dream pop",
        "cumbia pop",
        "protopunk",
        "outlaw country",
        "southern soul",
        "german pop",
        "melodic metalcore",
        "hollywood",
        "christian rock",
        "anthem worship",
        "detroit hip hop",
        "deep dutch hip hop",
        "electric blues",
        "cantautor",
        "pagode",
        "glam metal",
        "deep german pop rock",
        "indiecoustica",
        "britpop",
        "italian arena pop",
        "korean pop",
        "deep groove house",
        "chicago soul",
        "classify",
        "deep australian indie",
        "traditional country",
        "mariachi",
        "glam rock",
        "alternative hip hop",
        "underground pop rap",
        "italian pop",
        "scorecore",
        "funk metal",
        "deep pop edm",
        "speed metal",
        "samba",
        "trip hop",
        "grime",
        "complextro",
        "downtempo",
        "british invasion",
        "channel pop",
        "tracestep",
        "lilith",
        "vapor twitch",
        "classical",
        "bachata",
        "catstep",
        "deep house",
        "melancholia",
        "lift kit",
        "skate punk",
        "bossa nova",
        "anti-folk",
        "pop emo",
        "australian dance",
        "disco house",
        "bubblegum pop",
        "grunge",
        "symphonic rock",
        "duranguense",
        "traditional folk",
        "comic",
        "chillhop",
        "la indie",
        "sertanejo",
        "cumbia",
        "rockabilly",
        "jazz",
        "australian alternative rock",
        "reggae fusion",
        "hoerspiel",
        "otacore",
        "video game music",
        "swedish folk pop",
        "romantic",
        "texas country",
        "roots reggae",
        "nueva cancion",
        "slow core",
        "space rock",
        "progressive rock",
        "nu jazz",
        "alt-indie rock",
        "world worship",
        "dancehall",
        "deep trap",
        "french pop",
        "progressive metal",
        "power metal",
        "nu gaze",
        "reggae",
        "madchester",
        "spanish rock",
        "forro",
        "brazilian hip hop",
        "industrial metal",
        "mandopop",
        "opm",
        "deep danish pop",
        "alternative country",
        "sky room",
        "deep southern trap",
        "bolero",
        "nashville sound",
        "lounge",
        "taiwanese pop",
        "merseybeat",
        "finnish dance pop",
        "thrash metal",
        "indie garage rock",
        "danish pop",
        "trance",
        "deep latin hip hop",
        "post-punk",
        "turkish pop",
        "jazz funk",
        "chamber psych",
        "cool jazz",
        "jam band",
        "eurodance",
        "deep taiwanese pop",
        "salsa",
        "preverb",
        "deep cumbia sonidera",
        "c-pop",
        "candy pop",
        "german techno",
        "pixie",
        "brooklyn indie",
        "chilean rock",
        "minimal",
        "swedish alternative rock",
        "bow pop",
        "french hip hop",
        "punk blues",
        "deep new americana",
        "axe",
        "deep euro house",
        "alternative emo",
        "post-screamo",
        "vocal house",
        "filter house",
        "cabaret",
        "industrial rock",
        "swedish indie rock",
        "etherpop",
        "merengue",
        "big beat",
        "progressive trance",
        "garage psych",
        "finnish pop",
        "chanson",
        "uk post-punk",
        "power pop",
        "ninja",
        "country dawn",
        "jazz fusion",
        "bubblegum dance",
        "melodic death metal",
        "deep swedish hip hop",
        "show tunes",
        "cantopop",
        "deep regional mexican",
        "bebop",
        "shiver pop",
        "vallenato",
        "post-disco",
        "italian hip hop",
        "dutch hip hop",
        "post rock",
        "spanish pop rock",
        "dutch pop",
        "contemporary post-bop",
        "modern classical",
        "turkish rock",
        "irish rock",
        "easy listening",
        "swedish eurodance",
        "danspunk",
        "dutch house",
        "minimal techno",
        "swedish hip hop",
        "indonesian pop",
        "canadian indie",
        "cumbia villera",
        "texas blues",
        "celtic rock",
        "australian pop",
        "wrestling",
        "west coast trap",
        "hip house",
        "microhouse",
        "anthem emo",
        "pinoy alternative",
        "blues",
        "acid jazz",
        "broadway",
        "chillstep",
        "tech house",
        "movie tunes",
        "uk funky",
        "french indietronica",
        "experimental rock",
        "classic swedish pop",
        "norwegian indie",
        "norwegian pop",
        "turntablism",
        "soul jazz",
        "traditional blues",
        "progressive bluegrass",
        "stoner rock",
        "melodic hardcore",
        "swing",
        "electro",
        "indie jazz",
        "dreamo",
        "rock gaucho",
        "fourth world",
        "minimal dub",
        "french rock",
        "latin christian",
        "post-hardcore",
        "progressive post-hardcore",
        "zapstep",
        "hard bop",
        "sheffield indie",
        "azontobeats",
        "epicore",
        "deep chiptune",
        "antiviral pop",
        "uplifting trance",
        "noise rock",
        "electro latino",
        "anime",
        "indie punk",
        "country blues",
        "new age",
        "ambient",
        "aussietronica",
        "death core",
        "deep funk",
        "reggae rock",
        "country gospel",
        "electro swing",
        "indie rockism",
        "groove room",
        "deep melodic euro house",
        "j-pop",
        "french reggae",
        "death metal",
        "nu disco",
        "lovers rock",
        "brazilian gospel",
        "uk garage",
        "neo classical metal",
        "industrial",
        "stride",
        "canadian metal",
        "christian uplift",
        "gothic metal",
        "mexican indie",
        "future funk",
        "christian hip hop",
        "ska",
        "french indie pop",
        "stoner metal",
        "gauze pop",
        "latin jazz",
        "german metal",
        "swedish indie pop",
        "turkish jazz",
        "experimental",
        "deep ccm",
        "classic norwegian pop",
        "memphis blues",
        "hyphy",
        "pub rock",
        "merengue urbano",
        "liquid funk",
        "ska punk",
        "suomi rock",
        "afrobeats",
        "drum and bass",
        "louvor",
        "smooth jazz",
        "drill",
        "world",
        "swedish synthpop",
        "vaporwave",
        "dub",
        "chicago blues",
        "neue deutsche harte",
        "new orleans blues",
        "new weird america",
        "trova",
        "hardcore punk",
        "j-rock",
        "memphis hip hop",
        "old school hip hop",
        "big band",
        "german pop rock",
        "relaxative",
        "baroque",
        "flamenco",
        "indonesian indie",
        "stomp pop",
        "comedy",
        "mambo",
        "russelater",
        "bass music",
        "viking metal",
        "djent",
        "gospel",
        "norwegian rock",
        "acoustic blues",
        "deep texas country",
        "doo-wop",
        "delta blues",
        "icelandic pop",
        "christian relaxative",
        "swedish metal",
        "spanish indie pop",
        "operatic pop",
        "wonky",
        "classical period",
        "cumbia sonidera",
        "deep swedish indie pop",
        "minimal tech house",
        "latin metal",
        "piedmont blues",
        "cowboy western",
        "hardstyle",
        "desi",
        "deep disco house",
        "turkish folk",
        "shoegaze",
        "dangdut",
        "celtic",
        "hands up",
        "pop house",
        "tejano",
        "meditation",
        "danish pop rock",
        "indian pop",
        "nwobhm",
        "deep hardstyle",
        "boogaloo",
        "dansband",
        "gothic symphonic metal",
        "japanese r&b",
        "electropowerpop",
        "argentine reggae",
        "finnish hip hop",
        "drone",
        "desi hip hop",
        "symphonic metal",
        "intelligent dance music",
        "schlager",
        "healing",
        "contemporary jazz",
        "melbourne bounce",
        "sleep",
        "filthstep",
        "spanish punk",
        "chicano rap",
        "brazilian indie",
        "electroclash",
        "louisiana blues",
        "velha guarda",
        "cubaton",
        "children's music",
        "jangle pop",
        "afrobeat",
        "spanish hip hop",
        "polish pop",
        "k-hop",
        "opera",
        "retro electro",
        "uk drill",
        "alternative r&b",
        "british folk",
        "folk punk",
        "j-rap",
        "future garage",
        "boston rock",
        "j-dance",
        "nu-cumbia",
        "alternative pop rock",
        "classic danish pop",
        "crossover thrash",
        "a cappella",
        "mathcore",
        "environmental",
        "glitch",
        "levenslied",
        "reading",
        "azonto",
        "german indie",
        "coverchill",
        "rumba",
        "jazz metal",
        "filmi",
        "glitch hop",
        "vapor pop",
        "northern soul",
        "spanish new wave",
        "arabesk",
        "underground rap",
        "polynesian pop",
        "zolo",
        "brazilian punk",
        "melodipop",
        "liedermacher",
        "australian hip hop",
        "christian dance",
        "folk metal",
        "abstract hip hop",
        "neoclassical",
        "norwegian hip hop",
        "discofox",
        "deep turkish pop",
        "piano blues",
        "strut",
        "danseband",
        "bluegrass",
        "sludge metal",
        "new tribe",
        "neo-singer-songwriter",
        "canadian country",
        "italo dance",
        "breakbeat",
        "finnish metal",
        "technical death metal",
        "german punk",
        "jump blues",
        "float house",
        "fluxwork",
        "hardcore techno",
        "welsh rock",
        "fingerstyle",
        "sleaze rock",
        "australian country",
        "folklore argentino",
        "rock steady",
        "deep uplifting trance",
        "electro jazz",
        "alternative ccm",
        "swamp blues",
        "grave wave",
        "alternative pop",
        "kiwi rock",
        "slow game",
        "modern performance",
        "doom metal",
        "russian pop",
        "portland indie",
        "techno",
        "j-metal",
        "no wave",
        "stomp and flutter",
        "dutch rock",
        "post-metal",
        "black metal",
        "neurofunk",
        "christian metal",
        "jump up",
        "pagan black metal",
        "hard alternative",
        "polish hip hop",
        "drift",
        "pop flamenco",
        "kirtan",
        "brega",
        "peruvian rock",
        "classic italian pop",
        "ectofolk",
        "symphonic black metal",
        "turkish hip hop",
        "italian indie pop",
        "cuban rumba",
        "dark jazz",
        "deathgrind",
        "happy hardcore",
        "deep norteno",
        "irish folk",
        "jungle",
        "scottish rock",
        "medieval rock",
        "carnaval",
        "belgian rock",
        "chicago house",
        "chamame",
        "dark wave",
        "idol",
        "classic chinese pop",
        "rap chileno",
        "avant-garde jazz",
        "austindie",
        "chicago indie",
        "progressive uplifting trance",
        "medieval",
        "orgcore",
        "bay area indie",
        "western swing",
        "new orleans jazz",
        "japanese city pop",
        "russian rock",
        "harmonica blues",
        "italian disco",
        "romantico",
        "j-idol",
        "eurovision",
        "post-doom metal",
        "outsider house",
        "mexican rock-and-roll",
        "puerto rican rock",
        "classic finnish pop",
        "colombian rock",
        "malaysian pop",
        "portuguese rock",
        "arab pop",
        "dubstep",
        "seattle indie",
        "soul flow",
        "sertanejo tradicional",
        "nasheed",
        "gbvfi",
        "brutal death metal",
        "salsa international",
        "hardcore",
        "psychedelic doom",
        "avantgarde metal",
        "baile funk",
        "riddim",
        "speed garage",
        "grindcore",
        "brazilian ccm",
        "funky tech house",
        "quebecois",
        "austropop",
        "psychedelic trance",
        "celtic punk",
        "classic russian rock",
        "j-poprock",
        "spanish noise pop",
        "warm drone",
        "math pop",
        "italian pop rock",
        "soca",
        "barnmusik",
        "freestyle",
        "ebm",
        "ethereal wave",
        "garage pop",
        "balearic",
        "nursery",
        "world meditation",
        "african gospel",
        "math rock",
        "progressive deathcore",
        "destroy techno",
        "nintendocore",
        "indie dream pop",
        "polish punk",
        "russiavision",
        "kindermusik",
        "mande pop",
        "acid house",
        "albuquerque indie",
        "emo punk",
        "deep latin christian",
        "laiko",
        "electrofox",
        "k-indie",
        "entehno",
        "british alternative rock",
        "ambeat",
        "bassline",
        "drill and bass",
        "substep",
        "classic finnish rock",
        "turbo folk",
        "deep minimal techno",
        "musica para ninos",
        "ska revival",
        "british indie rock",
        "rock catala",
        "bmore",
        "chill lounge",
        "free jazz",
        "romanian pop",
        "canterbury scene",
        "deep comedy",
        "electro-industrial",
        "gypsy jazz",
        "volksmusik",
        "latin electronica",
        "argentine indie",
        "twee pop",
        "oi",
        "classic garage rock",
        "post-post-hardcore",
        "swedish hard rock",
        "christian hardcore",
        "world fusion",
        "singaporean pop",
        "slovak pop",
        "dansktop",
        "kabarett",
        "straight edge",
        "steampunk",
        "kraut rock",
        "gothic rock",
        "bhangra",
        "retro metal",
        "chaotic hardcore",
        "gabba",
        "nu age",
        "surf music",
        "thai idol",
        "canzone napoletana",
        "cello",
        "laboratorio",
        "ye ye",
        "mandible",
        "swedish jazz",
        "mashup",
        "christelijk",
        "old-time",
        "dixieland",
        "tango",
        "ballroom",
        "christian punk",
        "alternative roots rock",
        "choro",
        "futurepop",
        "african rock",
        "e6fi",
        "deep talent show",
        "freakbeat",
        "punjabi",
        "vancouver indie",
        "russian hip hop",
        "electro bailando",
        "hawaiian",
        "nordic house",
        "detroit techno",
        "andean",
        "drone metal",
        "early music",
        "horror punk",
        "psychobilly",
        "thai pop",
        "comedy rock",
        "progressive trance house",
        "deep indian pop",
        "progressive psytrance",
        "orchestral",
        "tribal house",
        "psychill",
        "atmospheric black metal",
        "jazz trio",
        "zouk riddim",
        "danish hip hop",
        "czech rock",
        "voidgaze",
        "fado",
        "uk hip hop",
        "classical piano",
        "israeli rock",
        "classical performance",
        "persian pop",
        "norwegian metal",
        "athens indie",
        "hungarian rock",
        "praise",
        "exotica",
        "dub techno",
        "neo-trad metal",
        "venezuelan rock",
        "swedish reggae",
        "theme",
        "avant-garde",
        "aggrotech",
        "czech folk",
        "turkish alternative",
        "kizomba",
        "neo-progressive",
        "classic colombian pop",
        "choral",
        "hungarian pop",
        "columbus ohio indie",
        "abstract beats",
        "visual kei",
        "italian metal",
        "deep latin alternative",
        "anime score",
        "popgaze",
        "power-pop punk",
        "indian folk",
        "mizrahi",
        "barnemusikk",
        "deep chill",
        "classic turkish pop",
        "melodic hard rock",
        "vintage italian soundtrack",
        "french movie tunes",
        "bubble trance",
        "j-indie",
        "deep tech house",
        "goregrind",
        "ok indie",
        "deep pop punk",
        "p funk",
        "dark cabaret",
        "rai",
        "power blues-rock",
        "russian punk",
        "shibuya-kei",
        "swedish punk",
        "folkmusik",
        "spanish reggae",
        "albanian pop",
        "nu skool breaks",
        "shimmer psych",
        "musica nativista",
        "melodic power metal",
        "fidget house",
        "basque rock",
        "horrorcore",
        "violin",
        "black thrash",
        "soukous",
        "classic belgian pop",
        "indie psych-pop",
        "lds",
        "turkish classical",
        "chiptune",
        "highlife",
        "belly dance",
        "string quartet",
        "southern gospel",
        "irish country",
        "instrumental post rock",
        "acid techno",
        "bouncy house",
        "brass band",
        "classic peruvian pop",
        "classic polish pop",
        "vintage swedish pop",
        "timba",
        "renaissance",
        "swiss rock",
        "norwegian gospel",
        "classic icelandic pop",
        "yugoslav rock",
        "dominican pop",
        "zouk",
        "neue deutsche welle",
        "perth indie",
        "arab folk",
        "southern soul blues",
        "sega",
        "deep melodic metalcore",
        "rio de la plata",
        "mod revival",
        "french folk pop",
        "native american",
        "pakistani pop",
        "c86",
        "deep christian rock",
        "deep soul house",
        "jazz bass",
        "swamp pop",
        "nordic folk",
        "college a cappella",
        "uk dub",
        "hauntology",
        "vienna indie",
        "polish reggae",
        "miami bass",
        "ambient idm",
        "digital hardcore",
        "girl group",
        "chanson quebecois",
        "hip hop quebecois",
        "deep neofolk",
        "catalan folk",
        "vintage french electronic",
        "brazilian composition",
        "modern uplift",
        "hip hop tuga",
        "bounce",
        "italian jazz",
        "desert blues",
        "samba-enredo",
        "croatian pop",
        "vocaloid",
        "garage punk",
        "vintage tango",
        "spanish folk",
        "hard minimal techno",
        "drumfunk",
        "german oi",
        "hiplife",
        "appalachian folk",
        "czech hip hop",
        "classical guitar",
        "mexican son",
        "vietnamese pop",
        "free improvisation",
        "balkan brass",
        "boogie-woogie",
        "morna",
        "serialism",
        "cante flamenco",
        "rosary",
        "riot grrrl",
        "electronica",
        "underground latin hip hop",
        "tico",
        "karneval",
        "tin pan alley",
        "deep soundtrack",
        "portuguese pop",
        "disco polo",
        "german show tunes",
        "harpsichord",
        "ecuadoria",
        "mbalax",
        "traditional rock 'n roll",
        "estonian pop",
        "polish indie",
        "kids dance party",
        "deep liquid",
        "full on",
        "thrash core",
        "outsider",
        "cyber metal",
        "metal guitar",
        "composition d",
        "kompa",
        "electropunk",
        "beats",
        "classic czech pop",
        "brutal deathcore",
        "jumpstyle",
        "new age piano",
        "stomp and whittle",
        "slovak hip hop",
        "heavy alternative",
        "finnish indie",
        "kwaito house",
        "witch house",
        "j-ambient",
        "makossa",
        "funk carioca",
        "gothic alternative",
        "atmospheric post rock",
        "zillertal",
        "qawwali",
        "latvian pop",
        "psych gaze",
        "classic venezuelan pop",
        "rva indie",
        "crust punk",
        "grunge pop",
        "blackgaze",
        "oshare kei",
        "irish indie",
        "orquesta tropical",
        "ghazal",
        "beatdown",
        "hungarian hip hop",
        "electro dub",
        "deep gothic post-punk",
        "denver indie",
        "deep rai",
        "traditional ska",
        "ethiopian pop",
        "world chill",
        "fake",
        "deep acoustic pop",
        "neo-rockabilly",
        "japanese psychedelic",
        "deep flow",
        "drone folk",
        "judaica",
        "dirty texas rap",
        "louisville indie",
        "neofolk",
        "canadian hip hop",
        "traditional british folk",
        "workout",
        "anarcho-punk",
        "swiss hip hop",
        "calypso",
        "orquesta tipica",
        "geek rock",
        "austrian hip hop",
        "guidance",
        "ragtime",
        "nwothm",
        "deep adult standards",
        "deep smooth jazz",
        "neo-synthpop",
        "blaskapelle",
        "dark black metal",
        "abstract",
        "deep dance pop",
        "classic french pop",
        "tone",
        "minimal melodic techno",
        "modern southern rock",
        "euroska",
        "kayokyoku",
        "nerdcore",
        "ukrainian rock",
        "ukulele",
        "lithumania",
        "kurdish folk",
        "new beat",
        "broken beat",
        "minimal wave",
        "zouglou",
        "k-rock",
        "acousmatic",
        "atmospheric post-metal",
        "lo star",
        "indie emo",
        "australian indie",
        "classic soundtrack",
        "marching band",
        "lounge house",
        "psychedelic blues-rock",
        "alternative americana",
        "semba",
        "darkstep",
        "solipsynthm",
        "underground power pop",
        "swedish prog",
        "nl folk",
        "vegan straight edge",
        "yoik",
        "crack rock steady",
        "musiikkia lapsille",
        "traditional swing",
        "schranz",
        "breakcore",
        "footwork",
        "chalga",
        "motivation",
        "slc indie",
        "classic dutch pop",
        "leeds indie",
        "didgeridoo",
        "deep contemporary country",
        "belgian indie",
        "indian classical",
        "danish indie",
        "funky breaks",
        "tribute",
        "classic afrobeat",
        "jazz brass",
        "dark hardcore",
        "electro trash",
        "black death",
        "japanese jazztronica",
        "corrosion",
        "gothic americana",
        "slavic metal",
        "deep brazilian pop",
        "scratch",
        "indie singer-songwriter",
        "garage punk blues",
        "deep german punk",
        "zydeco",
        "deep disco",
        "electronicore",
        "hebrew pop",
        "hindustani classical",
        "traditional scottish folk",
        "islamic recitation",
        "usbm",
        "beach music",
        "string folk",
        "spanish invasion",
        "luk thung",
        "south african jazz",
        "michigan indie",
        "deep orchestral",
        "russian alternative",
        "martial industrial",
        "enka",
        "porro",
        "dark ambient",
        "deep discofox",
        "fast melodic punk",
        "progressive alternative",
        "mallet",
        "ragga jungle",
        "kwaito",
        "spanish classical",
        "downtempo fusion",
        "ostrock",
        "monastic",
        "power violence",
        "deep melodic hard rock",
        "vapor house",
        "classic russian pop",
        "finnish hardcore",
        "neurostep",
        "deep psychobilly",
        "rebetiko",
        "musica per bambini",
        "abstract idm",
        "afrikaans",
        "string band",
        "panpipe",
        "romanian rock",
        "faroese pop",
        "ambient psychill",
        "ugandan pop",
        "concert piano",
        "library music",
        "russian folk",
        "bass trip",
        "power electronics",
        "french punk",
        "musique pour enfants",
        "hard house",
        "j-reggae",
        "norwegian jazz",
        "wind ensemble",
        "deep jazz guitar",
        "trash rock",
        "gospel reggae",
        "coupe decale",
        "neo metal",
        "persian traditional",
        "traditional soul",
        "deep liquid bass",
        "magyar",
        "italian progressive rock",
        "melodic progressive metal",
        "bossa nova jazz",
        "german ccm",
        "bay area hip hop",
        "deep opera",
        "greek indie",
        "japanoise",
        "manele",
        "galego",
        "classic schlager",
        "deep progressive trance",
        "deep ambient",
        "slam death metal",
        "chaotic black metal",
        "rap metalcore",
        "polyphony",
        "consort",
        "nz indie",
        "military band",
        "tekno",
        "dark psytrance",
        "indie fuzzpop",
        "shanty",
        "experimental psych",
        "italian folk",
        "jig and reel",
        "breton folk",
        "iskelma",
        "deep canadian indie",
        "tzadik",
        "armenian folk",
        "liturgical",
        "gamecore",
        "technical brutal death metal",
        "contemporary composition",
        "go-go",
        "deep folk metal",
        "neo-pagan",
        "speedcore",
        "depressive black metal",
        "harp",
        "ambient fusion",
        "bulgarian rock",
        "remix",
        "pipe band",
        "funeral doom",
        "accordion",
        "skinhead reggae",
        "spoken word",
        "future ambient",
        "minimal dubstep",
        "deep sunset lounge",
        "danish jazz",
        "j-core",
        "klezmer",
        "deep soft rock",
        "deep german indie",
        "screamocore",
        "flick hop",
        "nepali",
        "corsican folk",
        "indorock",
        "vintage chanson",
        "bemani",
        "greek house",
        "indie shoegaze",
        "doujin",
        "punta",
        "kuduro",
        "college marching band",
        "neo-industrial rock",
        "barbershop",
        "greek hip hop",
        "screamo punk",
        "benga",
        "jazz orchestra",
        "west african jazz",
        "ghettotech",
        "blues-rock guitar",
        "dallas indie",
        "deep happy hardcore",
        "stl indie",
        "mantra",
        "african percussion",
        "british dance band",
        "brass ensemble",
        "guitar case",
        "hard glam",
        "outer hip hop",
        "throat singing",
        "deep darkpsy",
        "triangle indie",
        "geek folk",
        "cumbia funk",
        "swedish pop punk",
        "sinhala",
        "thrash-groove metal",
        "carnatic",
        "indie pop rock",
        "jug band",
        "unblack metal",
        "power noise",
        "italian punk",
        "deep vocal jazz",
        "deep deep house",
        "dark minimal techno",
        "cornetas y tambores",
        "chinese traditional",
        "commons",
        "halloween",
        "finnish jazz",
        "byzantine",
        "chinese indie rock",
        "capoeira",
        "contemporary folk",
        "black sludge",
        "zim",
        "post-disco soul",
        "drama",
        "gospel blues",
        "light music",
        "breaks",
        "deep new wave",
        "abstractro",
        "deep psytrance",
        "vintage jazz",
        "dubsteppe",
        "street punk",
        "british brass band",
        "noise punk",
        "traditional funk",
        "northern irish indie",
        "deep indie singer-songwriter",
        "deep southern soul",
        "deep indie rock",
        "mexican traditional",
        "gothic post-punk",
        "cajun",
        "baroque ensemble",
        "heavy gothic rock",
        "covertrance",
        "deep downtempo fusion",
        "polish jazz",
        "deep ragga",
        "deep vocal house",
        "bangla",
        "japanese traditional",
        "demoscene",
        "c64",
        "musique concrete",
        "classical organ",
        "makina",
        "classical flute",
        "polka",
        "spytrack",
        "deep freestyle",
        "grim death metal",
        "deep full on",
        "electroacoustic improvisation",
        "muziek voor kinderen",
        "fallen angel",
        "skiffle",
        "poetry",
        "classic eurovision",
        "chamber choir",
        "slash punk",
        "deep jazz fusion",
        "deep funk house",
        "steelpan",
        "grisly death metal",
        "belorush",
        "fussball",
        "spanish indie rock",
        "sunset lounge",
        "early music ensemble",
        "oratory",
        "deep east coast hip hop",
        "traditional reggae",
        "indian rock",
        "deep melodic death metal",
        "deep progressive house",
        "contemporary classical",
        "deep jazz piano",
        "punk ska",
        "lowercase",
        "hardcore breaks",
        "skinhead oi",
        "clarinet",
        "glitch beats",
        "traditional rockabilly",
        "deep indie pop",
        "deep nordic folk",
        "deep pop emo",
        "neo soul-jazz",
        "deep classic garage rock",
        "vintage swing",
        "villancicos",
        "hatecore",
        "deep swedish rock",
        "deep filthstep",
        "deep hardcore",
        "klapa",
        "soda pop",
        "deep chill-out",
        "football",
        "organic ambient",
        "wrock",
        "crossover prog",
        "gamelan",
        "experimental dubstep",
        "deep northern soul",
        "raw black metal",
        "norwegian punk",
        "deep surf music",
        "classic psychedelic rock",
        "thai indie",
        "dubstep product",
        "deep free jazz",
        "slovenian rock",
        "deep thrash metal",
        "maghreb",
        "ambient dub techno",
        "goa trance",
        "accordeon",
        "deep g funk",
        "deep italo disco",
        "charred death",
        "re:techno",
        "dark progressive house",
        "tanzlmusi",
        "hard stoner rock",
        "deep dub techno",
        "noise",
        "neo honky tonk",
        "j-punk",
        "malagasy folk",
        "chill groove",
        "zeuhl",
        "kc indie",
        "deep power-pop punk",
        "deep punk rock",
        "j-poppunk",
        "tibetan",
        "deep motown",
        "deep nz indie",
        "new jack smooth",
        "deep space rock",
        "italo beats",
        "chill-out trance",
        "deep eurodance",
        "doomcore",
        "terrorcore",
        "twin cities indie",
        "vintage rockabilly",
        "chinese opera",
        "alternative metalcore",
        "german street punk",
        "deep cello",
        "glitter trance",
        "jangle rock",
        "ceilidh",
        "skweee",
        "alternative hardcore",
        "bulgarian folk",
        "nu electro",
        "french folk",
        "deep classical piano",
        "indie emo rock",
        "deep hardcore punk",
        "ethereal gothic",
        "ghoststep",
        "swedish jazz orkester",
        "jazz composition",
        "deep neo-synthpop",
        "rhythm and boogie",
        "modern downshift",
        "anime cv",
        "chinese experimental",
        "vintage schlager",
        "song poem",
        "modern free jazz",
        "cryptic black metal",
        "cinematic dubstep",
        "vintage gospel",
        "neo-traditional country",
        "gothic doom",
        "deep orgcore",
        "vintage country folk",
        "deep delta blues",
        "chip hop",
        "deep german jazz",
        "deep symphonic black metal",
        "twee indie pop",
        "saxophone",
        "caucasian folk",
        "dark electro-industrial",
        "deep breakcore",
        "vintage reggae",
        "necrogrind",
        "deep latin jazz",
        "drone psych",
        "vintage swoon",
        "smooth urban r&b",
        "vintage western",
        "rock noise",
        "central asian folk",
        "deep string quartet",
        "deep deep tech house"
    ];

    $('#search-field').autocomplete({
        source: tags
    });
});