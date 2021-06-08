define z = Character("Zhongli", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])

label parlor:
    scene bg wangsheng with fade
    show zh happy at left with dissolve
    show paimon happy at right with dissolve
    p "Hey, Zhongli. It's so nice to see you!"
    z "Ah~ Paimon, Traveler, good to see you too. To what do I owe the pleasure?"
    p "Well, it is more of a business visit than a pleasure one. This does not mean that it is not a pleasure to see you..."
    t "What Paimon wants to say is \"Hi, how are you?\""
    z "Haha ~ I've been good. Keeping myself busy with consulting here at the Wangsheng Funeral Parlor. How about you two?"
    t "You know how the life of an adventurer goes. Some daily commissions, dealing with the Abyss whenever they are spreading evil and helping unblock the roads."
    z "Good to hear you are keeping the situation in Liyue under control. The Abyss can be a tricky enemy to fight. Have they done something evil recently?"
    t "Um..not that we are aware of. Just the usual dances around open bonfires and harassing unsuspecting merchants on the road. Nothing the guild can't handle."
    z "If not the Abyss, then what is that \"business\" visit that Paimon is referring to?"
    t "Well we can't fully rule out the Abyss just yet. But the reason we came to see you today is that somebody trashed the Wanmin Restaurant last night."
    z "Is that so? "
    p "Yes, and there are rocks."
    z "Rocks? Did somebody vandalize the restaurant?"
    p "That's what we thought at first. But then we went inside and saw the rocks. We could not recognize their origin. They don't look like ordinary Liyue rocks."
    t "On top of that, some of them are pretty big. Doesn't look like a one-man job. But if it was, it must have been someone {i}powerful{/i}. And I mean not your everyday strong man."
    z "I see."
    p "We are coming to ask for your help with this issue. The Wanmin Restaurant has stopped its business because one of the boulders damaged the stove. We can't help repair it, but we can find who is responsible."
    t "Well, we are trying to. We were wondering if you would be willing to land us a hand. Nobody knows rocks better than you."
    z "I suppose I can take a look right now. "
    p "But aren't you on duty with the Wangsheng Funeral Parlor at the moment?"
    z "I am. But I doubt the boss will mind me taking a break at this time of day."
    z "Besides, she is busy trying to come up with a better promotion than the 2 for 1 she ran last time. It wasn't very successful."
    p "Yeah... Paimon remembers. She spooked a bunch of people in Liyue with her sales pitch."
    t "Thank you for agreeing to help us on such a short notice, Zhongli. As soon as the Wanmin Restaurant is back in business, we are going to treat you to a nice bowl of Boiled Fish."
    z "That would be a nice change from the usual I get at the Liuli Pavilion. We have a deal. Lead the way!"
    $ end_txt = "Back at the Wanmin Restaurant..."
    call end_screen(end_txt)

    scene bg wanmin trashed
    show zh happy at left with dissolve
    show paimon happy at right with dissolve

    p "Wow wee...what a mess. There are rocks everywhere."
    z "Hmm... I see now what you meant. These types of rocks are not from the Liyue region."
    t "Do you know where they could be from?"
    z "I can't say for certain. Some rock formations don't look natural at all. Perhaps they were conjured?"
    p "If the rocks were conjured, there would be elemental traces left over, right, Zhongli?"
    z "That's correct. It is highly likely that they have been conjured using the power of Geo."
    p "Well, if that's the case, Traveler, you can use your elemental sight to check for elemental particles!"
    t "You're absolutely right. Let me give it a try..."

    play sound "audio/sight_effect.wav" volume 10
    pause 0.1
    scene bg wanmin trace with flashbulb

    pause 1
    scene bg wanmin trashed with flashbulb
    show zh happy at left
    show paimon happy at right

    t "Wow, the rocks are resonating strong geo energy. I was able to see it clearly with my elemental sight."
    p "*gasp* .. Paimon is afraid we are not dealing with small town vandals anymore."
    z "You have every right to be concerned, Paimon. Whoever did this must have a good motive. They've put so much geo energy into this unlawful act."
    t "But Chef Mao said that there is nobody that holds a grudge over his family or business. We don't have a list of suspects to work off of..."
    p "Maybe we should put the motive aside for a moment and think of the people who could actually have committed the crime... you know... the people who can manipulate the geo element."
    t "Paimon! Don't look at me like that... I've been with you this entire time. When could have I done it?"
    p "Well, Paimon was sound asleep last night. What were you doing?"
    t "Uh.. Sleeping... next to you... I like the Wanmin Restaurant and Xiangling is a good friend of ours. Besides, I think you would have noticed if I had gone missing in the storm last night. My clothes would not have had the time to dry until the morning."
    p "You are right... Silly Paimon, doubting the Traveler like that. Soo..."
    z "Me? Haha~ Paimon, please. If I wanted to damage the Wanmin Restaurant, I would have summoned a whole meteor to crush the place, don't you think?"
    z "Chef Mao is an honest businessman and runs an exquisite restaurant. It would be unethical of me to ruin it. This will damage Liyue's economy and is not in my best interest."
    p "Sorry, Zhongli. Paimon should have not doubted any of you in the first place. Just trying to cross names of the suspect list. If not you two, who do we have left?"
    menu:
        p "{cps=0}Sorry, Zhongli. Paimon should have not doubted any of you in the first place. Just trying to cross names of the suspect list. If not you two, who do we have left?"

        "Lady Ningguang":
            t "The only other Liyue Geo vision bearer would be Lady Ningguang."
            p "The Tianquan of the Liyue Qixing? She has no interest in hurling rocks at a local restaurant. But then again, who does?"
            z "Lady Ningguang is a busy woman. I'm not even sure she makes her way to this part of the town these days. In my opinion, paying her a visit would be a waste of time."
            p "There aren't many options available anyway. Might as well cross them off one by one."
            z "I suppose that's one way of looking at it. By the process of elimination we might get to a reasonable conclusion."
            p "Exactly! So should we pay her a visit?"
            jump choices_ningguang

        "Mondstadt folk":
            t "Lol Mondstadt folk"

    t "Here we are again"

label choices_ningguang:

    menu:
        p "{cps=0}Exactly! So should we pay her a visit?"

        "We have time for a visit":
            t "It shouldn't take long. Let's try and clear the more obviously innocent people first and later we can focus on the vague options."
            z "I guess we are going to the Yuehai Pavilion then?"
            p "Yup! To the Yuehai Pavilion to clear Lady Ningguang's name."
            $ end_txt = "The party makes its way to the Yuehai Pavilion..."
            call end_screen(end_txt)

            jump ningguang_office

        "Let's not waste time visiting":
            t "I'm going to agree with Zhongli on this one. Visiting her will be a waste of our time for now. We might want to act quickly while the crime is still fresh"
            p "Hmpf~ fine. Paimon will scratch her off of the list... for now."
            jump mondstadt_trip_talk
