define s = Character("Sara", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])
define tim = Character("Timaeus", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])
define n = Character("Noelle", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])

label mondstadt_square:
    play music "audio/bg_mondstadt.wav" fadein 2.0
    scene bg ms_sq with fade
    pause 3
    show zh happy at left
    show paimon happy at center

    z "Ah..the city of Freedom! It's been a while since I've been here."
    p "We've been traveling back and forth between here and Liyue quite a lot recently. Has Mondstadt changed a lot since your last visit, Zhongli?"
    z "You could say that. But at heart, it is still the same. The people are walking the streets freely. Not that many guards in sight and everybody seems to be smiling."
    p "Speaking of guards, should we find one and ask them where to find...?"
    t "No need. I think there is a better source for that information."
    z "Oh?"
    t "See the Knights of Favonious are occupied with their daily tasks and don't pay too much attention to the common folk. Not unless something out of the ordinary happens."
    t "News travels by the merchant's mouth much quicker than any protocols followed by the Knights."
    p "That's right. For all the latest gossip, we should just ask the merchants around The Fountain Square. Traveler, do you have anyone in mind?"
    t "I think that Sara over there at Good Hunter might have a good idea where we can find our girl. They are pretty close."
    p "You're right! Hey, look - there isn't any queue for Good Hunter for once. This is our time."
    t "Let's not make a crowd where one is not needed. I'll just go and ask Sara quickly. You wait here!"
    z "Sounds like a good plan to me. You know the Mondstadt folk best."
    p "Okay, but while you are over there, could you get Paimon one Fisherman's toast, please?"
    t "Paimon! You're always hungry! Now is not the best time for food. Let's get the job done first and then we can feast."
    p "Oh...okay~"
    t "I won't be long."
    z "See you soon!"

    scene bg ms_sara with fade
    pause 1

    s "Welcome to Good Hunter. How can I help you?"
    t "Hey, Sara. I was wondering if you knew where I could find Noelle at this time of day?"
    s "Hello, Traveler! I think I saw her today. She grabbed a Satisfying Salad to go and said she needs to {i}\"Hit the books.\"{/i}"
    t "Did she say what books?"
    s "I'm afraid not. I didn't think bookkeeping is one of her maidly duties."
    t "It could mean that she went to the library to study for her Knightly exam."
    s "Ooh yes... that makes perfect sense. We spoke about how she has less than 6 months until her exam. You helped her prepare recently, didn't you?"
    t "I did, but I haven't seen her since."
    s "She told me all about it and seemed very happy with the help that you provided."
    t "Glad I was of use to her!"
    s "Are you having some food today?"
    t "I would love to. However, I don't have time just now. There are more important matters to attend to. I'll make sure to stop by soon though. Paimon is always craving some of your Fisherman's Toast."
    s "Haha~ I know she is."
    t "Looks like there's a customer on the queue. I won't take up more of your time. Thanks a lot for the help, Sara."
    s "You're very welcome. Take care, Traveler."

    scene bg ms_sq with fade
    pause 1
    show zh happy at left
    show paimon happy at center

    p "Soo...what did Sara say?"
    t "She can't be certain but it is highly likely we should head to the library."
    p "Still studying for that Knightly exam, is she?"
    t "You know it. Every moment she does not have a task assigned, she would spend studying."
    z "Is the library still at the Knights of Favonious' headquarters?"
    p "Look at you, Zhongli, it's like you never left heh."
    t "Let's hurry and get there before our suspect goes running errands for somebody."
    p "You're right! Let's get going!"

    scene bg ms_lib with fade
    pause 2
    scene bg ms_lib_2 with dissolve
    pause 1
    show zh happy at left with dissolve
    show paimon happy at center with dissolve
    show noelle happy at right with dissolve

    t "Noelle!"
    n "Honorary Knight! Paimon! What a pleasant surprise! And you brought a friend!"
    p "This is Zhongli - a consultant for the Wangshang Funeral Parlor in Liyue!"
    n "Greetings. I'm Noelle, maid at the Knights of Favonious."
    z "Pleasure to meet you, Noelle. The tales of the Maid-Knight are quite popular on the streets of Liyue these days."
    n "Oh... I hadn't realized. I hope the stories are not too exaggerated."
    p "Well, they still are, but the people seem to like them."
    n "I hope I have not given you the wrong impression about the maids from Mondstadt."
    z "Not at all. Everybody in Liyue knows that storytellers like to put an extra bling to their stories to attract and retain customers. There's no need to worry about your reputation."
    n "That's good to hear. What brings you to the library today?"
    t "Noelle, there is something we need to talk to you about."
    n "Is everything okay? You sound worried."
    t "Everything is fine around here. There is some trouble in Liyue that we are helping with though."
    n "Is this why you brought visitors from Liyue? Oh my... a consultant for a funeral parlor... something terrible must have happened."
    p "No-no calm down, Noelle. Nobody's hurt. Zhongli is here because he is an expert of...uhm... rocks."
    n "Rocks? I don't understand?!"
    t "Noelle, do you remember the trip we took to Liyue recently?"
    n "Yes, I do. How can I forget? I remember all the places you took me to."
    t "So you remember the Wanmin Restaurant and chef Mao?"
    n "The time I burned my tongue on authentic Liyue spicy food..heh.. One does not simply forget such an experience."
    t "See that's the thing... we hope you had forgotten about the unpleasant experience and hold no grudge with chef Mao."
    n "Unpleasant? Grudge? What are you saying? I had a good time. It made me stronger and more adventurous! I would never hold a grudge with someone who made me a better person!"
    p "You say that, but we have to be certain. Sorry for asking you these uncomfortable questions, but we have to be sure."
    n "Sure? Sure of what? What's happened to chef Mao?"
    p "Nothing, he is fine. Can't say the same for his restaurant though. Somebody trashed it and smashed his oven. He can't continue his business right now. We are here investigating."
    n "And you think I might have something to do with it? How could you..."
    z "Please calm down, Miss Noelle. Could you tell us a bit about your vision?"
    n "My...vision...? What does {i}it{/i} have to do with it?"
    z "We suspect that whoever trashed the place used a Geo vision and the traveler mentioned you posses one."
    n "I do, but all I use it for is to protect myself and the people of Mondstadt. I use it primarily to shield us from incoming attacks. When it comes to offense, all I do is imbue my greatsword with the power of Geo."
    z "So no conjuring powers of any sort?"
    n "I wouldn't use it to conjure anything. I have everything I need already."
    t "It's not about what you have, it's about what you could have or do with it."
    n "I..I...I would never hurt anybody with my vision. It is a gift from the Archons and I would only ever use it for good!"
    t "Please, you have to understand that we never doubted you in the first place. There are only so many Geo vision bearers that we are visiting everyone we know. Nothing personal."
    n "I understand but it still hurt my feeling to know that you thought of me as a criminal. I thought we had a better relationship, Honorary Knight."
    t "Noelle...we do! I promised to help you prepare for your knightly exam and I will be there the day you get your title! You can count on me!"
    n "Okay. It's reassuring to hear that after being accused of a violent crime. By the way, when did it even happen? It's been some time since our trip to Liyue."
    t "It happened a few days ago."
    n "Then you can definitely be sure it wasn't me. I was in Dragonspine with Mr. Albedo, Sucrose and Timaeus. I was helping to tidy Mr. Albedo's camp."
    p "Albedo is back in Dragonspine again?"
    n "Yes he is. He found a new scene with 7 unique pine trees to paint. He and Sucrose have been staying there for the past week. Timaeus and I came back to Mondstadt yesterday. He will restock some alchemy and food supplies and go back to them."
    t "So Albedo has been in Dragonspine for the past week as well?"
    n "Mhm~ his art has improved dramatically. Two should catch up once he returns."
    z "Who are this party of people if I may ask?"
    n "Mr. Albedo is the chief alchemist of the Knights of Favonious, Sucrose is his assistant and Timaeus is a scholar of alchemy."
    p "Yes, that's right. And Albedo is also a Geo vision bearer. Paimon needs to scratch another name of the list."
    n "The List?"
    p "Ehe...just people we need to talk to for the investigation."
    n "Oh...I see. Well you can find his camp near the Starglow Cavern in southern Dragonspine."
    t "I don't think this will be necessary. Do you know if Timaeus is still around? I would just like to confirm your words with him real quick."
    n "He should still be around. Try checking either by the alchemy table or near Good Hunter."
    p "That's right! Food and alchemy supplies. Good thinking, Noelle!"
    t "I'm sorry if we've upset you today, Noelle. It's just that chef Mao has trusted us with this, and we want to be thorough with our investigation."
    n "I will be okay, don't worry about me. Just remember your promise."
    t "I wouldn't miss it for the world! Your knightly exam is important for me too. Make sure you are taking breaks from studying though!"
    n "I am! I remember our lessons from last time."
    t "Very well then! We will be on our way. Gotta catch Timaeus before he leaves."
    n "Happy to help here! Take care of yourselves, everyone."
    p "Thanks, Noelle. You take care as well!"
    z "Nice meeting you, Miss Noelle! Goodbye for now."

    scene bg ms_sq_2 with fade
    show zh happy at left
    show paimon happy at center

    p "Hey look, it's Timaeus over by the alchemy table."
    t "That's right. Good catch, Paimon. Looks like he is in a hurry. Let's not corner him. I'll just go over and ask him really quick. If he confirms Noelle's story, then we can essentially take down two birds with one stone."
    z "Sounds like a good idea to me. Paimon and I will just hang around back here by the fountain."
    p "Mhm~"
    t "Okay then, speak soon."

    scene bg ms_tim with fade

    t "Hey, Timaeus! Packing bags?"
    tim "Honorary Knight! Did you come by to use the alchemy table again?"
    t "No, I was just passing by and thought I'd say hi."
    tim "Oh that's strange of you. You usually just come around, do your business with the alchemy table and go away. Sometimes I feel like the only time you say 'hi' to me is by accident."
    t "Nonsense, Timaeus. I think highly of your alchemical research and experience. It's just that sometimes I'm in a hurry and can't stay to chat, although I would love to. But I have some time just now. Where are you off to?"
    tim "Well I'm packing some supplies for Albedo and Sucrose. They are in Dragonspine and the expedition is taking longer than anticipated. I came back today to restock and will be back on the road."
    t "You came back today? Alone?"
    tim "As a matter of fact, no. I traveled with Noelle. She was there to tidy the camp."
    t "Ah... and how long was the expedition supposed to be originally."
    tim "Just a week, but it looks like it will be closer to two. Maybe a couple of days extra on top. Why the sudden interest in our expeditions? It's been a while since we've seen you in Dragonspine."
    t "Oh...  you know, just trying to make a conversation, but I can see that you are busy packing, so I'll let you be. Wish all the best to Albedo and Sucrose from me when you see them again. We will catch up once your expedition is over!"
    tim "Sure, will do. In the meantime, feel free to use the alchemy table as usual."
    t "Thanks, Timaeus! Safe trip!"
    tim "Goodbye, Traveler!"

    scene bg ms_sq_3 with fade
    show zh happy at left
    show paimon happy at center

    p "So... what did Timaeus say?"
    t "Exactly what Noelle said. The group has been in Dragonspine the past week. Noelle was there to tidy the camp because the group will be staying longer. And the two of them came back today."
    p "That means there is no way Noelle of Albedo were in Liyue a few days ago."
    z "That would seem correct. Seems like these two have a solid alibi. Do you trust them enough to take their word for it?"
    t "I do. I took a peak at Timaeus' bags while he was packing, and they were full of alchemy supplies. I think I caught a glimpse of some containers of paint and some food boxes as well."
    p "And Noelle was just calmly studying for her knightly exam before we disturbed her."
    z "That's true, she is either the greatest actor in Mondstadt or she was genuinely worried about people being hurt."
    p "Yep, that's Noelle for you. Always trying to protect people, even if she doesn't know them."
    z "Does that mean that we have reached a dead end?"
    t "Unfortunately, it seems so..."
    p "Oof.. Paimon hates being stuck on a puzzle! Wish we could just look up the answer and be done with it. But there isn't even anybody to give us hints."
    t "You're right. But it's a good thing we crossed our friend off of the list of suspects. That means we are dealing with a new and unknown enemy."
    p "Zhongli, do you think the abyss could have snuck into Liyue undetected and wrecked the Wanmin restaurant?"
    z "Next to impossible. Ever since the Rite of Parting, the Millelith have been on the lookout with stricter schedules and more frequent patrols. It suprises me that the act of vandalism happened unnoticed in the first place."
    t "It is rather strange."
    p "Hey look at those dark clouds. Looks like another storm is on the way. Should we find a place to stay for the night?"
    z "Well, if our work here is done, then technically there is no reason to stay. We could rent a transport balloon and be in Liyue by nightfall. Hopefully we won't catch the storm."
    p "But staying here would be safer and it means you can have a taste of the dandelions wine you mentioned before."
    z "You make an excellent point, Paimon. The sooner we solve the case, the better, but is it worth the risk of getting caught in the storm or should we wait for it to pass?"
    p "We deserve a bit of a break, Paimon is tired from talking to all those people today. And we still haven't had food."
    z "We can always just get some food on the go. But we have to decide now. A night in Mondstadt or hitting the road on a transport balloon? What do you think, Traveler?"

label choices_mondstadt_night:

    menu:
        z "{cps=0}We can always just get some food on the go. But we have to decide now. A night in Mondstadt or hitting the road on a transport balloon? What do you think, Traveler?{/cps}"

        "Stay in Mondstadt":
            t "As much as I want to get this done, I think that staying one night in Mondstadt will do us good. We can continue the investigation tomorrow when we are well rested."
            p "And well-fed!"
            t "And well-fed, Paimon. I think that taking a break and clearing our heads will be good for us."
            z "Very well then. We are off for the day. Now where to?"
            p "Zhongli, you said that you are after some dandelions wine, right?"
            z "Well, yes, but do you have anything else in mind?"
            p "Our friend, Diona, makes the best cocktails in the Cat's Tail. No matter what she adds, her mixing process is so unique that it can't produce a bad concoction."
            z "This sounds intriguing."
            p "Plus, the tavern is full of cats you can play with while drinking your cocktail."
            z "I do enjoy the company of a feline friend while enjoying a refreshing drink. What is the alternative though?"
            p "Well there's always the Angel's Share. The classic Mondstadt tavern with the locally sourced dandelions wine from the Dawn Winery. It is just what you came here for."
            z "Although I came for the dandelions wine, I wouldn't mind experiencing the new buzz in town with your friend's cocktails."
            p "Well if both sound good, which one should we go to?"
            jump choices_mondstadt_drinks

        "Rent a transport balloon":
            $ stayed_in_mondstadt = False
            t "It is best to resolve the issue as fast as possible. Besides, if we spend too much time out of Liyue, we are giving the criminal more time to get away."
            z "I haven't thought about it that way. Since we cleared all Mondstadt folk, the criminal must be in Liyue. And we have already wasted so much time with our trip."
            t "I wouldn't call it wasted but I agree. We should spend as much time as possible close to the person responsible. Let's hope they are not long gone by now."
            p "Let's find a transport balloon to rent quickly. Paimon doesn't want to travel in the storm."
            t "The clouds are coming from behind the town square. That means that the storm will hit Mondstadt first. If it moves slowly, we should be able to outrun it and make it to Liyue dry."
            z "You've got a good eye for meteorology."
            t "I've picked up a few things during my travels."
            p "Enough chit-chat, people, the more time we spend here, the higher chance of getting wet."
            t "Paimon's right. Let's find a balloon and get out of here as soon as possible."
            $ end_txt = "The party rents a transport balloon and makes it back to Liyue before the storm"

            call end_screen(end_txt) from _call_end_screen_4
            jump in_front_of_guesthouse

label choices_mondstadt_drinks:
    menu:
        p "{cps=0}Well if both sound good, which one should we go to?{/cps}"

        "Cat's Tail":
            t "Let's pay Diona a visit at the Cat's Tail. She can make us some non-alcoholic drink that will surely satisfy our taste buds."
            p "Mmm~ yummy cocktails as always. They will go well with the dinner Paimon is ready for."
            t "Let's show Zhongli how the younger people of Mondstadt blow off steam."
            z "Oh my... I didn't pin you down as a party animal, Traveler."
            t "Heh... I'm not, but I do like spending time in a good company."
            z "It is settled then. Lead the way!"
            $ end_txt = "The party enjoys a night of cocktails at the Cat's Tail..."
            call end_screen(end_txt) from _call_end_screen_5
            jump mondstadt_day_after

        "Angel's Share":
            t "Let's give Zhongli what he came for. It is not common for him to leave Liyue these days. Might as well enjoy the trip to Mondstadt to the fullest."
            z "Thank you, Traveler. Very considerate of you."
            t "Besides, you love the atmosphere at the Angel's Share, don't you, Paimon."
            p "They do have comfy seats and a secluded upstairs area that is convenient for a nice long conversation."
            t "Exactly, we don't need the best cocktails in town to have a lovely evening. A non-alcoholic apple cider will go just fine with dinner."
            p "You're right, Traveler. Let's make this a night Zhongli can't forget."
            t "Or can't remember - it all depends on the amount of dandelions wine."
            z "Haha~ it would take a lot of dandelions wine for someone like me to not remember the night before."
            p "Is that a challenge I hear?"
            z "No, not a challenge but a fact!"
            p "We'll see, Zhongli. Let's go find a table before it's too late."
            $ end_txt = "The party enjoys a nice dinner at the Angel's Share..."
            call end_screen(end_txt) from _call_end_screen_6
            jump mondstadt_day_after

label mondstadt_day_after:
    scene bg ms_sq_2
    show paimon happy at center with dissolve
    p "Brrr, it is pretty cold outside today."
    t "Yes, indeed. Did you see how much rain poured down last night?"
    p "Mhm~ it saw scary...and all the thunder and lightning. Paimon barely caught sleep."
    t "Imagine if we had traveled to Liyue last night. We might have not made it to Liyue in time."
    p "Paimon doesn't like being wet! So Paimon is very thankful that you chose to stay the night in Mondstadt."
    t "It was a good choice. And Zhongli thoroughly enjoyed himself here."
    p "Speaking of..."
    show zh happy at left with dissolve
    z "Good morning! How was your sleep last night?"
    p "Morning! We've had better. The storm was terrifying."
    z "That's precisely what I was thinking. Thank you for convincing me to stay in Mondstadt for the night. A night of leisure was long overdue."
    t "I'm glad you enjoyed yourself, Zhongli. But we need to get back to work now."
    z "You're absolutely right. The sky looks clearer now. We can make it to Liyue on foot without any issues."
    p "Hehe~ {i}on foot{/i}...."
    t "Yeah... Paimon is just going to be floating around. It wouldn't make much difference."
    p "Heeey! Floating is exhausting as well, I'll have you know! You try and float whole day without a break and see how you like it."
    t "It would be my pleasure...if I could that is. The best I can do is use my Wind Glider to stay afloat."
    z "Aaahh... Friendly bickering... never gets old. And I have to spend the whole trip back listening to this."
    p "Yes, right, the trip. Let's get going!"
    $ end_txt = "The party takes a trip back to Liyue Harbor..."
    call end_screen(end_txt) from _call_end_screen_7
    jump day_after_liyue
