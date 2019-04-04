import re
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
seperator = re.compile('&')
textFile = open('c:\\pythonscripts\\wikiprizepool.txt','w')
a=1
for participant in participants:
    list = re.split(seperator,participant)
    b=list[0]
    c=list[1]
    if a == 4:
        text = "{{TournamentResultsLineDuos|place="+ str(a) + "|prize=|prizeunit=USD|player="+b+"|player1="+c+"|hide=true}}\n"
    else:
        text = "{{TournamentResultsLineDuos|place="+ str(a) + "|prize=|prizeunit=USD|player="+b+"|player1="+c+"}}\n"
    a = a +1
    textFile.write(text)

textFile.close()
