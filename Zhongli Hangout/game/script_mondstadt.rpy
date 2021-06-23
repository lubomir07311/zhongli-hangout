define s = Character("Sara", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])
define tim = Character("Timaeus", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])
define n = Character("Noelle", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])

label mondstadt_square:
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
