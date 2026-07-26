---
title: Störande bakgrundsljus och provtagningsbetingelser
---

# Störande bakgrundsljus och provtagningsbetingelser

Den här sidan förklarar hur vi definierar och beräknar när bakgrundsljuset under natten blir så pass störande att ljusbaserade nattfjärilsfällor inte längre fungerar tillfredsställande — och när provtagningen kan återupptas. Den vänder sig till dig som vill förstå bakgrunden; det räcker att följa tabellen på [gradientsidan](gradient-lund-abisko.md) om du bara behöver veta vilka perioder som gäller för din lokal.

## Problemet: bakgrundsljus varierar med breddgrad och årstid

Ljusfällor för nattfjärilar bygger på att fällans UV-ljus sticker ut mot en mörk bakgrund. Ju ljusare natten är, desto svagare kontrast och desto sämre fångstefektivitet. Detta är inte ett problem i södra Sverige, där sommarnätterna ändå är tillräckligt mörka, men längs en gradient upp till Abisko blir effekten påtaglig: vid tillräckligt höga breddgrader försvinner den astronomiska skymningen helt under en period runt midsommar.

För att kunna jämföra fångster rättvist längs gradienten — och inför framtida nationell övervakning — behöver vi en standardiserad och principiellt förankrad definition av när bakgrundsljuset anses störande. Det är den definitionen som redovisas här.

## Solhöjden vid astronomisk midnatt

Bakgrundsljusets intensitet under natten beror på solens position under horisonten. Det relevanta måttet är **solhöjden vid astronomisk midnatt** — den tidpunkt på dygnet då solen befinner sig som lägst.

Solens deklination (δ), det vill säga hur långt solen befinner sig norr eller söder om ekvatorplanet, varierar sinusformigt under året:

> δ = −23,44° × cos(2π(N + 10) / 365)

där N är årets dag (1 = 1 januari). Maximum +23,44° nås vid midsommar, minimum −23,44° vid midvinter.

Solhöjden vid astronomisk midnatt för en given breddgrad (φ) ges av:

> h = δ + φ − 90°

Negativa värden innebär att solen befinner sig under horisonten. Ju mer negativt h är, desto mörkare är natten och desto bättre betingelser för ljusfällor.

## Tröskelvärdet: vad är störande bakgrundsljus?

Var gränsen går för när bakgrundsljuset blir störande kan inte avgöras rent astronomiskt — det beror på hur nattfjärilar faktiskt reagerar på ljusförhållandena. Vi har i stället kalibrerat tröskeln mot fältobservationer.

En av projektets deltagare genomförde ljusfångst vid **Norrfjärden (65,42°N)** under ett antal säsonger. Erfarenheten var att fällorna gav meningsfulla resultat till och med den **31 maj**, men att bakgrundsljuset under natten runt midsommar var för störande för tillfredsställande fångst. Det datum då provtagningen bedömdes kunna **återupptas** var **1 augusti**.

Den 31 maj ger vid Norrfjärdens breddgrad ett beräknat h-värde på **−2,73°**, vilket används som projektets tröskel för störande bakgrundsljus. Provtagning rekommenderas när h ≤ −2,73°; är h högre än så anses bakgrundsljuset vara för störande för jämförbara resultat.

## Diagram

Figuren nedan visar solhöjden vid astronomisk midnatt för ett urval av projektets lokaler under april–september 2026. Perioder då kurvan överstiger tröskeln (orange prickad linje) är perioder med störande bakgrundsljus.

![Solhöjd vid astronomisk midnatt för gradientlokaler](../assets/images/ljusberakningar_diagram.jpg)

Lokaler söder om ungefär 65°N — från Revinge till Umeå — håller sig under tröskeln under hela säsongen. För de fem nordligaste lokalerna överstigs tröskeln under en period runt midsommar.

## Perioder med störande bakgrundsljus

Tabellen nedan visar de beräknade perioderna med störande bakgrundsljus för projektets nordligaste lokaler, baserat på tröskeln h = −2,73°.

| Lokal | Bakgrundsljuset stör från | Provtagning kan återupptas | Antal dagar |
|---|---|---|---|
| Marsfjäll (9) | 3 juni | 11 juli | 38 dagar |
| Norrfjärden (10a) | 1 juni | 13 juli | 42 dagar |
| Luleå (10b) | 30 maj | 15 juli | 46 dagar |
| Överkalix (11) | 26 maj | 19 juli | 54 dagar |
| Abisko (12) | 16 maj | 29 juli | 74 dagar |

Lokaler 1–8 (Revinge–Umeå) har inga perioder med störande bakgrundsljus och kan provtas hela säsongen.

## Osäkerhet och begränsningar

**Asymmetri i kalibreringen.** Fältobservationerna antyder att provtagningen slutade fungera runt 31 maj och kunde återupptas runt 1 augusti. De två datumen ger inte exakt samma tröskelvärde — 31 maj ger h = −2,73°, medan 1 augusti ger ett något lägre värde (~−6,7°). Skillnaden beror sannolikt på att fällorna inte testades aktivt i perioden närmast midsommar. Det konservativare värdet (31 maj) används, vilket ger kortare perioder med störande bakgrundsljus snarare än längre.

**Lokala variationer.** Molntäcke, topografi och lokal ljusföroreningar kan påverka gränsen i båda riktningarna. Beräkningarna avser astronomiska förhållanden, inte faktiska väderbetingelser.

**Tidiga provtagningsförsök välkomnas.** Observationer från nordliga lokaler nära periodernas gränsdatum är värdefulla och bidrar till att kalibrera tröskeln inför framtida säsonger.

## Externa resurser

- [SMHI:s Soluret](https://www.smhi.se/kunskapsbanken/meteorologi/sol-och-mane/soluret-1.3798) — information om soluppgång och solnedgång i Sverige
- [timeanddate.com](https://www.timeanddate.com/sun/sweden/) — interaktiv solkalkylator med exakta tider för valfri plats och datum
- [Lunds observatorium](https://www.astro.lu.se/) — astronomisk referensdata

---

*Beräkningarna på den här sidan kan reproduceras med den sinusoidala soldeklarationsmodellen ovan. För högre precision kan paket som [PyEphem](https://rhodesmill.org/pyephem/) (Python) användas, vilket beräknar solens position mer exakt och tar hänsyn till hur atmosfären böjer ljuset nära horisonten.*
