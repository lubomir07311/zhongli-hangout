define t = Character("Traveler", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])
define p = Character("Paimon", color="#AFEEEE", who_outlines=[(2, "#000", 0, 0)])
define x = Character("Xiuhua", color="#FFFFFF", who_outlines=[(2, "#000", 0, 0)])
define u = Character("???", color="#FFFFFF", who_outlines=[(2, "#000", 0, 0)])

$ end_txt = ""

# The game starts here!

label start:

    scene bg room
    play music "audio/bg_liyue_1.ogg"

    t "Good morning, Paimon."
    p "Five more minutes, please."
    t "You said that five minutes ago. Come on, it's a beautiful day outside."

    show paimon happy with dissolve

    p "It better be. Paimon barely got any sleep last night with all the thunder and lightning."
    t "It was pretty scary, wasn't it. {p}I haven't seen a storm like that in a while. Especially over Liyue."
    t "I'm glad we could find a room at the Baiju Guesthouse for the night. {p}I don't want to think what could have happened to us if we camped out in the open."
    p "Paimon doesn't like being wet. {p}Remember the time when you fished Paimon up from that lake?"
    p "Paimon was so grateful to be on dry land again that Paimon vowed to be your guide in the world of Teyvat. And look at us now."
    t "If I recall correctly, Paimon also stole some of my food at the time."
    p "Hey, it wasn't stealing. You offered and Paimon accepted politely. Besides, you are a far better chef than Paimon."
    p "Speaking of food, how about some breakfast?"
    p "I suggest we go downstairs and grab something to eat."

    jump choices

label choices:

    menu:
        p "{cps=0}I suggest we go downstairs and grab something to eat. "

        "Go Downstairs for Breakfast":
            jump choices_in

        "Go Out for Breakfast":
            jump choices_out

label choices_in:
    t "I heard that the kitchen at the Baiju Guesthouse serves the best Fullmoon Egg in Liyue."
    p "Mmmm.. Fullmoon Egg. Fresh fish, mixed with the finest shrimp, diced and minced to perfection. Stuffed in an eggy dough and steamed over medium heat. "
    t " Um, Paimon, you're drooling."
    "Paimon wipes her drool off"
    p "Okay then, let's get going."
    $ end_txt = "Paimon and the Traveler head downstairs for breakfast..."
    call end_screen(end_txt) from _call_end_screen
    jump downstairs
    return

label choices_out:
    t "Would you like to go out for food, instead of eating downstairs?"
    p "This sounds lovely. Paimon has almost forgotten the taste of Wanmin Restaurant's Boiled Fish. Can we go to Wanmin Restaurant, Traveler? Please please please?"
    t "Well the Wanmin Restaurant is on the way to the Adventurer's Guild. Which is where we should head after breakfast anyway."
    t "I guess we are taking down two birds with one stone. But I think that the Boiled Fish might be a bit too heavy for breakfast. I might stick to some good old Mora Meat. "
    p "Nothing is too heavy when Paimon is having it. Hecc, Paimon might get a side of Mora Meat to go with that Boiled Fish as well haha."
    t "Oh Paimon, you never cease amaze me. Would you be able to assist with the daily commissions that the Adventurer's Guild has for us after all that food?"
    p "No biggie. Paimon can float, remember. It sure is a blessing."
    t "Yeah, how does that work anyway?"
    p "It just does ... hehe... Now about that breakfast..."
    $ end_txt = "Paimon and the Traveler head to the Wanmin Restaurant..."
    call end_screen(end_txt) from _call_end_screen_1
    return

label downstairs:
    scene bg downstairs with fade
    show paimon happy at left with dissolve
    pause 1
    show xiuhua happy at center with dissolve

    u "Good morning! I'm Xiuhua and I will be your waitress this morning. Have you decided what you are having today?"
    p "Two portions of Fullmoon Egg for Paimon, please. And a glass of water. What are you having, Traveler?"
    t "What?! I thought you ordered two Fullmoon Eggs - one for each of us. Guess you are eating both portions then..."
    x "*chuckles*"
    x "Such a small person with a big appetite. There's plenty of Fullmoon Egg in the kitchen for both of you. Unless you want to try something else?"
    x "We could also offer you Jueyun Guoba, Noodles with Mountain Delicacies or Stir-Fried Filet. What will it be?"

    menu:
        x "{cps=0}We could also offer you Jueyun Guoba, Noodles with Mountain Delicacies or Stir-Fried Filet. What will it be?"

        "Jueyun Guoba":
            $ food = "Jueyun Guoba"

        "Noodles with Mountain Delicacies":
            $ food = "Noodles with Mountain Delicacies"

        "Stir-Fried Filet":
            $ food = "Stir-Fried Filet"


    x "Excellent choice. So all together - one [food] for you and two Fullmoon Eggs with a glass of water for the little one."
    p "Hey! Who are you calling little? I'll have you know that Paimon has a very big personality... and appetite."
    "Paimon's stomach rumbles"
    p "Please hurry with the order. Paimon is starving."
    x "Oh, my. Your order will be with you shortly."
    hide xiuhua with dissolve

    "Xiuhua leaves your table"
    show paimon happy at center with move
    p "So what's today's agenda? Do we have any important meetings to attend? Maybe some treasure horders to whoop up? "
    t "I don't know... The treasure hoarders have been quiet lately. Ever since the treasure hunt during the Lantern Festival, we haven't seen much activity from them. "
    t "As for meetings, nothing scheduled for today. We should probably head to Lan and Katheryne at the Adventurer's Guild. Check if there are any daily commissions for us. "
    p "Paimon really hopes Lan doesn't send us looking for that sword again. We've look everywhere for it without any success. Guess they call it the *Unseen* Razor for a reason."
    t "Yeah, that's a bummer. I hate disappoining Lan everytime we clean up the monsters and there is no sign of the sword. Let's hope the next hint will lead us straight to it."
    p "That's the spirit! Everytime we go out looking for it, Paimon imagines wielding the sword. *Swoosh* *Swash* Left. Right. Bonk that hilichurl on the head... hehe..."
    t "Paimon! I didn't know you wanted to wield a sword. Why haven't you said anything to me before?"
    p "Well Paimon doesn't really want to. Paimon likes being on the sidelines while you are fighting, doing the best cheering possible."
    p "You can't deny that Paimon helps you in battle mentally...just... not physically."
    p "Anyway, Paimon is not strong enough to lift a sword, but it is fun to imagine."
    t "Maybe we can check back with the blacksmith Wagner in Mondstadt."
    t "We asked him to design a Paimon sized sword once as a joke. If you are up to the challenge, we can maybe get him to actually make you one?"
    p "Ehe..no need. The sidelines are just fine for now."
    show xiuhua happy behind paimon:
        xalign 0.0 yalign 0.0
        linear 1.5 xalign 1.0
    "{cps=0}Xiuhua brings the food to the table"

    x "One [food] for you and two Fullmoon Eggs with a glass of water for you. Enjoy your meal!"
    p "Thank you, Xiuhua!"
    t "Thank you very much!"
    p "Mmmm...This smells so tasty."
    t "Dig in Paimon. Before it gets too cold. Once we are finished here we'll head to the Adventurer's Guild and check out those commissions."
    p "Mhm... Shoundsh gud... *gulp*"

    $ end_txt = "Paimon and Traveler head to the Adventurer's Guild after breakfast..."
    call end_screen(end_txt) from _call_end_screen_2
    return

label end_screen(end_txt):

    image bg black = "#000"

    scene bg black with Fade(0.5, 0, 0)
    show text "{size=44} [end_txt]" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    return
