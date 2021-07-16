label inazuma_ending_1:
    t "Well then, nobody else crosses my mind."
    p "Seems like we would need to take this investigation to Inazuma. But how are we going to get there when all the boarders have been sealed?"
    z "I might be able to do something. But it is risky."
    p "What is it, Zhongli?"
    z "While we can't go to any of the populated areas in Inazuma, we might be able to sneak into one of their islands. Once there, I can call an old favor and we can meet an insider."
    t "Zhongli! I didn't suspect you would have contacts all the way to Inazuma."
    z "One's reach can extend much further than you can imagine, Traveler."
    p "Erm... hello... newsflash - have you forgotten who you are talking to, Traveler?"
    t "Oh, right. You've been around longer than almost everyone. Of course you have presence far and wide. And you must have quite the amount of favors racked up."
    z "I do. But I'm not sure if this will work. We would need to be extremely discrete. If any of this reaches the Electro Archon, there might be consequences."
    p "Right! We will be very careful in Inazuma. But, how do we get there in the first place? It's not like we can just swim."
    z "I know a fleet that might be able to sail us there. But that would require an immense amount of effort and resources."
    t "What can we do to facilitate our journey?"
    z "I will ask around and let you know. For now though, you may go rest and pack your bags. We might have a long journey ahead of us."
    p "Fingers crossed everything goes right and we are able to sail off as soon as possible!"
    z "Please remember! And this is very important. Even though it is just a suspicion for now, do not discuss the presence of an Inazuman Geo Vision Bearer on Liyue's territory with {i}anyone{/i}! You got that?"
    p "Loud and clear!"
    z "If our suspicions are true, we need to gather as much information on them before the inevitable confrontation. Trust me, it will be better if we find them before the Electro Archon does. For all of us."
    t "You got it, Zhongli. We will not discuss the progress of our investigation with anyone!"
    z "Good! Now that we are clear, I need to go and call in the favors. I will contact you later today to confirm the plans with you."
    p "Sounds good. In the meantime, can we go and have some food, please, Traveler?"
    t "Sure. Would you like to go back to the Baiju Guesthouse and have food there? Then we can go up to our room and pack our bags?"
    p "Mhm. Since the Wanmin Restaurant is still closed, the Baiju Guesthouse's food will do."
    z "It is settled then. I've gotta run. See you soon!"
    p "Bye, Zhongli!"

    scene bg downstairs with fade
    show paimon happy at center with dissolve

    p "Gee~ the situation is getting pretty serious. This might be our first journey by boat to a forbidden land. Excited?"
    t "I would have been more excited if the circumstances were different."
    p "Cheer up! We will find the bad guy! And once we do, Paimon is going to ..."
    t "You are going to do what, Paimon? Float around them until they are dizzy?"
    p "Hey, it's not Paimon's fault Paimon is so small and fragile."
    t "That Paimon sized sword seems like a better idea by the day. Just imagine - Battle Paimon - full plate armor, sword in one hand, a tiny shield in the other - floating around and catching crystalflies."
    p "Paimon can take on more than just crystalflies! Just wait until we find that bad guy and there will be trouble for them!"
    t "Big words, Paimon. What if they are a well-trained swordsman? Or a skilled archer? Maybe they will just pin you to a nearby Fir tree with one shot."
    p "Paimon is nimble - like a butterfly."
    t "Butterflies aren't that nimble. You could have gone for a crystalfly at least..."
    p "Okay, a crystalfly. Paimon will fly up into the air and..."
    t "...and stay there? Wait until me and Zhongli tie up the guy and then you can swoop in and give them a bad nickname?"
    p "Yeah!!! That's exactly what Paimon will do. Hurt them with words. That will show them not to mess with Liyue's local business."
    t "Haha~ you never cease to amaze me, Paimon! Aren't you worried about the whole trip though?"
    p "Not at all! Paimon believes in Zhongli. He will come through and take care of the trip."
    t "It is a bit risky to rely on his so much. I'm thankful he is on our side."
    p "We have helped him in the past. As a matter of fact, he owes us!"
    t "Oh, does he now? I always thought of it as us having a common goal and just working together towards it."
    p "One does not simply go out of their way to save the land of the Geo Archon. No wonder the people of Liyue have dubbed you the local hero."
    t "It was nothing. Just a small step on my larger journey. Sometimes I wonder when this will end and what lies on the other side."
    p "There's only one way to find out. You need to go through the journey. But don't worry! Paimon will be there to guide you along the way!"
    t "Thanks, Paimon. I can always count on you!"
    p "Mhm~ Now, let's finish our Fullmoon Eggs and go upstairs to pack."

    $ end_txt = "Later on upstairs..."
    call end_screen(end_txt)

    scene bg room with dissolve

    "*knock knock*"
    t "Who is it?"
    u "There's a letter for you."
    "*door opens*"
    "*door closes*"

    show paimon happy at center with dissolve
    p "What is it, Traveler?"
    t "It's a letter. The person said it's for me."
    p "Are you just going to stare at it? Come on, open it."

    scene bg room_letter with dissolve
    pause
    scene bg room with dissolve
    show paimon happy at center with dissolve

    t "It's from Zhongli. And I don't think you'll like it."
    p "What does it say?"
    t "We have an early start tomorrow morning."
    p "How early?"
    t "We have to be at the docks at dawn."
    p "At dawn?! Is he insane? Why so early? Paimon's not going to get enough beauty sleep."
    t "Sometimes, sacrifices must be made. He also mentioned that we would need to \"jump through some hoops\" whatever that means."
    p "Paimon doesn't feel like jumping that early in the morning."
    t "I don't think he means literally jumping. Nevertheless, it seems like we would need to put in some extra effort to get to Inazuma."
    p "Zhongli surely pulled a lot of strings in such a short time frame to arrange the trip."
    t "Yeah, when the safety of the people in Liyue is at steak, you can count on Zhongli to come through."
    p "He is amazing, isn't he."
    t "Pretty remarkable."
    t "Since we are getting up so early tomorrow we should go to bed soon."
    p "Oh, Paimon is ready just now."
    t "Alrighty then. Lights out."

    $ end_txt = "Early the next morning..."
    call end_screen(end_txt)

    scene bg docks with dissolve
    p "Hey, wait up."
    show paimon happy at left with dissolve
    p "How can you be so energetic this early. The sun isn't even up yet."
    t "Come on, Paimon. We have to meet Zhongli. We are at the docks. Keep your eyes open for him."
    p "Paimon is trying to. It's not as easy as it looks you know. Lack of sleep makes Paimon dizzy."
    z "Traveler, Paimon, over here."
    show zh happy at right with dissolve
    t "Good morning, Zhongli."
    p "Yeah, morning."
    t "Don't pay attention to Paimon. She is still sleepy."
    z "I'm glad you got my message and made it in time."
    t "We did! I'm impressed that you were able to arrange a transport on such a short notice."
    z "It wasn't easy, I'll tell you that."
    t "Is this the ship in the back?"
    z "Yes. That's The Mizar. One of the ships from The Crux Fleet."
    t "The Crux? That would make it one of Captain Beidou's ships."
    z "Indeed it is."
    t "How did you manage to arrange that?"
    z "Let's just say that every ship has its price, and this one was no exception."
    t "Surely the price to privately hire one of The Crux Fleet's ships for such a dangerous trip must be quite high!"
    z "If you are talking in terms of Mora, that's taken care of...sort of."
    t "What do you mean {i}\"...sort of?\"{/i} Last time I checked you weren't very good with Mora."
    z "Perhaps I'm not, but I have friends who are. And they have agreed to lend me the Mora in exchange for some goods that we will be providing them shortly."
    p "Did Paimon hear right? {i}We{/i} are providing goods to this friend of yours?"
    z "Yes, Paimon, we are."
    t "But what are those goods? We don't have anything this valuable to pay for the trip."
    z "Neither do I. However, we are going to Yashiori Island. And if I'm not mistaken, there should be plenty of the goods for us to pick up and take back from there."
    t "Are we stealing stuff from Inazuma?!"
    z "It's not stealing. We will be harvesting goods."
    p "Harvesting? Does our investigation consist of a farming mission as well?"
    z "Not exactly. Let me explain."
    z "The person, who lent me the money runs a very successful pharmaceutical business in Liyue. They said that they would like for us to bring them back a bag of Sea Ganoderma from the trip."
    p "Sea Ganoderma? What's that?"
    z "The Sea Ganoderma is a plant species that only grows in certain regions and islands of the ocean. Though it looks like a fungus of some sort, it actually comes from a substance secreted by certain soft-bodied organisms."
    p "We are doing mushroom picking for your friend?"
    z "A common misconception. It looks like a mushroom but it is more like the honey from jellyfish."
    p "Ewww~ Jellyfish jelly. It will be slimy..."
    t "Oh suck it up, Paimon. It's not like we aren't covered in slime condensate all the time."
    p "But it's different. This is Inazuman aquatic slime. Yuck!"
    t "You'll be fine. Just a few handful in the bag and we are done. What is your friend using it for anyway, Zhongli?"
    z "I don't know. I learned not to ask more questions than I need to. And seeing as how generous my friend was being, I was happy with the deal we made."
    t "Is this Sea Ganoderma dangerous?"
    z "It shouldn't be. They didn't warn me for anything out of the ordinary. Once we arrive, keep your eyes open near shallow water. It's usually found around wet rocks as well."
    p "Paimon bets it's sticky and that's why it's all around the rocks. Just stuck there waiting for us to pick it up."
    t "I'll keep my eyes open as well!"
    z "Very well then."
    t "Hey, what about your insider. Were you able to make contact? Are they going to meet us at this island we're going to?"
    z "I've sent her a message. It should arrive before us. Meaning she would have time to plan our arrival and meet us at Yashiori island."
    t "Let's hope she makes it in time. Because as it stands, she is our only hope for progressing this investigation."
    p "Paimon has no doubt Zhongli's contact will show up. Zhongli surrounds himself only with reliable people."
    z "Reliability is not all that matters when it comes to people from Inazuma. I have no doubt she is reliable but the political situation in the nation is too strict to allow outsiders to just come in and visit."
    t "Yeah, let alone come in for information."
    p "Information on a potential Vision bearer."
    t "Shhh!!! Paimon. Keep it quiet. The crew might overhear."
    p "Oh... right... the vacation we are taking to this weird island that is usually off limits... hehe~"
    z "Seeing as the sun is about to rise, we should board The Mizar and sail off."
    t "Okay! Come on, Paimon. You can sleep on-board."
    p "Paimon doubts it!"
    z "You should be fine. At least until we reach the storm."
    p "The storm?!"
    p "What storm?"
    p "Zhongli!!!"

    $ end_txt = "The party sails off into the sea..."
    call end_screen(end_txt)
    play music "audio/bg_inazuma.mp3"
    pause 0.1
    scene bg inazuma with dissolve
    show paimon happy at left
    show zh happy at right
    z "Welcome to Yashiori island."
    t "Not very welcoming if you're asking me."
    p "Paimon agrees. This is one spooky place you chose, Zhongli. The presence of evil is palpable here."
    z "I know it's not the most pleasant place, but trust me - it is the safest."
    t "Are those bones in the distance?"
    z "The skeleton of a great snake rests on this island. This is a story for another time though."
    p "A skeleton?! Why couldn't you have picked a creepier island? Maybe one enshrouded in fog or an island that has some sort of natural disaster on it constantly?"
    z "I would have loved to. However, this is by far the one island where the Electro Archon has the least presence. We could potentially get away with this visit without any consequences."
    "*Bushes rustling*"
    p "Did you hear that? You just mention her on Inazuman land and the bushes start to tremble"
    t "I'm sure that was just a coincidence, Paimon. Look, there's nothing over there."
    "*Rustling intensifies*"
    p "That was no coincidence. Paimon's shaking."
    t "Hello! Anyone there?"
    z "There shouldn't be anyone here. Unless..."
    u "Pst, Zhongli? Is it really you?"
    z "Yes. I'm right here in the open. You can come out. It's safe. These are the Traveler and Paimon. They are the companions I told you about."
    show zh happy at center with move
    show ay sil at right with dissolve
    p "Who is it?"
    z "It's my contact. She is coming our way."
    t "Paimon, be cool!"
    z "Traveler, Paimon, I'd like you to meet the princess of the Kamisato house - Miss Kamisato Ayaka."
    show ay happy at right with dissolve
    p "Pleasure to meet you... your highness."
    a "Please, call me Ayaka. No need for formalities."
    t "Nice to meet you... pri.. Ayaka."
    a "I've heard things about you, Traveler. Good things. When Zhongli reached out to me I was thrilled to be meeting you here."
    t "My reputation preceds me I see. Although I haven't done much around here. I'm just on my journey."
    a "I would love for us to have more time to get to know each other, but in your message I picked up a sense of urgency, Zhongli. What is going on?"

    $ end_txt = "Zhongli fills Ayaka in on the incidents in Liyue..."
    call end_screen(end_txt)

    scene bg inazuma
    show paimon happy at left
    show zh happy at center
    show ay happy at right

    a "A potential Inazuma Geo Vision bearer in Liyue?"
    z "That's what we are suspecting. They are able to conjure Geo Mimics and one of them was shaped like an electric eel."
    a "I can tell you for certain, that nobody has left the borders of Inazuma recently. And the Vision Hunt Decree is going strong."
    p "Is it possible that somebody snuck out illegally?"
    a "No, impossible. The Kanjobugyo patrol the borders day and night. Only merchant ships are allowed in and out. And even then, they are monitored non-stop. All the goods loaded and unloaded are inspected thoroughly."
    z "If it is nobody recent, would you know of a vision bearer that has left Inazuma years ago? Perhaps they've made their way into Liyue without our knowledge."
    a "If there is such a person, I'm unaware of them. Inazuma does not have emigrant records dating far into the past. Besides, if you are a Vision bearer in Inazuma, you better lay low in times like this."
    p "Why? What's so bad about being a Vision bearer in Inazuma?"
    a "It's not that it's bad. It's that the Electro Archon, Baal, will do anything to get her hands on your vision. She will then seize it and use it for her own personal good."
    t "Can't people just choose to give up their vision?"
    a "It's not that simple. Once you get a vision you can understand better but for one to give up their vision would be like giving up a little piece of yourself. Nearly impossible. That's why most visions have been seized by force."
    p "And what happens if the bearer doesn't or can't give up their vision?"
    a "It's complicated. One way or another, after someone is exposed as a vision bearer, they won't be for long. Drastic measures are taken in extreme cases. Even..."
    z "Even what, Ayaka?"
    a "Some bearers can't handle the thought of not having their vision with them. What I'm about to tell you is highly classified. I'm only telling you this because it might be linked to your investigation."
    z "Go on, you can trust us."
    a "It was a dark and gloomy night in Inazuma. The night sky was clear and the air was warm. All businesses were closing down for the day. There was an anonymous tip handed in to the Bakufu."
    a "A local shopkeeper was suspected to be an Electro Vision bearer. As Vision Hunt Decree protocols follows, the Inazuma Bakufu tracked him down and tried to seize his vision."
    a "The man tried to flee from the Bakufu but got cornered in an alley. The Bakufu reported that the man kneeled and said: {i}\"I hope she understands this better than I did...\"{/i}"
    a "The bearer raised his hand and his vision started to glow. Bright purple light engulfed the whole alley and a dozen dark clouds appeared above the old man's head. The Bakufu were shocked as the clouds filled the space above their heads."
    a "With a snap of his fingers..."

    show zh happy at center with flashbulb

    a "...a lightning came crashing down. It light up the whole alley, briefly blinding the Bakufu."
    play sound "audio/thunder_two.wav"
    pause 0.1

    a "Thunder followed. Thunder so loud that it deafened the Bakufu. They braced for the worst and hoped for the best."

    a "In a blip, it was all over. The ally was once again as dark as it was minutes ago. The clouds dispersed. The electrified air gently caressed the cheeks of the members of the Bakufu."
    a "Recovering from the initial shock, they could not believe their eyes. Each and every one of them was safe and sound. However, the same could not have been said for the vision bearer."
    a "He was lying there in front of them, pinned to the ground. His silhouette scorched on the street. The light in his Vision slowly dimmed. Then disappeared completely. The elemental core vanished. All that was left was an empty metal frame."
    a "Nobody knows what happened with the Vision itself. Usually, when a Vision bearer passes away, the Vision left behind becomes a Masterless Vision. No element, no master. Just an empty shell, waiting to be rekindled."
    a "Many have tried to harness the power of a Masterless Vision but have failed. Ultimately, the Masterless Visions would still be brought to Baal. But in this case, the vision was gone."
    a "Some stories suggest that when a Vision bearer passes away, their Vision may resonate with somebody else. That's one way of obtaining a vision. But the new master should be someone worthy. Someone special. Someone the vision chose for a reason."
    a "The Bakufu have been on the lookout for the Vision manifesting itself within Inazuma's borders. But is seems like it either hasn't or it has been kept hidden well."
    p "Wow... Ayaka... shivers are running down Paimon's spine."
    t "You couldn't have picked a worse spot to tell that story. With all the bones around us..."
    z "Refocus here! Aren't you hearing what Ayaka is trying to tell us. There might be a brand new Vision bearer in Liyue. One that we are unaware of!"
    "*the wind picks up*"
    p "This information totally went over Paimon's head. Good thing we have you with us, Zhongli."
    t "If what Ayaka suggests is true, how can we verify it? Is there a way to identify the new Vision bearer?"
    z "People usually wear their Vision proudly. It won't be long before they reveal themselves. We just need to be vigilant and keep looking within Liyue."
    a "If my suspicions turn out to be true, there is going to be a political clash between the nations of Liyue and Inazuma. Baal won't rest until that Vision is in her hands."
    z "I'm well aware of that. Which is why we need to find the individual first."
    p "Maybe seizing their Vision is not such a bad idea in this case? They've had it for a couple of weeks and all they've done is cause trouble to the local businessman in Liyue. They are using their Vision for evil!"
    z "Obtaining a Vision can be an extremely taxing event and a test to a person's character. We can't be sure what is going on in their head right now. Best thing to do is talk to the person and try to reason with them."
    "*inaudible dialogue in the distance*"
    t "What was that?"
    a "Oh no! The Kanjobugyo are here."
    p "The Kanjo-what-now?"
    a "The Kanjobugyo.The authority who monitors Inazuma's borders and one of the three organizations that comprise the Tri-Commission. They work with the Inazuma Bakufu, and are led by the Electro Archon, Baal."
    p "Yikes, border control is here for us illegal immigrants."
    t "Zhongli, I thought that this island was safe? What happened?"
    z "It is supposed to be. Ayaka?"
    a "I didn't want to worry you, but ever since the incident with the old shopkeeper, there are new protocols. They are searching far and wide for that missing vision. They must have extended their range to include the Yashiori island."
    p "What are we going to do? Paimon doesn't want to become Baal's prisoner."
    a "You won't! I'll try and divert their attention. You make a run for your ship. Did you hide it well?"
    z "It's in the bay behind the massive hill in the back. Can't be seen from here."
    a "Good. Go there and wait till sundown. You should be safe to leave by then. I'll make sure the Kanjobugyo don't make it to the bay."
    z "Thank you so much, Ayaka. Thank you for the information and the trouble you're going through."
    a "I appreciate the gratitude. Hopefully one day we will meet again, Traveler. And the circumstances will be different."
    t "Looking forward to it. Thank you, Ayaka!"
    a "Get going. Hurry!"
    p "Wait, what about the jellyfish honey?"
    a "Jellyfish honey?"
    z "Ah... we are supposed to gather a bag of Sea Ganoderma on the way back to cover for our trip."
    a "That's insane. And highly dangerous. The Kanjobugyo might see you!"
    z "I saw some on the way here. If we keep our heads down, we can gather what we find on the way to the ship. Then try to fill up the rest of the bag from whatever we can find in the bay."
    a "Okay, I'll try and lead them further inland. You pick up you Sea Ganoderma and stay quiet until sundown."
    t "Paimon, float around and gather as much of these stuff as you can on the way to the ship. Zhongli will be carrying the bag. I will try to pick up as much as possible as well. Ready?"
    p "Mentally, no. But let's go."
    a "Safe trip back home and do keep me updated on the situation."
    z "Will do! Thanks again!"
    hide ay with dissolve
    t "She is away. We should get going as well."
    p "Sticky jellyfish secretions, here we come."
    hide paimon with dissolve
    z "This is the bag, let's split up but still keep close enough to increase picking potential."
    t "Sounds good to me. Let's go."

    $ end_txt = "The party fills the bag and makes it to the ship..."
    call end_screen(end_txt)
    $ end_txt = "...then they sail off into the night..."
    call end_screen(end_txt)

    scene bg liyue_back with dissolve

    t "We're almost back in Liyue. I can see the harbor from here."
    z "Hmm... strange. What is this shape in the distance?"
    p "Looks like just another ship."
    z "It does look like it, but it's not {i}just another ship{/i}."
    t "I can't tell from that far. Maybe as we approach, things will clear a bit."

    scene bg liyue_back_closer_rail with dissolve
    show zh happy at center
    show paimon happy at left

    t "It is just another ship. But it's built differently. I haven't seen a ship like that in Liyue before."
    z "That's because it is an Inazuman cruiser. It's not your ordinary fleet ship like the Mizar here. It's built for fast military navigation."
    p "M-m-military? You mean Inazuma is invading Liyue?"
    z "With only one cruiser - highly unlikely. And it looks like they have docked peacefully on the harbor."
    p "Paimon wonders what could a military ship be doing in Liyue waters."
    t "I have a bad feeling about this."
    z "So do I. We can't do much from here anyway. It's pointless worrying what might be happening down there."
    t "I guess we'll just have to wait and see once we dock."
    z "There should be plenty of Millelith on the docks. We should find one easily and ask what's happening once we arrive."

    $ end_txt = "The Mizar docks at Liyue harbor safely..."
    call end_screen(end_txt)

    scene bg millelith with dissolve
    show paimon happy at left with dissolve
    show zh happy at right with dissolve

    p "Um, excuse me, good sir. Would you mind telling us what is going on here? Why is there an Inazuman military ship docked at Liyue harbor."
    g "This is official business. Civilians should refrain from interfering."
    p "We don't want to interfere, we just want to know what's happening."
    g "It turns out that there is an illegal immigrant from Inazuma living in Liyue. It is suspected she is involved in the attacks on the local businesses over the past couple of weeks."
    z "Oh really? And how is that so?"
    g "Rumor is she has a Geo Vision and she has been using it to smash the rocks through the local businesses' doors and windows to damage their inventory. Because of the Vision Hunt Decree, it is out of the Millileth's hands now."
    z "A rumor? Where did that originate from?"
    g "The Bakufu told us about it. Apparently, some new information was brought to Inazuma recently and it didn't take long to reach the Electro Archon's ears."
    p "Zhongli, she told on us..."
    z "Shh... This ... new information. You wouldn't happen to know how it reached the Electro Archon's ears, would you?"
    g "Apparently, it wasn't pretty. It had to be forced out from a member of the Kamisato house by some pretty unpleasant means but Baal always gets what Baal desires - one way or another."
    u "No, please! I don't want to go back! Somebody help me!!!"
    p "Look, they are dragging that poor girl on-board."
    t "We have to help her. Zhongli!"
    z "I wouldn't, if I were you. We are too late. This is beyond our jurisdiction now. The girl committed crimes and she will have to answer to Baal for them."
    u "Anyone!!! Please!!!"
    "{i}The Bakufu walk past you with the girl~{/i}"
    t "Wait a second, I recognize her. That's Atsuko - the girl we found a job for here in Liyue a while ago. How could I not remember that she was a refugee from Inazuma earlier?"
    p "She is crying. Look into her eyes."
    "{i}Zhongli grabs you by the wrist~{/i}"
    z "Let it go! This is a battle we could not win."

    play sound "audio/thunder_two.wav"
    pause 0.1

    $ end_txt = "Baal always gets what she desires..."
    call end_screen(end_txt)
    $ end_txt = "The End #1"
    call end_screen(end_txt)
