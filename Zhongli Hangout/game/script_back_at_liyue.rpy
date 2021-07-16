label in_front_of_guesthouse:
    scene bg guesthouse_night
    show paimon happy at right
    show zh happy at left
    t "Look at how dark the sky is... I didn't think we would make it in time!"
    z "And the wind has picked up significantly. It is going to be a heavy storm indeed. Are you going to be staying at the Baiju Guesthouse again?"
    t "Yes, I think it would be best. We can get a good night's sleep and pick up where we left off tomorrow morning."
    p "Paimon is not going anywhere before this thing passes. Even if it takes a week!"
    z "Relax, Paimon. It looks like the storm will be heavy but brief. There are a lot of dark clouds but if you look in the distance, you can see their end."
    t "So, Zhongli, are you thinking the storm will pass until the morning?"
    z "Certainly. Unless the wind changes direction and decides to keep the clouds around for longer. But that's highly unlikely."
    t "Okay so the original plan stands. We will meet up tomorrow morning in front of the Adventurers' Guild. Granted there is no rain in the morning, we can reconvene and resume the investigation?"
    z "You've got it! But I better get going before the rain starts. It looks like it could happen any moment now!"
    p "Okay... Hurry home, Zhongli. We'll see you tomorrow!"
    z "Be safe tonight! Both of you."
    p "B-bye~"
    $ end_txt = "The morning after..."
    call end_screen(end_txt) from _call_end_screen_21
    jump day_after_liyue

label day_after_liyue:
    play music "audio/bg_liyue_1.ogg"
    scene bg adv_far
    show paimon happy at right
    if stayed_in_mondstadt:
        show zh happy at left
        z "Mmm~ there's no place like home."
        t "Yeah... you can say that again."
        z "Oh, I'm sorry, I didn't mean to upset you. I just meant it's good to be back in Liyue..."
        t "Don't worry, it's okay. I still have a lot to do here before going home anyway."
        p "Mhm~ and one of the things you need to do is bring this investigation to an end!"
        z "Paimon's right! We need to get more clues to keep us going."
        t "I know, but where do we find them? We've already looked at the crime scene twice, and we've gotten all the useful information out of it."
        z "Well, we eliminated all the suspects from Mondstadt but we've been away from Liyue for a few days now. Maybe there is some development within Liyue that we are not aware of."
        p "Zhongli, do you think we should ask the Millelith?"
        z "The Millelith might not be the best affiliation to ask. They have stricter protocols and might not be willing to give any information to us."
        p "Is there another central hub for information then?"
        t "How about the Adventurers' Guild?. All adventurers are required to check in with the Adventurers' Guild. Which means the coordinator will have a lot of information about events going around Liyue."
        z "You are absolutely right, Traveler!"
        p "And as members of the Adventurers' Guild, we can access that information. Especially if we are trying to eliminate a threat!"
        t "That's right! I see Lan, the branch master is around. We can go talk to her."
        z "Sounds good! Lead the way!"
        scene bg lan
        show paimon happy at center with dissolve
        show zh happy at right with dissolve
        p "Hey, Lan!"
        l "Well, well, well. What do we have here? Paimon, Traveler, you brought extra company."
        p "This is Zhongli, he is helping us with an investigation."
        l "Well, this is a nice search party you've got together. Unfortunately, I don't have any new leads regarding the Unseen Razor."
        p "We are not here for that commission this time. In fact, we are not after any commission. We were out of town for a few days and were wondering what the latest news were around here."
        l "Not sure when you left, but Liyue is in a pretty serious shock after the recent attacks."
        t "Attacks? As in plural?"
        l "Yes! It started with the Wanmin Restaurant a few days ago."
        p "We were here for that. We are trying to help Chef Mao catch the person responsible."
        l "Well, the Millelith is also on the job and has been for the past few days. Unfortunately without any success. Seems like whoever trashed the restaurant is now targeting other small local businesses."
        t "Please, tell us more! We need as much information as possible!"
        l "I don't have any official reports but the latest news is that someone broke in the Scent of Spring a couple of nights ago. They damaged most of the goods inside. There are rocks and shattered perfume bottles everywhere."
        p "Uh-oh ... rocks you say..."
        l "Yeah, similar to the ones thrown in the Wanmin Restaurant. The Millelith have been restless. Increasing patrol duty. Investigating the whole situation. It's out of control."
        t "I think it's time to take matters in our hands once again!"
        z "Sounds like whoever struck once is not afraid to do it again. And in such a short time frame. And just a couple of streets away."
        t "At least we can be almost certain that whoever did that is still around. Maybe planning another attack? If we can figure out their pattern, maybe we can prevent the next one."
        l "The pattern so far is that it always happens in the middle of the night and there are always rocks of various shapes and sizes involved."
        z "Under the night's cover. That's smart. Lan, you said that it happened a couple of nights ago. Do you know which night exactly?"
        l "Yes, of course. It was the night of the second big storm over Liyue. There've been only two recently."
        p "Heey~ the night before the attack of the Wanmin Restaurant was stormy as well, wasn't it?"
        l "Yes, that was the night of the first big storm."
        t "Paimon! You're right! The pattern begins to form. I wonder if the Millelith have connected the dots yet."
        l "They probably have. Their highest ranks are involved now."
        z "Now that we have a possible pattern for the timing, let's go and investigate the method of execution."
        t "Are you saying we should visit the crime scene?"
        z "Yes, and better get going fast! The Millelith might have already messed it up since it has been sitting there for a couple of days."
        p "Oh yes, yes, yes. Let's go look at some more weird rocks."
        t "Someone is eager."
        p "Eager to catch some bad guys! Now that we have more information, Paimon feels like it will be easier."
        z "Don't get your hopes up, Paimon. It could all be just a coincidence."
        p "There's no such thing as coincidences. It's a pattern!"
        z "If you say so... just don't want to see you disappointed if we hit another dead end."
        p "Not this time! Hurry, before the Millelith messes up the crime scene!"
        hide paimon happy with dissolve
        t "Thanks for the information, Lan. Once we are done with this investigation we will resume the search for the Unseen Razor. It is bound to pop up some place!"
        l "Thanks, Traveler. I hope you're right. And good luck with your current investigation!"
        t "Thanks!"
        jump outside_shop
    else:
        p "Ughh~ Where is he?"
        t "Don't worry, Paimon. He will be here soon."
        p "It's not typical for Zhongli to be late."
        t "Come on, cut him some slack. The trip to Mondstadt must have brought back memories."
        p "Okay, okay~ but Paimon is eager to pick up the investigation. We are at a dead end... What's our next move?"
        t "We'll decide together, once Zhongli arrives. Until then, just try to enjoy the sun while it's out."
        p "I guess you've got a point. With so many storms recently, Paimon should be happy to floating in the sun."
        t "Hehe~ that's right. But don't get too comfortable. I see someone in the distance coming our way."
        p "Wait, who is it? Paimon can't see that far!"
        show paimon happy at center with move
        show zh happy at right with dissolve
        z "Good morning!"
        p "Oh.. if it isn't {i}Mr. I-can-show-up-whenever-I-want-to.{/i}"
        z "Sorry to keep you waiting this morning. I had some errands to run earlier."
        t "Don't mind Paimon. She is just grumpy because we are going nowhere with our investigation..."
        z "Ah, I see. Well, I'm here now. We can get back on it. Do you have any new information?"
        t "No, we haven't asked around yet. We were waiting for you since we are partners in this!"
        z "Oh, I'm flattered. But I'm just a consultant here. You are the lead investigators on this case."
        p "We might be, but Paimons list is pretty dry at this point. We need to find some new suspects!"
        t "Well, I can see Lan over there by the Adventurers' Guild. She is a very resourceful individual. How about asking her if there has been any progress within Liyue?"
        z "Excellent idea, Traveler. All adventurers report to the Adventurers' Guild daily. So if anyone has seen anything unusual, Lan would know!"
        p "Paimon's list is ready to be filled once again! Let's go talk to Lan!"
        scene bg lan
        show paimon happy at center with dissolve
        show zh happy at right with dissolve
        p "Hey, Lan!"
        l "Well, well, well. What do we have here? Paimon, Traveler, you brought extra company."
        p "This is Zhongli, he is helping us with an investigation."
        l "Well, this is a nice search party you've got together. Unfortunately, I don't have any new leads regarding the Unseen Razor."
        p "We are not here for that commission this time. In fact, we are not after any commission. We were out of town for a few days and were wondering what the latest news were around here."
        l "Not sure when you left, but Liyue is in a pretty serious shock after the recent attacks."
        t "Attacks? As in plural?"
        l "Yes! It started with the Wanmin Restaurant a few days ago."
        p "We were here for that. We are trying to help Chef Mao catch the person responsible."
        l "Well, the Millelith is also on the job and has been for the past few days. Unfortunatly without any success. Seems like whoever trashed the restaurant is now targeting other small local businesses."
        t "Please, tell us more! We need as much information as possible!"
        l "I don't have any official reports but the latest news is that someone broke in the Scent of Spring last night. They damaged most of the goods inside. There's rocks and shattered perfume bottles everywhere."
        p "Uh-oh ... rocks you say..."
        l "Yeah, similar to the ones thrown in the Wanmin Restaurant. The Millelith have been restless. Increasing patrol duty. Investigating the whole situation. It's out of control."
        t "I think it's time to take matters in our hands once again!"
        z "Sounds like whoever struck once is not afraid to do it again. And in such a short time frame. And just a couple of streets away."
        t "At least we can be almost certain that whoever did that is still around. Maybe planning another attack? If we can figure out their pattern, maybe we can prevent the next one."
        l "The pattern so far is that it always happends in the middle of the night and there are always rocks of various shapes and sizes involved."
        z "Under the night's cover. That's smart. Last night there was a storm as well, so the thunder and lightning could provide visual and audio distractions."
        p "Heey~ the night before the attack of the Wanmin Restaurant was stormy as well, wasn't it?"
        t "Paimon! You're right! The pattern begins to form. I wonder if the Millelith have connected the dots yet."
        l "They probably have. Their highest ranks are involved now."
        z "Now that we have a possible pattern for the timing, let's go and investigate the method of execution."
        t "Are you saying we should visit the crime scene?"
        z "Yes, and better get going fast, while it's fresh!"
        p "Oh yes, yes, yes. Let's go look at some more weird rocks."
        t "Someone is eager."
        p "Eager to catch some bad guys! Now that we have more information, Paimon feels like it will be easier."
        z "Don't get your hopes up, Paimon. It could all be just a coincidence."
        p "There's no such thing as coincidences. It's a pattern!"
        z "If you say so... just don't want to see you disappointed if we hit another dead end."
        p "Not this time! Hurry, before the Millelith messes up the crime scene!"
        hide paimon happy with dissolve
        t "Thanks for the information, Lan. Once we are done with this investigation we will resume the search for the Unsees Razor. It is bound to pop up some place!"
        l "Thanks, Traveler. I hope you're right. And good luck with your current investigation!"
        t "Thanks!"
        jump outside_shop

label outside_shop:
    scene bg yinger
    show paimon happy at center with dissolve
    show zh happy at left with dissolve

    p "Hello, Ying'er! So sorry to hear your shop has been attacked."
    y "Not only has it been attacked, but the Millelith won't even let me in. They say it's a crime scene and until they gather all the evidence, they won't let me clean it up."
    z "Perhaps I can do something about it."
    y "Oh... what is it that you can do to make the Millelith just go away?"
    z "They won't go away, but I might persuade them to at least let you in the shop and start cleaning up."
    y "It's a start I suppose. But so many of my perfumes have just been smashed. Now my backlog of orders would have to wait until I replenish the ones that were ready for shipment..."
    t "I'm sorry to hear that, Ying'er. We are here to help though!"
    z "While you three are having a chat, I'll go talk to the Millelith - see if I can get us inside."
    hide zh happy with dissolve
    t "In order for us to help you, we need to ask you a couple of questions. Is that okay with you?"
    y "I've already told the Millelith everything I know. Haven't you read the report?"
    p "We are not working with the Millelith on this. We are conducting an investigation of our own. So far we have been able to eliminate a lot of suspects! With your help, we can narrow it down even further!"
    t "That's right. We've been on the case for quite some time now."
    y "Surely you have suspects by now. Tell me who they are and I will give you all of their orders and any information I have on them regarding their business with the Scent of Spring."
    p "Ehe~ we can't... um... disclose the information we might or might not have on any suspects. But you can help us in other ways. Like, have you seen anybody unusual around here? Somebody who might not be physically strong?"
    y "No, not really. I've seen a couple of more Millelith patrolling the area after the attack on the Wanmin Restaurant but that's about it. And a few of the kids like to play in the are but I doubt they can hurl those rocks inside."
    p "Hmm... the kids you say... Any of them dislike you?"
    y "What?! No! I even made a light and refreshing perfume for Little Lulu. The kids love me!"
    p "Is there a chance that Litte Lulu didn't like her perfume?"
    y "Why would you say that? Do you think my perfumes are not good enough?"
    t "No, no. Walking by here I always get a good tingling sensation in my nose. Paimon wants to know if there is perhaps somebody who would benefit from trashing your business?"
    y "I can't think of anybody off the top of my head. Everybody in Liyue loves their fragrances. I have a lot of repeat customers as well!"
    t "Seems a bit odd for somebody to attack a restaurant and a perfume shop. Assuming it was the same person or people both times. You are two very different lines of business."
    y "Well it is highly likely it was the same people, because I heard that some large rocks smashed the Wanmin Restaurant's oven the same way they smashed my shelves of glass bottles."
    t "Yes, yes. It seems like the method of execution was the same."
    p "And Paimon thinks that there aren't that many people nearby capable of committing such a crime. We will catch them, don't you worry! It would have been convenient if someone disliked you though."
    t "Paimon! That's not a nice thing to say! You should apologize to Ying'er right now!"
    p "Sorry, Ying'er. Detective Paimon can be mean at times."
    y "Apology accepted. I just hope you catch the people responsible and bring them to justice. I would like my fair share of compensation for the damage they've caused and the delays that will occur because of their actions."
    show zh happy at left with dissolve
    z "Traveler, Paimon, I got us in. The Millelith have agreed for us to go inside the shop and have a look at the rocks."
    y "What about me? I need to start cleaning up as soon as possible."
    z "I've spoken to the Millelith about that as well. They said that the earliest you can access your shop would be tomorrow."
    y "Unbelievable! I've gotten nothing from then and you walk over and tell me I can have my shop back tomorrow?"
    z "What can I say - I'm a person of many talents and persuasion is one of them."
    y "Thank you for your help. I'll be on my way now if there's nothing else I can help you with."
    p "It seems like you don't have enemies around here or people that would benefit from interrupting your business, but if you think of anyone, please, let us know."
    y "Will do! And good luck with your investigation."
    t "Thanks! So, Zhongli, lead the way I guess!"
    z "Follow me!"
    scene bg shop_trashed with dissolve
    show zh happy at left
    show paimon happy at right
    p "Look at the mess... It's worse than the Wanmin Restaurant. Whoever did that surely knew how to strike. Ying'er would be in here cleaning up for days!"
    z "Never mind the mess, Paimon. We need to focus on the actual evidence - the rocks."
    p "You're right. Just to confirm they are similar to the ones in the Wanmin Restaurant, Traveler, would you do us the honors of using your elemental sight once again, please?"
    t "Sure! Hold on."
    play sound "audio/sight_effect.wav" volume 10
    pause 0.1
    scene bg shop_traced with flashbulb
    pause 1
    scene bg shop_trashed with flashbulb
    show zh happy at left
    show paimon happy at right
    t "Yep, the stones have elemental traces on them. Just like the ones at the Wanmin Restaurant."
    z "Yes, it seems like these stones have also been conjured."
    p "Hey, look that one kinda looks like a boar hehe~"
    t "Is everything a joke to you, Paimon? Can't you take this investigation a bit more seriously?"
    z "No, no. Paimon's got a point. Look closer. Here's the snout, and a couple of broken tusks and you can clearly see the remains of what look like boar ears broken off to the side."
    t "Zhongli, are you seeing thing as well? What's gotten into you two?"
    p "No, Traveler, come! Look closer. Next to the boar - this one looks like half a squirrel."
    z "And there's the other half - on the other side of the broken shelf."
    t "Oohh... I see. The shapes do vaguely resemble animals. What a coincidence!"
    z "One or two might be a coincidence, but look here, beneath this pile of rubble."
    t "Are those crab claws?"
    p "Mhm~ And there's a squirrel's tail if Paimon's not mistaken."
    t "So back at the Wanmin Restaurant, you weren't being silly, Paimon. There were actual clues and I just dismissed them quickly."
    p "You should trust Paimon more! Paimons has eagle eyes! They see all!"
    z "So what do we have here? Boars, squirrels, crabs..."
    p "That looks like a crane's beak broken in half."
    z "...crane..."
    t "Hey, does that look like an animal to you guys? There's an eye but the shape is very strange. Kinda looks like a small snake?"
    p "Hm~ Oh Paimon knows! That's an {i}electric eel{/i}!"
    t "An electric eel? What's an electric eel?"
    p "Electric eels are a special type of fish that is known for their ability to stun their prey by generating electricity."
    z "Basically, they are the next evolutionary step from the electro slimes. They have minor innate electro abilities but can be a serious threat if not handled properly."
    p "But if handled properly, they can make a very tasty snack!"
    t "That's the first I'm hearing of them. How come the Liyue cuisine does not cook them then?"
    z "See electric eels are exclusive to the region of Inazuma. Liyue just never imported them or adopted them in the local cuisine."
    t "But if they are exclusive to Inazuma, what are they doing in Ying'er's perfume shop? Petrified?"
    p "We already know that these rocks were conjured. Do you think somebody actually let wild animals run loose in the shop and once they were done trashing the place - petrified them?"
    z "Highly unlikely. It looks like the animals are Geo constructs themselves."
    p "You mean to tell us that just like Rhodeia the Oceanid is able to conjure Hydro mimics, somebody is conjuring Geo mimics and letting them destroy local businesses?"
    z "It is a good theory, don't you think?"
    p "But why? And more importantly, who?!"
    z "This is something we need to figure out for ourselves."
    t "See, I was confused when I first saw the Geo animals. You said that the electric eels are exclusive to the region of Inazuma, right?"
    z "That's correct."
    t "And for someone to conjure an animal, they must have seen it before, right?"
    p "Paimon likes where you're headed, Traveler. Keep going!"
    t "So for someone to conjure an eel, they must have seen an eel. That means they must have been to Inazuma!"
    z "That's some impressive detective skills, Traveler."
    t "I would not have done it without you! Now we can narrow down the list of suspects quite a lot."
    z "There's just one problem. As we know, Inazuma is a closed nation. No one has been there for a while and there are no Inazumans in Liyue as far as I'm aware. Do you know of anybody from Inazuma in Liyue?"
    jump choices_liyue

label choices_liyue:

    $ globals()['menu_yalign'] = 0.6
    menu:
        z "{cps=0}There's just one problem. As we know, Inazuma is a closed nation. No one has been there for a while and there are no Inazumans in Liyue as far as I'm aware. Do you know of anybody from Inazuma in Liyue?{/cps}"

        "Bibo":
            p "The fishmonger? No - he is local, although he did say he once rescued a woman from Inazuma and that was the last time someone left Inazuma illegally."
            jump choices_liyue_no_bibo
        "Ivanovich":
            p "No, you silly goose, Ivanovich is a traveling merchant from Snezhnaya. He gave us that Shivada Jade Fragment, remember?"
        "Changshun":
            z "No, she is has pure Liyue blood running through her veins. Woman thinks she can get rich by selling potatoes, cheese and sugar. Good luck to her!"
        "Xingxi":
            z "The Mingxing Jewelry owner? It is a family business that has been in Liyue for hundreds of years. Some even call it the Rex Lapis of the market for precious stones. She can't be Inazuman."
        "Linlang":
            z "The Xigu Antiques owner? She is one of the biggest Liyue patriots there are. She studied ancient Liyue history. She and Soraya share a passion for the antiques."
            p "The only odd thing about her is that glowing piece of rock she gave us. She said it came from a star but the ore suppliers tell crazy stories just to sell their stock these days."
        "Atsuko":
            jump atsuko_ending_2
        "Qiming":
            z "The fortune-teller? Oh no, no. Born and raised in Liyue. And besides, if she could conjure mimics the first thing she would do is conjure a crane and fly Zhihua as far away from her as possible."

    jump inazuma_ending_1
label choices_liyue_no_bibo:

    $ globals()['menu_yalign'] = 0.65
    menu:
        p "{cps=0}The fishmonger? No - he is local, although he did say he once rescued a woman from Inazuma and that was the last time someone left Inazuma illegally.{/cps}"

        "Changshun":
            z "No, she is has pure Liyue blood running through her veins. Woman thinks she can get rich by selling potatoes, cheese and sugar. Good luck to her!"
        "Xingxi":
            z "The Mingxing Jewelry owner? It is a family business that has been in Liyue for hundreds of years. Some even call it the Rex Lapis of the market for precious stones. She can't be Inazuman."
        "Linlang":
            z "The Xigu Antiques owner? She is one of the biggest Liyue patriots there are. She studied ancient Liyue history. She and Soraya share a passion for the antiques."
            p "The only odd thing about her is that glowing piece of rock she gave us. She said it came from a star but the ore suppliers tell crazy stories just to sell their stock these days."
        "Atsuko":
            jump atsuko_ending_2
        "Qiming":
            z "The fortune-teller? Oh no, no. Born and raised in Liyue. And besides, if she could conjure mimics the first thing she would do is conjure a crane and fly Zhihua as far away from her as possible."

    jump inazuma_ending_1
