define b = Character("Bu'yun", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])

label ningguang_office:
    scene bg ning_far with fade
    pause 2
    scene bg ning_close with dissolve
    pause 1
    show zh happy at left
    show paimon happy at center
    show bu happy at right

    b "The moon drinks alone in Guyun's skies, while the great mansion sinks beneath its tides..."
    b "...I wonder, what business brings you here today, honored guests?"
    z "Greetings good man. We are here to meet Lady Ningguang."
    b "I'm afraid that she is occupied by administrative tedium, and cannot meet you presently."
    p "It is super-duper important, Mr. Bu'yun. You know us. We won't bother Lady Ningguang if we didn't have a solid reason."
    b "May I offer you an appointment at a suitable time perchance?"
    z "This is an urgent Liyue business  matter. Someone has damaged a well respected authentic local cuisine center. The crook must be found and punished accordingly."
    b "While the safety and wellbeing of Lyiue's residents is a tremendous concern within Lady Ningguang's mind, I believe she is currently occupied with the process of rebuilding the Jade Chamber."
    b "Wouldn't it be more suitable for you to seek the assistance of The Ministry of affairs?"
    z "We would have, but this issue is concerning Lady Ningguang personally. So would you please arrange us a meeting immediately?"
    b "I'm sorry I have to let you down, honored guests, but at present Lady Ningguang is negotiating with third party contractors. They are arranging the supply chain for the materials needed in order to construct a new Jade Chamber."
    b "The Tianquan has been meeting potential suppliers whole week. I've seen dozens of people come and go through these doors, but Lady Ningguang never leaves or sees anyone without an appointment."
    b "She has food delivered to her office and even sleeps inside the Yuehai Pavilion. Her three secretaries have been busier than ever."
    p "Back up one moment, will you? You said that Lady Ningguang hasn't left the Yuehai Pavilion in a week. Is that right?"
    b "This is the 8th day in a row, so just over a week to be precise. Because suppliers line up from all over Teyvat, her schedule has been packed with meetings at various times throughout the day."
    b "Therefore, it would not be possible for her to leave her workplace for an extended period of time."
    z "Can the Millelith confirm that?"
    b "Absolutely! You are more than welcome to ask the guards around if you don't trust my words."
    z "I don't see a reason to doubt yourself or the Millelith. A meeting with Lady Ningguang will not be necessary after all. We will take the matters into our own capable hands."
    t "Thank you for your time and cooperation, Mr. Bu'yun."
    b "Take care, honored guests."

    scene bg ning_far with fade
    show zh happy at left
    show paimon happy at right

    p "Well at least we can scratch Lady Ningguang off the list of suspects. There is no way she could have went down to the Wanmin restaurant without leaving the Yuehai Pavilion."
    z "Agreed. And as I suspected, we did waste quite a bit of our time. At least we didn't waste any of Lady Ningguang's time as precious as it is, considering the business she is dealing with."

label mondstadt_trip_talk:
    p "Hey Zhongli, are there any other Geo vision bearers around? Has the Geo archon granted any new visions lately that we aren't aware of?"
    z "The Geo archon is {i}\"gone\"{/i} as you know very well. Don't think new Geo visions will be issued anytime soon."
    p "Had to check, just in case. You know... eliminating all possibilities."
    z "If it wasn't anyone from Liyue, maybe it is a guest of the city? Someone who couldn't handle Liyue's spicy cuisine and decided to take it out on the restaurant?"
    t "Uh-uh..."
    p "What do you mean with that {i}\"Uh-uh...\"{/i}, Traveler?"
    t "Now that you mention it, there was a person that vaguely fits that criteria."
    z "What criteria do you mean?"
    t "Well... guest of the city... Geo vision bearer... ate at the Wanmin restaurant... couldn't handle spicy food..."
    p "Nooo...."
    p "You can't seriously be considering..."
    t "Well I wasn't considering Lady Ningguang either, but you insisted on visiting her. So now this is my hunch."
    z "Could somebody please fill me in. I think I'm lost."
    t "See there is this girl in Mondstadt. She is the sweetest maid and would never hurt anybody."
    z "Maid? Is that the girl from The Knight-Maid's Tale that Iron Tongue Tian has been telling recently?"
    p "Yup. Same maid. However, Tian may have exaggerated the story a little. And by a little, Paimon means a lot."
    t "Stories aside, I was helping her prepare for her knightly exam, and we decided to take a trip to Liyue. I took her to the Wanmin restaurant and she did have authentic cuisine, which as we all know is fairly spicy."
    p "Fairly spicy and currently unavailable. Paimon is sad and hungry..."
    t "She had the food and complained a little bit but after all was said and done, there were no hard feelings left. We went back to Mondstadt on our merry way to continue with the preparation for the exam."
    z "I see. And this girl you say wouldn't hurt anybody?"
    t "Typically, no. She is well known in Mondstadt to be a protector of the weaker. Everybody has good relations with her. But last time we saw her, I was worried she might have overworked herself."
    p "Who knows what goes inside that pretty little head of hers. What if something has finally snapped and she came back to Liyue to destroy the man who burned her delicate tongue?"
    t "Um... highly unlikely... but I don't have any better suggestions. Anyone else?"
    p "Too late. She has been added to Paimon's list. Time for a trip to Mondstadt. Zhongli, will you be accompanying us?"
    z "An opportunity to taste an authentic dandelion wine once more? How can I decline such an invitation? While at it, I might catch up with an old friend I haven't seen in a while."
    t "It is settled then. Let's pack our things and get going."

    $ end_txt = "The party takes a trip to the city of Mondstadt..."

    call end_screen(end_txt)

    jump mondstadt_square
