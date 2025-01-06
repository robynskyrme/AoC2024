
# AoC 2024
# Day 3: Mull It Over

# 5.1.2025

# yo *Roger* please remember to comment stuff



import time


def is_string(slab,index,string):
    for i in range(len(string)):
        if slab[index] != string[i]:
            return i
        index += 1
    return True

def valid_mult(slab):
    opencheck = is_string(slab,0,"mul(")

    if opencheck is not True:
        return False,0,0

    x = number_digout(slab,4)

    if not x[0]:
        return False,0,0

    if not is_string(slab,4+len(str(x[1])),","):
        #print("boom ONE")
        return False,0,0

    y = number_digout(slab,5+len(str(x[1])))

    if not y[0]:
        #print("boom TWO")
        return False,0,0

    if not is_string(slab,5+len(str(x[1]))+len(str(y[1])),")"):
        #print("boom THREE")
        return False,0,0

    return True,x[1],y[1]

def number_digout(slab,index):
    if not slab[index].isdigit():
        return False,0

    numst = slab[index]
    index += 1

    while index < len(slab):
        if slab[index].isdigit() == True:
            numst += slab[index]
        else:
            return True,int(numst)
        index += 1

    return True,int(numst)


def process(slab):
    valid_data = []

    do = True

    index = 0

    while slab:
        if is_string(slab,0,"don't()") is True:     # added these checks for Part Two
#            print("boom FOUR")
#            print(slab[:7])
            do = False
        if is_string(slab,0,"do()") is True:
#            print("boom FIVE")
#            print(slab[:7])
            do = True

        valid,x,y = valid_mult(slab)

        if valid == True and do == True:
            valid_data.append(x)
            valid_data.append(y)

        slab = slab[1:]

    return(valid_data)

def add_multiplications(data):
    sum = 0
    for i in range(0,len(data),2):
        m = data[i] * data[i+1]
        sum += m

    return sum


if __name__ == "__main__":
    stopwatch = time.time()

    data = process("mul(168,87)}*:mul(911,800)(%,)where()#&&$mul(734,19)?when()why(){$:?mul(829,495)do()mul(724,312){;^mul(520,383) mul(137,485)select()-mul(700,211) <(who()who()/mul(295,600)]~<select()'$why()do()when()mul(310,255)^}where()who()(!+mul(16,916),)what()@:@#where()mul(918,822),when()~/)mul(177,722)<&]:who()where()>mul(439,650)?+$mul(349,399)mul(807,317)what()?@[%mul(674,778)!mul(104,928)~[!!mul(60,636){where()when()&@why()-+mul(742,28)select()why()'&why()@>select()mul(527,483)mul(797,855)how()mul(502,647)what() {(*'}%mul(688,600))!??,+$mul(538,127)&from(),>~&*mul(963,787)~mul(820,259)~}~how()>do()what()^<}[?{'mul(202,9)$select(795,484);from()<!mul(913,93)/{{what()#-select()how()]mul(520,288),^&what()mul(583,623)mul(657,601)>;^@what()mul(671,74)&@how(151,76)!?:{mul(933,567)/)&select()do()>+,~?>mul(627,488) *mul(437,91){!#}%?how()who()mul(741,704)select():where()mul(258,129),&why():)mul(770,13)@ from()?-!what()$mul(229,613)from() select()why()};select()mul(59,263)where()from(97,930)?where()mul(514,278)(-don't()&$[how()why(783,866)&who(589,80)#; mul(130,239)don't()mul(195,249),~>>who()mul(945,698) /}how()>mul(983,248)[~why()({from()-(how()?mul(206,469)&>~who()]mul(661,410)how()&mul(768,601)/!--select()>,%mul(455,805)(}]how();<who(735,631)why()mul(216,340))what(181,514)mul(736,427)^when()]$%where()'<;mul(754,836)*@!why()select()]mul(869,551)~mul(752,713) <(~&@#mul(124,162)why()/mul(512,273); /where()why()mul(471,915)/(where():?}mul(608,515){[@:'select()[][ mul(983,96)%where(),why(){~-+]mul(102,860):#?select()%who(105,947):who(416,728)mul(765,635)@(mul(898,549)$where(580,81){mul(497,154)>/from())mul(728,180)'(what()[mul(915,20)who()+&don't()select()^)}$!who()+>mul(481,439)- *mul(332,923)when()-why()!mul(625,335)?mul(156,134)why()*'$:mul(104,186)^?#>/mul(605,863),,?mul(161,457)!#~,#~>/mul(514how()where(),'$;'$+)mul(207,90)&>$how()mul(394,95),where()'mul(827,742)how()[from()(]:/why()$+mul(46,294)>who()who()^@[^mul(500,356){]{mul(989,398)(}: mul(300,17):how()who()%?#@why()!mul(362,556)>$mul(29,294)who()<;when()mul(108,898),#<<~-*(where()@mul(86,710),'-$&what()(mul(573,832)),?{mul(953,794)why()^what()-*,/?)mul(511,634):how()/how()'what()what()mul(709,593)]mul(721,842)(!&why()where()&mul(259,304/$[*why()+#mul(932,748)? {mul(979,591)mul(576,282)(-when():^,select()>@mul(146,41){[<#(#'*}mul(615,174)&>when()what()&(mul(914,488)[~why(267,875)mul(167,385)+<%~}@![why()mul(221,316):,;[:@(!who()mul(340,617)&*how()%mul(151,744) >},-)'?mul(414,238)mul(100,868)%%what()where()mul(467,880):mul(266,276)!@!#'who()'mul(500,629)[#^select()*+how()(mul(538,599):* [;'mul(919,315)mul(760,200) <$/$}{why()'(mul(794,683)from()**'$,}}mul(915,608)>$$mul(114,893)what()select()do():^from()??from()from()^mul(316,793)>'/when()+mul(199,368)[~mul(539,838) ^(*??%mul(162,286){mul(647,357)who()$(>what()?,why()>from()mul(239,449){select()who()mul(408,790)mul(567,879)when(),who()[what()mul(874,22)mul*'mul(908,653)>~)@mul(773,355)#mul(716,195) ?@who()mul(128,574)^select(),{:mul(799,387)who()-)+]select()'mul[mul(153,811)from(854,516)select()'(',#mul(760,387from()mul(434,344)@?what(),&!'mul(108,675) 'who()%>+why()mul>]%select()[mul(793,13)mul(333,332)~why()/what()mul(774,658)**mul(375,739)[)*what()what(),>::>mul(702,335)%}{-@'~who();mul(992,903)}where()$(~@)'%mul(488,891)where()*);why()what():{&why()mul(29,881)&]where()where()~*mul(886,964)}&):where()who(){?mul(60,664)why()from()< +select()[when(789,49)$mul(40,510)<how()who()mul(755,503)mul(851,686)?#;}{{from()~'do()>from()~ who()>?from(431,14)%[mul(313,439)mul(999,227)[how()']what()(%,don't()who()><{#~'where()?mul(796,988)what()$/why()#select()/#what();mul(401{~mul(949,141)when()why())/^$$}^(mul(472,738){]:+mul(372,612)mul(647,895)>&$***mul(619,883)(;^mul(864,456-}#/?mul(68,612)~,}>from()!>-when()mul(997,365)mul(524,378)where()where()/!mul(301,937) ++?^what()mul(656,303)}{}mul(953,842);select()select()~[)<mul(617,87)where()what(517,442)~{mul(412,205)-?^?from()],+mul#?%#mul(389,357)how()!$<mul(809,511)who()>do() !;!mul(344,321)from()mul(819,403)+how()where()where()<($mul(908(,>%*why()what()^mul(533,374)-,select()mul(905,803)mul(140,691)what()([mul(874,79)]?how()what()?->mul(344,908)$#&#;from()!mul(256,631){where()#@,]~*:why()mul(225,679)where()?[mul(141,585)+)@~#how()mul(933,177)((+select()mul(312,241)+mul(247,632)how()^[,&from():where()%mul(663,72)![@@when()mul(274,536)>who()@mul(269,240)mul(732,115)!%@'%mul(479,836)-why()mul(502,828)#mul(548,385))mul(312,586)/&{//+{^mul(275,705)where(377,884)$ *!who()mul(382,713)+<@(<>)[select()'don't()mul(182,291)select()]:*select()where(872,531)what()&)mul(361,941)why()/+mul(832,469),-$)mul(753,874)^when(){,@mul(865,352),+#what()mul(749,612)!?#]from(),#mul(734,31)when()^mul(992,318)mul(396,187where()mul(134,182)&<&%$[>,mul(527,215)mul(400,794)'~what()mul(427,148)where()from()<<mul(867,258)<>-mul(495,578)where()}-don't()select()%+^{]what()where()mul(730,966)%$where()'mul(507,416)from()~)how(488,343) %<%>$mul(486,368)what()why()[mul}^^{who()what()[select()'why()who()mul(214,853)from()how(301,437)^):)]how()mul(657,161))(^@select()'mul(313,702)(mul(486,323)*&;&why(){'&how()-mul(911,603)-what()%mul(519,498))select():from()mul(652,991)!!/,mul(308,418)- &#+(who())~)mul(749,786);what()(mul(731,76)<!mul(572,33)/%:;select()from()mul(509,810)~mul(861,431)>do(){&what()$+-^how()mul(214,122)mul(540,414)from()mul(640,157)select()< #:;]^mul~mul(705,467)(?[}when()>where()?mul(45,584)~when()^;mul(519,782)}#when()+[mul(670,319?>]mul(451,604):mul(646,328)when()^mul(326,180)why();who();'$mul(642,425)from();?+when()]mul(907,636)what()%;do()what()?{who()mul(974,27)>{how()(^}mul(357,294)${~[@mul(983,221)who(){(!~from()^mul(128,197)*mul(942,48)>:+]{/from()#mul(237,772)<+select()@mul(361,84);why()]!)who()}+mul(740,305)&,[>]how()mul(660,613):)from()do() select()?when()%select() (mul(835,437)why();)</? how()mul(417,353)-( !select(480,286)mul(935,409)who()/*^+$mul(48,5)>how()mul(819<%/{how(675,621)where()@(>from()mul(722,49)+)do()%;!who()who(772,423)]$<-mul(328,361))mul(149,957))do(){#!where()>#what()(select()/mul(756,781) *-select()?why(713,643)mul(514,277)$]how()/^mul(7,203)%when()how()who()mul(389,589~]who()*>$^@mul(129,92)~;mul(759,369)how()*!&from()/when()%mul(650,562),*who()*'%when()mul(236,299) }?how()how():don't(),who()how()'why()who()what()@mul(322,510):-@:$@^mul(634,343)-what()#what()from(38,805),<+mul*where(835,107)where()&where(816,43)(%{mul(617,254)where()!^![ who()?;<mul(166,155),$*:<mul(827>/~*;why()mul(788,442))-what())!?(mul(662,916)mul(401,521)mul(234,405)+~,{>from() :{select()mul(635,416)+[~[,mul(562,550)mul(152,551)#]mul(164,957)~<what()#where()>from() mul(761$who()?--<where()+mul(795,259)[~{?<select()&:mul(229,87)mul(864,182)how()?mul(974,34),mul(627-mul(177,523);,^mul(45,82)[-!}mul(370,437)(#:];:(mul(818,270)'}^]when()how(934,258)don't()'{+*why()}mul(530,297)]^/$from()<who()*$mul(842,310)from()^/)%select())+mul(482why()select()&from(415,942)!]how()why()mul(279,984)~when()>}~'/who()when();mul(796,168)what()mul(199,983)>:]when()?why() mul(410,263) when()how()?mul(413,448)]mul(825,830)# mul$mul(261,686)@~{>{what(276,567)mul(341,638)who(){?*$[why(831,759)^ from()mul(741,711)'who()select(){mul(61,52)[what(){%don't():who()@mul(219!)?];where();' *mul(371,514)>[:mul(53,428!mul(538,853)]$#~do()@mul(200%{$$[$#$)mul(57,357)/mul(399,855)~<(*@~what()(@mul(814select():what()]~[#mul(507,982)**mul(68,893)}#mul(631,348)from()mul(205,133)mul(497,687from() !mul(728,117)[;)'@/}@{mul(678,169)who()@$@@~%how()mul(959,969)%@^&{~! ]%mul(324,123)'from()who()}^%mul(763,855)from()^when()#{ /from()#]mul(316,502)what())^<^%%mul(813,959)&why()~~-?-mul(798,375)$>{#'why()&:,why()mul(83,95)(don't()mul(798,687)when(506,624)from()(,how()^: ]>mul(149,563)why()~mul(41,612)-:?when()^/)mul(974,373)>when()?how()*mul(36,761)what(){&@)mul(390,671)when()mul(696,964,@when()@$/?~>~mul(548,987)select()what()% who();$mul(80,587)&^{+,don't()?what()*why(),( mul(124-^>how()/>'mul(155,901)?<;when()!!mul(90,13))/'^from()&[,)mul(805,998):@select()/~from()+(^/mul(823,626)%where()select()how()%&>mul(257,517))#->mul(304,899))mul(255?mul(302,286)>?@<mul(777,721)^&what() !from()/*where()mul(817,696)why()#+&who()why(351,81)}where()$mul(237,864)<&(do()^?from():*{<who()select())mul(975,616),{+where()/@@who()mul(549,977)@<)when(),mul(508+<$mul(716,515)^,-]who()#select()<+mul(118,226how()mul(543,380)(how()?select()from()@}mul(28,144);;'>mul(899,21)@mul(619,488)$->&^@from()(*-mul(266,282)/]from()@who(109,244)()mul(98,720)why()what()>;% mul(681,256)#~)]from()@&mul(517,40)@@what())mul(725,452)mul(852,71)?$mul(612,673*select()what())#mul(120,4),where()who())mul(808,259)who()'^~mul(325,215)!>select()~mul(853,581)%why()mul(652,100)%<select()##what()~mul(237,441)when()!how(753,120)^mul(890,518)from():,who(196,65)+#$ mul(664,43)}%^how()/from()[[when()mul(39,906)mul(324,714)#[#from()mul(569,489)'<who()*@mul(167,880)*select(){>^@don't()/,when()~what(),+&mul(975,420){+*when()]^how()*why()who()mul(448,331)!/when()~mul(235,190)^$}+*++{#mul(96,137):?%where()mul(511,78)};^{&:when()!don't()&when()''&#:{mul(205,318)*!where()?when()~/&from(733,701)?mul*#&#where()where()]{select()mul(474,265)from(755,678)why()!;#]'>-]mul(132,817);&)]^*what()[mul(831,118)select()<mul(181,530)%)mul,])!<>+how()how()mul(292,875)%&select()[@*mul(868,274)&@select(),{mul(427,903)/@]mul(620,307-+what()select()-where()mul(206,860)-mul(937,784):where()!+mul(347,517)#!/usr/bin/perl(select()~from()mul(730-,what()!where(360,351)what()*how(600,916)mul(929,974)~]#<!when()[~*<mul(132-+why()#%*~:@mul(416,703){@#';>mul(190,848)?{from() }where()<mul(527,529)-mul(209,184)?[what()when()mul(77,529)why()how()<#who(360,918)-mul(417,741)where()what(269,273)from()(mul(322,695)select()@^][don't()]mul(739,357)']when(789,549)/:&when()>mul(532,685)#+~^&]^where(947,658){mul(835,556)mul(785,197)@mul(20,129)>(%*$?,%^]mul(309,855)(!select(){[?](mul(408,217)+;who()why()-&$ ,$mul(824,38)&mul(848,553)@where()who(774,973)-[;mul(590,491)what()'/mul(625,672)!}~~%>-{]-mul(113,831)}+//>(what()mul(822,256):<*$!select()mul(743,335)how()^* (<mul(341,513)do() {,(how()*,^&mul(777,587){>^what()'{[,select(249,901)mul(795,853)@$;mul(486,10)>>?~mulwhere()<~}mul(375,790)/}when()*!mul~-select(){select()select()<]don't()''-'mul(934,731)select()';*select()&why()mul(280,932>mul(530,961)how(),-{how()&what()>(mul(285,204)who()+select()>~>?/<)mul(791,587)from();~mul(142,801),from()~>when()mul(636,737)mul(122,583)select()mul(29,534)[<}>~?;++,mul(853,461)where()&/where()>do()what()where()mul(224,748)when()(from()$%>mul(537,689)@how()from(97,626)%!mul(854,118)when(998,592)-+>how()'when()/mul(548,649)who()who()#) &@!,do()}[^[@mul(154,777)mul(96,225)when()mul(951,144)what()mul(358,785)select()+from()what()-$mul(507,770);select()where()where()mul(696,121)who()when()]&$}how()what(){mul(63,669)+*where()/why()mul}&@where()!?'@;mul(81,559)*]how(372,376)mul(602,773)+mul(511,514)) (,}mul!#%$where()from()%~?>+mul(451,596);from()mul(719,514)^who(533,943)}how()@mul(382,562)!#[,@*)>mul(234,778)&-mul(280,479){, [do()how()!&{mul(971,30)'@why()) ?:+>don't()where()%from()/*&&!mul(551,129)where()!when()@@>[$mul(266,378)&mul(354,236)where()who()mul(198,648)when()~<[what()what()mul(215,213)mul(687,432){,mul(595,927)+<why()*@how()*{%mul(764,459)>who(829,436)^+mul(424,283)@why(),mul(169,939)/[*from()> %!(mul(537,425)%^mul(352,791)*#when()when()-&;what()mul(904,80) select() how()how()mul(34,66)@%<mul(276,65)where()when()how()})mul(52,448)who();select()mul(692,130)what()${%&^%mul(444,170)[)(,<mul(297,209)%&]select(170,397)$mul(577,234),select()^:~,[*>do()mul(921,346)/#what()mul(49,901)mul(734,885)/)(:mul(553,997)(who()mul(62,853)from(535,930);where()#what()mul(457,969)&(+(*}why()mul(317,972)where()when()$do()why() why():~%:^mul(447,529){mul(612,477)how()$when()mul(66,532)>$$*mul(945+*<how(289,725) who() what()how()how()}mul(304,883)select()^':{/':'-mul(715,525)!mul(270,804)from()::['when()why()mul(93,166),-when()!mul(736,616)+;mul(531,606)<how()&[+&mul(967-^'}+-}from()mul(178,389)who()<*mul(116,273)#);#select()mul(628,521)@}where()<where()(;how(376,88)<mul(99,450)}<how()$mul(612(mul(214,455)?:mul(841,59)~~mul(162,250)^]#&>*^)who()mul(291,880)/mul(903,311)*;how()mul(58,539)]-@+&%),what()mul(501,878)*[[mul(626,427)]}how()?when()[mul(280,653)/when()]-<mul(765,466)~-<(select()}{){do()from()*where()!;mul(701,836)'~mul(529,579);!:'+@/'mul(54,282)^<'mul(792,927)&mul(470,236)who() @ ])+??mul(693,230#+~?:-^mul(814,574)from()<when()@#mul(430,705)where(),when()@*$!what()$how()mul(95,323)who()when()mul(38,704)@{where()why(),from()where()[{<mul(455,604)}where()from()~mul(719,681)mul(131why()^where(389,683)**mul(331,541)-}{mul(320,970):}#mul(737,307) *?)~,]mul(740,642))><mul(666,137)why()where()where()from()why()$ mul(709when(),select()*]when()(mul(510,937)&+>where()why()mul(235,299){;select()mul(543,852)>mul(456,133)(>mul(671,153)'?*who()(mul(12,640)<{##+mul(432,266)*>)'[~>$~?mul(816,840)what()-mul(698,399)how()mul(45,603))~*what()mul(737,715){when()why()~from()mul(995,968)where()mul(262,96)^?who(){; )from()who(615,278)mulhow()mul(838,616)}from())mul(865,576))~-;how()mul(192,403)))[-$]^select(),mul(184,369)#why()*^;)(do()#,'mul(423,897);)]what()/[$]mul(867,533)select(138,395)*-how()mul+#<why()}[~{mul(925,163)<mul(798,343):mul(137,381)~/>;mul(515,882)]:(mul(364,946)&!&,how()select()- mul(111,167):~$from()^]don't()&mul(829,425)!'/how()where()]/<what()mul(521,742)mul(316,792)mul(311,104)from()<%mul(869,189)^&why()[&:mul(683,138)how()mul(533,311)from()%what()@mul(785;select()~?{}++where()mul(102,590)}&what()}(^[<:mul(997,376)'@/$;mul(25,111)~+$]^;+?mul(786,845)@why()&mul(737,79)''from(340,968) how()where()^?mul(803$select()*why()!select()*/%-mul(450,746)who()-(from()where()when(525,894)mul(110,878)-%select()$)@;mul(445)]-~~*/)&mul(205,632)$[^}select(599,536)how()how()who()]mul(952,986)who()/#*:]who()+/mul(346,355)^where() don't()@who()?+&;mul(617,393)&how()>mul(195,257)*mul(953,79);who()when()$,from()<>why()mul(529,405)from()&mul(492,793)&#*[;+;-mul(331,898)?/{+}mul(424,343)$~[mul(523,74)why();mul(772,703):;mul(17,157)! }why()/]!^mul(979,338when()$?mul(898,616)}why(359,279)+from()what())}$from()!mul(612,784)(where()mul(640,368){#!mul(69,807)]how()( #mul(739,987)'*~&%who()!}@mul(834,525)when())::$mul(122,894)%+^(who()@when()%mul>when()from()?mul(464,80)$^! !/@?@,mul-what()!!@:[mul(283,21)([how()[mul(11,617)]}where()/mul(976,268)mul(843,731)<how()why()[mul(601,412)%how()!]@*why(136,791) -mul(371,365)@~$*'~[/ mul(15,594)how(),/{#-}>'mul(676,131)where()}{(]'where()mul(459,88);(where():mul(64,747);[&$})+select()&;mul(750#[{;*&mul(458,334)?where()select()%)mul  what()?when()mul(808,879)what()*}-$+from()where()@mul(152,857)'#%where() /<:+?mul(304,149)from()!<when(865,985)mul(238,815))~!+<)@from()mul(401,975)%&mul(625>*!mul(802,11)!*select(),; )-;how()mul(199,993)/!when()^;[)mul(577,723)!?^who()+what()<mul(489,809)~what(625,812)<?;*#)how()do()!(]who()what()where()*from()+mul(705,108)(who()why(815,180)[]^[mul(821,379)&^(&<,%mul(197,678)%-what()mul(944,295)select()how()!mul(357,711))$-what()'&)'mul(114,910)}<*@-from(688,563)[mul(279,269)from()}$mul(707,287)<;*+what()*>when()mul(447,881)+'(+&@&do()mul(192]what()%/mul(463,832)mul?^*>why()where()from()what(){*mul(456,920) $where(911,93)select()+who()select()}don't()}!how()what()~+what()mul(404,558)>,>{(?{'&,mul(936,304);mul(232,989~;>]who()mul(582,897)*!mul(11,23),~>!{<who()$>mul(542,522)^;,from()(?mul(177,928)how(985,316)}who()@](-#why()mul>~why(851,863)[)!@>mul(101,448)select()+?%&select()~((mul(11,450)how()^)mul(344,639)}+;mul(343,648)^why()!where()&{/'#mul(9,810)where()-%mul(877,263)&select();where(240,275)[mul(289,282)how()&<{who()} ['do(){mul(818,421)/}$]mul(617,829)~['why()?&~)mul(741,559)mul(133,701)$]:@&mul(594,307)[',how()^{how()mul(388,657!({'mul(492,896)#@/why()why()mul(127,225)}>where()-/,^mul(219,314))mul(682,893)what()why(){(,from()(?mul(219,360)what()' ](mul(80,569)select(82,585)mul(693,510)%$what()from()mul(740,749){~'<]mul(281,263)when()(!?>/% +mul(116,41)-*-when(506,165)?^}mul(651,943){~,/what(){#{!mul(629,41)/mul(74,998)?mul(525,86)&how()do()+/%mul(15,103)#select(671,57)from()who()]mul(309,559)%>mul(311,459)'when()@#mul(980,750)when()+%how()how()~:mul(484,554) )+{ - :]mul(113,626)[^<%,mul(187,326)*:!]*!mul(374,45)from(),mul(41,137),^)-,#when()?who()mul(93,289)select(853,56)]^where()mul(43,349)*where()mul(406,653)from()from()*&*mul(486,350);)*~how()mul(817,387)>>when()who():mul(417,224)^!&{from()}@mul(342,365)why()^who()+~!}when()do()why()when(939,686)^)((mul(160,438)what()>mul(23,766)+]*mul(618,433[/~where()[;why()what(){mul(292,318)*$why(664,963)how(68,975)why()who(276,89)where()!why(777,555){mul(875,358)@'[#who();)mul(198,992)?:(?~where()what()how()-'mul(956,332)mul(889,561)from()((what()mul(753,443)#>? , -mul(267,527):when()+mul(225,923)>>?^mul(726,980)~when()'mul(760,283)!;why(),;when()mul(358,713)//select()]%^{why()*'mul(406,429,(: {how()!^;mul(363,272)--where()*:select()when()?when()mul(242,130);why()>:!&why()$mul(386,685)@!}>when()why()>how()how(872,684)mul(418,627)why()[{:[-%mul(946,701)(}mul(10,874)&mul(109,151)],mul(676,79:;]}),mul(206,822)mul(228,261)-how()?]+mul(295,706)/]@( how()-mul(558,819)@::!>where()*when()?}mul(709,558)*)~;?}> how()from()mul(489,495)[*where():}(*%mul(189,692)how()/where()why()(mul(895,190))]<select();'who()when(309,317)mul(204,524)from(),&# mul(563,48)what()mul(207,241)&mul(450,18)when()what()select()^]{$why(565,783): mul(422,431){,}?+how()what()where()mul(782,229)[%}:~mul(994,946)){,$*,mul(84,333)#?@^]mul(324,259)<mul(723,626)*)/select()mul(22,373)from()mul(158,952) #mul(862,250)'$#;{mul(816,365)&$who(930,819) mul(440,442)^@@mul(35,883))>{+mul(904,446)~(?-*:select():]?mul(21,770){&?/what()mul(810,761)( <{#^why()select()mul(542,583)mul(517,719)*who()]mul(229,391)^:,;where()who()[&mul(181,416)>when()( %+{mul(376,885)+}/}*what()[%when()mul(412,213)who() mul(151,478)do()+when()mul(683,117)@how()[@>(*%mul(666,434)%+mul(83,30)^}:mul(983,213)@-what()mul(36,788)';%-#+]#mul(575,6)#when()'&@who()<$ who()mul(764,292)<,where()where()mul(230,519)<<^('mul(384,769)%,what()@who()when()where()when()mul(104,361)&select()what()-!mul(523,283)do()mul(920,551)mul(589,394)$(select()?#>&*'mul(672,365)+:]@$)mul(373,982)mul(810,292)-mul(990,386)?mul(372,766)where(),]^mul(651,898)from()from(){?;select()mul(293,197)why()( [;&^~@mul(505,310)what()what()select():]-what(873,670)mul(885,505);-#{';-how(967,119)select() mul(956,774)mul(51,516)mul(756,597)^~select()how()%&from()mul(463,747)&why()who()())mul(193,948)from()when()what()why()from():select()%select();mul(143,694)(mul(448,194)@<(-where(536,660)?select()mul(280,832)select()#^}mul(296,908)where()@{> #*do(); ;how()mul(417,4)mul(939,57)&'~?-'(#do())[where()+<<where()mul(223,643):%/mul(367,601)}*}[mul(451,653)why()<when()from();(#<;mul(960,745)>%:?(}mul(975,356):,select(275,833),#?(when()&]")

#    print(data)

    sum = add_multiplications(data)

    print("Total: " + str(sum))

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
