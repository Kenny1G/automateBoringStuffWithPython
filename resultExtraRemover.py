import re,pyperclip
main = """
1	KEPHRII | TWITCHTVBIRD	-44	0	4	7	87
2	z1unknown | Jotobo	-35	10	3	7	79
3	Twitch: Karazz_Tv | twitch.tv/dahmien7	7	51	0	10	15
4	Overpowered | Sonii	12	56	2	4	55
5	Gotaga | Mickalow	13	57	0	8	43
6	BagginsTV | Bonkar	34	78	1	6	27
7	JusDas | ChokeEveryday	53	97	0	3	22
8	OWN3D.TV WhoisRoxis | OWN3D.TV EmDy	54	98	0	4	19
9	twitch.tv/DatKoko | ConflictScurry	64	108	0	4	14
10	Forsen | Kowa	66	110	0	2	26
11	frag^m | cml	72	116	0	2	10
12	420Brain | Gamehunter	73	117	0	3	9
13	eU PrinceDannyTV | SK Alternit	76	120	0	2	22
14	TSM Gale Adelade | Dyrus	76	120	0	2	24
15	twitchtvchapo | RNG|Viral	78	122	0	3	13
16	xil7 | Tempted	81	125	0	2	14
17	Twitch.Voiiid | Synergy	82	126	0	2	16
18	twitch LAIKbl | Ikaros	83	127	0	4	7
19	Mad_Ruski | C9 Chappie	84	128	0	3	13
20	Mtashed | Truevanguard32	85	129	0	2	14
21	Teldo | twitch.tv/thordg	88	132	0	1	14
23	HighscoreHero | Gorg	94	138	0	3	4
22	.tv/TheLuffyTV | Enta	94	138	0	1	14
24	Kwolve | KevaFlazh	98	142	0	2	17
25	DeGuN :o) | Locklear	99	143	0	3	14
26	Jaggerous | Ry.	102	146	0	1	0
27	ZombiUnicorn | AimzAtchu AimzAtchu	104	148	0	1	0
28	Lassiz | Incon	105	149	0	0	17
29	mykL | MOETORIOUS	105	149	0	2	4
30	twitch.tv/1cePrime | GIDDERS14	107	151	0	2	4
31	unge | INNERVAULT	109	153	0	0	4
32	Cirouss | k1llsen.BIG	111	155	0	1	6
33	Onylight | Faz	111	155	0	1	9
34	pF.OctanePro | pF.Scissors	123	167	0	0	5
35	Whitey | OWN3D.TV hEnGzT	136	180	0	2	3
36	Dhalucard | Dadosch	165	209	0	0	4
37	Der Butterer | MarcoOPz	172	216	0	0	2
38	Shlorox | LaraLoft	174	218	0	0	0
39	NokSs | !b3uZ	175	219	0	0	0 """

regex = re.compile(r'-?\d*\t*')
noNumbers = regex.sub('',main)
list = noNumbers.split('\n')
pyperclip.copy(str(list))
