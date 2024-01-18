# Svarīgi!

### Programma nestrādā github, jo tiek izmantota selenium bibliotēka, lai atvērtu un nolasītu informāciju no inteneta vārdu definīciju bibliotēkām.
#

# Programmas apraksts
## 1. Mērķis un uzdevums
Studiju laikā salīdzinoši bieži ir ietecams vai nepieciešams izmantot dažādus papildus materiālus, kas galvenokārt ir angliski, taču ne allaž students zina visu terminu nozīmi, īpaši, ja jālasa tehniskie apraksti, it īpaši, ja tas ir zintnātnikie pētnieciskie darbs vai pat Bakalaura vai Maģistra vai Doktoranta grāda darbs.

Un šādos gadījumos vēl papildus jāmeklē, ko šie termini nozīmē, saprotams šis process parasa laiku, turklāt ļoti iespējams, ka ir vairāk par pāris no tiem, kas vēl jo vairāk norāda uz to, ka vajadzētu izmantot kodu, lai tos atrastu programma. Turklāt, izmantojot, programmu, tos nozīmes var arī momentā saglabāt un veidot terminu vārdnīcu.

Šie divi fakti noved pie programmas iezveidošans jēgas un uzdevuma - samazināt laiku, kas nepieciešams, lai atrastu dažādu jauni vai aizmirstu terminu nozīmi, turklāt saglabāt to "temporary" / "īslaicīgā" failā, jo nākošajā koda palaišanā vecās vērtības tiks izdzēstas. 

## 2. Izmantotās bibliotēkas

**1. selenium un selenium Webdriver** - bibliotēka, kas ļauj atvērt interneta resursus / mājaslapas

**2. from selenium.webdriver.common.keys import Keys**

**3. from openpyxl import Workbook, load_workbook** 

**4. time** - bibliotēka, kas atļauj veikt dažādas funkcijas, kas saistītas ar laiku, pimēram, noteik tā brīža laiku vai uzsākt atsakiti, vai uzņemt taimeri u.c. Kodā tiek izmantots, lai varētu ar funkciju ```time.sleep(2)``` varētu aizkavēt tālāk koda izpildi, lai atļautu mājaslapai atvērties

**5. sys** - bibliotēka, kuru izmantojot, litotājs spēj ar funkcijām ietekēt gan pašu python intepretāju vai arī apstrādāt mainīgos, kurus intepretājs izmanto vai "uztur". Projektā izmantotā ```sys.exit()``` funkcija aptur tālāka koda izpildi, līdz ar to apturot interpretāju, piemēram, ja kods palaist izmantojot IDLE, tad IDLE Shell.