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
    t "Okay so the original plan stands. We will meet up tomorrow morning in front of the Adventurer's Guild. Granted there is no rain in the morning, we can reconvene and resume the investigation?"
    z "You've got it! But I better get going before the rain starts. It looks like it could happen any moment now!"
    p "Okay... Hurry home, Zhongli. We'll see you tomorrow!"
    z "Be safe tonight! Both of you."
    p "B-bye~"
    $ end_txt = "The morning after..."
    call end_screen(end_txt)

label day_after_liyue:
    scene bg adv_far
    p "The End For Now"
