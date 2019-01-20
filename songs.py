# The following RTTTL tunes were extracted from the following:
# https://github.com/onebeartoe/media-players/blob/master/pi-ezo/src/main/java/org/onebeartoe/media/piezo/ports/rtttl/BuiltInSongs.java
# most of which originated from here:
# http://www.picaxe.com/RTTTL-Ringtones-for-Tune-Command/
#
# Keep in mind: The ESP8266's max PWM freq is around 1kHz

SONGS = [
    'supermario:d=4, o=4, b=125:a, 8f., 16c, 16d, 16f, 16p, f, 16d, 16c, 16p, 16f, 16p, 16f, 16p, 8c5, 8a., g, 16c, a, 8f., 16c, 16d, 16f, 16p, f, 16d, 16c, 16p, 16f, 16p, 16a#, 16a, 16g, 2f, 16p, 8a., 8f., 8c, 8a., f, 16g#, 16f, 16c, 16p, 8g#., 2g, 8a., 8f., 8c, 8a., f, 16g#, 16f, 8c, 2c5',
    'Super Mario - Title Music:d=4,o=4,b=125:8d5,8d5,8d5,8d,8d5,8d5,8d5,8d,2d#5,8d5,p,32p,8d,8b,8b,8b,8d,8b,8b,8b,8d,8b,8b,8b,16b,16c5,b,8a,8d,8a,8a,8a,8d,8a,8a,8a,8d,8a,8a,8a,16a,16b,a,8g,8d,8b,8b,8b,8d,8b,8b,8b,8d,8b,8b,8b,16a,16b,c5,e5,8d5,8d5,8d5,8d,8c5,8c5,8c5,8f#,2g',
    'SMBtheme:d=4,o=4,b=100:16e5,16e5,32p,8e5,16c5,8e5,8g5,8p,8g,8p,8c5,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e5,16g5,8a5,16f5,8g5,8e5,16c5,16d5,8b,16p,8c5,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e5,16g5,8a5,16f5,8g5,8e5,16c5,16d5,8b,8p,16g5,16f#5,16f5,16d#5,16p,16e5,16p,16g#,16a,16c5,16p,16a,16c5,16d5,8p,16g5,16f#5,16f5,16d#5,16p,16e5,16p,16c6,16p,16c6,16c6,p,16g5,16f#5,16f5,16d#5,16p,16e5,16p,16g#,16a,16c5,16p,16a,16c5,16d5,8p,16d#5,8p,16d5,8p,16c5',
    'SMBwater:d=8,o=5,b=225:4d4,4e4,4f#4,4g4,4a4,4a#4,b4,b4,b4,p,b4,p,2b4,p,g4,2e.,2d#.,2e.,p,g4,a4,b4,c,d,2e.,2d#,4f,2e.,2p,p,g4,2d.,2c#.,2d.,p,g4,a4,b4,c,c#,2d.,2g4,4f,2e.,2p,p,g4,2g.,2g.,2g.,4g,4a,p,g,2f.,2f.,2f.,4f,4g,p,f,2e.,4a4,4b4,4f,e,e,4e.,b4,2c.',
    'SMBunderground:d=16,o=5,b=100:c,c4,a4,a,a#4,a#,2p,8p,c,c4,a4,a,a#4,a#,2p,8p,f4,f,d4,d,d#4,d#,2p,8p,f4,f,d4,d,d#4,d#,2p,32d#,d,32c#,c,p,d#,p,d,p,g#4,p,g4,p,c#,p,32c,f#,32f,32e,a#,32a,g#,32p,d#,b4,32p,a#4,32p,a4,g#4',
    'The Simpsons:d=4,o=4,b=160:c.5,e5,f#5,8a5,g.5,e5,c5,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c5,8c5,8c5,c5',
    'Indiana:d=4,o=4,b=250:e,8p,8f,8g,8p,1c5,8p.,d,8p,8e,1f,p.,g,8p,8a,8b,8p,1f5,p,a,8p,8b,2c5,2d5,2e5,e,8p,8f,8g,8p,1c5,p,d5,8p,8e5,1f.5,g,8p,8g,e.5,8p,d5,8p,8g,e.5,8p,d5,8p,8g,f.5,8p,e5,8p,8d5,2c5',
    'TakeOnMe:d=4,o=4,b=160:8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5,8f#5,8e5,8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5',
    'Cantina:d=4,o=4,b=250:8a,8p,8d5,8p,8a,8p,8d5,8p,8a,8d5,8p,8a,8p,8g#,a,8a,8g#,8a,g,8f#,8g,8f#,f.,8d.,16p,p.,8a,8p,8d5,8p,8a,8p,8d5,8p,8a,8d5,8p,8a,8p,8g#,8a,8p,8g,8p,g.,8f#,8g,8p,8c5,a#,a,g',
    'Entertainer:d=4,o=4,b=140:8d,8d#,8e,c5,8e,c5,8e,2c.5,8c5,8d5,8d#5,8e5,8c5,8d5,e5,8b,d5,2c5,p,8d,8d#,8e,c5,8e,c5,8e,2c.5,8p,8a,8g,8f#,8a,8c5,e5,8d5,8c5,8a,2d5',
    'McGyver:d=4,o=4,b=160:8c5,8c5,8c5,8c5,2b,8f#,a,2g,8c5,c5,b,8a,8b,8a,g,e5,2a,b.,8p,8c5,8b,8a,c5,8b,8a,d5,8c5,8b,d5,8c5,8b,e5,8d5,8e5,f#5,b,1g5,8p,8g5,8e5,8c5,8f#5,8d5,8b,8e5,8c5,8a,8d5,8b,8g,c5,b,8c5,8b,8a,8g,a#,a,8g.',
    'StarWars:d=4,o=4,b=45:32p,32f#,32f#,32f#,8b.,8f#.5,32e5,32d#5,32c#5,8b.5,16f#.5,32e5,32d#5,32c#5,8b.5,16f#.5,32e5,32d#5,32e5,8c#.5,32f#,32f#,32f#,8b.,8f#.5,32e5,32d#5,32c#5,8b.5,16f#.5,32e5,32d#5,32c#5,8b.5,16f#.5,32e5,32d#5,32e5,8c#5',
    'TopGun:d=4,o=4,b=31:32p,16c#,16g#,16g#,32f#,32f,32f#,32f,16d#,16d#,32c#,32d#,16f,32d#,32f,16f#,32f,32c#,16f,d#,16c#,16g#,16g#,32f#,32f,32f#,32f,16d#,16d#,32c#,32d#,16f,32d#,32f,16f#,32f,32c#,g#',
    'A-Team:d=4,o=4,b=125:8f.5,16f5,8c5,2f5,8p,8a#,c5,2f,16a#,16c5,8f5,8c5,8g5,2f5,8p,8d#.5,16d5,16c5,a#,2c5,8f.5,16f5,8c5,2f5,8p,8a,a#,8c5,2f,8a#,8a,8p,8f,a#,a,a#,a,8f,g.,f,c5,a#,d#5,2f5,8f',
    'Smurfs:d=32,o=4,b=200:4c#5,16p,4f#5,p,16c#5,p,8d#5,p,8b,p,4g#,16p,4c#5,p,16a#,p,8f#,p,8a#,p,4g#,4p,g#,p,a#,p,b,p,c5,p,4c#5,16p,4f#5,p,16c#5,p,8d#5,p,8b,p,4g#,16p,4c#5,p,16a#,p,8b,p,8f,p,4f#',
    'starwars2:d=4,o=4,b=225:2c,1f,2g.,8g#,8a#,1g#,2c.,c,2f.,g,g#,c,8g#.,8c.,8c5,1a#.,2c,2f.,g,g#.,8f,c.5,8g#,1f5,2f,8g#.,8g.,8f,2c5,8c.5,8g#.,8f,2c,8c.,8c.,8c,2f,8f.,8f.,8f,2f',
    'ImperialMarch:d=4,o=5,b=112:8d.,16p,8d.,16p,8d.,16p,8a#4,16p,16f,8d.,16p,8a#4,16p,16f,d.,8p,8a.,16p,8a.,16p,8a.,16p,8a#,16p,16f,8c#.,16p,8a#4,16p,16f,d.,8p,8d.6,16p,8d,16p,16d,8d6,8p,8c#6,16p,16c6,16b,16a#,8b,8p,16d#,16p,8g#,8p,8g,16p,16f#,16f,16e,8f,8p,16a#4,16p,2c#',
    'MissionImp:d=16,o=5,b=95:32d,32d#,32d,32d#,32d,32d#,32d,32d#,32d,32d,32d#,32e,32f,32f#,32g,g,8p,g,8p,a#,p,c6,p,g,8p,g,8p,f,p,f#,p,g,8p,g,8p,a#,p,c6,p,g,8p,g,8p,f,p,f#,p,a#,g,2d,32p,a#,g,2c#,32p,a#,g,2c,a#4,8c,2p,32p,a#4,g4,2f#,32p,a#4,g4,2f,32p,a#4,g4,2e,d#,8d',
    'ItchyScratchy:d=4,o=4,b=160:8c5,8a,p,8c5,8a5,p,8c5,8a,8c5,8a,8c5,8a5,p,8p,8c5,8d5,8e5,8p,8e5,8f5,8g5,p,8d5,8c5,d5,8f5,a#5,a5,c6',
    'forest:d=4,o=5,b=120:8f4,8a4,b4,8f4,8a4,b4,8f4,8a4,8b4,8e,d,8b4,8c,8b4,8g4,2e4,8p,8d4,8e4,8g4,2e4,8p,8d4,8e4,f4,8g4,8a4,b4,8c,8b4,e4,8p,8d4,8e4,f4,8g4,8a4,b4,16c,16b4,16c,e,8p,8d4,8c4,8f4,8e4,8g4,8f4,8a4,8g4,16a4,16h4,16a4,16g4,2a4',
    '1up:d=16,o=5,b=180:e.,g.,e.,c.,d.,g.',
    'closed:d=32,o=4,b=160:e.,c.,d.,g.'

]


def find(name):
    for song in SONGS:
        song_name = song.split(':')[0]
        if song_name == name:
            return song
