  
# six_hun = ["600", "602", "604"]
# two_hun = ["200", "202", "204"]

# Upper hallway lists
sec200HO1 = ["207", "211", "213"]
sec200HE1 = ["200", "202", "204", "206"]
sec200HE2 = ["208", "210", "212"]
secEagleO = ["219", "221"]
secEagleE = ["218", "220", "215"]

sec300HO1 = ["309", "311", "313", "315"]
sec307 = ["307"]
sec300HO2 = ["301", "303", "305"]

sec400HO1 = ["401", "403", "405"]
sec400HO2 = ["407", "409", "411"]
sec400HE1 = ["400", "402"]
sec400HE2 = ["404", "406"]

sec500HO1 = ["501", "503", "505"]
sec500HO2 = ["509"]
sec500HE1 = ["500", "502", "504", "506"]
sec500HE2 = ["508", "510", "512", "514"]

sec600HO1 = ["601", "603", "605", "607"]
sec600HO2 = ["609", "611", "613"]
sec600HE1 = ["600", "602"]
sec600HE2 = ["604", "606"]

# Lower hallway lists

secL200HO1 = ["l205", "l207", "l209"]
secL200HE1 = ["l200", "l202", "l204", "l206"]
secL200HE2 = ["l208", "l210", "l212"]
secLEagleE = ["l216", "l218", "l220"]
secLEagleO = ["l213", "l217", "l218", "l219", "l220", "l221"]

secL400HO1 = ["l401", "l403", "l405"]
secL400HO2 = ["l407", "l409", "l411"]
secL400HE1 = ["l400", "l402", "l404"]
secL400HE2 = ["l406", "l408", "l410"]

secL500HO1 = ["l501", "l503", "l505"]
secL500HO2 = ["l509", "l511", "l513"]
secL500HE1 = ["l500", "l502", "l506"]
secL500HE2 = ["l510", "l512", "l514", "l516"]

secL600HO1 = ["l601", "l603", "l605"]
secL600HO2 = ["l609",]
secL600HE1 = ["l600", "l602"]
secL600HE2 = ["l604"]

# y = 1 and x = 0
secCafe = ["cafeteria", "cafe", "700", "lunch", "food", "lunchroom", "lunch room", "almuerzo", "el almuerzo", "comida"]
secCounseling = ["1101","counseling", "therapy", "counselor", "mental health", "mental health center", "counselor's office", "counseling office", "counselors office", "therapy office"]


# y = 1 and x = -1
secMainGym = ["1106","main gym", "maingym", "gimnasio", "gym"]
secAuxGym = ["1103","aux gym", "auxgym", "gimnasio auxiliar", "gimnasioauxiliar"]
secWeightRoom = ["weight room", "weightroom", "sala de pesas", "saladepesas", "913"]
secWrestling = ["wrestling", "wrestling room", "wrestlingroom", "lucha", "sala de lucha", "902"]

# y = 0 and x = 0          y needs to be zero so that it will go to the (1, 0) checkpoint
secMainEntrance = ["1105","main entrance", "entrance", "main doors", "mainentrance", "maindoors", "entrada principal", "entradaprincipal"]
secAuditorium = ["801", "auditorium", "paranifo", "el paranifo", "elparanifo", "801"]
secMediaCenter = ["media center", "mediacenter", "library", "100", "biblioteca"]
secMainOffice = ["1102","mainoffice", "main office", "oficina principal", "la oficina principal", "laoficinaprincipal", "oficinaprincipal"]
secClinic = ["1104", "clinic", "nurse", "nurses office", "nursesoffice", "clinic", "enfermeria"]


# y = 0 and x = -1
secBand = ["807", "band", "band room", "bandroom", "banda", "sala de banda", "saladebanda"]
secGuitar = ["805", "guitar", "guitar room", "guitarroom", "guitarra", "sala de guitarra", "saladeguitarra"]
secChorusOrchestra = ["803", "chorus", "chorus room", "chorusroom", "orchestra", "orchestra room" "orchestraroom", "strings", "coro", "sala de coro", "saladecoro", "orquesta", "sala de orquesta", "saladeorquesta", "803"]
secDrama = ["802", "drama", "theater", "theater room", "theaterroom", "teatro", "sala de teatro", "saladeteatro"]
secArt1 = ["804","art", "art room", "artroom", "arte", "sala de arte", "saladearte, photography", "fotografia", "photography class", "clase de fotografia", "photographyclass", "clasedefotografia"]
secArt2 = ["806", "ceramics", "ceramica", "ceramics class", "clase de ceraminca", "ceramicsclass", "clasedeceraminca"]



# For everything that does not have a defined value i.e. main office, room value is 1100
dictGuitar = {"805": secGuitar}
dictDrama = {"802": secDrama}
dictMainEntrance = {"1105": secMainEntrance}

dictAuditorium = {"801": secAuditorium}
dictMediaCenter = {"100": secMediaCenter}
dictMainOffice = {"1102": secMainOffice}
dictClinic = {"1104": secClinic}
dictBand = {"807": secBand}
dictChorusOrchestra = {"803": secChorusOrchestra}
dictArt = {"804": secArt1, "806": secArt2}
dictCafe = {"700": secCafe}
dictCounseling = {"1101": secCounseling}
dictMainGym = {"1106": secMainGym}
dictAuxGym = {"1103": secAuxGym}
dictWeightRoom = {"913": secWeightRoom}
dictWrestling = {"902": secWrestling}

dicts = [dictGuitar, dictDrama, dictMainEntrance, dictAuditorium, dictMediaCenter, dictMainOffice, dictClinic, dictBand, dictChorusOrchestra, dictArt, dictCafe, dictCounseling, dictMainGym, dictAuxGym, dictWeightRoom, dictWrestling]

hallways = [sec200HO1, sec200HE1, sec200HE2, secEagleO, secEagleE, sec300HO1, sec307, sec300HO2, sec400HO1, sec400HO2, sec400HE1, sec400HE2,sec500HE1, sec500HE2, sec500HO1, sec500HO2, sec600HE2, sec600HO1, sec600HO2, sec600HE1, sec600HE2, secCafe, secMainGym, secAuxGym, secWeightRoom, secWrestling, secMainEntrance, secMainOffice, secMediaCenter, secClinic, secBand, secGuitar, secChorusOrchestra, secDrama, secArt1, secArt2, secCounseling, secL200HE1, secL200HO1, secL200HE2, secLEagleE, secLEagleO, secL400HO1, secL400HO2, secL400HE1, secL400HE2, secL500HO1, secL500HO2, secL500HE1, secL500HE2, secL600HO1, secL600HO2, secL600HE1, secL600HE2]