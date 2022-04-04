#    ____  _________    ____     _____ ___    __  _____  ______  ___    ____
#   / __ )/ ____/   |  / __ \   / ___//   |  /  |/  / / / / __ \/   |  /  _/
#  / __  / __/ / /| | / /_/ /   \__ \/ /| | / /|_/ / / / / /_/ / /| |  / /
# / /_/ / /___/ ___ |/ _, _/   ___/ / ___ |/ /  / / /_/ / _, _/ ___ |_/ /
# /_____/_____/_/  |_/_/ |_|   /____/_/  |_/_/  /_/\____/_/ |_/_/  |_/___/
# By: Alex Slowik
# Made 2020
# Features: Multiple rooms, two skills and attacks that scale off different stats, die based success chance, turn based combat, animated start screen.
# Startup---------------------------------------------------------------------------------------------------------------#

import os  # OS for clear screen time for sleep
import time
import random

os.system('mode con cols=400 lines 40')  # set cmd window size
os.system('cls')  # clear screen

# Dialog/System---------------------------------------------------------------------------------------------------------#

intro_message1 = 'Long ago in a distant land, I Vox, the shape-shifting master of the deep, unleashed my legions of horrors. \n' \
                 'But a foolish bear wielding his ancestral family sword stepped forth to oppose me.\n\n' \
                 'Right as he readied his sword for the killing blow, I tore a portal in time.\n' \
                 'I flung him into the future where the deep ones roam the land and obey my rule as law.\n\n' \
                 'Now the foolish bear seeks to return to his past and undo the future that is VOX.'

tutorial_prompt = 'Have you played BEAR SAMURAI before? Please answer yes or no.'

tutorial_text = 'You are equal parts BEAR and SAMURAI.\n\n' \
                'You will roll a six die sided for all checks and will always go first in combat. \nYou have two stats:\n' \
                'BEAR and SAMURAI.\n' \
                'BEAR reflects your health. SAMURAI reflects your combat and poetry skills. There will be no time for poetry.\n\n' \
                'You have two skills, hopefully you can guess that they are:\n' \
                'BEAR and SAMURAI.\n' \
                'BEAR will allow you to tackle problems, sometimes literally, with your bear instincts and features.\n' \
                'BEAR scales off your max HP. \n\n' \
                'SAMURAI will allow you to solve problems with your Samurai skills.\n' \
                'SAMURAI scales off of damage.\n\n' \
                'Good luck samurai, may the salmon be fresh and the honey sticky. \n\n\n'

# Global-game-variables--------------------------------------------------------------------------------------------------#
die_result = int(0)  # player die result
foe_die_result = int(0)  # enemy die results
victory = int(0)  # Flips when the player wins
easter_egg = int(0)  # Flips when the player finds the easter egg
key_code = int(0)
key_card = int(0)
bee_puzzle_complete = int(0)
has_shield = int(0)
reception_clear = int(0)
hive_clear = int(0)
reactor_clear = int(0)
armory_clear = int(0)
training_clear = int(0)
lab_clear = int(0)
admin_clear = int(0)
elevator_clear = int(0)
boss_clear = int(0)
vox_alive = int(1)
# Room-descriptions-----------------------------------------------------------------------------------------------------#

wasteland_des = 'Your eyes slowly open adjusting to the harsh green light of the future.You lie face down in a pool of brown tepid water feeling numb and disoriented.\n' \
                'Being thrown into the future is not a pleasant experience, even for a creature such as yourself. \n' \
                'As your eyes adjust you find yourself on the outskirts of a dystopian city nothing like your hometown. \n' \
                'The small town you were raised in is gone. The calm, crisp, clear air  has been replaced with a heavy. \n' \
                'yellow-brown swirling fog. Grass has been replaced with dead slimy earth. No longer do groves of trees dot the landscape. \n' \
                'Instead towering hunks of metal covered in dimly glowing neon jut from the earth, tall enough to pierce the smog \n' \
                'North of you see one building rise above the rest, piercing straight upwards as if to proclaim its mastery over the terrain \n' \
                'In brightly glowing golden neon lettering you see your hated foes name emblazoned down the side. VOX will pay for this!\n' \
                'You slowly shake off the tingling numbness brought on by the portal you were thrown through and stagger to your paws to face the wasteland\n'

gate_des1 = 'As you trudge through the wasteland you find that VOX\'s tower is deceptively far away. Due to its massive size it constantly seems to be just around the corner\n' \
            'The slimy path becomes more of a structured road made of deep tread marks, as if something massive and heavy has passed through many times. You find the occasional\n' \
            'footprint though none are from any creature you recognize. Some are small and webbed, others massive and deep.\n\n' \
            '\"I must reach VOX before I run into whatever made those prints\" you mutter to yourself.\n\n' \
            'You start to become aware of the fact that you have been completely alone on your journey along this road to the city. The fog, at first, felt like an ally to shield you\n' \
            'from prying eyes. As you walk it starts to feel more menacing. The fur on the back of your neck tingles and stands up. You feel as if you are being watched.\n' \
            'You spin around and brandish your sword and snarl.\n'

gate_des2 = 'Nothing. Nothing is there. The mists swirl and drift but nothing appears. You sheath your sword and pull your tattered robe a bit tighter around you.\n\n' \
            '\"It\'s official, I hate this damn fog\"\n\n' \
            'The road dips down a hill deeper into the sickly cloying fog. Obscuring what little vision you had of the city ahead. You are completely immersed in the dank fog now.\n' \
            'You only have the road under your feet and the cutting golden glow of the word VOX to guide you towards your objective. You start to hear a low humming that shakes the\n' \
            'ground. It is coming from in front of you but does not change as you get closer. Suddenly you pass a threshold and the mist is gone. In front of you is a softly glimmering\n' \
            'shield wall around the city. It holds the mists at bay and as you get close some static stands your fur on end. You reach out to touch the wall and find it is cool and soft.\n' \
            'You push through the shield. The shield itself offers a slight resistance but you pass though.  '

gate_des3 = 'The act of passing though the shield is like the flipping of a switch. Abruptly every one of your senses is hit with the environment of the futuristic city in front of you. \n' \
            'Bee shaped drones swarm and buzz from tower to tower. Entering though different glowing hexagonal shaped entryways dotted along the smaller towers. You notice \n' \
            'that the main swarm seems to be coming from VOX\'s tower. The streets are paved and shop fronts with items on display crowd the streets. As do many creatures. Capes and \n' \
            'hooded robes seem to be in fashion and no one pays you any mind as you make your way through the stalls towards the central spire and towards your hated enemy. Walking \n' \
            'through the stalls is almost familiar. In your time there was less neon to be sure, but the street vendors hawking their wares and the hum of a busy city feels distinctly \n' \
            'more like home than the mists. None of the items in the stalls are familiar in the slightest. Some with glowing screens and characters you don\'t recognise, some that \n' \
            'you do. Perhaps the marks of a craftsman, you wonder to yourself idly. The smell of cooking food draws your attention. It is the first pleasant thing you have noticed \n' \
            'since arriving in the future. You continue through an alley packed by street food vendors, taking note of the food for sale. Some look and smell very tasty but you do not stop \n' \
            'Hunger can wait and you do not want to be recognised. '

gate_des4 = 'All of a sudden the buildings stop. You have arrived. The tower of VOX is before you. Its walls are jet black and smooth. It rises directly up in a massive spire\n' \
            'There are no stalls or street vendors here. The ground around the building in 100 paces in every direction is covered in an exquisite mosaic depicting the conquests \n' \
            'of VOX. You see depictions of bees being enslaved and forced to take on cybernetic enhancements to act as VOX\'s worker class. You walk clockwise around the base of the \n' \
            'tower. As you do the depictions change, you see salmon being imbued with vox\'s vile magic granting them enhanced consciousness and forming a pact. You continue to \n' \
            'circle the building. Dread and horror fills your soul as you see the final piece of the mosaic come into view. The annihilation of the bears and VOX\'s victory over\n' \
            'the world. You see your town burning, your temple pillaged, your own home desecrated, and your people slain to the very last soul. You have no doubt you are the last\n' \
            'of your kind in this place. The great sadness in your heart is overwhelmed by anger. In front you there is a great humming teal laser shield blocking the only entrance\n' \
            'to VOX\'s tower. Jutting from each side there is a small gate house. You set paw onto the mosaic to approach the gate. The moment you do the tower springs to life. \n' \
            'Red flood lights flip out of the wall with a loud clank bathing you in their light and a klaxon begins wailing and a voice booms \"BEAR DETECTED\" on repeat. To your \n' \
            'dismay two glowing orange multi-barreled mini-guns drop their laser sights onto your chest and with a high pitch whirring begin to spin up.\n\n'

reception_des = 'As you enter VOX\'s tower the laser gate snaps back to life. What you see before you is the horrifying splendor of VOX\'s Tower. The entire room is made of \n' \
                'black marble with gold and red streaks. The ceiling is hundreds of feet above you and there is one walkway with a white carpet on it that leads to a single desk.\n' \
                'Hanging from the ceiling are massive gold chandeliers made to look like circles of concentric light. They move and sway hanging on golden threads of energy that slowly ripple\n' \
                'down from the ceiling. As your attention wanders from the trappings of luxury you see heads mounted to the wall like hunting trophies. Bear heads. Your stomach sinks as you recognise\n' \
                'your Master. As you stare into his lifeless eyes, you hear his voice in your head {Do not stop to mourn me, find VOX and defeat him}. In the south of the room there is a giant elevator labeled\n' \
                '\"PENTHOUSE\" There is one door on either side. The east door is labeled \"armory\" while the west door is labeled \"hive\"\n'

hive_des = 'You walk through the door into the hive. In this massive room is a beehive of epic proportions, the walls dotted with massive honeycombs. It must contain millions of cow sized bees.\n' \
           'There are glass tubes everywhere. They criss-cross the room all pumping the golden honey that VOX uses to power his technology.  In the center of the room there is an open pit\n' \
           'with a small metal walkway that leads to a platform in the center. The pit goes down as far as the eye can see. As far as you can tell it is bottomless. The platform has\n' \
           'a key card suspended in a golden glowing field. Standing by the key card behind the force field you see a robotic beekeeper. They seem to be using a long staff to control the\n' \
           'bee population around them. One of these bees flies near enough for you to get a good look. You notice that the bees all have cybernetic implants that flash and change colors\n' \
           'according to the will of the beekeeper bot. The BeeBot has not noticed your entry into the hive and neither has the keeper. It seems that they are preoccupied with making honey.\n'

armory_des = 'You enter the armory, the room is covered in locked racks of unfamiliar weapons. Some of them resemble smaller hand held versions of the turrets from outside. Others appear to\n' \
             'be defensive in nature. Others defy your best guess at their purpose. They curl and shift; as you watch them the weapons watch you back. You break your gaze reflexively\n' \
             'and look around the room. Gone is the splendor of the entryway with its marble and grotesque trophies, instead you find this room is more utilitarian. Its lights embedded\n' \
             'in the ceiling, glowing a cool blueish white. The columns and floor are made of simple concrete. You walk up to touch one and it blinks.\n'\
              '\" Wait... What?! That column blinked at me\" You turn on your heel to face the blinking column.\n'\
             'Along the back wall of the room there is a closet labeled, \" Bear Armor \". Very lucky for you. To the west is \"reception\" to the south there is a door labeled \"lab\"\n' \

armory_victory = 'With that final strike the last of the salmon lay on the floor. The cybernetic augmentations lay fractured and sparking.' \



elevator_des = 'You plug in the usb containing the keycode into the pad next to the elevator door. The screen flashes to life and says \"1234567890...password accepted, your password change\n' \
               'is 1142 days overdue. Please swipe card to confirm two factor identification.\" You do and the doors slide open and inside is a marble covered room. Funny, it seems so small. The room is\n' \
               'filled with mirrors and softly pulsing teal lights. You do not see any other doors, strange. You cross the threshold and the door dings and softly closes behind you. You half \n' \
               'expected more robot assassins or a laser turret to pop out. You smell food, and track the smell to a little cabinet recessed into the wall. As you reach towards the cabinet\n' \
               'the doors gracefully slide out of the way of your paw. Inside is some honey glazed trail mix and a small platter of soy glazed sashimi. Finally some good food. Your health is set \n' \
               'back to full. You reach over and push the large button on the screen by the door labeled VOX\'S PENTHOUSE. ' \


bossroom_des = '(TBD)'  # Location description

bee_puzzle_failure = 'You look on with grim determination as one of the spires on the outskirts of the spire explodes though a monitor labeled QUEEN CONTAINMENT.\n' \
                     'You have done your best to save the Queen, but you have failed. You can no longer give her the justice she deserved after her long years of \n' \
                     'enslavement under VOX\'s rule. Now you will have to offer her spirit the only option you have left. You will offer her brood vengeance and \n' \
                     'VOX\'s head.'

bee_puzzle_success = 'You have successfully stopped the meltdown. The Queen will live, as will her brood. The restarting of the reactor caused the power to flicker for\n' \
                     'just a moment. The emergency weapons closet in the corner of the room swung open when the power turned back on. \n' \

guard_victory = 'The robot takes a step too close while swinging its sword in a wide flat arc in front of itself. This is the moment you have been waiting for. You take a deep breath and prepare\n' \
                'You compress your knees while falling forward as you get close to the ground you dig your claws into the ground and leap forward swinging your sword in a twisting motion.\n' \
                'The attack comes to a close as you lightly land on your paws behind the robot and sheathe your sword slowly. The bifurcated robot holds together for a moment before each half goes its\n' \
                'separate way.\n\n' \
                'You have made it into VOX\'s tower. Congratulations Samurai. You may now pick your own path. \n' \
                'To move you will use the cardinal directions, north east south and west.\n'

bear_armor = 'You walk to the closet labeled \"Bear Armor\". Upon opening it you see the most impressive set of armor you have ever laid eyes on. It has the familiar hallmarks of a suit of samurai armor\n' \
             'The helmet features a large golden arrowhead pointing down to accentuate your brow. Each intricate piece of armor fits together with interlocking tiny energy projectors. Together they\n' \
             'create scales along the chest, arms and legs. The armor is adorned in purple fiber optic tassels. A note is taped to it. You fold open the note it reads: \" This suit of experimental armor uses\n' \
             'experimental microshield technology to absorb impacts and deflect laser blasts. The unique nanofibers will conform to the users size. I have chose to style it after the foolish bear\'s ancient Gusoku armor.\n' \
             'VOX will be pleased to wear it. The armor will remind the populace of VOX\'s complete conquering of the known world!\n' \
             'You smile to yourself. You will use this tool against its creator. Hubris will be VOX\'s downfall. HP + 5, BEAR +1'

no_elevator_access = 'You walk up to the door labeled penthouse. The door has no knobs or handles. Just a smooth surface with a line down the middle. You notice a keypad next to the door. The keypad\n' \
                     'lights up and prompts you for a password. You try some random guesses to no avail. What would a monster such as this use as a password you wonder to yourself. ' \



hive_bear = 'Time to tackle your problems head on. You charge with every ounce of swiftness you can muster. The swarm director has nowhere to go, there is nothing it can do to escape its impending doom!\n' \
            'Even so in one final act of defiance it throws its robotic staff down and activates its gauntlets. They begin to crackle and tiny streams of electricity begin to leap to the metal floors \n' \
            'and railings. You grab the swarm director and raise it over your head, all the while being hit with the robot\'s lightning. You roar and carry it over to the edge of the metal platform and \n' \
            'heave it over the edge. It falls out of sight while lightning arcs all around. A beat passes after the robot passes out of sight down the hole. Then suddenly you are hit with concussive force.\n' \
            'a blast echoes down below and a klaxon begins to wail. \" OBJECT DETECTED IN COOLANT PUMP ONE, REACTOR CRITICAL \" You scan the room and see a sign to the south of you labeled \"reactor\"\n '\

hive_samurai = 'You take a moment to consider your surroundings while you are undetected. You begin to notice that the bees move to and fro around the room rhythmically. Often passing quite close to the robot\n' \
               'directing the swarm. You decide to use the timing of the bees to sneak up along the metal ramp that leads to the center platform. You keep a count in your head and quickly run from one \n' \
               'bee obstructing the swarm directors vision to the next. You cross the bridge in no time and have successfully made it behind the robot. You swiftly kick it towards a railing and\n' \
               'draw your sword immediately into a forward slice. You manage to cut the robot in half before it reaches the railing and both halves fly down the shaft. A beat passes after the robot falls out of sight \n' \
               'down the hole. Then suddenly you are hit with a concussive blast. The blast echoes down from down below and a klaxon beings to wail.\n' \
                ' \" OBJECT DETECTED IN COOLANT PUMP ONE, REACTOR CRITICAL \"\n You scan the room and see a sign to the south of you labeled \"reactor\"'\

reactor_des = 'You sprint into the reactor room, warnings continue to blare from the intercom. Incessantly informing you of the ever increasing disarray in the the reactor. You smash through the door  \n' \
              'throwing it off its hinges. The spinning door soars through the air in a graceful arc directly into the robot tending to the reactor. The room is small and covered in monitors\n' \
              'all of which look out over different parts of the city. There is a map on a large screen to your left. It seems that the reactor isn\'t in the same building you are. Instead you see that it \n'  \
              'is located in a building labeled \"Vertical Bee Pastures\" and \"Queen Bee Dormitories\". You push the robot and door mess that was made by your entrance off the console. A screen pops up and \n' \
              'says \" DRONES HAVE COMPLETED BLOCKAGE REMOVAL. RODS STILL HOT, RUNAWAY HAS STARTED. BEGIN MANUAL ROD REMOVAL. \" The screen disappears and you are left with a diagram of the reactor and each rod group\n' \
              'with its own number. '

training_des1 = 'You walk through the doorway into a dark two meter wide hallway. There are no overhead lights and the stone walls are slick with condensation and mold. The only lights are ankle high bars\n' \
                'of low power green neon lights. They bathe the hallway in a steady silent green glow. You continue to walk and the hallway does not end. You squint and peer into the darkness. Try as \n' \
                'you might you can not see far enough through the darkness. You carry onwards down the gentle decline of the perfectly straight hallway.  The light gets dimmer and dimmer until you are \n' \
                'alone in the darkness. You carry on, pressing forward for some time deeper into the darkness. It is completely black when suddenly:'

training_des_exit = 'You carry on. The floor slowly sloping downwards is illuminated by the same green neon that lit your path on the way in. After a short time you notice the corridor starting to turn. \n' \
                    'As you continue to walk the path keeps a smooth right turn, as you continue down you find yourself  still turning to the right going downhill and spot a single red neon tube.\n' \
                    'Curious, you bend down to examine it. This one tube is covered in strange symbols you do not understand.\n' \
                    'You continue to walk, padding softly down the corridor when ahead of you appears another red light. You continue to walk. After about the same interval appears a red light. Out of the \n' \
                    'corner of your eye you spot three long dark claw marks that have dug ragged shallow trenches in the wall by the light. Whatever made those marks was able to dig into concrete. Odd, you think to yourself.\n' \
                    'You continue deeper and like clockwork there comes another red light. You peer down and notice four marks this time and another one on the ground as long as the corridor is wide. You feel a wave of \n' \
                    'dread shoot down your body. The first three claw marks look exactly like the three from the last light. You turn around and double back to check the previous lights to see if you can find some \n' \
                    'significance in them. You turn around and take a step downwards and to the left.\n\n' \
                    '\"What is this?\" you mutter to yourself intensely disorientated.\n\n' \
                    'You take a few more steps and still find yourself heading down and to the left. You sprint and just like clockwork there is another red light. You look for the three claw marks and to your horror you\n' \
                    'find five. Five marks on the light behind you. You slash an arrow above the five marks to indicate the direction back the way you came.\n\n' \
                    '\"What insanity is this, next light I will make a similar mark\"\n\n' \
                    'You turn around feel panic rising in your chest and immediate paranoia sets in when you find yourself staring down a corridor that runs down and to the left.  You turn around back to face where you were looking.\n' \
                    'Sure enough it turns down and to the left. No matter which way you walk by the light you find yourself facing down and to the left. You head away from the light as suddenly this empty corridor starts\n' \
                    'to feel incredibly confining. You hurriedly head forward until you find another red light complete with your own arrow facing back at you the way you came. This time it has seven ghastly gouges.\n' \
                    'You feel eyes looking at your back, you spin around to confront them only for the feeling to get more intense. You hear something behind you faintly in the distance scrape slowly and grittily along the wall.\n' \
                    'a distant scraping begins and starts to draw closer. You turn back and forth unable to get the sound out from behind you. You sprint and hear a horrible screeching roar and bellow. It sounds as if \n' \
                    'death itself opened its maw somewhere behind you. You spring away back where you came as fast as you can. Suddenly the lights turn off and a glowing red door appears in front of you. The skittering and scraping\n'\
                    'growing louder and louder. You sprint for the glowing red door and yank it open running inside and slamming it shut. ' \


lab_choice_bear = 'You roar and rip the book to pieces. It catches on fire and bursts into the blue and purple flames that flow like blood out of the book. It splashes down onto the table spilling off the edges and setting the curtains ablaze.\n' \
                  'This does nothing to assuage your fears. Instead you find rage and panic spreading through your body and you lash out. You gouge deep cuts with your claws into the pipes over your head. It sprays hot wet liquid right back \n' \
                  'at you causing you to stumble backwards. You bump into something behind you and it startles you yet again. Your wild bear instincts kick in bringing you back to a savage level, you turn around and throw your huge bulk into the\n' \
                  'shelves. A knife flies out though the air and stabs you in the leg. The pain of the knife stuck in your leg causes you to tumble over the shelves and into the ritual circle in the center of the room. You slide across the tiles \n' \
                  'leaving a scraggly red line across the circle until you stop at the foot of the pedestal in the middle. The markings that make up the runes and structural lines of the circle begin to glow...black. You pull the knife from your leg and\n ' \
                  'take a moment to examine it. The hilt is made of an eight pointed star with an large eye embellished in the center. The blade is wicked and cruel; it is a sharpened slab of bismuth about seven inches long. You tuck it into your belt\n' \
                  'and notice to your horror that the ritual circle is glowing darker and darker. The symbols and the circle underneath you begin to suck the light away from around themselves bending the light from the room around it like\n' \
                  'a black hole pulling in light across its event horizon. The lensing effect increases and the room\'s floor begins to shake and fold into the runes. The crystal ensconced by its wire nest begins to glow brightly and a golden \n'  \
                  'rift opens in front of you. The golden shimmering line begins to crackle and pop with an inner fire and it explodes into a large golden fire wreathed door into blackness.\n\n' \
                  '{Luke, run!} You hear your master\'s voice echo in your head and you plunge into the doorway. You have obtained the time knife. Samurai +2' \


lab_choice_samurai = 'You slam the book closed and the feelings of bliss immediately leave you. Replaced by panic and dread at your situation. Your instincts pull you towards  \n' \
                     'the pedestal in the center of the room and ritual circle. The top of the pedestal is dished inwards and there is a tangle of cables and pipes with a large green jewel in the center.\n\n' \
                     '{Do not be afraid, my child, your timing is quite fortuitous. I do not have much time left.} a voice echos in your head, familiar like an old friend. {You must not linger here. You are a \n' \
                     'a being out of time and now out of space.}\n\n' \
                     '{I sense you are apprehensive. I do not have much time or energy left. My soul is trapped in this vile machine, the ritual on the ground will allow you to open a portal home.} \n' \
                     '\"What must I do? I must return to my world\"\n\n' \
                     '{Throw those four levers and repeat after me. When the time is right take that dagger on the desk and cut a portal home}\n\n' \
                     'You run over to the desk and find the knife. Its blade has a gold titanium coating on top of sharpened bismuth shard about seven inches long. The hilt is made of an eight pointed star with an large eye embellished in the center. \n' \
                     '{Good now speak with one voice along with me, feel the words and picture your world.}. Following the command you speak the foreign words echoing off the inside of your skull. \n' \
                     '\"{GIBIL GASHRU UMUNA YANDURU. TUSHTE YESH SHIR ILLAINI U MA YALKI. GISHBAR IA ZI AI. AI ZI DINGIR GIIRA KANPA.}\" as you speak the words the ground begins to shake. The words thunder off your skull. You taste blood.\n' \
                     'Still you chant the words. The symbols and the circle underneath you begin to suck the light away from around it bending the light from the room around it like a black hole pulling in light across its event horizon.\n' \
                     'You start to lose feeling in your arms and feel the knife floating upwards until you are holding it in front, arms outstretched. You notice with horror that the blade is pointed back towards you. The pounding reaches a crescendo\n' \
                     'and you notice between you and the knife a golden line is forming. The ritual intensifies, stripping the light from the room until it is just you, the knife, the golden shimmer, and a solid green glow of the gem in its basin.\n' \
                     'You cannot stop chanting, you cannot move your paws, the light begins to overtake your vision. You feel the knife start moving towards you. You fight it but all of a sudden you feel very small and the knife grows heavy. \n' \
                     'A panic sets in and deepens, it causes you to lose control for a moment and you shut your eyes. You pull the knife through the golden light and into your body. The blackness of your shut eyes is obliterated by an onslaught\n' \
                     'of light. You pop you eyes open to see a hole in space and time. The gash you cut has severed the fabric of time and space in front of you. The shaking under your feet stops. The tear causes the fringes of reality to unravel like pulling\n ' \
                     'on a thousand individual threads. Reality dissolves into blackness around you. You have obtained the time knife. Samurai +2.' \


lab_des = 'You have escaped the noise at your back and there does not appear to be any attempt at forcing the door behind you. It takes just a moment to get your bearings. You are surrounded by lit\n' \
          'candles, and steel pipes that zig and zag through the room. The room is circular and contains only the door you entered by. Thick red drapes cover the walls and shelves covered in strange\n' \
          'objects. Skulls, feathers, chalices, effigies of a man on a golden throne. As you pad over towards the red drapes that line the room you start noticing the strange runes and patterns that\n' \
          'adorn the floor. The tiles appear to all be made of out of unique asymmetrical octagons, the floor seems to be shifting underneath you as you stare at it. The runes remain unchanged in position\n' \
          'and the guiding lines that connect them into an intricate patterned circle remain unchanged. As you round a shelf you see in the center of the room there is a clearing with a marble pedestal that has glass tubes\n' \
          'inlaid into the sides of the marble, they flow with a red fluid that glows with its own light. You approach the curtain and pull it back. Immediately you are hit with a wave of vertigo.\n\n' \
          '\"How can this be? I am above the clouds\"\n\n' \
          'The cityscape below you is not that of VOX\'s dark and terrible future, gone are the slick buildings and glowing neon, replaced by cathedral like spires that seem to cover the entire globe.\n'  \
          'You are so high above the clouds that the tower you are in is scraping space. You close the curtain, dismayed at how far from your home you have come. You begin to scour the room for an \n' \
          'explanation of where and when you are. The little leaflets of paper that are affixed onto mechanical objects with red wax appear to be in some form of binary and another hieroglyphic language \n' \
          'you can not read. You scour the literature strewn about the laboratory. Every book you open to read is incomprehensible. You pick up a small black book with white lettering and a red circle\n' \
          'symbol on the front, you open it and start reading. You feel a wave of bliss strike you as you read, the symbols make no sense, but they give you the feeling of words. The longer you look  \n' \
          'at them the more sense they start making. You begin to sound out the characters in front of you, sounding out quickly turns to babbling, then soon you are unwillingly reading aloud at a breakneck pace.  \n\n' \
          '\"UTUK XUL, TA ARDATA. KUTULU, TA ATTALAKA. AZAG-THOTH, TA KALLA! IA ANUI! IA ENLIL! IA NNGI!\"\n\n' \
          'You start to taste the familiar coppery metallic tang of...blood? You snap out of it to find that your mouth is bleeding. You reach up to wipe off some of the blood only to find that your\n' \
          'eyes are starting to bleed and are dripping down your face as well.\n' \


admin_des = 'You step out of the portal and into an office space. Hanging on the walls are posters and phrases meant to motivate the office workers. You start to walk down the rows of cubicles taking in\n ' \
            'your surroundings. The office workers have small personal items in their cubes such as succulents and figurines. It strikes you at how normal it all looks considering you are in the tower of\n' \
            'a massively evil being. In the back of the room you see a portrait of an impressive cyborg with a human head and a label proudly declaring \"Adam Smasher\" as employee of the month. \n' \
            'Your musings on the nature of evil are shattered when you hear a klaxon begin to wail again.\n\n' \
            '\"BEAR DETECTED IN ADMINISTRATION BUILDING\"\n\n' \
            'The room locks down around you. Bulkheads come slamming down sealing the doorway behind you. The klaxons stop wailing and instead the intercom says. \n\n' \
            '\"Deploying Employee of the month\"\n\n' \
            'In the center of the room a group of cubes is ripped out of the ground and sent flying in all directions as an elevator lifts out of the floor. The door opens and a swirling wall of mist\n' \
            'flows out. Out of this mist steps VOX\'s number one assassin, Adam Smasher.' \
            '\"Smasher, I should have known that VOX would have kept you alive all these years. Finally we meet again, I will destroy you once and for all!\"' \
            'Adam Smasher laughs. \" You and I aren\'t so different, you see when I was a b-\"' \
            'You wait for him to start a monologue explaining his backstory, and as soon as he does you take the moment to engage in combat and launch yourself straight at him!'

admin_victory = 'You grab Adam Smasher\'s gamma cannon and slice it free from his arm. This causes the energy created by his reactor to have no outlet. It feeds back on itself and causes him to explode.\n' \
                'You walk over to the largest chunk and as you examine what is left a small USB stick pops out of a hidden compartment in the chest piece. It is labeled \"Elevator password do not share\"\n' \
                'You now have the password to VOX\'s Elevator.'

exit_elevator_des1 = 'Suddenly the lights in the elevator turn off. When they flip back on you find yourself slowly floating upwards in a field of stars. You hear a booming and terrifying female voice say\n' \
                     '\"You have been summoned here by VOX and you find yourself fortunate enough to be granted an audience with the shogun of sorrow, master of all the known universe. You have been instructed to\n' \
                     'put the affairs of your house and company in order before attendance. Should you displease the master you will not leave this place alive.\"\n' \
                     'As the voice talks the visions around you become more terrifying with each passing moment. You see planets destroyed, stars snuffed out and all the while you are hurdled towards a point\n' \
                     'of infinite blackness. The closer you get the faster you are pulled until your entire vision is absorbed into nothing but pitch blackness. A beat passes and then suddenly\n' \
                     'a pair of eyes snap open. They are wreathed in flames and the face of VOX fills your vision. The voice returns \"Your audience with VOX will begin in 5...4...3...2...1... \"\n' \
                     'The vision of VOX\'s vile visage disappears just as suddenly as the whole ordeal began. You find yourself again plunged in darkness. '

exit_elevator_des2 = 'You hear a \"DING!\" and the lights flip back on.\n' \
                     'You are standing in the elevator again. The doors open and you step out.' \

# Character-descriptions------------------------------------------------------------------------------------------------#

scavenger_des = 'As you rise you notice three medium sized creatures in brown hooded robes covered in dirt and slime from the wasteland.\n' \
                'The hoods veil their features in darkness, leaving only two glowing yellow eyes visible. One of them is holding a long object. \n' \
                'They visibly start at your rising, begin speaking frantically in a language you do not understand. On of them yells in a manner that needs no translation. \n' \
                'The three of them start to close around you. You steady your mind as your body sinks into a familiar fighting pose your paws reach down to grasp the hilt of your blade\n\n' \
                'Only to find it GONE! The scavengers have stolen your ancestral family blade, a crime punishable only with death! (SAMURAI is very weak without your sword)\n'

cyber_guard_des = 'Hesitating a moment, you walk towards the desk and notice there is a figure seated behind it. They rise to meet you.' \
                  '\"Hello samurai I am XK682. I have been in sleep mode waiting for this day for a long time. VOX has imbued me with one directive. Destroy you.\"\n' \
                  '\"End speech statement, run program DESTROY BEAR.EXE\" The robot moves towards you, cybernetic muscles tensing and lights turning red one after another.\n' \
                  'On its hip it carries a sword much like your own. It draws the sword, enters a fighting stance and begins to close on you.'

psychic_salmon_des = 'Then the column shifts and twists in front of you. The image of it dissolving as you disbelieve your own eyes. Out of the corner of your eye you see a weapon rack go through the same\n' \
                     'metamorphosis. A voice appears in your head and says {it seems the bear is not as stupid or weak as we thought brother} a second replies {yes I guess we will just have to kill him} \n' \
                     'In front of you appear two bear sized floating salmon. They are covered in cybernetic augmentations with no obvious explanation of how they are infront of you aside the voices in your head. \n' \
                     '{The fool doesn\'t even know of our power. Come sister let\'s give him a taste.}. Without warning the salmon split into dozens of fish, swarming and schooling around you. You hear a faint ringing \n' \
                     'beginning to build in your ears.'


vox_desc1 = 'You step foot into VOX\'s chamber. Its massive grand scale makes you feel tiny. The room has large pillars of blue and purple fire shooting up to the ceiling. The floor is the same black and red marble\n' \
            'that adorned the room below. There is a long white carpet leading to a throne entirely constructed from the metal plated skulls of VOX\'s enemies. Sitting upon it is the all black form of your hated foe.\n' \
            'VOX lounges on the chair currently taking the form of a tall and slender humanoid. His eyes are wreathed in ever burning flame. His back is laid on one arm rest and a leg is draped over the other as if \n' \
            'he has no care in the world.\n\n' \
            '\"Finally! You are here.\"\n VOX booms as you approach the throne. \"Can\'t belive, I the master of all darkness and lands, am saying this but I got terribly bored without you. With your clan wiped out,\n'  \
            'the salmon subjugated by my psychic prowess and the bees enslaved I have had nothing to do but... Govern. Ugh. It just didn\'t give me the zest for death and murder that fighting you did. Once you \n' \
            'are lord of all darkness it just turns into spreadsheets. Why did I even have my scientists invent those. I see you have acquired some of my tech. It matters not. Come lets make this a duel for the history\n' \
            'books. I am sure your defeat will make a fantastic mural.\" VOX waits a moment for you to say something. There are no words you have to describe this hateful being. Nothing now can be said that will\n' \
            'remedy the atrocities he has committed. All you have now is vengeance. You draw your sword.\n\n' \
            '\"No witty retort, fine have it your way\"\n\n' \
            'VOX springs from the throne with unnatural quickness. The thick blackness that makes up his form shifts and changes his arms into two long curved wicked blades. You charge into the final battle. '


vox_desc2 = 'VOX mistimes a step and your sword slashes forward glinting in the flames of the columns around you. Your blade glowing red hot and crackling with lightning slices through VOX\'s arm-blade he shrieks and recoils\n' \
            '\"You stupid bear you cut off my arm!\" VOX spits at you clearly in pain. \"It was fun but now you have made me angry.\" VOX\'s form starts to shift and dissolve. He raises his arms then starts to suck the fire from the \n' \
            'columns into his hands where it is quickly absorbed adding to his mass. You charge at him but it does no good as VOX has already absorbed enough power and transforms into a figure identical to you. It is almost as \n' \
            'if your shadow has come to life. You step to the right, Bear VOX mimics your step. You raise your sword, as does he.\n\n' \
            '\"Now don\'t go accusing me of not fighting fair.\"\n\n' \

vox_desc3 = 'VOX is before you leaking black fluid and blueish purple flame. He is clearly haggard and on the ropes. He hops backwards to try and steady his footing then catch his breath, but you are too quick. You grab\n' \
            'his head in your mighty paws and hurl him backwards into his own throne. Such is the force of your attack that VOX bursts through the back of the chair and slides out of sight behind the throne. You follow up but instead of VOX\n' \
            'you see a portal! Through the portal you see your own time. Your first battle with VOX. You run as fast as you can but the closer you get the slower you seem to move. You are forced to witness and relive that initial battle\n' \
            'Each step and sword blow is seared into your memory. VOX lays on the ground in front of your past self. You see yourself raise your sword with two hands to decapitate VOX. Just as you start to swing the wounded VOX from the future\n ' \
            'appears behind past you and opens a second portal and pushes you into it. Throwing your past self into the future. \"Now just one last thing\" says VOX looking down at his unconscious and wounded past self. Future VOX reaches \n' \
            'down turning his arm into a blade and stabs his past self in the heart. He chuckles and says \"Can\'t have any competition from myself now can I, now lets close this loop\" he reaches towards the portal and makes a zipping motion \n' \
            'just as you jump through it. \"Not this time VOX!\" You leap through the portal in the nick of time and stand firmly in your past facing a wounded VOX. Now is your chance to defeat him for good! You are back in your time and your\n' \
            'chance to undo the future is nigh. You activate the lightning module on your sword and prepare to attack. '\

victory_des = 'That final blow was enough, VOX staggers backwards and collapses. You stand over his amorphous mass and watch it leak purple blue flaming blood. You take but a moment to reflect back on your journey. You must end this now.\n '\
              'You raise your sword and plunge it into where you reckon VOX\'s heart must be. When you plunge it in nothing happens for a moment Then you feel a tugging and all the air around you starts to pull itself into VOX\'s lifeless\n'\
              'body. It folds and crumples and collapses as the wind begins to howl and shriek. The world around you reaches a shattering crescendo of wailing winds and demonic screeching. Then abruptly silence. It is over. VOX IS DEAD!\n' \
              'YOU WIN! You have saved the future and returned to the past. '


# Stats-----------------------------------------------------------------------------------------------------------------#

bear_base_stat = int(1)  # bear base stat will be // to give how much bonus to bear checks SET TO 1 FOR GAME DONT FORGET
samurai_base_stat = int(0)  # this is how much will be add to samurai checks SET BACK TO 0 FOR GAME DONT FORGET
bear_current_hp = int(10)  # kick off HP pool
bear_max_hp = int(10)  # This is the max hp from the start of the game
player_location = 'wasteland'  # Start Room
tower_room = 'reception'  # when the player has moved into the tower this ensures they are in the start room
has_sword = 0  # Can change from 0 to 1 to steal sword form player, without it they can not use the SAMURAI skill

num_scavengers = int(3)  # Set the number of scavengers in the wasteland. Needed for balance issues
scavenger_damage = int(1)  # How much damage the GROUP of scavengers deal. They are supposed to be weak and fight as a pack

cyber_guard_alive = int(1)
cyber_guard_hp = int(5)

num_psychic_salmon = int(2)
psychic_salmon_damage = int(2)

vox_hp = int(30)  # boss HP
vox_damage = 3  # boss damage

adam_smasher_hp = int(15)
adam_smasher_alive = int(1)
# Functions-------------------------------------------------------------------------------------------------------------#

def loading_screen():
    ascii_art = ['Animation1.txt', 'Animation2.txt', 'Animation3.txt', 'Animation4.txt']  # list of ascii art files
    frames = []  # Add contents of each frame file to the list so it only loads them once for speed

    for name in ascii_art:
        with open(name, 'r', encoding='utf8') as f:  # open the files in read mode unicode characters to prevent errors, not really ascii I know
            frames.append(f.readlines())  # take each and append to frames list

    for i in range(3):  # set up how many times it plays through the frames
        for frame in frames:  # each frame is a list of rows
            print(''.join(frame))  # print out each row appended as one
            time.sleep(1)  # interval for frame
            os.system('cls')  # ready frame for next animation

def victory_screen():
    ascii_art = ['victory1.txt', 'victory2.txt', 'victory3.txt', 'victory4.txt']  # list of ascii art files
    frames = []  # Add contents of each frame file to the list so it only loads them once for speed

    for name in ascii_art:
        with open(name, 'r', encoding='utf8') as f:  # open the files in read mode unicode characters to prevent errors, not really ascii I know
            frames.append(f.readlines())  # take each and append to frames list

    for i in range(3):  # set up how many times it plays through the frames
        for frame in frames:  # each frame is a list of rows
            print(''.join(frame))  # print out each row appended as one
            time.sleep(1)  # interval for frame
            os.system('cls')  # ready frame for next animation

def bear_die_roll():  # die rolling function for combat
    global bear_base_stat
    global die_result
    print('You charge, while roaring savagely and swinging your massive clawed paws.\n')
    die_result = random.randint(1, 6)  # number of die faces
    die_result = int(die_result + bear_base_stat)  # items will add +1 at a time to a stat, I want to die results to reflect that
    time.sleep(2)  # build a little tension
    print('You rolled a:', die_result)  # display to the user


def bear_skill_die_roll():  # die rolling function for combat
    global bear_base_stat
    global die_result
    die_result = random.randint(1, 6)  # number of die faces
    die_result = int(die_result + bear_base_stat)  # items will add +1 at a time to a stat, I want to die results to reflect that
    time.sleep(2)  # build a little tension
    print('You rolled a:', die_result)  # display to the user


def samurai_die_roll():  # die rolling function for combat
    global samurai_base_stat
    global has_sword
    global die_result
    if has_sword == 1:
        print('You ready your sword and strike.\n')
        die_result = random.randint(1, 6)  # number of die faces
        die_result = int(die_result + samurai_base_stat)  # items will add +1 at a time to a stat, I want to die results to reflect that
        time.sleep(2)  # build a little tension
        print('You rolled a:', die_result)  # display to the user
    else:
        print('You have lost your sword, the attack fails!')  # SAMURAI IS DISABLED without the sword


def samurai_skill_die_roll():  # die rolling function for combat
    global samurai_base_stat
    global has_sword
    global die_result
    if has_sword == 1:
        die_result = random.randint(1, 6)  # number of die faces
        die_result = int(die_result + samurai_base_stat)  # items will add +1 at a time to a stat, I want to die results to reflect that
        time.sleep(2)  # build a little tension
        print('You rolled a:', die_result)  # display to the user

    else:
        print('You do not have your sword!')  # SAMURAI IS DISABLED without the sword


def enemy_die_roll():  # die rolling function for combat
    global bear_current_hp
    global foe_die_result
    global scavenger_damage
    foe_die_result = random.randint(1, 6)  # number of die faces
    foe_die_result = int(die_result - 1)  # removing one gives the player an edge
    print('Rolling')  # display to the user
    time.sleep(2)  # build a little tension
    if foe_die_result < 4:  # miss number
        print('They miss!')
    if foe_die_result > 3:  # hit number
        print('The attack lands, wounding you.')
        bear_current_hp = bear_current_hp - scavenger_damage


def vox_die_roll():  # die rolling function for combat
    global bear_current_hp
    global foe_die_result
    foe_die_result = random.randint(1, 6)  # number of die faces vox will run at even odds
    print('Rolling')
    time.sleep(4)  # build a little tension
    print('Vox rolled a:', foe_die_result)  # display to the user
    if foe_die_result > 3:  # miss number
        print('The attack lands inflicting two wounds')
        bear_current_hp = bear_current_hp - 2
    if foe_die_result < 4:  # hit number
        print('You skillfully dodge out of the way, while doing your best to parry. You escape harm for now')


def tutorial():
    tutorial_prompt_response = ''  # set up string
    while tutorial_prompt_response != 'yes' or 'no':  # Prompt to see if someone has played before
        print(tutorial_prompt)  # a couple of my friends have asked to play
        tutorial_prompt_response = input()  # get response
        tutorial_prompt_response.strip()
        tutorial_prompt_response.lower()  # normalize inputs.
        if tutorial_prompt_response == 'yes':  # yes branch
            print('Good luck samurai, may the salmon be fresh and the honey sticky')
            return # send user to the game
        elif tutorial_prompt_response == 'no':  # brief game overview
            print(tutorial_text)  # print previously set up tutorial text
            return
        else:
            print('Enter a valid statement, yes or no, how hard can that be?')  # snarky response to invalid input


def gate_puzzle():
    global player_location
    print('You look around the gatehouse looking for a way to disable the turrets and shield door')
    print('You eventually find a console with a keyboard and a big red button labeled \"Allow Passage\"')
    print('Immediately you press the button, the screen flashes ENTER PASSWORD')
    time.sleep(2)
    password = ''  # player will enter a password
    while password != 'keyboard':  # while the player has not solved the riddle loop
        print('PASSWORD HINT: It has keys, but no locks. It has space, but no room. You can enter, but can’t go inside. What is it?')  # present riddle
        password = input('Enter password:')  # guess
        password.strip()  # remove whitespace
        password.lower()  # data validation
        if password == 'keyboard':  # victory logic
            print('Access granted, disabling defenses.')
            player_location = 'tower'  # setting this location allows they player to enter vox's tower
        else:
            print('INCORRECT')  # try again!


def reactor_puzzle():  # This is based off our simon says homework, but with a twist. This game is easy at first and gets harder as time goes on. The user must get the correct rods 7 times total.
    global bear_current_hp
    global bear_base_stat
    global bear_max_hp
    global bee_puzzle_complete

    user_score = 0  # start score at 0, every time they are successful it will raise. When they are wrong it does not raise but the number of rods that overheat
    reactor_code = ''  # every play through it will generate a different code.

    i = 1  # number of rods
    failure = 0  # lose condition
    while user_score <= 6 and failure != 1:

        print('&REACTOR MELTDOWN IN PROGRESS&\nPull the cooling rods in the same order they are presented\nYou will only have 8 seconds to memorize the order of the rods')
        print('7 sets of rods must be pulled in sequence to stop the meltdown')

        for i in range(i):  # every time we go through the loop we add a new rod
            number = (str(random.randint(0, 9)))  # changes every time someone plays the puzzle
            reactor_code += number  # append into one list.

        print('Rod(s) that need to be pulled:', reactor_code)  # give the player some time to look at the list
        time.sleep(8)  # same deal we are waiting for the player to memorize
        os.system('cls')  # clear the screen
        user_rod_order = input(str('Enter the rod numbers in order, no whitespace:'))  # prompt for an answer

        if user_rod_order == reactor_code:  # victory condition
            user_score = user_score + 1  # add to the user score
            i = i + 1  # iterate
            print('The screen flashes \"RODS PULLED\"')
            print(user_score, 'sets of rods pulled')

        elif i >= 35:  # if there are too many overheating rods the player will lose
            print('Reactor meltdown unavoidable, Bee population status: CRITICAL')
            print(bee_puzzle_failure)
            failure = 1  # the player loses
            bee_puzzle_complete = 1

        else:

            user_score = 0  # this is where I feel a little evil, but failing to pull the sets in order will set the user score down to 0 BUT NOT THE NUMBER OF RODS. This will lead to meltdown if the player is not careful.

    if user_score >= 7:
        print('Reactor Restarting')
        time.sleep(8)
        print('Reactor Nominal')
        print(bee_puzzle_success)  # Print victory speech
        bee_puzzle_complete = 1
        bear_current_hp = bear_current_hp + 5  # Upgrade HP
        bear_max_hp = bear_max_hp + 5  # Upgrade HP
        bear_base_stat = bear_base_stat + 1  # Upgrade bear rolls


def victory_cons():
    global victory
    global easter_egg

    if victory == 1 and easter_egg == 1:
        restart = input('Congratulations Samurai, you have 100% cleared the game. Want to play again? (yes or no): ')
        restart.lower()
        restart = restart.strip()
        if restart == 'yes':
            play_again()
            loading_screen()
        if restart == 'no':
            os.system('cls')
            loading_screen()

    if victory == 1 and easter_egg == 0:
        restart = input('Congratulations Samurai, would you like to play again and hunt for the easter egg you missed? (yes or no): ')
        restart.lower()
        restart = restart.strip()
        if restart == 'yes':
            play_again()
            loading_screen()
        if restart == 'no':
            os.system('cls')
            loading_screen()

    if bear_current_hp <= 0:
        restart = input('You have died. VOX wins and is the eternal master of all creation! Would you like to play again (yes or no): ')
        restart.lower()
        restart = restart.strip()
        if restart == 'yes':
            play_again()


def prologue():
    global player_location
    global num_scavengers
    global bear_current_hp
    global bear_max_hp
    global samurai_base_stat
    global has_sword
    global die_result

    while player_location == 'wasteland' and bear_current_hp >= 1:
        if num_scavengers >= 1:
            print('Current HP:', bear_current_hp)
            player_choice = input('It is your turn in combat.\nBEAR or SAMURAI: ')
            player_choice.strip()
            player_choice.lower()

            if player_choice == 'bear':
                bear_die_roll()

                if die_result >= 7:
                    print('MAXIMUM EFFECT! You barrel forwards scoop one scavenger\'s head in each massive paw and '
                          'with a ferocious crash slam them into either side of the third\'s head\nobliterating all '
                          'three in a shower of golden blood.')
                    print('You lean down to examine the bodies of the creatures to find they are machines. You lift '
                          'up a scrap of blood covered cloth and sniff it.')
                    print('To your bemusement you find that it is not blood at all, but honey! You search through the '
                          'broken machines and find three tanks of honey. Your HP has been restored to full!')
                    print('You have reclaimed your sword! SAMURAI CHECKS +2')
                    num_scavengers = 0
                    bear_current_hp = bear_max_hp
                    has_sword = 1
                    samurai_base_stat = samurai_base_stat + 1
                    player_location = 'gate'
                    print('Current HP:', bear_current_hp)
                    print('All roads in this world lead to VOX\'s Tower, you cover yourself in one of the scavenger\'s tattered robes to disguise your appearance and head North.')
                elif die_result > 3:
                    print("Using all of your strength you rake a claw through one of the scavengers in a "
                          "shower of golden blood,\n It's head and body fly in different directions.")
                    num_scavengers = num_scavengers - 1
                    print('Number of scavengers remaining:', num_scavengers)

            elif player_choice == 'samurai':
                samurai_die_roll()

            else:
                print('That is not a valid choice')

            if num_scavengers > 0:
                print('The enemy moves into attack!')
                enemy_die_roll()


        elif num_scavengers <= 0:
            print('The scavengers lay broken and defeated by your bear-like wrath!')
            print('You lean down to examine the bodies of the creatures to find they are machines. You lift '
                  'up a scrap of blood covered cloth and sniff it.')
            print('To your bemusement you find that it is not blood at all, but honey! You search through the '
                  'broken machines and find three tanks of honey. Your HP has been restored to full')
            print('You have reclaimed your sword! SAMURAI CHECKS +2')
            num_scavengers = 0
            bear_current_hp = bear_max_hp
            has_sword = 1
            samurai_base_stat = samurai_base_stat + 1
            player_location = 'gate'
            print('Current HP:', bear_current_hp)
            print('All roads in this world lead to VOX\'s Tower, you cover yourself in one the scavengers '
                  'tattered robes to disguise your appearance and head North.')


def travel_to_gate():
    clear_to_gate = ''
    while clear_to_gate != 'clear' and bear_current_hp >= 1:
        clear_to_gate = input('When you are ready to tidy up the screen and continue on your journey enter clear:')
        clear_to_gate.strip()
        clear_to_gate.lower()
        if clear_to_gate == 'clear':
            os.system('cls')
        else:
            print('that is not valid')

    print(gate_des1)

    clear_gate_des1 = ''
    while clear_gate_des1 != 'clear' and bear_current_hp >= 1:
        clear_gate_des1 = input('When you are ready to tidy up the screen and continue on your journey enter clear:')
        clear_gate_des1.strip()
        clear_gate_des1.lower()
        if clear_gate_des1 == 'clear':
            os.system('cls')
        else:
            print('that is not valid')

    time.sleep(5)
    print(gate_des2)

    clear_gate_des2 = ''
    while clear_gate_des2 != 'clear' and bear_current_hp >= 1:
        clear_gate_des2 = input('When you are ready to tidy up the screen and continue on your journey enter clear:')
        clear_gate_des2.strip()
        clear_gate_des2.lower()
        if clear_gate_des2 == 'clear':
            os.system('cls')
        else:
            print('that is not valid')

    print(gate_des3)

    clear_gate_des3 = ''
    while clear_gate_des3 != 'clear':
        clear_gate_des3 = input('When you are ready to tidy up the screen and continue on your journey enter clear:')
        clear_gate_des3.strip()
        clear_gate_des3.lower()
        if clear_gate_des3 == 'clear':
            os.system('cls')
        else:
            print('that is not valid')

    print(gate_des4)


def gate():
    global player_location
    global num_scavengers
    global bear_current_hp
    global bear_max_hp
    global samurai_base_stat
    global has_sword
    global die_result

    while player_location == 'gate' and bear_current_hp >= 1:

        gate_choice = input('BEAR or SAMURAI: ')
        gate_choice.strip()
        gate_choice.lower()

        if gate_choice == 'bear':
            print(
                'The anger at seeing your culture annihilated overwhelms you. You drop to all fours and charge towards the only cover from the laser turrets. Blasts of shimmering multicolored beams')
            print('spew from the turrets like a hailstorm pointed directly at you. You don\'t even feel the few blasts that connect. Your anger gives you speed and strength. ')
            bear_skill_die_roll()
            time.sleep(3)

            if die_result >= 3:
                print('You charge through the gatehouse door smashing the attending robot to pieces with your entrance. The gatehouse seems impervious to the fire from the cannons.')
                print('As your rage fades you notice just how lucky you were to get off with just a few glancing burns and one real hit on your shoulder.\n')
                bear_current_hp = bear_current_hp - 1
                print('Current HP:', bear_current_hp)
                gate_puzzle()

            elif die_result <= 2:
                print('MISFORTUNE!')
                print('The laser turrets swing as you charge the gatehouse. In your rage you don\'t even think to dodge them. A mistake.')
                time.sleep(6)
                print('Only a few paces from the gatehouse a laser blast slams directly into your forepaw. You trip and begin to slide. You barrel straight through the door smashing the attending')
                print('robot to pieces')
                bear_current_hp = bear_current_hp - 2
                print('Current HP:', bear_current_hp)
                gate_puzzle()

        elif gate_choice == 'samurai':
            print('You dash forward. Head down in a full sprint for two long strides. Paws on sword. Fluid like water, fast as the wind.')
            samurai_skill_die_roll()
            time.sleep(10)

            if die_result >= 5:
                print('The streams of laser fire quickly converge on you as you run. The moment before the bolts of energy connect, you twist out of your hooded cloak. ')
                time.sleep(8)
                print('You complete the quarter twist with a short hop to the right. The laser bolts meant for you riddle your cloak with flaming holes tearing it to pieces.')
                time.sleep(8)
                print('You carry your momentum from your skillful dodge into a full circular turn, drawing you sword and sweeping it just above the ground as you spin.')
                print('At the same moment you complete your turn, you channel all the momentum and weight you have into a diagonal rising slash as the torrent of laser fire converges on you.')
                time.sleep(8)
                print('Such as your skill is you connect with eerie precision reflecting the lasers back at the gate spotlights, klaxons and laser turrets. The torrent of laser fire meant for you')
                print('smashes the gates defenses to bits. The laser turrets power cells catch fire and with a short pause...')
                time.sleep(10)
                print('EXPLODE!')
                print('One explosion triggers another and then many more, shield power lines glow and burst, spotlights flicker and then explode outward in bursts of colored glass.')
                print('The teal laser gate dims, flickering for a moment before shining even brighter than before. Then without warning it shuts off. Now there is only the sound')
                print('of broken glass tinkling down from the sky around you and what is left of your cloak smoldering, you walk through the gate')
                player_location = 'tower'
            else:
                print('You draw your sword, slashing left and right and you duck and weave towards the gatehouse. Not so different than dealing with VOX\'s archers, you think to yourself.')
                print('Distracted for a moment you catch a laser blast to the shoulder. You must focus harder now. You redouble your efforts and gracefully make your way to the gatehouse.')
                print('The robot attendant barks \"You do not have the proper securi-\" as you cut it cleanly in half.')
                bear_current_hp = bear_current_hp - 1
                print('Current HP:', bear_current_hp)
                gate_puzzle()

    clear_gate_victory = ''
    while clear_gate_victory != 'clear':
        clear_gate_victory = input('When you are ready to tidy up the screen and continue on your journey enter clear:')
        clear_gate_victory.strip()
        clear_gate_victory.lower()
        if clear_gate_victory == 'clear':
            os.system('cls')
        else:
            print('that is not valid')


def tower_reception():
    global cyber_guard_hp
    global cyber_guard_alive
    global bear_current_hp
    global bear_max_hp
    global samurai_base_stat
    global die_result
    global reception_clear

    while cyber_guard_alive == 1 and bear_current_hp >= 1:
        print('Current HP:', bear_current_hp)
        player_choice = input('It is your turn in combat.\nBEAR or SAMURAI: ')
        player_choice.strip()
        player_choice.lower()

        if player_choice == 'bear':
            bear_die_roll()
            print('You drop to all fours and charge the Robot.')
            if die_result >= 4:
                print('You smash your shoulder into the robots chest flinging it backwards')
                cyber_guard_hp = cyber_guard_hp - bear_base_stat
            else:
                print('The attack misses, the duel continues')
        elif player_choice == 'samurai':
            print('You wait and watch the robot\'s footwork. You wait for a slight hesitation caused by the robot\'s unnatural gait.')
            samurai_die_roll()
            if die_result >= 4:
                print('The blow lands, affording you the chance to follow up')
                cyber_guard_hp = cyber_guard_hp - samurai_base_stat
            else:
                print('The attack misses, the duel continues')
        else:
            print('You entered something other than bear or samurai, the bear becomes distracted and your turn in combat is wasted!')

        if cyber_guard_hp >= 1:
            print('The robot moves in closer, holding its sword in a familiar stance. It strikes!')
            time.sleep(1)
            enemy_die_roll()

        if cyber_guard_hp < 1:
            reception_clear = 1
            cyber_guard_alive = 0
            print(guard_victory)

    if reception_clear == 1:
        move_look_choice()


def tower_hive():
    global hive_des
    global hive_clear
    global hive_bear
    global hive_samurai
    print(hive_des)
    while hive_clear == 0:
        player_choice = input('BEAR or SAMURAI:')
        player_choice = player_choice.strip()
        player_choice = player_choice.lower()

        if player_choice == 'bear':
            print(hive_bear)
            hive_clear = 1
        elif player_choice == 'samurai':
            print(hive_samurai)
            hive_clear = 1
        else:
            print('That is not valid.')

    move_look_choice()
    return


def tower_reactor():
    global reactor_des
    global reactor_clear

    print(reactor_des)

    clear_screen()

    while reactor_clear == 0:
        reactor_puzzle()
        reactor_clear = 1

    move_look_choice()
    return


def tower_armory():
    global player_location
    global num_psychic_salmon
    global psychic_salmon_des
    global psychic_salmon_damage
    global bear_current_hp
    global bear_max_hp
    global samurai_base_stat
    global bear_base_stat
    global die_result
    global armory_clear
    global armory_victory
    global foe_die_result

    print(armory_des)
    print(psychic_salmon_des)

    while armory_clear == 0 and bear_current_hp >= 1:
        print('Current HP:', bear_current_hp)
        player_choice = input('It is your turn in combat.\nBEAR or SAMURAI: ')
        player_choice.strip()
        player_choice.lower()

        if player_choice == 'bear':
            bear_die_roll()
            print('Your bear instincts take over and that salmon looks delicious. You barrel towards it to take a bite. ')
            if die_result >= 4:
                print('Your bite lands! It is delicious!')
                num_psychic_salmon = num_psychic_salmon - 1
            else:
                print('You charge into a phantom created by the salmons psychic powers. You hear a faint ringing in your ears.')
        elif player_choice == 'samurai':
            print('The salmon swirl around you. You steady yourself and wait for a tell.')
            samurai_die_roll()
            if die_result >= 4:
                print('There! You smell it, the tell tale odor of a real fish. You strike with your sword dicing the salmon into evenly cut cyber-sashimi.')
                num_psychic_salmon = num_psychic_salmon - 1
            else:
                print('You fail to identify the real fish before the ringing in your ears reaches a splitting volume')
        else:
            print('You entered something other than bear or samurai, the bear becomes distracted and your turn in combat is wasted!')

        if num_psychic_salmon <= 0:
            armory_clear = 1
            print(armory_victory)
            return
        if num_psychic_salmon >= 1:
            print('Just as the ringing reaches a shattering crescendo the illusory salmon disappear and a wave of purple energy ripples towards you. ')
            for num in range(num_psychic_salmon):
                enemy_die_roll()
                print('The illusory salmon fill the room again')


def tower_training():
    global training_des1
    global training_clear
    global die_result
    global samurai_base_stat
    global bear_current_hp

    while training_clear == 0:

        print(training_des1)
        time.sleep(25)
        player_choice = input('BEAR or SAMURAI:')
        player_choice = player_choice.strip()
        player_choice = player_choice.lower()

        if player_choice == 'bear':
            print(
                'You rage against the darkness and barrel forward smashing open a door not ten meters from the start of your charge. THe complete blackness becomes blinding white light. The light stuns')
            print('you for a second.')
            time.sleep(4)
            print(
                'SLAM! The door behind you shuts with a loud concussive bang and then locks itself with a loud clank. Your freshly adjusted eyes see a training room. To your right and left you see gun')
            print('rests and robot target dummies at the end of the range. Farther in front you an obstacle course. A cheery voice comes over the intercom and says \"Best the training course or be ')
            print(
                'terminated.\" The target dummies come to life and lights swing down on you from the ceiling. You charge the nearest target dummy and rip it off its stand. You use it as a shield and charge')
            print('towards the obstacle course. You discard it and leap onto the obstacle course... ')
            time.sleep(12)
            bear_skill_die_roll()
            if die_result >= 4:
                print('seemingly triggering every trap at once. Laser sights appear on your chest.')
                time.sleep(2)
                print('random floor tiles flip over into torrents of fire.')
                time.sleep(2)
                print('Holes open in the walls firing a swarm of feathered darts.')
                time.sleep(2)
                print('and nothing touches you. You dip, bob, and vault over every obstacle and explosive. After you leap off the final obstacle, you see a hand to hand combat bot beneath you. ')
                print('It doesnt stand a chance as you plummet down and smash it to pieces. Its shock unit flying out and into the air. You catch it and attach it to the hilt of your sword.')
                print('Shock attachment obtained! Samurai +2')
                samurai_base_stat = samurai_base_stat + 2
                training_clear = 1

            elif die_result <= 3:
                print('seemingly triggering every trap at once. Laser sights appear on your chest.')
                time.sleep(2)
                print('random floor tiles flip over into torrents of fire.')
                time.sleep(2)
                print('Holes open in the wall firing a swarm of feathered darts.')
                time.sleep(2)
                print('You catch a piece of everything over the course. You try to climb walls and lasers land all around you sending cement spalling flying into your armor, You leap over a small sandbag wall ')
                print('as a torrent of flame scorches you. Mere moments later you find yourself peppered with tiny stinging acid darts. You leap off the final sandbag into the house only to be greeted by a shock ')
                print('baton to the snout from a carefully placed placed hand to hand bot. Enough is enough! You smash it into to the wall. Its shock unit flying out and into the air. You catch it and attach it ')
                print('to the hilt of your sword. Shock attachment obtained. Samurai +2. -2 hp.')
                samurai_base_stat = samurai_base_stat + 2
                bear_current_hp = bear_current_hp - 2
                training_clear = 1

        elif player_choice == 'samurai':
            print('You pause for a moment and collect yourself. The pitch blackness is not the time for haste. You draw your sword and close your eyes, they do not serve you now anyways. You point ')
            print('the the sword down at your paws. You step forward into the pitch blackness in time with the swinging of your blade.')
            time.sleep(10)
            print('sweep')
            time.sleep(2)
            print('step')
            time.sleep(1)
            print('sweep')
            time.sleep(2)
            print('step')
            time.sleep(1)
            print('sweep')
            time.sleep(2)
            print('step')
            time.sleep(1)
            print('sweep. Clank.')
            print('You reach out and feel a door. You open the door slowly and peer through allowing your eyes to adjust to the brightness. Inside to your right and left you see gun rests')
            print('and robot target dummies at the end of the range. Further out you see an obstacle course with ramps and walls to climb and a series of sandbags surrounding a plywood house wall.')
            print('You notice just outside the door is a pressure plate and cameras swivel about the ceiling. You wait for one of the cameras to look away and dash to the nearest bulkhead between shooting')
            print('range rows. Littering the floor in your little stall are spent energy cells from some plasma rifles. You figure that they have a nice heft and scoop a pawful. You peek out from behind the')
            print('bulkhead and throw six in swift succession smashing several lights. You move into the darkness down to the other side of the training area successfully avoiding any other traps. As you peer')
            print('around the final corner of the course you find yourself face to face with a hand to hand robot. Its stun baton ignites in a crackle of electricity and sweeps downward. You catch its arm,')
            print('and smash it directly in the torso smashing it to pieces. You take the stun unit and attach it to the hilt of your sword. It glows red with heat and crackles with electricity. Samurai +2.')
            samurai_base_stat += 2
            training_clear = 1


def tower_lab():
    global lab_des
    global lab_clear
    global tower_room

    print(lab_des)

    while lab_clear == 0:
        player_choice = input('BEAR or SAMURAI:')
        player_choice = player_choice.strip()
        player_choice = player_choice.lower()


        if player_choice == 'bear': #trash the whole lab accidentally trigger a portal
            print(lab_choice_bear)
            lab_clear = 1
            clear_screen()
            tower_room = 'admin'

        elif player_choice == 'samurai': #ritual
            print(lab_choice_samurai)
            lab_clear = 1
            clear_screen()
            tower_room = 'admin'
        else:
            print('That is not valid')


def tower_admin():
    global admin_clear
    global adam_smasher_hp
    global adam_smasher_alive
    global die_result
    global bear_current_hp
    global foe_die_result
    global key_code
    print(admin_des)

    while adam_smasher_alive == 1 and bear_current_hp >= 1:
        print('Current HP:', bear_current_hp)
        player_choice = input('It is your turn in combat.\nBEAR or SAMURAI: ')
        player_choice.strip()
        player_choice.lower()

        if player_choice == 'bear':
            bear_die_roll()
            print('You drop to all fours and charge Adam Smasher.')
            if die_result >= 4:
                print('You smash your shoulder into the cyborg knocking it off its feet.')
                adam_smasher_hp = adam_smasher_hp - bear_base_stat
            else:
                print('The attack misses, the battle rages through the office.')
        elif player_choice == 'samurai':
            print('Adam Smasher charges you and you sidestep deftly striking at them with your sword.')
            samurai_die_roll()
            if die_result >= 5:
                print('The blow lands, affording you the chance to follow up')
                adam_smasher_hp = adam_smasher_hp - samurai_base_stat
            else:
                print('The attack misses, the battle continues')
        else:
            print('You entered something other than bear or samurai, the bear becomes distracted and your turn in combat is wasted!')

        if adam_smasher_hp >= 1:
            print('Adam Smasher circuits glow and become blinding he shoots a beam of gamma radiation out from the cannon attached to his arm!')
            time.sleep(1)
            enemy_die_roll()

        if adam_smasher_hp < 1:
            admin_clear = 1
            adam_smasher_alive = 0
            key_code = 1
            print(admin_victory)


    if admin_clear == 1:
        move_look_choice()


    admin_clear = 1
    return


def tower_elevator():
    global elevator_des
    global elevator_clear
    global bear_max_hp
    global bear_current_hp
    global tower_room
    print(elevator_des)

    while elevator_clear == 0:
        bear_current_hp = bear_max_hp
        print(exit_elevator_des1)
        clear_screen()
        print(exit_elevator_des2)
        elevator_clear = 1
        clear_screen()
        return


def tower_boss():
    global boss_clear
    global bear_current_hp
    global vox_hp
    global vox_alive
    global foe_die_result
    global die_result
    global victory
    if vox_hp == 30:
        print(vox_desc1)
    while vox_alive == 1 and bear_current_hp >= 1 and vox_hp >=20:
        print('Current HP:', bear_current_hp)
        player_choice = input('It is your turn in combat.\nBEAR or SAMURAI: ')
        player_choice.strip()
        player_choice.lower()

        if player_choice == 'bear':
            bear_die_roll()
            print('You roar savagely and attempt to grapple VOX')
            if die_result >= 6:
                print('You grab the master of darkness and smash him to the ground')
                vox_hp = vox_hp - bear_base_stat
            else:
                print('VOX frees himself from your grasp and twists around to attack.')
        elif player_choice == 'samurai':
            print('Blade meets arm-blade as you strike and parry, you trade blows back and forth.')
            samurai_die_roll()
            if die_result >= 5:
                print('You raise your sword and slash downwards only to cut and change direction at the last second. VOX falls for it and you land a blow.')
                vox_hp = vox_hp - samurai_base_stat
            else:
                print('The attack misses, the battle continues')
        else:
            print('You entered something other than bear or samurai, the bear becomes distracted and your turn in combat is wasted!')

        if vox_hp >= 20:
            print('Vox dashes from right to left with impossible swiftness, he is only a blur as he closes on you. He dashes next to you and spins with both arm blades wide.')
            time.sleep(3)
            enemy_die_roll()

    if vox_hp <= 19 and vox_hp >= 10:
        print(vox_desc2)
    while vox_alive == 1 and bear_current_hp >= 1 and vox_hp >=10 and vox_hp < 20:
        print('Current HP:', bear_current_hp)
        player_choice = input('It is your turn in combat.\nBEAR or SAMURAI: ')
        player_choice.strip()
        player_choice.lower()

        if player_choice == 'bear':
            bear_die_roll()
            print('You see your shadow before you and put vox to the test in a battle of pure strength')
            if die_result >= 6:
                print('You grapple VOX and bite him as hard as you can! Your bite draws drops of flaming blood')
                vox_hp = vox_hp - bear_base_stat
            else:
                print('VOX frees himself from your grasp and twists around to attack.')
        elif player_choice == 'samurai':
            print('Your ready your sword and so does VOX mimicking your every move. You lock blades and activate the lightning attempting to shock VOX with his own sword.')
            samurai_die_roll()
            if die_result >= 5:
                print('He does not pull the blade away fast enough and lighting races around his body!')
                vox_hp = vox_hp - samurai_base_stat
            else:
                print('He pulls away in time but you have found an opening.')
        else:
            print('You entered something other than bear or samurai, the bear becomes distracted and your turn in combat is wasted!')

        if vox_hp >= 10:
            print('VOX mimics your every move until he sees an opening then breaks the pattern!')
            time.sleep(3)
            enemy_die_roll()

    if vox_hp <=10:
        print(vox_desc3)
    while vox_alive == 1 and bear_current_hp >= 1 and vox_hp > 1 and vox_hp < 10:
        print('Current HP:', bear_current_hp)
        player_choice = input('It is your turn in combat.\nBEAR or SAMURAI: ')
        player_choice.strip()
        player_choice.lower()

        if player_choice == 'bear':
            bear_die_roll()
            print('You rage for your family, you rage for the bees, your rage for the future that must never come!')
            if die_result >= 6:
                print('You pound vox mercilessly. He takes massive damage. ')
                vox_hp = vox_hp - bear_base_stat
            else:
                print('The wounded vox coolly steps around your blows.')
        elif player_choice == 'samurai':
            print('You leave the lightning on and the blade glows white hot from the extended heat of the lightning spewing forth. You charge and attack, swinging right and left with every ounce of speed you have.')
            samurai_die_roll()
            if die_result >= 5:
                print('The blows land, slashing burning and electrocuting VOX for massive damage')
                vox_hp = vox_hp - samurai_base_stat
            else:
                print('He staggers back barely defending himself against your blows. ')
        else:
            print('You entered something other than bear or samurai, the bear becomes distracted and your turn in combat is wasted!')

        if vox_hp >= 1:
            print('All attempts at mimicking your attacks are gone. Instead VOX raises his hands and spews forth psychic flame!')
            time.sleep(3)
            enemy_die_roll()

    if vox_hp <= 0:
        vox_alive = 0
        print(victory_des)
        boss_clear = 1


    return


def look():
    global tower_room
    global bee_puzzle_complete
    global bear_base_stat
    global bear_max_hp
    global bear_current_hp
    global samurai_base_stat
    global key_card
    global has_shield

    if tower_room == 'reception':

        print(
            'In the south of the room there is a giant elevator labeled \"PENTHOUSE\" There is one door on either side to. The east door is labeled \"armory\" while the west door is labeled \"hive\".\n')
        print('There are no items.\n')
        move()
        return

    elif tower_room == 'hive':

        if bee_puzzle_complete == 1:
            print(
                'All the business with the reactor seems have to dropped the shield around the the floating elevator keycard. You walk over and swipe it out of the field it is hovering in. You have obtained the keycard!')
            key_card = 1
            move()
            return
        elif bee_puzzle_complete == 0:
            print('The keycard floats behind a glowing shield. You reach out to grab it and are stopped by the field. Perhaps you can do something in another room to gain access to the keycard')
            move()
            return

    elif tower_room == 'reactor':
        #easter egg this room allows the player to increase HP and bear to infinite by looking here more than once
        print('The emergency weapons closet in the corner of the room swung open when the power turned back on. You investigate the contents of the')
        print('locker and you find an energy shield! You strap the small lightly glowing teal disk to your arm and activate it. The world becomes slightly muffled for ')
        print('just a moment as your entire body is coated in a thin energy shield. Max HP + 5, BEAR +1')
        has_shield = 1
        bear_current_hp = bear_current_hp + 5
        bear_base_stat += 1
        bear_max_hp = bear_max_hp + 5
        move()
        return

    elif tower_room == 'armory':
        print(bear_armor)
        bear_current_hp = bear_current_hp + 5
        bear_max_hp = bear_max_hp + 5
        bear_base_stat = bear_base_stat + 1
        move()
        return

    elif tower_room == 'training':
        print('You have already collected the shock attachment. North is back to the armoury. To the south is an unmarked passageway. ')
        move()
        return

    elif tower_room == 'elevator':
        print('You have already eaten the food. It was delicious.')
        move()
        return
    elif tower_room == 'lab':
        print('Nothing more than paper and printers. You do notice some stress balls shaped like little lobsters and some terrible office candies but nothing else. There is no sign of the ritual room. ')
        move()
        return
    elif tower_room == 'admin':
        print('There is nothing else in this room except the wreckage of Smasher and the cubicles.')
        move()
        return


def move():
    global tower_room

    while tower_room == 'reception':
        move_choice = input('Which direction will you move in?\n')
        move_choice = move_choice.strip()
        move_choice = move_choice.lower()

        if move_choice == 'north':
            print('The laser gate has snapped shut behind you. There is no way out of the tower. You must destroy VOX.')

        elif move_choice == 'south':
            if key_card == 0 or key_code == 0:
                print(no_elevator_access)
                tower_room = 'reception'
                return
            elif key_card == 1 and key_code == 1:
                tower_room = 'elevator'
                os.system('cls')
                return

        elif move_choice == 'east':
            tower_room = 'armory'
            os.system('cls')
            return

        elif move_choice == 'west':
            tower_room = 'hive'
            os.system('cls')
            return

        else:
            print('Invalid input.')

    while tower_room == 'hive':
        move_choice = input('Which direction will you move in?\n')
        move_choice = move_choice.strip()
        move_choice = move_choice.lower()

        if move_choice == 'north':
            print('There are no doors north.')

        elif move_choice == 'south':
            tower_room = 'reactor'
            os.system('cls')
            return

        elif move_choice == 'east':
            tower_room = 'reception'
            os.system('cls')
            return

        elif move_choice == 'west':
            print('There are no rooms west')

        else:
            print('Invalid input.')

    while tower_room == 'reactor':
        move_choice = input('Which direction will you move in?\n')
        move_choice = move_choice.strip()
        move_choice = move_choice.lower()

        if move_choice == 'north':
            tower_room = 'hive'
            os.system('cls')
            return

        elif move_choice == 'south':
            print('There are no rooms south.')

        elif move_choice == 'east':
            print('There are no rooms east')


        elif move_choice == 'west':
            print('There are no rooms west')

        else:
            print('Invalid input.')

    while tower_room == 'armory':
        move_choice = input('Which direction will you move in?\n')
        move_choice = move_choice.strip()
        move_choice = move_choice.lower()

        if move_choice == 'north':
            print('There are no doors north.')

        elif move_choice == 'south':
            tower_room = 'training'
            os.system('cls')
            return

        elif move_choice == 'east':
            print('There are no rooms east')


        elif move_choice == 'west':
            tower_room = 'reception'
            os.system('cls')
            return

        else:
            print('Invalid input.')

    while tower_room == 'training':
        move_choice = input('Which direction will you move in?\n')
        move_choice = move_choice.strip()
        move_choice = move_choice.lower()

        if move_choice == 'north':
            tower_room = 'armory'
            os.system('cls')
            return

        elif move_choice == 'south':
            tower_room = 'lab'
            os.system('cls')
            return

        elif move_choice == 'east':
            print('There are no rooms east.')

        elif move_choice == 'west':
            print('There are no rooms west')

        else:
            print('Invalid input.')

    while tower_room == 'lab':
        move_choice = input('Which direction will you move in?\n')
        move_choice = move_choice.strip()
        move_choice = move_choice.lower()

        if move_choice == 'north':
            tower_room = 'training'
            os.system('cls')
            return

        elif move_choice == 'south':
            print('There are no rooms south.')

        elif move_choice == 'east':
            print('There are no rooms east')

        elif move_choice == 'west':
            tower_room = 'admin'
            os.system('cls')
            return

        else:
            print('Invalid input.')

    while tower_room == 'admin':
        move_choice = input('Which direction will you move in? East is back the way you came. There are no other doors.\n')
        move_choice = move_choice.strip()
        move_choice = move_choice.lower()

        if move_choice == 'north':
            print('There are no doors north.')

        elif move_choice == 'south':
            print('There are no rooms south')

        elif move_choice == 'east':
            tower_room = 'lab'
            os.system('cls')
            return

        elif move_choice == 'west':
            print('There are no rooms west')

        else:
            print('Invalid input.')


def clear_screen():

    move_bool = 0

    while move_bool != 'clear' and bear_current_hp >= 1:
        move_bool = input('When you are ready to tidy up the screen and continue on your journey enter clear:')
        clear_tutorial.strip()
        clear_tutorial.lower()
        if clear_tutorial == 'clear':
            os.system('cls')
        else:
            print('that is not valid')

def move_look_choice():
    move_look = str(input('Do you want to look around or move (enter look or move)?\n'))
    move_look = move_look.lower()
    move_look = move_look.strip()

    if move_look == 'look':
        look()
        return
    elif move_look == 'move':
        move()
        return
    else:
        print('Enter valid choice\n')


def play_again():
    global bear_base_stat
    bear_base_stat = int(1)  # bear base stat bonus to bear checks
    global samurai_base_stat
    samurai_base_stat = int(1)  # this is how much will be add to samurai checks
    global bear_current_hp
    bear_current_hp = int(10)  # kick off HP pool
    global bear_max_hp
    bear_max_hp = int(10)  # This is the max hp from the start of the game
    global player_location
    player_location = 'wasteland'  # Start Room
    global vox_hp  # boss hp
    vox_hp = int(30)
    global die_result  # reset the dice
    die_result = int(0)
    global num_scavengers  # respawn the scavengers
    num_scavengers = int(3)
    global has_sword  # take away the sword
    has_sword = int(0)
    global cyber_guard_alive
    cyber_guard_alive = 1
    global key_code  # reset elevator code
    key_code = int(0)
    global key_card  # reset keycard
    key_card = int(0)
    global bee_puzzle_complete
    bee_puzzle_complete = int(0)
    global has_shield
    has_shield = int(0)
    global reception_clear
    reception_clear = int(0)
    global hive_clear
    hive_clear = int(0)
    global reactor_clear
    reactor_clear = int(0)
    global armory_clear
    armory_clear = int(0)
    global training_clear
    training_clear = int(0)
    global lab_clear
    lab_clear = int(0)
    global admin_clear
    admin_clear = int(0)
    global elevator_clear
    elevator_clear = int(0)
    global adam_smasher_hp
    adam_smasher_hp = 15
    global adam_smasher_alive
    adam_smasher_alive = int(1)
    global victory
    victory = 0
    global num_psychic_salmon
    num_psychic_salmon = int(2)
    global tower_room
    tower_room = ''

def easter_egg_state():
    global easter_egg

    if bear_max_hp >= 35:
        easter_egg = 1
        return
    else:
        return




# Pregame-warning------------------------------------------------------------------------------------------------------#
print('This game must be run in a large CMD window')  # loading screen doesnt work without enough character space
time.sleep(4)  # gives time for the user to fullscreen
os.system('cls')  # clear instructions
loading_screen()  # run loading screen

# Start-prologue---------------------------------------------------------------------------------------------------------#
print(intro_message1)  # sets up the story

clear_intro = ''
while clear_intro != 'clear' and bear_current_hp >= 1:
    clear_intro = input('When you are ready to tidy up the screen and continue on your journey enter clear:')
    clear_intro.strip()
    clear_intro.lower()
    if clear_intro == 'clear':
        os.system('cls')
    else:
        print('that is not valid')

tutorial()  # tutorial start

clear_tutorial = ''
while clear_tutorial != 'clear' and bear_current_hp >= 1:
    clear_tutorial = input('When you are ready to tidy up the screen and continue on your journey enter clear:')
    clear_tutorial.strip()
    clear_tutorial.lower()
    if clear_tutorial == 'clear':
        os.system('cls')
    else:
        print('that is not valid')

while True:

    victory_cons()
    os.system('cls')

    print(wasteland_des)
    print(scavenger_des)

    prologue()

    travel_to_gate()

    gate()

#Official-project-game-start-------------------------------------------------------------------------------------------------------------------------------#
    while player_location == 'tower' and bear_current_hp >= 1:

        while tower_room == 'reception':
            if reception_clear == 0:
                print(reception_des)
                print(cyber_guard_des)
                tower_reception()
            elif reception_clear == 1:
                print('You have cleared this room, there may still be items. The Elevator is to the south, Hive is to the west, and armory to the east')
                move_look_choice()

        while tower_room == 'hive':
            if hive_clear == 0:
                tower_hive()
            elif hive_clear == 1:
                print('You have cleared this room, there may still be items. Reception is to the east, Reactor is to the south')
                move_look_choice()

        while tower_room == 'reactor':
            if reactor_clear == 0:
                tower_reactor()
            elif reactor_clear == 1:
                print('You have cleared this room, there may still be items. The hive is to the north, there are no other rooms in this wing')
                move_look_choice()

        while tower_room == 'armory':
            if armory_clear == 0:
                tower_armory()
            elif armory_clear == 1:
                print('You have cleared this room, there may still be items. Reception is to the west, training is to the south.')
                move_look_choice()

        while tower_room == 'training':
            if training_clear == 0:
                tower_training()
            elif training_clear == 1:
                print('You have cleared this room, there may still be items. Armory is to the north, there is a dark hallway to the south.')
                move_look_choice()

        while tower_room == 'lab':
            if lab_clear == 0:
                print(training_des_exit)
                clear_screen()
                tower_lab()
            elif lab_clear == 1:
                print('You open the same door you came in. Instead of a portal to another dimension or flaming ruin you find a printer and shelves stacked with reams of paper. Then another door into training.')
                print('You have cleared this room, there may still be items. Training is to the north, administration is to the west.')
                move_look_choice()

        while tower_room == 'admin':
            if admin_clear == 0:
                tower_admin()
            elif admin_clear == 1:
                print('You have cleared this room, there may still be items. There is a door to the east, there are no other rooms in this wing.')

        while tower_room == 'elevator':
            if key_card == 0 or key_code == 0:
                print(no_elevator_access)
                tower_room = 'reception'
            else:
                tower_elevator()
                tower_room = 'boss'

        while tower_room == 'boss':
            if boss_clear == 0:
                tower_boss()
            elif boss_clear == 1:
                easter_egg_state()
                victory = 1
                clear_screen()
                victory_screen()
                victory_cons()

    continue
