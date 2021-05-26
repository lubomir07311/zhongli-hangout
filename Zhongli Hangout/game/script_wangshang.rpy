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

    t "Here we are"
    play sound "audio/sight_effect.wav" volume 7
    pause 0.1
    scene bg wanmin trace with flashbulb

    pause 1
    scene bg wanmin trashed with flashbulb
    show zh happy at left
    show paimon happy at right

    t "Here we are again"
