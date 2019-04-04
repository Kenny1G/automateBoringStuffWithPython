import re,pyperclip
seperator = re.compile('&')
# participants = ['Onylight & Faz','Kwolve & Kevaflazh','DaretoCare & Santans','Mtashed & twitch.voiiid','Twitchtvchapo & Weak3n','Kephrii & Twitchtvbird',
#'TSM Gale Adelade  & Dyrus','eU PrinceDannyTV & SK Alternit','Mykl & Moetorious','Mad Ruski & .tv/TheLuffyTV','BagginsTV & Bonkar',
#'Z1unknown & Jotobo','Frag^m & Znatch','1cePrime & InsomGG','Nosyt & Epindary','Warchi^^ & TwitchTV_fak3zito','Lasbra & Mikey',
#'Sonii & Overpowered','Handwerk3r & Fahrrad','Buddha & Gamehunter','ONCA|enQ. & ONCA|unikat','Youngbae & Balrogx','Lassiz & Incon','Twitch.Karazz_TV & StandiiN',
#'IHOLDSHIFT & SSLCK','C9 Chappie & Twitch.tv/Anonymouse','ONCA|Jonek & ONCA|AleHAJT','ZombiUnicorn & AimzAtchu',
#'Mixer.com/1HP & Mixer.com/incision','Twitch/Shaw & G2 Vex30','JusDas_ & ChokeEveryday']
finale = []
participants = [ 'KEPHRII & TWITCHTVBIRD', 'zunknown & Jotobo',
'Twitch: Karazz_Tv & twitch.tv/dahmien', 'Overpowered & Sonii',
'Gotaga & Mickalow', 'BagginsTV & Bonkar', 'JusDas & ChokeEveryday',
'OWND.TV WhoisRoxis & OWND.TV EmDy', 'twitch.tv/DatKoko & ConflictScurry',
'Forsen & Kowa', 'frag^m & cml', 'Brain & Gamehunter', 'eU PrinceDannyTV & SK Alternit',
'TSM Gale Adelade & Dyrus', 'twitchtvchapo & RNG|Viral', 'xil & Tempted',
'Twitch.Voiiid & Synergy', 'twitch LAIKbl & Ikaros',
 'Mad_Ruski & C9 Chappie', 'Mtashed & Truevanguard', 'Teldo & twitch.tv/thordg',
 'HighscoreHero & Gorg', '.tv/TheLuffyTV & Enta', 'Kwolve & KevaFlazh',
 'DeGuN :o) & Locklear', 'Jaggerous & Ry.', 'ZombiUnicorn & AimzAtchu AimzAtchu',
 'Lassiz & Incon', 'mykL & MOETORIOUS', 'twitch.tv/cePrime & GIDDERS', 'unge & INNERVAULT',
 'Cirouss & kllsen.BIG', 'Onylight & Faz', 'pF.OctanePro & pF.Scissors', 'Whitey & OWND.TV hEnGzT', 
 'Dhalucard & Dadosch', 'Der Butterer & MarcoOPz', 'Shlorox & LaraLoft', 'NokSs & !buZ ']
# main = "/{/{TeamRoster/Duos|team=" + c + "|player1="+ a + "|flag1=|player2=" + b + "|flag2=/}/} /{/{BlockBox|break/}/}"

for participant in participants:
    c = participant
    list = re.split(seperator,participant)
    a = list[0]
    b = list[1]
    main = "{{TeamRoster/Duos|team=" + c + "|player1="+ a + "|flag1=|player2=" + b + "|flag2=}} \n {{BlockBox|break}}"
    finale.append(main)

realFinale = '\n'.join(finale)
pyperclip.copy(realFinale)
