---
title: "Golle, P. Revisiting the Uniqueness of Simple Demographics in the US Population. WPES 2006"
type: fonte
formato: pdf
url: "https://crypto.stanford.edu/~pgolle/papers/census.pdf"
wayback: "https://web.archive.org/web/20261116055811/https://crypto.stanford.edu/~pgolle/papers/census.pdf"
acessado: 2026-11-19
conversor: pdftotext
---

> [!info] Cópia para leitura
> Original: <https://crypto.stanford.edu/~pgolle/papers/census.pdf>
> Wayback: <https://web.archive.org/web/20261116055811/https://crypto.stanford.edu/~pgolle/papers/census.pdf>
> Capturado em 2026-11-19 com `pdftotext`. Em caso de dúvida, vale o original.

Arquivo original: [[2006-golle-uniqueness-demographics.pdf]]

```text
Revisiting the Uniqueness of Simple Demographics
                          in the US Population

                                                                         Philippe Golle
                                                                 Palo Alto Research Center
                                                                      pgolle@parc.com


ABSTRACT                                                                             resides. Even at the county level, {gender, county, date of
According to a famous study [10] of the 1990 census data,                            birth} uniquely identifies 18% of the U.S. population. In
87% of the US population can be uniquely identified by gen-                          general [10] shows that “few characteristics are needed to
der, ZIP code and full date of birth. This short paper revisits                      uniquely identify a person.”
the uniqueness of simple demographics in the US population                              The results of this study are influential and widely cited.
based on the most recent census data (the 2000 census). We                           They informed the design of U.S. standards of privacy for
offer a detailed, comprehensive and up-to-date picture of                            health information [6, 12] and for the release of Census, re-
the threat to privacy posed by the disclosure of simple de-                          search and statistical information [3, 5]. They shed light on
mographic information. Our results generally agree with                              the surprising privacy behavior of individuals [2], and moti-
the findings of [10], although we find that disclosing one’s                         vated research in efficient algorithms to protect the anonymity
gender, ZIP code and full date of birth allows for unique                            of data [1, 7].
identification of fewer individuals (63% of the US popula-                              This paper updates, extends and in one instance finds a
tion) than reported in [10]. We hope that our study will                             discrepancy with the results of [10]. Specifically, we make
be a useful reference for privacy researchers who need sim-                          the following contributions:
ple estimates of the comparative threat of disclosing various
                                                                                        • We study the uniqueness of simple demograph-
demographic data.
                                                                                          ics using the most recent census data (the 2000
                                                                                          census [4]). Our results generally confirm the find-
Categories and Subject Descriptors                                                        ings of [10], although we find that disclosing one’s gen-
K.4.1 [Computers and Society]: Public Policy Issues—                                      der, ZIP code and date of birth allows for unique iden-
Privacy                                                                                   tification of fewer individuals than reported in [10].
                                                                                          We found that in 1990 (resp. 2000), only 61% (resp.
                                                                                          63%) of the US population was uniquely identifiable
General Terms                                                                             by {gender, ZIP code, full date of birth}, whereas [10]
Measurement                                                                               reported that the same attributes allowed for unique
                                                                                          identification of 87% of the US population in 1990.
                                                                                          Unfortunately, we can not explain this discrepancy be-
Keywords                                                                                  cause we lack detailed information about the data col-
Privacy, Anonymity, Census Data                                                           lection and analysis techniques of [10]. Our data col-
                                                                                          lection and methodology are explained in detail in the
1.     INTRODUCTION                                                                       following sections, so our results can be replicated and
   A famous study [10] of the 1990 census data showed that                                verified.
87% (216 million of 248 million) of the population in the
                                                                                        • We offer a fine-grained characterization of the
United States reported characteristics that likely made them
                                                                                          privacy threat of disclosing simple demograph-
unique based only on gender, 5-digit ZIP code and full date
                                                                                          ics. We define precisely the degree of privacy of in-
of birth (day, month and year). The study further reported
                                                                                          dividuals on a scale that goes from uniquely identi-
that 53% of the U.S. population is uniquely identified only
                                                                                          fiable to k-anonymous (i.e. hidden indistinguishably
by {gender, place, date of birth}, where “place” is basi-
                                                                                          in a group of size k). Compared to [10], this offers a
cally the city, town, or municipality in which the person
                                                                                          finer-grained view of the degree of privacy of individ-
                                                                                          uals who are not uniquely identifiable.

Permission to make digital or hard copies of all or part of this work for               • We study the privacy implications, by age, of
personal or classroom use is granted without fee provided that copies are                 releasing simple demographics. We show that the
not made or distributed for profit or commercial advantage and that copies                privacy threat is smallest for individuals around age
bear this notice and the full citation on the first page. To copy otherwise, to           20, then rises rapidly. This has important implications
republish, to post on servers or to redistribute to lists, requires prior specific        for the release of data about individuals in specific age
permission and/or a fee.                                                                  ranges. For example, much greater care must be taken
WPES’06, October 30, 2006, Alexandria, Virginia, USA.
Copyright 2006 ACM 1-59593-556-8/06/0010 ...$5.00.                                        with the medical data of elderly populations.
2.    DATA COLLECTION                                                                                   5-digit      County
                                                                                                       ZIP code
   The focus of this paper is on the threat to privacy of dis-
closing one’s gender, location (ZIP code or county) and age        Year of birth                         0.2%         0.0%
(either year of birth only, or year, month and day of birth).      Year and month of birth               4.2%         0.2%
These simple demographic characteristics were chosen be-           Year, month and day of birth         63.3%         14.8%
cause they appear to be the most valuable to marketers,
retailers and social and medical researchers. They are also
                                                                  Table 1: Fraction of the U.S. population uniquely
the most commonly disclosed demographic characteristics in
                                                                  identifiable by {gender, location, date of birth}.
registration forms, surveys and medical and financial files.
   To evaluate the privacy threat of disclosing these demo-
graphic characteristics, we need to estimate the number
of individuals of a given gender and age in a given loca-         birth (year, month and day). Our results are summarized
tion. The more individuals, the lesser the privacy threat.        in Table 1.
When a group of k individuals share the same gender, lo-             Our findings are close to [10] at the county level, but dif-
cation and age, each individual in the group is said to be        fer significantly at the level of ZIP codes. We show that in
k-anonymous [9, 11] after disclosing these characteristics.       2000, only 63% of the US population is uniquely identifi-
   Our source of demographic information is the 2000 Cen-         able by {gender, ZIP code, full date of birth}, whereas [10]
sus data, which is available free of charge on the Census         found 87% uniquely identifiable by the same characteristics
Bureau’s website [4]. We looked at table PCT12 (Sex by            in 1990. Unfortunately, we lack detailed information about
Age), which lists the number of males and the number of           the methodology and data collection of [10], so we can offer
females of a given age (from 0 to 99 years old) in a given        no definite explanation for this discrepancy. We speculate
geographic area. We retrieved this data for:                      however that the discrepancy might come in part from the
                                                                  fact that the 1990 census does not directly tabulate data
     • All 3, 219 counties and county equivalents (boroughs,
                                                                  by ZIP codes: Summary Tape File 1, which contains 100%
       census tracts, parishes, independent cities and Munici-
                                                                  of the 1990 census data, can not be queried by ZIP code.
       pios) in all 50 States, the District of Columbia and
                                                                  A smaller set of sample data from the 1990 census data,
       Puerto Rico.
                                                                  in Summary Tape File 3, can be queried by ZIP code, but
     • All 33, 233 ZIP Code Tabulation Areas (ZCTAs) in the       gives only a coarser representation of the age distribution of
       50 states, District of Columbia and Puerto Rico as of      individuals (ages are aggregated in 5 year intervals).
       Census 2000. The list of ZCTAs can be downloaded              The overall number of individuals uniquely identifiable by
       from [13].                                                 {gender, location, full date of birth}, while dramatic, says
                                                                  nothing about the degree of anonymity enjoyed by the rest
   This data is almost all we need, but not quite. To consider    of the population, nor about the effect of age on anonymity.
the privacy implications of revealing one’s full date of birth    For example, we want to know if the threat to privacy of dis-
(year, month and day), we must estimate the number of             closing demographic data is confined mostly to older people
individuals who live in a given location and were born on a       in thinly populated ZIP codes, or if the threat is uniformly
given day, month and year. Table PCT12 gives the year of          distributed across the population.
birth, but not the month or day (no other table in the census
data gives such detailed information, precisely because it is     Anonymity, by age, given {Gender, Location, Full
a threat to privacy). We can however compute a precise            date of birth}. Figures 1 and 2 provide a first answer to
estimate of the number of individuals born on a given day         this question. They give a more fine-grained view of the
and month of the year as follows.                                 degree of anonymity of the US population, by age, given
   We assume that births are uniformly distributed across         {gender, location, full date of birth}, where location is ei-
the days of the year. For our purpose, this is a reasonably       ther a 5-digit ZIP code (Figure 1) or a county (Figure 2).
close approximation ([8] shows that month-to-month varia-         These graphs show that the privacy threat of disclosing sim-
tions in birth rates are negligible and intra-week variations     ple demographics is fairly uniform between the ages of 0 and
are small). With this assumption, if n people are born in a       50, then rises rapidly after 50. The graphs also show that
given year, the expected number fk (n) of days on which k         even individuals who are not uniquely identifiable enjoy very
individuals are born is given by                                  little anonymity. For example, disclosing {gender, county,
                            !                                     full date of birth} leaves 14.8% of the population uniquely
                          n
               fk (n) =      (365)1−n (364)n−k .                  identifiable (1-anonymous) but also leaves 43.6% of the pop-
                          k                                       ulation 5-anonymous or less (i.e. hidden indistinguishably
                                                                  in a group of size 5 or less). The proportion of individuals
This formula is proved in the appendix. We now have all the
                                                                  who are 5-anonymous or less rises to 63% for people over
data needed to study the privacy threat of disclosing simple
                                                                  the age of 60 (see Figure 2).
demographics (one’s gender, location and age).
                                                                  Anonymity, by age, given {Gender, Location, Year
3.    RESULTS                                                     of birth}. We have shown that disclosing one’s full date
   Following [10], we compute first the percentage of the U.S.    of birth, together with location information, clearly compro-
population which is uniquely identifiable by {gender, loca-       mises privacy. In practice, however, surveys and registration
tion, date of birth}, where location is either a 5-digit ZIP      forms often ask only for an individual’s year of birth (or
code or a county, and date of birth is either the year of birth   equivalently, age) rather than the full date of birth. Even
only, or the year and month of birth, or the full date of         when the day and month of birth are asked, one can of-
                            100                                                                                                                    100

                             90                                                                                                                     90

                             80                                                                                                                     80




  Percentage of age group                                                                                                Percentage of age group
                             70                                                                                                                     70

                             60                                                                                                                     60
                                                                                            1-anonymous                                                                                                             1-anonymous
                             50                                                             2-anonymous or less                                     50                                                              5-anonymous or less
                                                                                            5-anonymous or less                                                                                                     10-anonymous or less
                             40                                                                                                                     40

                             30                                                                                                                     30

                             20                                                                                                                     20

                             10                                                                                                                     10
                              0                                                                                                                      0
                                  0   10   20    30    40    50    60   70   80   90 100                                                                 0    10   20    30    40    50   60   70   80   90 100
                                                       Age (years)                                                                                                            Age (years)


 Figure 1: Anonymity of the U.S. population, by age,                                                                  Figure 2: Anonymity of the U.S. population, by age,
 given {Gender, ZIP code, Full date of birth}.                                                                        given {Gender, County, Full date of birth}.

                            900                                                                                                                      100000

                            800

                                                                                                                                                         10000
                            700



                                                                                                                            k-anonymity
                            600
                                                                                                                                                          1000


  k-anonymity
                            500                                                                   90th percentile                                                                                                             90th percentile
                                                                                                  50th percentile                                                                                                             50th percentile


                                                                                                                         (Logarithmic scale)
                            400                                                                   10th percentile                                                                                                             10th percentile
                                                                                                                                                             100
                            300

                            200                                                                                                                               10

                            100

                              0                                                                                                                                1
                                  0   10    20    30        40    50    60   70   80   90   100                                                                    0    10    20    30    40   50   60   70   80   90   100

                                                            Age (years)                                                                                                                  Age (years)


 Figure 3: Anonymity of the U.S. population, by age,                                                                  Figure 4: Anonymity of the U.S. population, by age,
 given {Gender, ZIP code, Year of birth}.                                                                             given {Gender, County, Year of birth}.


ten lie without negative consequence (lying about one’s age                                                         (78705). All three ZIP codes are home to large universities.
is more problematic, since the lie is more easily detectable                                                           The conclusion we can draw from this data is that, for 90%
and may result in inadequate service). Table 1 shows that                                                           of the population under the age of 50, disclosing {gender,
revealing one’s {gender, location, year of birth} allows for                                                        ZIP code, year of birth} will result in 40-anonymity or more,
unique identification of only 0.2% of individuals. Is it then                                                       while disclosing {gender, county, year of birth} will result in
safe for most people to disclose this information? In what                                                          250-anonymity or better.
follows, we analyze in more detail the privacy implications                                                            Finally, those willing to sacrifice truthfulness for optimal
of disclosing one’s {gender, location, year of birth}.                                                              anonymity should claim, when asked for their age and ZIP
   Figures 3 and 4 show the degree of anonymity of the US                                                           code, to be a 21-year-old male from Camp Pendleton, Cal-
population, by age, given {gender, location, year of birth},                                                        ifornia (ZIP code 92054); or, if female, to be a 19-year-
where location is either a 5-digit ZIP code (Figure 3) or                                                           old from College Station, Texas (ZIP code 77840). They
a county (Figure 4). In both graphs, the green curve (the                                                           will share these characteristics with respectively 4, 099 other
middle curve) shows the median degree of anonymity by age                                                           males and 3, 744 other females.
(the degree of anonymity of the 50-th percentile). We see for
example that the median anonymity of the population under                                                           4.                        CONCLUSION
age 50 after disclosing {gender, ZIP code, year of birth} is                                                          This short paper revisits the uniqueness of simple demo-
200-anonymity (the median is 3000-anonymity if the county                                                           graphics in the US population based on the most recent
is disclosed instead of the ZIP code).                                                                              census data (the 2000 census). We offer a detailed, com-
   The blue line shows the anonymity of the lower 10-th per-                                                        prehensive and up-to-date picture of the threat to privacy
centile. In other words, 10% of the population enjoys less                                                          posed by the disclosure of simple demographic information.
anonymity than indicated by the blue line, and 90% of the                                                           We hope this study will be a useful reference for privacy
population enjoys more anonymity.                                                                                   researchers who need simple estimates of the comparative
   Finally, the red line shows the anonymity of the 90-th per-                                                      threat of disclosing various demographic data.
centile. We observe a sharp spike in the degree of anonymity
of the 90-th percentile (the 10% of the population who are
the most anonymous) around age 20. Analysis reveals that
                                                                                                                    5.                        REFERENCES
                                                                                                                     [1] G. Aggarwal, T. Feder, K. Kenthapadi, R. Motwani,
this spike comes from college and university towns with                                                                  R. Panigrahy, D. Thomas and A. Zhu. Approximation
high concentrations of individuals between the ages of 18                                                                Algorithms for k-Anonymity. Journal of Privacy
and 22. For example, the 3 ZIP codes with the highest de-                                                                Technology, 2005.
gree of anonymity in the range [18–22] are College Station,                                                          [2] A. Acquisti and J. Grossklags. Privacy and
TX (77840); West Lafayette, IN (47906); and Austin, TX                                                                   Rationality in Individual Decision Making. IEEE
     Security and Privacy, IEEE Computer Society, Vol. 3,     [13] 2000 Zip Code Tabulation Areas. http:
     No. 1, January/February 2005, pp. 26-33.                      //www.census.gov/tiger/tms/gazetteer/zcta5.txt
 [3] EPIC. The Census and Privacy.
     http://www.epic.org/privacy/census/                      APPENDIX
 [4] U.S. Census Bureau FactFinder.
     http://factfinder.census.gov                             A.    LEMMA
 [5] United States General Accounting Office. Record
     linkage and privacy. Issues in creating new federal        Lemma A.1. Assume that n individuals are distributed
     research and statistical information. GAO-01-126SP.      uniformly independently at random into N bins. Let fi (n)
 [6] L. Lamberg. Confidentiality and Privacy of Electronic    be the expected number of bins that contain i individuals.
     Medical Records. JAMA 2001, 285(24):3075-3076.           Then
                                                                                        !
 [7] K. LeFevre, D. DeWitt, and R. Ramakrishnan.                                      n
     Incognito: Efficient Full-Domain K-Anonymity. In                        fi (n) =    N 1−n (N − 1)n−i
                                                                                      i
     ACM SIGMOD International Conference on
     Management of Data, June 2005.                              Proof. The value fi (n) is determined for all i ≥ 0 and
 [8] National Center for Health Statistics. Births: Final     all n ≥ 0 by the following formulas
     Data for 2003. National Vital Statistics Reports
     Volume 54, Number 2. (116) pp. 2005-1120.                            f0 (0) =    N
     http://www.cdc.gov/nchs/                                         f0 (n + 1) =    f0 (n)(1 − 1/N )
 [9] P. Samarati. Protecting Respondents’ Identities in               fi (n + 1) =    fi (n)(1 − 1/N ) + fi−1 (n)/N
     Microdata Release. IEEE Trans. Knowl. Data Eng.
     13(6): 1010-1027 (2001)                                  Let us define gi (n) = fi (n)N i−1 (1−1/N )i−n . The equations
[10] L. Sweeney, Uniqueness of Simple Demographics in         above become:
     the U.S. Population, LIDAPWP4. Carnegie Mellon                              g0 (0) =    1
     University, Laboratory for International Data Privacy,
                                                                            g0 (n + 1) =     g0 (n)
     Pittsburgh, PA, 2000.
[11] L. Sweeney. K-anonymity: a Model for Protecting                          gi (n + 1) = gi (n) + gi−1 (n)
     Privacy. International Journal on Uncertainty,           Therefore gi (n) = ni and fi (n) = ni N 1−i (1 − 1/N )n−i =
                                                                                                  
     Fuzziness and Knowledge-based Systems, 10 (5), 2002;      n
                                                                 
                                                                   N 1−n (N − 1)n−i .
                                                               i
     557-570.
[12] L. Sweeney. Comments to the Department of Health
     and Human Services On “Standards of Privacy of
     Individually Identifiable Health Information”.
     http://privacy.cs.cmu.edu/dataprivacy/HIPAA/
     HIPAAcomments.html
```
