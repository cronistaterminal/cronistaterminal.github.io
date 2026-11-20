---
title: "Ware (ed.). Security Controls for Computer Systems (Ware Report), RAND R-609, 1970"
type: fonte
formato: pdf
url: "https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf"
wayback: "https://web.archive.org/web/20261014064846/https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf"
acessado: 2026-11-19
conversor: pdftotext
---

> [!info] Cópia para leitura
> Original: <https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf>
> Wayback: <https://web.archive.org/web/20261014064846/https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf>
> Capturado em 2026-11-19 com `pdftotext`. Em caso de dúvida, vale o original.

Arquivo original: [[1970-ware-security-controls.pdf]]

```text
\;.;-~-~1-UI:~--liA~-~-~{~-~-~;·7)~1·
                                      '             '\!'       \
                                                               \




                                               2   :r-r



SECURITY CONTROLS FOR
 COMPUTER SYSTEMS (U)
  Report of Defense Science Board
  Task Force on Computer Security




                 11 FEBRUARY 1970
                        ·,




      Published by The Rand Corporation for the
 OFFICE OF THE DIRECTOR OF DEFENSE RESEARCH
     AND EN~INEERING, WAS[JINGTON, D. C.
            ~-;
           ~~~                   ...      ;/               ­
Although this report contains no information not available in a well stocked
technical library or not known to computer experts, and although there is little
or nothing in it directly attributable to classified sources, the partiCipation of
representatives from government agencies in its preparation makes the informa­
tion assume an official character. It will tend to be viewed as an authoritative
Department of Defense product, and suggestive of the policies and guidelines
that will eventually have to be established. As a prudent step to control dissemi­
nation, it is classified CONFIDENTIAL overall.
         '-'
           ~ :-..- ..i "




                               ;   ,'




SECURITY CONTRO'LS FOR
 COMPUT.ER SYSTEMS (U)
  Report of Defense Science Board
  Task Force on Computer Security




                            11 FEBRUARY 1970




         Published byThe Rand Corporation for the
  OFFICE OF THE DIRECTOR OF DEFENSE RESEARCH
      AND ENGINEERING, WASHINGTON, D. C.




                                                       }
                           <(.:C)~IriBEts.:l+lts:l   /'/
Published by The RAND Corporation
OFFICE OF THE DIRECTOR OF DEFENSE RESEARCH AND ENGINEERING
                                WASHINGTON, 0. C. 20301




                                                                     11 Febru·ary 1970




MEMORANDUM FOR CHAIRMAN, DEFENSE SCIENCE BOARD



SUBJECT:    Final Report of Task Force on Computer System Security




The Task Force on Computer Security herewith transmits the final report on its study:
Security Controls for Computer Systems. We visualize that this document will have wide
interest and application; therefore, it contains an informative discussion of the problem
as well as guidelines for implementing solutions.

It should be noted that this is the first attempt to codify the principles and details of
a very involved technical-administrative problem. Thus, this report reflects the best
ideas of individuals knowledgeable about a problem which is relatively new, has been
solved only a few times, and has never been solved with the generality and breadth of
scope attempted in this report. There is no significant difference of opinion within the
Task Force on the general content of this document. However, some aspects of the
problem are so new and controversial that there is a residual difference of opinion on
a few fine details.

Our recommendations and guidelines address the most difficult security control situa­
tion-a time-sharing multi-access computer system serving geographically distributed
users, and processing the most sensitive information. This report is a compilation of
those aspects which should be considered separately and in combination when design­
ing or adapting computer systems to provide security control or user privacy. It is
impossible to address the multitude of details that will arise in the design or operation
of a particular resource-sharing computer system in an individual installation.

Thus, the security problem of specific computer systems must, at this point in time,
be solved on a case-by-case basis, employing the best judgment of a team consisting
of system programmers, technical hardware and communication specialists, and
security experts.

This report provides guidance to those responsible for designing and certifying that a
given system has satisfactory security controls and procedures.



                                       v

                         rfll\.ICIIlCl\.ITI A I
                             -- •    , .......... . _ , . , I II \L




In its study, the Task Force reached certain conclusions.

      1:~ · Providing satisfactory security controls in a computer system is
           in itself a system design problem. A combination of hardware,
           software, communication, physical, personnel, and administra­
           tive-procedural safeguards is required for comprehensive
           security. In particular, software safeguards alone are not suffi­
           cient.

     2.    Contemporary technology can provide a secure system accepta­
           bly resistant to external attack, accidental disclosures, internal
           subversion, and denial of use to legitimate users for a closed
           environment(cleared users working with classified information at
           physically protected consoles connected to the system by pro­
           tected communication circuits).

      3.   Contemporary technology cannot provide a secure system in an
           open environment, which includes uncleared users working at
           physically unprotected consoles connected to the system by un­
           protected communications.

      4.   It is unwise to incorporate classified or sensitive information in
           a system functioning in an open environment unless a significant
           risk of accidental disclosure can be accepted.

      5.   Acceptable procedures and safeguards exist and can be imple­
           mented so that a system can function alternately in a closed
           environment and in an open environment.

      6.   Designers of secure systems are still on the steep part of the
           learning curve and much insight and operational experience with
           such systems is needed.

      7.   Substantial improvement (e.g., cost, performance) in security­
           controlling systems can be expected if certain research areas can
           be successfully pursued.

This report contains a series of recommendations of use to designers, implementers,
certifiers, and operators of secure systems. There is, however, a second and independ­
ent set of recommendations which are directed to the Defense Science Board. They are
contained only in this memorandum and are as follows.

There is an immediate action item.

                The security policy directives presently in effect pro­
                hibit the operation of resource-sharing computer sys­
                tems. This policy must be modified to permit contrac­
                tors and military centers to acquire and operate such
                systems. This first step is essential in order that ex­
                perience and insight with such systems be . ac­
                cumulated, and in order that technical solutions be
                tried.

Interim standards and regulations must be drafted to serve as design and operational
guidelines for the early resource-sharing security-controlling systems. Technical exper­
tise is required in the preparation of these documents and must be provided to the
Directorate of Security Policy at least initially, and perhaps also on a continuing basis
to furnish both technical-assistance to operational systems and technical judgment for
interpretation of policy. There are several sources of concepts and specific recommen­


                                              vi
dations for inclusion in interim regulations. They include this report, the documents of
the DIA/ ANSR system, the JCCRG Collocation Study, and the documents of the NSA
et ai/COINS system.

There is also a near-term action item.

                 A technical agent must be identified to establish
                 procedures and techniques for certifying security-con­
                 trolling systems, especially the computer software por­
                 tions and for actually certifying such systems.

The need for this agent is immediate, but it will be difficult to create on short notice.
System certification is a new technical area, and substantial technical expertise in
several disciplines is required. Two models come to mind for such an agent. The
responsibility could be assigned to an existing agency of government if it has the
requisite skills, e.g., NSA, DIA, JTSA. Alternatively, an attractive idea is a multi-service
agency, operated and staffed by a contractor, and created in the image of the Electro­
magnetic Compatibility Analysis Center.

It is important to influence designers of future computers and software so that security
controls can be installed before the fact and as an integral part of the system. It is also
important to ascertain what can be done with equipment presently installed or owned
by the government. Thus, a program of studies and research is required. This need
should be made known to various agencies of the Department of Defense that support
studies and research in computers; some aspects of the program are appropriate for
ARPA. Typical topics are those which

           Facilitate progress toward handling the open environment:

                       A program of research to develop encryp­
                       tion devices to function internally within the
                       computer proper.

                       A program of research to investigate spe­
                       cial hardware configurations that can pro­
                       vide satisfactory security controls in an
                       open environment.

           Improve the understanding of. failure risks:

                       A program of research to study the proc­
                       ess of certification, and to develop me­
                     . thodology for automatic recertification.

           Improve the efficiency of security controlling systems:

                       A program of research to establish new
                       computer architectures which can imple­
                       ment security control more efficiently and
                       less expensively.

                     · A program of research to study failure
                       modes in computer systems and to formu­
                       late methodology for accurately predicting
                       failure probabilities.

           Solve a latent and not fully understood leakage point:

                      Continued research in methods for ade­
                      quately erasing information stored on mag­
                      netic media, i.e., sanitization or degaussing.


                                             Vll


                                rry;,.. l£:11""\l:t...I'TI A I
Finally, it is suggested that the Task Force be maintained intact formally to provide
technical advice as required to the Directorate of Security Policy and the Technical
Agent, and to designers, certifiers, and operators of secure systems.

The issue of providing security controls in computer systems will transcend the Depart­
ment of Defense. Furthermore, the computing industry will eventually have to supply
computers and systems with appropriate safeguards. Thus, the content of this report
is of interest to, and should be circulated to other government agencies, industry,
research groups, and defense contractors.

A number of working papers have been produced during this study. The Chairman will
maintain for five years a complete file of such documents, all relevant correspondence
and minutes, comments on draft reports, etc. At the end of th<,~t time, the material will
be microfilmed and deposited with an agency specified by the Defense Science Board.

The Task Force and its members are available to assist in the implementing of any of
these recommendations, and to assist with policy and technical issues which may arise
in connection with formulation of policy and regulations for security controls in comput­
ers.




                                                  Willis H. Ware
                                                  Chairman, Task Force
                                                  on Computer System Security




                                           viii

                               rf\1'1.. ll:lr'\1:11..111 A I
                                          CONTENTS

Memorandum for the Secretary of Defense ................................ iii

Memorandum for Chairman, Defense Science Board . . . . . . . . . . . . . . . . . . . . . . . . v

Preface ................................................................. xi

Introduction     •.•••.••••••••••••••••••.••••••••••••••••••••.•••••••••••••• XV



    Part A.     NATURE OF THE PROBLEM ............................... 1
          I.    The Security Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
         II.    Types of Computer Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
        III.    Threats to System Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
        IV.     Areas of Security Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
          v.    System Characteristics ....... , .............................. 10
         VI.    Definitions ................................................. 12

    Part B.     POLICY CONSIDERATIONS AND RECOMMENDATIONS .... 14
          I.    Fundamental Principles ..................................... 14
         II.    System Personnel .......................................... 14
        III.    Information Structure and Transforms ....................... 17
        IV.     System Transaction Accounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
          v.    Reliability and Auto-Testing ................................. 19
        VI.     Information Security Labels ................................. 21
        VII.    Management of Storage Resources ........................... 21
       VIII.    System Certification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

    Part C.     TECHNICAL RECOMMENDATIONS ........................ 26
          I.    Introduction ............................................... 26
         II.    Central Processor Hardware ................................. 27
        III.    Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
        IV.     Access Control Throughout the System ....................... 31
          v.    Communication Lines ....................................... 38
        VI.     Terminals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
        VII.    Certification .......... : . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
       VIII.    Open Environment Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
         IX.    Research Needed . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
          X.    Overall System Problems . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

                                                         ix

                                         rtll\.ll=lnJ:I\.ITI A I
                           LVI'IriUCI'\j IIAL




  Part D.   MANAGEMENT AND ADMINISTRATIVE CONTROL ........ 46

Appendix:   AUTOMATION OF A MULTILEVEL SECURITY SYSTEM .... 48
            Introduction ............................................... 48
            Computer System Catalogs .................................. 50
            Security Control System Generation ......................... 50
            Security Structure Definition ................................ 51
            Personnel Security Definition and User Clearance
               Update .................................................. 54
            Authorization Group Definition .............................. 55
            Universal Privileges ........................................ 55
            Terminal Security Definition and Update ..................... 56
            File Access Processing ...................................... 56
            Annex A: Formal System Access Specification ................ 58
            Annex B: Security Component Definition Examples ........... 62




                                      X
                               PREFACE

     The question of security control in resource-sharing systems was brought
into focus for the Department ofDefense by aseries of events in the spring and
summer of 1967. Such systems were being procured in increasing numbers for
government installations; the problems of security for them were becoming of
pressing concern both to defense contractors and to military operations; the
Research Security Administrators had forwarded a position paper through the
Defense Supply Agency to the Director for Security Policy in the Office of
Assistant Secretary of Defense (Administration) soliciting action. Since the
matter involved technical issues, the paper was referred to the Office of the
Director of Defense Research and Engineering for consideration.
     In June 1967, the Deputy Director (Administration, Evaluation and Man­
agement) requested the Director of the Advanced Research Projects Agency
(ARPA) to form a Task Force to study and recommend hardware and software
safeguards that would satisfactorily protect classified information in multi­
access, resource-sharing computer systems. Within ARPA, the responsibility
for this task was forwarded to Mr. Robert W. Taylor, Director of the Office of
Information Processing Techniques.
    A series of discussions was held during the summer and fall months of
1967 with people from the university and industrial communities, culminating
in the formation by October 1967 ofa Task Force consisting ofa Steering Group
and two Panels. The organizatiop.al meeting was held the following month, and
thereafter the Panels and the Steering Group met on a regular basis to formu­
late the recommendations that constitute the body of this Report.
    The Task Force has operated formally under the authority of the Defense
Science Board. Following are the members of the Steering Group:

   Willis H. Ware, Chairman, The Rand Corporation, Santa Monica, Calif
   J. Patrick Hav~rty, Deputy Chairman, The R~nd Corporation, Santa
       Monica, Calif
   Robert A. Mosier, Vice Chairman, System Development Corporation, Santa
       Monica, Calif
   Arthur A. Bushkin, Secretary, Lockheed Missiles and Space Co., Palo Alto,
       Calif (formerly, Massachusetts Institute of Technology and Bolt, Bera­
       nek and Newman)
   Elliot Cassidy, Directorate for Security Policy, Department of Defense,
        Washington, D.C.
   John F. Egan, Office of the Secretary of Defense/DDR&E, Department of
       Defense, Washington, D.C.
   Edward L. Glaser, Case Western Reserve University, Cleveland, Ohio

                                      Xl
   John W. Kuipers, Central Intelligence Agency, Washington, D.C.
   Jerome D. Moskowitz, National Security Agency, Fort George G. Meade,
       Maryland
   Lawrence G. Roberts (formerly, Robert W. Taylor), Advanced Research
       Projects Agency, Department of Defense, Washington, D.C.
   Robert von Buelow, System Development Corporation, Santa Monica,
       Calif.

   The two panels organized under the Steering Group are the Policy Panel
and the Technical Panel. The following are members of the Policy Panel:

   Jerome D. Moskowitz, Chairman, National Security Agency, Fort George G.
       Meade, Maryland
   Donal Burns, Central Intelligence Agency, Washington, D.C.
   Thomas Chittenden, National Security Agency, Fort George G. Meade,
       Maryland
   Richard G. Cleaveland, Defense Communication Agency, Washington, D.C.
   Roy McCabe, System Development Corporation, Sacramento, Calif.
   Barry Wessler, Advanced Research Projects Agency, Department of De­
       fense, Washington, D.C.
   Ronald Wigington, Chemical Abstracts Service, Columbus, Ohio
   Edward L. Glaser (ex officio), Case Western Reserve University, Cleveland,
       Ohio
   Willis H. Ware (ex officio), The Rand Corporation, Santa Monica, Calif.

   The Technical Panel consists of the following:

   Edward L. Glaser, Chairman, Case Western Reserve University, Cleveland,
       Ohio
   Arthur A. Bushkin, Secretary, Lockheed Missiles and Space, Co., Palo
       Alto, Calif.
   James P. Anderson, James P. Anderson and Co., Fort Washington, Pa.
   Edward H. Bensley, The MITRE Corporation, Bedford, Mass.
   Charles R. Blair, International Business Machines Corp., Yorktown, N.Y.
   Daniel L. Edwards, National Security Agency, Washington, D.C.
   Harold M. Jayne, Executive Office of The President, Washington, D.C.
   Lawrence G. Roberts, Advanced Research Projects Agency, Department of
       Defense, Washington, D. C.
   Jerome H. Saltzer, Massachusetts Institute of Technology, Cambridge,
       Mass.
   Jerome D. Moskowitz (ex officio), National Security Agency, Fort George G.
       Meade, Maryland
   Willis H. Ware (ex officio), The Rand Corporation, Santa Monica, Calif.

    Initially, the representative of the Directorate for Security Policy was
Lieutenant Commander Armen Chertavian (USN); and the representative to
the Policy Panel from the Central Intelligence Agency, was Mr. Fred Ohm.




                                    xii
AUTHORSHIP
     The members ofthe Task Force participated as individuals knowledgeable
of the technical, policy, and administrative issues involved. Thus, the views
stated herein do not reflect the policy of the Federal Government, any of its
agencies, or any university or industrial corporation.
     Ultimately, a Report has to be written by one person. The original draft
was written by Willis H. Ware using sources as noted below. It was then
critiqued, modified, emended, and shaped by the members of the Steering
Group and the Panels. A second complete draft was written by Thomas Chit­
tenden, and the final version by Willis H. Ware.
     Each Panel produced a series of papers which formed the basis for the
recommendations on software, hardware, procedures, and policy. The Intro­
duction and portions of Part A were initially authored by Wade B. Holland,
utilizing material provided by Willis H. Ware and other sources. Section V of
Part A, on System Characteristics, is largely from Willis H. Ware, incorporat­
ing material from a paper by the Technical Panel and some information from
personal letters of Prof. E. L. Glaser.
     Part B, the Policy Considerations and Recommendations, is substantially
from the final paper produced by the Policy Panel. Many of the explanatory
comments come from the original paper, although some were added in the final
writing. The Technical Recommendations, Part C, mainly reflect the content
of two papers produced by the Technical Panel, modified to a minor extent by
information from personal letters of Prof. Glaser. Finally, Part D, on Manage­
ment and Administrative Control, was written by Willis H. Ware, and utilizes
ideas from "Security of Classified Information in the Defense Intelligence
Agency's Analyst Support and Research System" (February 1969, C-3663/MS­
5), and from "Security Procedures for the RYE System" (W. B. Ellis, December
1968).                          .
     The Appendix was first drafted by Arthur A. Bushkin and Willis H. Ware;
it was subsequently extended and rewritten by Mr. Bushkin and Robert M.
Balzer.
     The final editing and details of format and style are due to Wade B. Hol­
land. The Report was printed and published by The Rand Corporation, under
ARPA sponsorship.



ACKNOWLEDGMENTS
    The success ofa venture such as this depends upon the personal dedication
and volunteer participation ofthe individuals involved. In addition to the listed
members ofthe Steering Group and the Panels, it is also a pleasure to acknowl­
edge the contributions of Dr. Robert M. Balzer and Mr. Wade B. Holland, The
Rand Corporation, Santa Monica, California; Miss Hilda Faust, National
Security Agency, Fort George G. Meade, Maryland; and Mr. Clark Weissman,
System Development Corporation, Santa Monica, California. A special ac­
knowledgment is due Thomas Chittenden, National Security Agency, Fort
George G. Meade, Maryland, who rewrote the entire document to produce the
all-important second draft.

                                      xiii
    The subject ofsecurity control in multi-access computer systems is ofsuffi­
ciently wide interest that many members ofthe Steering Group and the Panels
contacted a number of individuals, organizations, and agencies in the course
of this effort. It would be impossible to mention every person with whom we
have talked and who in some way has influenced our final recommendations.
Among others, however, we interacted with Colonel Roy Morgan ofthe Defense
Intelligence Agency representing the ANSR computing system, and Mr.
George Hicken, National Security Agency, representing the RYE and COINS
systems. The Steering Group and its Panels also acknowledge the contributions
of the many individuals who read our draft material and supplied valuable
comments and suggestions.

                                                              Willis H Ware
                                                              January 1, 1970




                                      XIV
                             INTRODUCTION


    With the advent of resource-sharing computer systems that distribute the
capabilities and components ofthe machine configuration among several users
or several tasks, a new dimension has been added to the problem of safeguard­
ing computer-resident classified information. The basic problems associated
with machine processing of classified information are not new. They have been
encountered in the batch-processing mode of operation and, more recently, in
the use of remote job-entry systems; the methods used to safeguard information
in these systems have, for the most part, been extensions of the traditional
manual means of handling classified documents.
    The increasingly widespread use of resource-sharing systems has intro­
duced new complexities to the problem. Moreover, the use of such systems has
focused attention on the broader issue of using computers, regardless of the
configuration, to store and process classified information.
    Resource-sharing systems are those that distribute the resources of a com­
puter system (e.g., memory space, arithmetic units, peripheral equipment,
channels) among a number of simultaneous users. The term includes systems
commonly called time-sharing, multiprogrammed, remote batch, on-line, multi­
access, and, where two or more processors share all of the primary memory,
 multiprocessing. The principle distinction among the systems is whether a user
must be present (at a terminal, for example) to interact with his job (time­
sharing, on-line, multi-access), or whether the jobs execute autonomously (mul­
tiprogrammed, remote batch). Resource-sharing allows many people to use the
same complex of computer equipment concurrently. The users are generally,
although not necessarily, geographically separated from the central processing
equipment and interact with the machine via remote terminals or consoles.
Each user's program is executed in some order and for some period oftime, not
necessarily to completion. The central processing equipment devotes its re­
sources to servicing users in turn, resuming with each where it left off in the
previous processing cycle. Due to the speeds of modern computers, the in­
dividual user is rarely aware that he is receiving only a fraction ofthe system's
attention or that his job is being fragmented into pieces for processing.
    Multiprogramming is a technique by which resource-sharing is accom­
plished. Several jobs are simultaneously resident in the system, each being
handled by the various system components so as to maximize efficient utiliza­
tion ofthe entire configuration. The operating system 1 switches control from
one job to another in such a way that advantage is taken ofthe machine's most

     'The system software, which schedules work through the computer system, assigns resources
to each job, accounts for resources used, etc.


                                             XV
                                                     Part A
                               NATURE OF THE PROBLEM


 I. THE SECURITY PROBLEM                                       to users who wish to preserve the integrity of their
                                                               data and their programs. Thus, designers and manu­
     The wide use of computers in military and de­             facturers of resource-sharing systems are concerned
  fense installations has long necessitated the applica­       with the fundamental problem of protecting infor­
  tion ofsecurity rules and regulations. A basic princi­       mation. In protecting classified information, there
  ple underlying the security of computer systems has          are differences of degree, and there are new surface
  traditionally been that of isolation-simply remov­           problems, but the basic issues are generally equiva­
  ing the entire system to a physical environment in           lent. The solutions the manufacturer designs into
  which penetrability is acceptably minimized. The in­         the hardware and software must be augmented and
  creasing use of systems in which some equipment              refined to provide the additional level of protection
  components, such as user access terminals, are               demanded of machines functioning in a security en­
  widely spread geographically has introduced new              vironment.
  complexities and issues. These problems are not                 The recommendations of the Defense Science
  amenable to solution through the elementary safe­            Board's Task Force on Computer Security represent
  guard of physical isolation.                                 a compilation of techniques and procedures which
     In one sense, the expanded problems of security           should be considered both separately and in combi­
  provoked by resource-sharing systems might be                nation when designing or adopting data processing
  viewed as the price one pays for the advantages              systems to provide security or user privacy. The solu­
  these systems have to offer. However, viewing the            tions to specific problems are intended to be flexible
  question from the aspect ofsuch a simplistic tradeoff        and adaptive to the needs of any installation, rather
  obscures more fundamental issues. First, the                 than being oriented to any one applications environ­
  security problem is not unique to any one type of            ment. It is intended that the general guidelines in
  computer system or configuration; it applies across          this Report be of use to DOD components, other gov­
  the spectrum of computational technology. While              ernment installations, and contractors.
  the present paper frames the discussions in terms of
  time-sharing or multiprogramming, we are really
  dealing not with system configurations, but with
  security; today's computational technology has               II. TYPES OF COMPUTER SYSTEMS
  served as catalyst for focusing attention on the prob­
  lem of protecting classified information resident in            There are several ways in which a computer sys­
  computer systems.                                            tem can be physically and operationally organized to
     Secondly, resource-sharing systems, where the             serve its users. The security controls will depend on
  problems of security are admittedly most acute at            the configuration and the sensitivity of data proc­
. present, must be designed to protect each user from          essed in the system. The following discussion pre­
  interference by another user or by the system itself,        sents two ways of viewing the physical and opera­
  and must provide some sort of "privacy" protection           tional configurations.

                                                           1
                                --•      ,.    •--·,         I   II   t.L.




Local-Access   Remote-Access          Local-Access                      Remote-Access        Remote-Access
     ....
     ...           ...                        .....
                                              ...                            .....
                                                                              ...                 ....
                                                                                                  ...
   Batch           ""
                  Batch             Multiprogramming                  Multiprogramming        Time-Shared



                                                                        Difficulty and
                                                                       Complexity of
                                                                      Security Controls




                                         Figure 1




                                                                  Type Ill

                                                           PROGRAMMING VIA
   Type I                 Type II                         LIMITED LANGUAGES                     Type IV
                                                                  AND
    FILE           PROGRAMMING VIA                           CHECKED-OUT                   FULL PROGRAMMING
   QUERY            INTERPRETATION                             COMPILERS                       CAPABILITY


     •
  Limited
 Application
                            •                                           • Increasing
                                                                                                  •
                                                                                             New Languages
                                                                                             New Compilers
 Programs·
                                                                       User Capability,
                                                                        Difficulty, and           ...
                                                                        Complexity of
                                                                       Security Controls



                                         Figure 2




                                                      2
organization of the protection system (e.g., in access        files or the system. 1
control, in user identification and authentication,               Active Infiltration. One method of accomplish­
etc.). How serious any one of these might be depends          ing active infiltration is for a legitimate user to pene­
on the sensitivity (classification) of the information        trate portions of the system for which he has no
being handled, the class of users, the computational          authorization. The design problem is one of prevent­
capabilities available to the user, the operating envi­       ing access to files by someone who is aware of the
ronment, the skill with which the system has been             access control mechanisms and who has the knowl­
designed, and the capabilities of potential attackers         edge and desire to manipulate them to his own ad­
of the system.                                                vantage. For example, if the access control codes are
   These points ofvulnerability are applicable both           all four-digit numbers, a user can pick any four-digit
in industrial environments handling proprietary in­           number, and then, having gained access to some file,
formation and in government installations process­            begin interacting with it in order to learn its con­
ing classified data. This Report is concerned directly        tents.
with only the latter; it is sufficient here to acknowl­           Another class of active infiltration techniques in­
edge that the entire range of issues considered also          v.oiv€8 the exploitation of trap-door 2 entry points in
has a "civil" side to which this work is relevant.            the system that by-pass the control facilities and
                                                              permit direct access to files. Trap-door entry points
Types of Vulnerabilities                                      often are created deliberately during the design and
                                                              development stage to simplify the insertion of au­
    The design of a secure system must provide pro­           thorized program changes by legitimate system pro­
tection against the various types of vulnerabilities.         grammers, with the intent of closing the trap-door
These fall into three major categories: accidental dis­       prior to operational use. Unauthorized entry points
closures, deliberate penetrations, and physical at­           can be created by a system programmer who wishes
tack.                                                         to provide a means for bypassing internal security
    Accidental Disclosure. A failure of compo­                controls and thus subverting the system. There is
nents, equipment, software, or subsystems, resulting          also the risk of implicit trap-doors that may exist
in an exposure of information or violation of any             because of incomplete system design-i.e., loopholes
element of the system. Accidental disclosures are             in the protection mechanisms.. For example, it might
frequently the result of failures of hardware or soft­        be possible to find an unusual combination ofsystem
ware. Such failures can involve the coupling ofinfor­         eontrol variables that will create an entry path
mation from one user (or computer program) with               around some or all of the safeguards.
that ofanother user, the "clobbering" ofinformation               Another potential mode of active infiltration is
(i.e., rendering files or programs unusable), the de­         the use of a special terminal illegally tied into the
feat or circumvention of security measures, or unin­          communication system. Such a terminal can be used
tended change in security status of users, files, or          to intercept information flowing between a legiti­
terminals. Accidental disclosures may also occur by           mate terminal and the central processor, or to
improper actions of machine operating or mainte­              manipulate the system. For example, a legitimate
nance personnel without deliberate intent.                    user's sign-off signal can be interc::epted and can­
    Deliberate Penetration. A deliberate and cov­             celled; then, the illegal terminal can take over in­
ert attempt to (1) obtain information contained in            teraction with the processor. Or, an illegal terminal
the system, (2) cause the system to operate to the            can maintain activity during periods when the legiti­
advantage of the threatening party, or (3) manipu­            mate user is inactive but still maintaining an open
late the system so as to render it unreliable or unusa­
ble to the legitimate operator. Deliberate efforts to            1
                                                                   The discussion ofsubversion is largely based on the article by
penetrate secure systems can either be active or pas­         H. E. Petersen and R. Turn, "System Implications ofInformation
sive. Passive methods include wire tapping and                Privacy," AFIPS Conference Proceedings, Vol. 30, Thompson
                                                              Books, Washington, D.C., 1967, pp. 291-300.
monitoring of electromagnetic emanations. Active
                                                                 2
                                                                   Any opportunity to penetrate, subvert, mislead, or by-pass
infiltration is an attempt to enter the system so as to       security controls through an idiosyncracy of the software, soft­
obtain data from the files or to interfere with data          ware-hardware, hardware, procedural controls, etc.


                                                          4
line. Finally, the illegal terminal might drain off             counteract both accidental and deliberate events.
output directed to a legitimate terminal and pass on            The specific leakage points touched upon in the
an error message in its place so as to delay detection. ·       foregoing discussion can be classified in five groups:
    Active infiltration also can be by an agent oper­           physical surroundings, hardware, software, com­
ating within the secure organization. This technique            munication links, and organizational (personnel and
may be restricted to taking advantage of system pro­            procedures). The overall safeguarding of informa­
tection inadequacies in order to commit acts that               tion in a computer system, regardless of configura­
appear accidental but which are disruptive to the               tion, is achieved by a combination of protection fea­
system or to its users, or which could result in acqui­         tures aimed at the different areas ofleakage points.
sition of classified information. At the other ex­              Procedures, regulations, and doctrine for some of
treme, the agent may actively seek to obtain remova­            these areas are already established within DOD, and
ble files or to create trap doors that can be exploited         are not therefore within the purview of the Task
at a later date. Finally, an agent might be placed in           Force. However, there is some overlap between the
the organization simply to learn about the system               various areas, and when the application of security
and the operation of the installation, and to obtain            controls to computer systems raises a new aspect of
what pieces of information come his way without                 an old problem, the issue is discussed. An overview
any particularly covert attempts on his part at subv­           of the threat points is depicted in Fig. 3.
ersion.
    Passive Subversion. In passive subversion,                  Physical Protection
means are applied to monitor information resident
within the system or being transmitted through the                 Security controls applied to safeguard the physi­
communication lines without any corollary attempt.              cal equipment apply not only to the computer equip­
to interfere with or manipulate the system. The most            ment itself and to its terminals, but also to such
obvious method of passive infiltration is the wire tap.         removable items as printouts, magnetic tapes, mag­
 If communications between remote terminals and                 netic disc packs, punchcards, etc. Adequate DOD
 the central processor are over unprotected circuits,           regulations exist for dissemination, control, storage,
the problem of applying a wire tap to the computer              and accountability of classified removable items.
 line is similar to that of bugging a telephone call. It        Therefore, security measures for these elements of
 is also possible to monitor the electromagnetic ema­           the system are not examined in this Report unless
 nations that are radiated by the high-speed elec­              there are some unique considerations. The following
tronic circuits that characterize so much of the                general guidelines apply to physical protection.
equipment used in computational systems. Energy
given off in this form can be remotely recorded with­             (a) The area containing the central computing
 out having to gain physical access to the system or                  complex and associated equipment (the ma­
 to any of its components or communication lines.                     chine room or operational area) must be
The possibility ofsuccessful exploitation ofthis tech­                secured to the level commensurate with the
 nique must always be considered.                                     most highly classified and sensitive material
    Physical Attack. Overt assault against or at­                     handled by the system.
tack upon the physical environment (e.g., mob ac­                 (b) Physical protection must be continuous in
tion) is a type of vulnerability outside the scope of                 time, because ofthe threat posed by the possi­
this Report.                                                          bility of physical tampering with equipment
                                                                      and because of the likelihood that classified
                                                                      information will be stored within the com­
IV. AREAS OF SECURITY                                                 puter system even when it is not operating.
PROTECTION                                                        (c) Remote terminal devices must be afforded
                                                                      physical protection commensurate with the
  The system designer must be aware ofthe points                      classification and sensitivity of information
ofvulnerability, which may be thought ofas leakage                    that can be handled through them. While re­
points, and he mustprovide adequate mechanisms to                     sponsibility for instituting and maintaining

                                                            5

                                               rtli\.IJ:InJ:I\.ITI A I
                                           _._.   ,.   • - .....   ,   I   II~._




                          eOMPIJTER NETWORK VIILNERABILITIE5
                                                                                                             RADIATION
                                                                                                    .      TAPS
                                                                                                                  a.j Q
                 RADIATION


                      1
                                     RADIATION
                                                  TAPS
                                                               CROSSTALK               l
                                                                                   RADIATION      RADIATION ~
                                                                                            CROSSTALK   t ~ll-.
                                        l 1
                                       COMMUNICATION
                                                                   --1--+---~      SWITCHING
                 PROCESSOR                 LINES
                                                                                    CENTER




   FILES
THE~
                                       ~t ~ ~\                                          ~ARE
                                                                                    IMP~OPER CONNECTIONS
                                                                                                           "':     ~
                                                                                                                  tw
COPYING                             OPERATOR                                         CROSS COUPLING
UNAUTHO~IZEO ACCESS           REPLACE SUPERVISOR                       SYSTEMS PROGRAMMER                     REMOTE
                              REVEAL PROTECTIVE                        DISA&LE PROTECTIVE FEATURES           CONSOLES
                               MEASURES                                PROVIDE "INS"
                                                                       REVEAL PROTECTIVE MEASURES
      . HARDWARE
  FAILURE OF PROTECTION CIRCUITS        MAINTENANCE MAN                                     ACCESS
  CONTRI&UTE TO SOFTWARE FAILURES  OISA&LE HARDWARE DEVICES         ATTACHMENT OF RECORDERS
                                   USE STANO-ALONE UTILITY PROGRAMS
                  SOFTWARE                                          &UGS                    USER
           FAILURE Of PROTECTION FEATURES                                             IDENTIF'iCifi'ON
                 ACCESS CONTROL                                                       AUTHENTICATION
                 &OUNDS CONTROL                                                       SU&TLE SOFTWARE
                 ETC.                                                                  MODIFICATIONS

                                                   Figure 3




                                                           6
       physical protection measures is normally as­               isolated systems can be physically shielded to elimi­
       signed to the organization that controls the               nate emanations beyond the limits of the secure in­
       terminal, it is advisable for a central au­                stallation, but with geographically dispersed sys­
       thority to establish uniform physical security             tems comprehensive shielding is more difficult and
       standards (specific protection measures and                expensive. Currently, the only practical solutions
       regulations) for all terminals in a given sys­             are those used to protect communications systems.
       tem to insure that a specified security level                 The problem of emanation security is covered by
       can be achieved for an entire system. Termi­               existing regulations; there are no new aspects to this
       nal protection is important in order to:                   problem raised by modern computing systems. It
                                                                  should be emphasized, however, that control of
       • Prevent tampering with a terminal (in­
                                                                  spurious emanations must be applied not only to the
         stalling intelligence sensors);
                                                                  main computing center, but to the remote equip­
       • Prevent visual inspection of classified
                                                                  ment as well.
         work in progress;
                                                                     Although difficult to accomplish, the possibility
       • Prevent unauthorized persons from trying
                                                                  exists that covert monitoring devices can be in­
         to call and execute classified programs or
                                                                  stalled within the central processor. The problem is
         obtain classified data.
                                                                  that the computer hardware involved is ofsuch com­
   If parts of the computer system (e.g., magnetic                plexity that it is easy for a knowledgeable person to
disc files, copies of printouts) contain unusually sen­           incorporate the necessary equipment in such a way
sitive data, or must be physically isolated during                as to make detection very difficult. His capability to
maintenance procedures, it may be necessary to                    do so assumes access to the equipment during manu­
physically separate them and independently control                facture or major maintenance. Equipment is also
access to them. In such cases, it may be practical to             vulnerable to deliberate or accidental rewiring by
provide direct or remote visual surveillance of the               maintenance personnel so that installed hardware
ultra-sensitive areas. Ifvisual surveillance is used, it          appears to function normally, but in fact by-passes
must be designed and installed in such a manner                   or changes the protection mechanisms.
that it cannot be used as a trap-door to the highly                  Remote consoles also present potential radiation
sensitive material it is intended to protect.                     vulnerabilities. Moreover, there is a possibility that
                                                                  recording devices might be attached to a console to
Hardware Leakage Points                                           pirate information. Other remote or peripheral
                                                                  equipment can present dangers. Printer ribbons or
   Hardware portions of the system are subject to                 platens may bear impressions that can be analyzed;
malfunctions that can result directly in a leak or                removable storage media (magnetic tapes, disc
cause a failure of security protection mechanisms                 packs, even punchcards) can be stolen, or at least
elsewhere in the system, including inducing a soft­               removed long enough to be copied.
ware malfunction. In addition, properly operating                    Erasure standards for magnetic media are not
equipment is susceptible to being tapped or other­                within the scope of this Task Force to review or es­
wise exploited. The types of failures that most di­               tablish. However, system designers should be aware
rectly affect security include malfunctioning of the              that the phenomena of retentivity in magnetic
circuits for such protections as bounds registers,                materials is inadequately understood, and is a threat
memory read-write protect, privileged mode opera­                 to system security.
tion, or priority interrupt. Any hardware failure po­
tentially can affect security controls; e.g., a single-bit          Software Leakage Points
error in memory.
   Both active and passive penetration techniques                      Software leakage points include all vulnerabili­
can be used against hardware leakage points. In the                 ties directly related to the software in the computer
passive mode, the intervener may attempt to moni­                   system. Of special concern is the operating system
tor the system by tapping into communication lines,                 and the supplementary programs that support the
or by monitoring compromising emanations. Wholly                    operating system because they contain the software

                                                              7

                                                        • - • - . . - ..   1-.-1   A   I
  safeguards. Weaknesses can result from improper              tacker could mount a deliberate search for such loop­
  design, or from failure to check adequately for com­         holes with the expectation of exploiting them to
. binations of circumstances that can lead· to un­             acquire information either from the system or about
  predictable consequences. More serious, however, is          the system-e.g., the details of its information safe­
  the fact that operating systems are very large, com­         guards.
  plex structures, and thus it is impossible to exhaus­
  tively test for every conceivable set of conditions          Communication Leakage Points
  that might arise. Unanticipated behavior can be
  triggered by a particular userprogram or by a rare              The communications linking the central proces­
  combination of user actions. Malfunctions might              sor, the switching center and the remote terminals
  only disrupt a particular user's files or programs; as       present a potential vulnerability. Wiretapping may
  such, there might be no risk to security, but there is       be employed to steal information from land lines,
  a serious implication for system reliability and             and radio intercept equipment can do the same to
  utility. On the other hand, operating system mal­            microwave links. Techniques for intercepting com­
  functions might couple information from one pro­             promising emanations maybe employed against the
  gram (or user) to another; clobber information in the        communications equipment even more readily than
  system (including information within the operating           against the central processor or terminal equipment.
  system software itself); or change classification of         For example, crosstalk between communications
  users, files, or programs. Thus, malfunctions in the         lines or within the switching central itself can pre­
  system software represent potentially serious                sent a vulnerability. Lastly, the switch gear itself is
  security risks. Conceivably, a clever attacker might         subject to error and can link the central processor to
  establish a capability to induce software malfunc­           the wrong user terminal.
  tions deliberately; hiding beneath the apparently
  genuine trouble, an on-site agent may be able to tap         Organizational Leakage Points
  files or to interfere with system operation over long
  periods without detection.                                      There are two prime organizational leakage
      The security safeguards provided by the oper­            points, personnel security clearances and institu­
  ating system software include access controls, user          tional operating procedures. The first concerns the
  identification, memory bounds control, etc. As a re­         structure, administration, and mechanism ofthe na­
  sult of a hardware malfunction, especially a tran­           tional apparatus for granting personnel security
  sient one, such controls can become inoperative.             clearances. It is. accepted that adequate standards
  Thus, internal checks are necessary to insure that           and techniques exist and are used by the cognizant
  the protection is operative.· Even when this is done,        authority to insure the reliability of those cleared.
  the simultaneous failure of both the protection fea­         This does not, however, relieve the system designer
  ture and its check mechanism must always be re­              of a severe obligation to incorporate techniques that
  garded as a possibility. With proper design and              minimize the damage that can be done by a subver­
  awareness of the risk, it appears possible to reduce         sive individual working from within the secure
  the probability of undetected failure of software            organization. A secure system must be based on the
  safeguards to an acceptable level.                           concept of isolating any given individual from all
      Probably the most serious risk in system software        elements of the system to which he has no need for
  is incomplete design, in the sense that inadvertent          access. In the past, this was accomplished by denying
  loopholes exist in the protective barriers and have          physical access to anyone without a security clear­
  not been foreseen by the designers. Thus, unusual            ance of the appropriate level. In resource-sharing
  actions on the part of users, or unusual ways in             systems ofthe future, a population of users ranging
  which their programs behave, can induce a loophole.          from uncleared to those with the highest clearance
  There may result a security breach, a suspension or          levels will interact with the system simultaneously.
   modification of software safeguards (perhaps un­            This places a heavy burden on the overall security
   detected), or wholesale clobbering of internal pro­         control apparatus to insure that the control mech­
   grams, data, and files. It is conceivable that an at­       anisms incorporated into the computer system are

                                                           8
properly informed of the clearances and restrictions          bility and responsibility to control the movement of
applicable to each user. The machine system must be           personnel into and within the central computing
designed to apply these user access restrictions relia­       area in order to insure that only authorized individu­
bly.                                                          als operate equipment located there, have access to
   In some installations, it may be feasible to re­           removable storage media, and have access to any
serve certain terminals for highly classified or              machine parts not ordinarily open to casual inspec­
highly sensitive or restricted work, while other ter­         tion.
minals are used exclusively for less sensitive opera­
tion. Conversely, in some installations any terminal
can be used to any degree of classification or sen­           Leakage Point Ecology
sitivity, depending on the clearance and needs ofthe
user at the given moment. In either of these cases,              In dealing with threats to system security, the
the authentication and verification mechanisms                various leakage points cannot be considered only in­
built into the machine system can be relied upon              dividually. Almost any imaginable deliberate at­
only to the degree that the data on personnel and on          tempt to exploit weaknesses will necessarily involve
operational characteristics provided it by the                a combination of factors. Deliberate acts mounted
security apparatus are accurate.                              against the system to take advantage of or to create
   The second element of organizational leakage               leakage points would usually require both a system
points concerns institutional operating procedures.           design shortcoming, either unforeseen or un­
The consequences of inadequate organizational                 detected, and the placement ofsomeone in a position
procedures, or of their haphazard application and             to initiate action. Thus, espionage activity is based
unsupervised use, can be just as severe as any other          on exploiting a combination of deficiencies and cir­
malfunction. Procedures include the insertion of              cumstances. A software leak may be caused by a
clearance and status information into the security            hardware malfunction. The capability to tap or tam­
checking mechanisms of the machine system, the                per with hardware may be enhanced because ofdefi­
methods of authenticating users and of receipting             ciencies in software checking routines. A minor, os­
for classified information, the scheduling of comput­         tensibly acceptable, weakness in one area, in combi­
ing operations and maintenance periods, the provi­            nation with similar shortcomings in seemingly un­
sions for storing and keeping track of removable              related activities, may add up to a serious potential
storage media, the handling of printe9 machine out­           for system subversion. The system designer must be
put and reports, the monitoring and control of ma­            aware of the totality of potential leakage points in
chine-generated records for the security apparatus,           any system in order to create or prescribe techniques
and all other functions whose purpose is to insure            and procedures to block entry and exploitation.
reliable but unobtrusive operation from a security               The security problem of specific computer sys­
control viewpoint. Procedural shortcomings repre­             tems must be solved on a case-by-case basis employ­
sent an area of potential weakness that can be ex­            ing the best judgment of a team consisting ofsystem
ploited or manipulated, and which can provide an              programmers, technical, hardware, and communica­
agent with innumerable opportunities for system               tions specialists, and security experts. This Report
subversion. Thus, the installation operating proce­           cannot address the multitude of details that will
dures have the dual function of providing overall             arise in the operation ofa particular resource-shared
management efficiency and of providing the ad­                computer system in an individual installation. In­
ministrative bridge between the security control ap­          stead, it is intended that the Report provide guide­
paratus and the computing system and its users.               lines to those responsible for designing and certify­
   The Task Force has no specific comments to make            ing that a given system has satisfactory security con­
with respect to personnel security issues, other than         trols and procedures. On the other hand, the security
to note that control of the movement of people must           controls described in Parts B through D can
include control over access to remote terminals that          markedly reduce the probability that an undetected
handle classified information, even if only intermit­         attempt to penetrate a resource-sharing computer
tently. The machine room staffmust have the capa­             system will succeed.

                                                          9
   This Report addresses the most difficult security          for maintaining it under conditions of shifting job
control situation, a time-sharing system serving geo­         assignments, issuance and withdrawal ofclearances,
graphically distributed users. Where circumstances            changes in need-to-know parameters, transfer ofper­
warrant, a lesser set of controls may be satisfactory,        sonnel from one duty assignment to another, etc.
and it is not intended that in such cases there be                The system should be responsive to changing op­
prohibitions on implementing a system with a lesser           erational conditions, particularly in time of emer­
set of safeguards. The recommendations have been              gency. While not an aspect of security control per se,
framed to provide maximum latitude and freedom of             it is important that the system be responsive in that
action in adapting the ideas to specific installations.       it does not deny service completely to any class of
                                                              users as the total system load increases. It may prove
                                                            . desirable to design special emergency features into
                                                              the system that can suspend or modify security con­
V. SYSTEM CHARACTERISTICS
                                                              trols, impose special restrictions, grant broad access
                                                              privileges to designated individuals, and facilitate
Constraints                                                   rapid change of security parameters. 3
   The U.S. Government classifies defense informa­                The system should be auditable. It must provide
tion within a well defined and long established struc­        records to the security control supervisor, so that
ture. Although it might be desirable from the com­            system performance, security safeguards, and user
puter point of view to modify these rules, to do so           activities can be monitored. This implies that both
would be equivalent to tailoring the structure to fit         manual and automatic monitoring facilities are
the computer operation and would constitute an                desirable.
inappropriate recommendation. Obviously then, a                   The system should be reliable from a security
constraint is that a secure computer system must be           point ofview. It ought to be fail-safe in the sense that
consonant with the existing security classification           if the system cannot fulfill its security controls, can­
structure.                                                    not make the proper decisions to grant access, or
   A second constraint, at least initially, is the as­        cannot pass its internal self-checks, it will withhold
sumption that the general tenets of the existing,             information from those users about which it is un­
familiar, manual security control procedures will             certain, but ideally will continue to provide service
prevail. For example, the Task Force recommenda­              to verified users. A fallback and independent set of
tions require not only that a secure computer system          security safeguards must be available to function
identify a user, but also that the user establish             and to provide the best level of security possible un­
(prove) his authenticity; furthermore, he will be             der the degraded conditions if the system is to con­
asked to receipt by a simple response for any and all         tinue operation.
classified information that is made available to him              The system should be manageable from the
through any type of terminal. This is a desirable              point of view of security control. The records, audit
feature, not only from a consideration of system ac­          controls, visual displays, manual inputs, etc., used to
countability, but also from the point of view of pro­         monitor the system should be supplemented by the
tection for the user. It is conceivable that an error by      capability to make appropriate modifications in the
the computer system might result in an allegation             operational status ofthe system in the event ofcatas­
that it had given a user certain information, when,           trophic system failure, degradation of performance,
in fact, it had not.                                          change in workload, or conditions of crisis, etc.
                                                                  The system should be adaptable so that security
                                                              controls can be adjusted to reflect changes in the
General Characteristics                                       classification and sensitivity of the files, operations,
   In formulating its recommendations, the Task               ana the needs of the local installation. There should
Force recognized the following general characteris­           be a convenient mechanism whereby special
tics as desirable in a secure system.                         security controls needed by a particular user can be
   The system should be flexible; that is, there
should be convenient mechanisms and procedures                  •see the definition of Security Parameters, p. 13.


                                                           10

                                              CONFIDENTIAL
                                              ' - ' - ' 1 .,.   IL....I'l-1.,    I   1/\1­




embedded easily in its system. Thus, the security                      lute and demonstrable security risk-level. Since the
control problem ideally must be solved with general­                   security risk probabilities of present manual sys­
ity and economy. It would be too costly to treat each                  tems are not well known, it is difficult to determine
installation as an individual instance and to con­                     whether a given design for a secure computer system
ceive an appropriate set of unique safeguards.                         will do ·as well as or better than a corresponding
   The system must be dependable; it must not                          manual arrangement. This issue is likely to raise
deny service to users. In times of crisis or urgent                    considerable discussion at such time as official policy
need, the system must be self-protecting in that it                    decisions about security control in computer systems
rejects effo!"ts to capture it and thus make it unavail­               must be made.
able to legitimate users ..This point bears on the                        As described above, computer systems differ
number and kinds of internal records that the sys­                     widely in the capabilities they make available to the
tem must keep, and implies that some form ofration­                    user. Jn the most sophisticated (and highest security­
ing algorithm must be incorporated so that a pene­                     risk) case, a user can construct both new programs
tration would capture no more than a specified share                   and new programming languages from his console,
of system capability.                                                  and embed such new languages into the computer
   The system must automatically assure configu­                       system for use. In such a computer system, offering
ration integrity. It must self-test, violate its own                   the broadest capability to the user, the security prob­
safeguards deliberately, attempt illegal operations,                   lems and risks are considerably greater when users
monitor communication continuity, monitor user ac­                     from the following two classes must be served simul­
tions, etc., on a short time basis.                                    taneously:

Uncertainties                                                               •         Uncleared users over whom there is a mini­
                                                                                      mum administrative control and who work
   The Task Force has identified several aspects of                                   with unclassified data through physically un­
secure computer systems which are currently im­                                       protected terminals connected to the comput­
practical or impossible to assess.                                                    ing central by unprotected. communications
    Failure Prediction. In the present state of com­                                  lines.
puter technology, it is impossible to completely an­                        •         Cleared users operating with classified infor­
ticipate, much less specify, all hardware failure                                     mation through appropriately protected ter­
modes, all software design errors or omissions, and,                                  minals and communication links.
most seriously, all failure modes in which hardware
malfunctions lead to software malfunctions. Exist­                              It is the opinion of the Task Force that it is un­
ing commercial machines have only a minimum of                          wise at the present time to attempt to accommodate
redundancy and error-checking circuits, and thus                        both classes of users simultaneously. However, it is
for most military applications there may be unsatis­                    recognized that many installations have an opera­
factory hardware facilities to assist in the control of                 tional need to serve both uncleared and cleared us­
hardware/software malfunctions. Furthermore, in                         ers, and recommendations addressed to this point
the present state of knowledge, it is very difficult to                 are presented in Parts B through D.
predict the probability of failure of complex hard­                        Cost. Unfortunately, it is not easy at this time to
ware and software configurations; thus, redundancy                      estimate the cost of security controls in a computer
is an important design concept.                                         system. Only a few computer systems are currently
   Risk Level. Because failure modes and their                          in operation that attempt to provide service to a
probability of occurrence cannot be completely cata­                    broad base of users working with classified informa­
loged or stated, it is very difficult to arrive at an                   tion. While such systems are serving the practical
overall probability of accidental divulgence of clas­                   needs of their users, they are the products of re­
sified information in a security-controlling system.                    search efforts, and good data reflecting the incre­
Therefore, it is difficult to make a quantitative meas­                 mental cost ofadding security controls to the system
urement of the security risk-level of such a system,                    and operating with them are not yet available.
and it is also difficult to design to some a priori abso­                  In computer systems designed for time-sharing

                                                                  11
applications, some of the capabilities that are pre­            spoken of as having a given level of clearance, it is
sent in order to make a time-sharing system work at             implied that certain investigative procedures and
all are also applicable to the provision of security            tests have established that the corresponding level of
controls. In other computing systems, any facilities            classified information can be safely transmitted
for security control would have to be specially in­             through that terminal. When referring to an aggre­
stalled. Thus, the Task Force cannot give an accu­              gation of equipment, together with its management
rate estimate ofthe cost ofsecurity. It will depend on          controls and procedures, facility clearance is some­
the age of the software and hardware, but certainly             times used.
security control will be cheapest ifit is considered in            Need-to-know. An administrative action certi­
the system architecture prior to hardware and soft­             fying that a given individual requires access to spe­
ware design. In the opinion of some, the investment             cified classified information in order to perform his
in the security controls will give a good return in             assigned duties. The combination of a clearance and
tighter and more accurate accountability and dis­               a need-to-know constitutes the necessary and suffi­
semination of classified information, and in im­                cient conditions for granting access to classified in­
proved system reliability.                                      formation.
   The cost of security may depend on the workloatl                 Classification. The act of identifying the sen­
of the installation. If all classified operations can be        sitivity of defense information by ascertaining the
accommodated on a single computer, and all unclas­              potential level of damage to the interests of the
sified operations on a second computer, the least ex­           United States were the information to be divulged to
pensive way to maintain the integrity of the clas­              an unfriendly foreign agent. The classification of in­
sified information may be to retain both machines.              formation is formally defined in Executive Order
Such a configuration will present operational ineffi­           10501. There are only three formal levels of national
ciency for those users who need to work with both               classification: Top Secret, Secret, and Confidential,
classified and unclassified data bases, but the con­            but it is expedient from the computer point of view
cept of a dual installation-with one machine work­              also to consider Unclassified as a fourth level ofclas­
ing in the clear and a second machine fully protected           sification. The identifiers associated with an item of
-cannot be summarily rejected.                                  classified information, indicating the level ofclassifi­
                                                                cation or any special status, are generically called
                                                                 labels.
VI. DEFINITIONS                                                     Special Category (or: Special-Access Category
                                                                or Compartment). Classified defense information
   There are many terms commonly used in connec­                that is segregated and entrusted to a particular
tion with security control for which usage is not com­          agency or organizational group for safeguarding. For
pletely standardized. Terms used throughout this                example, that portion of defense classified informa­
Report are defined below as a group; certain other              tion that concerns nuclear matters is entrusted to
terms (especially computer-related ones) are defined            the Atomic Energy Commission, which is responsi­
at appropriate places in the text.                               ble for establishing and promulgating rules and
   Clearance. The privilege granted to an in­                    regulations for safeguarding it and for controlling its
dividual on the basis of prescribed investigative                dissemination. Classified information in a special
procedures to have formal access to classified infor­            category is normally identified by some special
mation when such access is necessary to his work.                marking, label, or letter; e.g., AEC information,
The three formal national clearances are Top Secret,             whether classified Confidential, Secret, or Top Se­
Secret, and Confidential. However, it is also expedi­            cret, is collectively identified as Q-information. It is
ent from the computer point of view to recognize                 often called Q-classified, but note that this use of
 Uncleared as a fourth level ofclearance. A clearance            classification is an extended sense of the formal us­
is a necessary but not sufficient condition to have              age of the word.
access to classified information. By extension, the                 Sometimes, special investigative procedures are
concept of clearance can be applied also to equip­               stipulated for granting access to information in spe­
ment. For example, when a computer terminal is                   cial categories. Thus, while formally there are only

                                                           12
three broadly defined national clearance levels, in                 protected, or utilized. Examples: "Limited Distri­
practice there is a further structure within each                   bution," "Special Handling Required," "Group 1
level. In part, this reflects the separation of informa­            -Excluded from Automatic Downgrading and
tion into special categories, and, in part, the fact that           Declassification."
many different agencies are authorized to grant                     Fully Cleared. An individual who has the clear­
clearances. For example, an individual functioning               ance and all need-to-know authorizations granting
within the AEC domain and cleared to Top Secret                  him access to all classified information contained in
will often be said to have a Q-clearance because he              a computer system. By extension, the term can be
is authorized access to Top Secret information en­               applied to equipment, in which case it implies that
trusted to the AEC for safeguarding and identified               all necessary safeguards are present to enable the
by the special category Q. These special types of                equipment to store and process information with
clearances at given levels are not always specifically           many levels of classification and caveated in many
identified with a unique additional marking or label.            different ways.
   Caveat. A special letter, word, phrase, sentence,                Security Flag. For the purposes ofthis Report, it
marking, or combination thereof, which labels clas­              is convenient to introduce this new term. It is a com­
sified material as being in a special category and               posite term, reflecting the level of classification, all
hence subject to additional access controls. Thus, a             caveats (including codewords and labels), and need­
caveat is an indicator of a special subset of informa­           to-know requirements, which together are the fac­
tion within one or more levels of classification. The            tors establishing the access restrictions on informa­
caveat may be juxtaposed with the classification la­             tion or the access privileges of an individual. By ex­
bel, may appear by itself, or sometimes does not ap­             tel1sion, the concept can be applied to equipment,
pear explicitly but is only inferred. Particular kinds           and indicates the class of information that can be
of caveats are:                                                  stored and processed.
                                                                    Thus, the security flag contains all the informa­
  Codewords. An individual word or a group of                    tion necessary to control access. One security flag is
  words labelling a particular collection ofclassified           considered to be equal to or higher than a second if
  information.                          '                        a requestor with the first flag is authorized access to
                                                                 information which has the second flag.
  Dissemination Labels (Access Control Labels).                     Security Parameters. The totality of informa­
  A group of words that imposes an additional re­                tion about users, files, terminals, communications,
  striction on how classified information can be                 etc., which a computer system requires in order to
  used, disseminated, or divulged; such labels are an            exercise security control over the information that it
  additional means for controlling access. Exam­                 contains. Included are such things as user names,
  ples: "No Foreign Dissemination," "U.S. Eyes                   clearances, need-to-know authorizations, physical lo­
  Only," "Not Releasable Outside the Department                  cation; terminal locations and. clearances; file clas­
  of Defense."                                                   sifications and dissemination restrictions. Thus, a
  Information Labels. A group of words that con­                 set of security parameters particularizes a general­
  veys to the recipient of information some addi­                ized security control system to the specific equip­
  tional guidance as to how the information may be               ment configuration, class of information, class of us­
  further disseminated, controlled, transmitted,                 ers, etc., in a given installation.




                                                            13
                                                 Part B
   POLICY CONSIDERATIONS AND RECOMMENDATIONS

   The policy recommendations that follow are in­            words, authentication words, and specifically desig­
tended to provide a security skeleton around which           nated sensitive procedures shall require classifica­
a specific secure computer system may be built. Ad­          tion.
ditionally, these recommendations set forth there­           Comment: These principles reflect the constraint
sponsibilities and functions of the personnel needed         that the recommendations of the Task Force be con­
to evaluate, supervise, and operate a secure system.         sistent with generally accepted, existing security doc­
This is a new field, and this Report represents the          trine. The last item is considered relevant in order to
first major attempt to codify its principles. In some        permit maximum operational convenience.
cases, the rationale behind a specific recommenda­
tion and appropriate examples are presented in a
Comment.
                                                             II. SYSTEM PERSONNEL
                                                                Depending upon the nature of the individual
I. FUNDAMENTAL PRINCIPLES                                    computing installation, some or all of the following
                                                             categories of personnel will be associated with it. It
   Automatic data processing systems shall accom­            is recognized that a given individual may have more
modate, without exception, the responsibilities ofin­        than one responsibility, and either simultaneously
dividuals to ensure that certain official information        or at different times perform more than one func­
affecting national defense is protected against unau­        tion. It is also recognized that the scope of responsi­
thorized disclosure, pursuant to Executive Order             bility may imply a substantial organizational group
10501 (Amended), "Safeguarding Official Informa­             for each function.
tion in the Interests of the Defense of the United               Responsible Authority. The head ofthe depart­
States."                                                     ment or agency responsible for the proper operation
   A computer system shall grant access to classified        of the secured computer system.
information only to persons for whom it can deter­               User. Any individual who interacts directly
mine that their official duties require such access,         with the computer system by virtue of inserting in­
and that they have received the proper security              formation into the system or accepting information
clearances and need-to-know authorizations.                  from it. "Information" is considered to include both
   The means employed to achieve system security             computer programs and data.
objectives shall be based on any combination of soft­        Comment: A user is thus defined whether he in­
ware, hardware, and procedural measures sufficient           teracts with the system from a remote terminal or
to assure suitable protection for all classification         submits work directly to the computing central
categories resident in the system.                           through a batch-process mode.
   To the maximum extent possible, the policies and
procedures incorporated to achieve system security             System Administrator. An individual desig­
shall be unclassified. However, specific keys, pass­         nated as responsible for the overall management of

                                                        14
 all system resources, both the physical resources of            bility in order to maintain system integrity with re­
 the system and the personnel attached to it.                    spect to security matters, and (2) maintain the basic
 Comment: The users are generally excluded from                  functioning of the system.
 the System Administrator's management purview,                  Comment: The hardware and software mainte­
 although personnel under his control may also be                nance personnel are permitted to service not only the
 users at times.                                                 normal, basic features of the computing system, but
                                                                 also the security control features. However, there need
   System Certifier. An individual designated by                 be no prohibition on the assignment of these two
an appropriate authority to verify and certify that              classes of maintenance requirements to separate in­
th~ security measures of a given computer system                 dividuals or groups of individuals.
and of its operation meet all applicable, current cri­
teria for handling classified information; and to es­               System Operators. Those personnel responsible
tablish the maximum security level at which a sys­               for performing the manual procedures necessary to
tem (and each of its parts) can operate.                         provide and maintain on-going service operations of
   System Security Officer. An individual desig­                 the system.
nated by a Responsible Authority as specifically re­
sponsible for (1) proper verification of personnel               Personnel Designations and
clearances and information-access authorizations;                Responsibilities
(2) determination of operational system security
status (including terminals); (3) surveillance and                  System Administrators, System Security Offic­
maintainance of system security; (4) insertion of                ers, and System Maintenance and Operations Per­
security parameters into the computing system, as                sonnel shall be formally designated by the Responsi­
well as general security-related system matters; (5)             ble Authority. The total number of such personnel
security assurance. ·                                            should be kept to a minimum. Where necessary to
                                                                 meet special operational needs ofa particular instal­
  Comment: The System Certifier will establish the               lation, special restrictions affecting personnel may
  maximum security level at which the system (and                be incorporated into the individual agency's proce­
  each part of it) can operate; the System Security              dures, formulated under the cognizance of the Re­
  Officer will determine on an operational basis· the .          sponsible Authority.
  level at which it does operate. He will normally verify
  personnel clearances with the overall security offi­           Comment: This recommendation is intended to per­
  cials of the organization, and need-to-know authori­           mit installations that have special operational needs,
  zations with the organizational element that has cog­          either because of mission or sensitivity of informa­
  nizance over the information in question (e.g., an             tion, to impose additional constraints on system per­
. Office of Primary Interest).                                   sonnel or on their responsibilities.
 Security assurance implies an independent group                 As a general approach, it is desirable that persons
 that continuously monitors security provisions in the           designated as System Personnel have sufficient clear­
 computer system. It includes such functions as con­             ance and need-to-know authorization for all informa­
 tinuously probing the system to ascertain its weak­             tion resident in the computer system. However, it is
 nesses and vulnerabilities, recommending additional             conceivable that even for System Personnel, access
 safeguards as need is determined, and validating the            could be segmented so that such clearance would not
 security provisions in a system. Because ofthe techni­          be absoluteiy necessary. For example, Operators and
 cal expertise implied by security assurance, it is prob­        Administrators may not have access to the keys or
 able that this responsibility will be shared by the             mechanism that allow access to the interior of the
 System Certifier.                                               hardware. This policy will accommodate either ap­
                                                                 proach as found to be necess.ary by the exact nature
   System Maintenance Personnel. The individu­                   of the computer system involved and the information
als designated as responsible for the technical                  to be protected. A typical user-agency decision might
maintenance ofthose hardware and software system                 be to limit System Personnel to U. S. Government
features that (1) must operate with very high relia­             personnel, or to special two-man teams, each ofwhich

                                                            15
may be limited to partial access. Another user-agency           selfand to authenticate his identity to the system at
decision might be to require some degree of sanitiza­           any time requested by it, using authentication tech­
tion preliminary to the performance of certain types            niques or devices assigned by the System Security
ofsystem maintenance, especially if the person capa­            Officer. Such techniques or devices shall be sufficient
ble ofperforming such maintenance is not or cannot              to reduce the risk of unauthorized divulgence, com­
be cleared adequately. Sanitization refers to the pro­          promise, or sabotage below that required by the sen­
tection ofclassified information resident in computer           sitivity of the data resident in the system.
files either by deliberate erasure or by physically             Comment: Identification is for the purposes of sys­
removing and/or protecting the storage medium or                tem accounting and billing, whereas authentication
device.                                                         is the verification procedure necessary before the sys­
Although it is recognized that System Personnel may             tem can grant access to classified information. Th.e
fulfill more than one responsibility, this option may           choice oftechnique or device obviously will depend.on
not be exploitable in practice because of the signifi­          the sensitivity of the data resident within the com­
cantly different skills required. For example, skilled          puting system, the physical location ofthe user termi­
and experienced system programmers will be required             nal, the security level to which it and its communica­
to maintain the software, whereas computer engi­                tion links are protected, the set of users that have
neers will be required for the hardware, and com­               access to it at any time, etc.
munication engineers for the communications.
                                                                User Responsibility
User Designation
                                                                   A properly authenticated user is responsible for
   Each user (or specific group of users) shall be ad­          all action at a given terminal between the time that
ministratively designated (identified) to the com­              his identity has been established and verified, and
puter system by the System Administrator, with the              his interaction with the system is terminated and
concurrence of the System Security Officer. The                 acknowledged. Termination can occur because he
designation shall include indicators of the user's              notifies the system of his departure, or because the
status in sufficient detail to enable the system to             system suspends further operation with him. The
provide him with all material to which he is author­            user is responsible for observing all designated
ized access, but no more.                                       procedures and for insuring against observation of
Comment: As will be seen in the Appendix, which                 classified material by persons not cleared for access
defines a language and schema for identifying both a            to it; this includes proper protection of classified
security structure and security parameters to a com­            hard copy. Furthermore, he is responsible for report­
puting system, the number ofparameters that must                ing system anomalies or malfunctions that appear to
be kept within the system for each user will reflect the        be related to system security controls to the System
kind ofclassified information with which the system             Security Officer, especially when such occurrences
deals. In some instances, it will be necessary to verify        suggest that system security control measures may
more than a user's clearance and need-to-know status            be degraded, or that a deliberate attempt to tamper
before access to classified information can be granted;         with or penetrate the system is occurring. Other sys­
e.g., it may be necessary to verify his agency ofemploy­        tem anomalies should be reported to System Mainte­
ment. It may also be desirable to keep within the               nance Personnel, who, in turn, must report to the
computing system extensive info;mation on each                  System Security Officer those hardware or software
user, not for routine verification of his access privi­         malfunctions that investigation shows have affected
leges, but for the convenience of the System Security           security controls.
Officer when he finds it necessary to intervene in the
system~ operation.                                              Access
                                                                  Access to classified information stored within the
User Authentication                                             computer system shall be on the basis of specific
   Each user shall be required both to identify him­            authorization from the System Security Officer to

                                                           16
receive such information, or by automatic processes               recting a computational process to declare and
operating under his control and authority. The au­                verify the classification and any applicable caveats
thority of the System Security Officer to authorize               and other labels for an information unit produced as
system users to have access to classified information             a result of some computer process (e.g., calculations
stored in the system does not implicity apply to the              of bomber ranges or weapon effectiveness), or as a
System Security Officer himself. Separate and spe­                result of a transformation of some previously exist­
cific restraints over his access to classified informa­           ing unit (e.g., merging or sorting of files). 1 This re­
tion shall be established by the System Administra­               sponsibility extends to security control and manage­
tor. A specific algorithm (or combination of al­                  ment ofinformation subunits. Procedures analogous
gorithms) for controlling access to all classl.fied infor­        to those in force for controlling introduction ofinfor­
mation shall be specified and embedded in the sys­                mation from or release of information to entities
tem. Moreover, a specific protocol and mechanism                  outside the system must be observed, and are de­
shall be specified for inserting into the computer                scribed in Sec. VI below, "Information Security La­
system those security parameters that grant andre­                bels." Since a hierarchical structure of information
scind access privileges. For both purposes, hardware,             classification will usually exist, a composite unit
software, and procedural mechanisms shall be im­                  must be at least at the highest level of classification
plemented .that insure that neither the access con­               of the units contained in the composite, but, in fact,
trol algorithm nor the security-parameter insertion               may be higher. Automatic algorithms may be used to
mechanism is circumvented, either accidentally                    aid the user in the execution of these responsibili­
(through component failure) or intentionally.                     ties.
Comment: This recommendation establishes the                      Comment: The intent of this recommendation is to
general principle on which user access to classified              provide procedures analogous to those for handling
information within the system is granted. The details             documents, as specified in Section 3 ofExecutive Or­
of the algorithm that permits access to classified in­            der 10501 (Amended). The recommendation on infor­
formation obviously will depend on that part of the               mation structure and transforms leaves unspecified
total security structure with which the computer sys­             whether a computer-based file is classified as an en­
tem is concerned, and also on the status information              tity, or whether the individual entries or elements of
kept within the system for each user. The Appendix                the file are separately classified. The design of the file
illustrates a particular algorithm that appears to be             structure and the details of how it shall be classified
sufficiently comprehensive to cover all requirements              are operational matters, not a problem ofproviding
known to the Task Force. It should be noted that this             security control mechanisms. However, where the
recommendation attempts to incorporate redundancy                 security structure of the file is established, the proce­
into the access control mechanism, and also into the              dures outlined in this recommendation will apply.
parameter insertion mechanisms, by requiring a com­               This recommendation also permits the use of com­
bination of hardware, software, and procedural                    puter algorithms to assist in classifying new informa­
mechanisms.                                                       tion. In the Appendix, examples are given which sug­
                                                                  gest how such algorithms may be applied, but the
                                                                  computer system may not be able to establish classifi­
III. INFORMATION STRUCTURE                                        cation level or applicable special caveats and labels
                                                                  in every circumstance. At most, the system can tell a
AND TRANSFORMS
                                                                  user that he has had access to classified information
   Data storage shall be organized and controlled at
the level of the basic computer system in terms of                    'This statement is not adequate for nongovernmental organi­
information units, each ofwhich has a classification              zations, nor in some government situations. For example, an em­
                                                                  ployee of an industrial contractor can only suggest the classifica­
descriptor plus applicable special-access categories              tion of information which he creates; the formal .declaration of
(as required by the presence of caveats) and other                classification is made by a designated, appropriate authority,
                                                                  sometimes external to the contractor company. Some secure com­
labels that apply to the information unit as a whole.             puter systems will require a supplementary procedure to validate
It is the explicit responsibility of the individual di­           classifications suggested by users.


                                                             17
vith given caveats and labels; it' will be his responsi­            overlaps somewhat the control offile integrity, and it
•ility to confirm to the computer system the classifica­            may prove desirable for some of the audit informa­
ion, special caveats, and labels that should apply. If              tion to be made available to the System Administra­
he sensitivity ofthe information warrants, audit in­                tor.
ormation should be made available to the System                     The number and kinds ofaudits and the periodicity
~ecurity Officer, informing him that a user has taken
                                                                    with which they are made will depend on such fac­
ome specified action in establishing or modifying a                 tors as sensitivity ofthe information contained in the
learance level, applicable caveats, or labels.                      computer system, the class of users it services and
                                                                    their clearance status, the operational requirements
                                                                    ofthe system, etc. Some portions ofthe status log will
V.   SYSTEM TRANSACTION                                             be only historical, others will be used operationally.
~CCOUNTING                                                          It is conceivable that in some installations it will
                                                                    prove desirable to provide the System Se~urity Officer
. .ogging of Transactions                                           with a visual display of the system transaction log.
                                                                    It should be noted that when the System Security
  All relevant transactions between users and the                   Officer is interacting with the system (e.g., inserting
omputer system shall be automatically logged (in­                   new security parameters), he is considered by the sys­
luding date and time) by the computer system so                     tem to be a user. Thus, even though his actions are
b.at an audit oftransactions involving access to and                privileged and executable only by himself, his activi­
eneration, classification, reclassification, and de­                ties will be automatically logged. Furthermore,
truction of files is possible. The provisions of this               maintenance personnel will also be considered users
aragraph also apply to unclassified information                     when their activity can be accomplished with the
b.at resides in a system containing, or cleared to                  system in an operational status, and their actions
ontain, classified information. Supplementary                       will also. be automatically logged. Finally, the in­
1anual logs (including date and time) must record                   teractions of the operating personal, especially the
ll significant events that cannot be automatically                  console operators, will be considered as user activity
>gged.                                                              and logged.
:Omment: Transaction as used here includes such
hings as a user logging onto or off the system; the                 Receipting
ystem granting a user access to a specified file; the
terging offiles by a user; the generation ofnew infor­                 Where required by applicable regulations, a re­
tation to which a user assigns classification;                      ceipt shall be obtained from any user who has re­
hanges made in a classified file by a user; and ex­                 ceived classified information from the system. Re­
hanges of information with another computer. The                    ceipting shall require an overt action on the part of
"tclusion of unclassified information is intended to                the user following delivery (or presentation) to him
rovide for the case where "unclassified" information                of the classified information. The purpose of the re­
ecomes upgraded, and to protect against unobserved                  ceipt is to insure that the user is aware that he has
ctivity in the manipulation of the system by users.                 received classified data. For the purposes of this re­
'he audit-trail data should be made available to the                quirement, the bounds of a dialogue between a user
'ystem Security Officer to aid him in the continuous                and the computer system are defined to be based on
wnitoring of the security of the system.                            the beginning and ending of access to a particular
t may prove operationally desirable to aggregate in­                unit of information contained within the system or
)rmation of this type and present it in various peri­               transferred to or from the system.
die reports. Thus, for example, the System Security                 Comment: While a properly functioning system al­
lfficer could be informed at the end of each shift as               ready knows, to the degree adequate for logging of
) which files have been addressed by or released to                 system activity, where information should be or to
zch user, or which files have been updated or had                   whom it has been delivered, the requirement for a
1eir classification changed. The control of security                receipt recognizes a need for an acknowledgment

                                                               18

                                               ,.....,.~""   ,_. __ ·-· ....
                                                                     ._
from the recipient (person or program) that he is                mode wherein no information may be transmitted to
aware that he has received classified information of             or accepted from the user community. In order that
a particular level. It is essential for system efficiency        there be no unnecessary interruption of services, the
and man-machine effectiveness that the receipting                nystem must concurrently check all its internal pro­
procedure not be imposed excessively. Thus, defini­              t;ectiori mechanisms. Should the detected failure
tion ofappropriate transaction boundaries is crucial.            prove to be the consequence of a transient error, the
Although it is undesirable to burden the user with               system should so notify the System Security Officer
unnecessary actions, nonetheless it may be to his ad­            and be returned to its full operational status by an
vantage tu require a receipt for all information. He             overt action of the System Security Officer. In the
will be aware of, and the system transaction log will            event the failure persists, it shall be the responsibil­
reflect, precisely the information to which .he has had          ity of the System Security Officer to take any action
access. His liability is therefore defined, and any              indicated. He may return the system to full or par­
investigation which later may arise because of a sys­            tial operational status in spite of impaired security
tem malfunction or divulgence ofclassified informa­              controls; he may attempt to remove malfunctioning
tion would be facilitated.                                       equipment and restore a modified configuration to
                                                                 full status. In any event, the action required of him
                                                                 must be sufficiently overt that the possible security
V. RELIABILITY AND                                               implications of his action will be patently· clear.
AUTO-TESTING                                                         Special instructions shall be provided to the Sys­
                                                                 tem Security Officer in those installations that deal
   All security control or assurance mechanisms                  with information of high sensitivity, and for which.
and procedures shall be designed to include suffi­               special procedures are deemed necessary in order to
cient redundancy and independent checks so that                  insure that the system is not allowed to operate in a
the failure of one control mechanism will not allow              manner that increases the risk of compromise or
an undetected compromise to occur. Frequent auto­                 unauthorized disclosure.
matic checks of these protection mechanisms by the
computing system itself, and periodic checks of the              Comment: The issue raised by this recommendation
procedures by system personnel shall be made. The                 is a delicate one because it addresses a conflict be­
computing system shall have the capability of guar­              .tween policy objectives of the system: maintaining
anteeing that some specified minimum fraction ofits              service to the users ofa computing system, and main­
time is spent on performing automatic system check­               taining proper security control over the information
ing. The percentage of time spent on automatic                   stored within it. If an agent knows how to create an
checking shall be a design parameter ofthe comput­                error on demand, total shutdown of a system when
ing system (capable of change at the local installa­              trouble is detected is a serious vulnerability. Thus, a
tion as necessary), and shall be established with the             capability for flexible response, depending upon the
concurrence of the System Certifier. The interval                conditions of the moment, is essential. The action
between automatic internal self checks may depend                 taken by the System Security Officer, perhaps in con­
on the classification and sensitivity of the informa­            junction with the Responsible Authority or the Sys­
tion that the system is designed to accommodate.                  tem Administrator, must reflect the operational
The System Security Officer shall be provided means               situation that the system supports. In a military com­
for establishing what fraction of the time the in­                mand and control system where delay can mean
stalled system spends in self-checking and be respon­             disaster, operational urgency may dictate that a cal­
sible for controlling the time so spent, depending on             culated risk of unauthorized divulgence be assumed
the classification and sensitivity of the information             in order to maintain continued service to users. On
that his system is handling. Means shall be provided              the other hand, a technical information system can
for the System Security Officer to initiate these                 alford to suspend service totally in case of trouble,
checks manually.                                                  especially if it deals with very sensitive information.
   A detected failure of the protection mechanisms               The fraction of its time that a computing system
shall cause the system to enter a unique operating               must spend in selfchecking, and the scope and depth

                                                            19
'Jf such self checks are not matters that can be      as­would need to be provided           with a great deal of visu­
~essed readily by the local System Security Officer.     ally displayed information and with appropriate
 flence, this recommendation requires that the      prob­manual controls over         system performance.
lem be addressed at the level of design and installa­    Typical actions that the System Security Officer
tion certification. However, it is reasonable that the   might take, depending on the type offailure detected
System Security Officer have the option of adjusting     and upon the operational urgency of the moment,
the periodicity and depth and scope ofself-checking,     include:
1ccording to the level of information that his system
must accommodate.                                        (a) Disabling the system completely-i.e., closing it
 rt is not possible to make positive statements about         down and requesting maintenance.
 the frequency with which internal self-checking must    (b)  Continuing to operate the system in the degraded
 ~eperformed. In part, this reflects lack ofinsight into      mode, but under his continuous manual surveil­
 1nd experience with the security control mechanisms          lance.
 to be installed in the computing systems under con­     (c)  Prohibiting      new users, while allowing current
 ;ideration. It may be desirable to perform internal          users  to  continue    interaction with files presently
 ;elf-checking on some scheduled periodic basis, or,          accessible    to them.
 oerhaps more wisely, the internal self-checking         (d) Restricting access to classified files to those ter­
 ;hould take place on an aperiodic basis, such as when        minals over which he or some other responsible
 1 user from a terminal requests access to a file. Aperi­     authority     has visual cognizance. Alternatively,
 )dic checking denies a potential penetrator the assur­       he  might    suspend     all but fully-cleared users.
 mce that he has guaranteed intervals of time in         (e)  Denying     all  user requests     to access files ofspecial
 '.Vhich to attempt to subvert or bypass the security         sensitivity.
 ~ontrol mechanisms, but it also increases the self­     (f)  Electrically severing malfunctioning storage de­
 ~hecking load on the machine as the user load in­            vices, thus permitting the balance ofthe system to
 ~reases. In any event, the maximum interval between          continue    in operation. If these devices contain the
 ~nternal self-tests should be chosen jointly by the   us­    security control and        checking programs and au­
  ~r-agency and the System Security Officer. The objec­       thentication      words,    etc.,  then a choice must be
 tive is to find an acceptable balance between system         made    between     this  option    and point (g) below.
  ~fficiency and the amount of classified information    (g)  By-passing      all security    checks  and operating the
  that could be compromised between tests, while main­        system    "wide-open.     "
  taining a risk acceptable to the user-agency.          (h) Electing to operate with unprotected communi­
                                                              cations.
  rn the event of an automatically detected failure of
  z control mechanism, it is clear that the computing    It is reasonable that the system be designed so that
  rystem must shift to a degraded mode of operation      the action options available to the System Security
  'Jecause ofthe risk of unauthorized divulgence.   How­ Officer can be automatically           presented tp him by the
  mer, the system design must be such that the system    system itself. It is also reasonable that each option
  zttempts to maintain maximum service to the      great­displayed be accompanied            by instructions detailing
  ~st number of users. It is also clear that the issue   the manual and procedural actions that he ought to
  ~ranscends the computing central and its procedures;    take.
  z response to malfunction can also involve communi­     Ultimately, the amount of self-checking incor­
  :ations, remote terminals, other computers, etc.       porated into a system, the frequency with which self­
rhe degraded mode suggested by the wording of this      checking is done, and the precise details of how the
·ecommendation seems to be reasonable, but it is not    system functions in a degraded mode, will represent
~he only possibility. Another, for example, is to bring a design compromise betwf!en maintaining maximum
~he System Security Officer into the access control     service to the users and maintaining maximum
Jrocedure and let him manually verify each user      re­safety of the information resident within the system.
ruest for access to a given file. If such a procedure   When circumstances warrant, the system can be de­
.vere to be implemented, the System Security Officer    signed to automatically go into a more extensive

                                      20
mode of internal selfchecking, or even to switch au­                   separate page or display ofinformation, means must
tomatically to alternate software packages that can                    be provided for the user to obtain them at his re­
substitute for malfunctioning hardware or software                     quest.
protection mechanisms.                                                  Comment: Ideally, all information provided a user,
                                                                        whether printed out in hard copy or electronically
                                                                        displayed, should be accompanied by all relevant
VI. INFORMATION SECURITY                                                security parameters. However, practical limitations
LABELS                                                                  in the capabilities of display devices or printers may
                                                                        make alternati.ve procedures necessary. At the mini­
                                                                        mum, the classification level must be displayed or
Information Input
                                                                        printed with each page. The user must be able to
   The system shall not accept information, even for                    obtain the complete set of security parameters as­
temporary use, without first receiving from the user                    sociated with information when he is being asked to
a declaration of the relevant security parameters,                      receipt for it.
which in this case inch.ide classification, all caveats,
and labels. These parameters will be used by the
system to control further use or dissemination ofthe                    VII. MANAGEMENT OF STORAGE
information. The security parameters can be han­                        RESOURCES
dled as a declaration covering a definable set of in­
teractions between a user and the system--e.g., the                     User-to-User Leakage
totality of a dialogue between user and system, be­
ginning when the user logs on and ending when he                          Allocation, use, and erasure of storage resources
logs off. The capability for specifying security param­                 ofall types in the computing system shall be handled
eters as a declaration covering a set of interactions                   both by the system and by operational procedures in
is provided in order that the user not be burdened                      such a way that no information from a prior use of
with specifying security information more often                         the storage medium can leak to the current use.
than absolutely necessary.                                              Comment: The consequence ofthis recommendation
Comment: The requirement that the security                              is to require that appropriate schemes for manage­
parameters be specified before the system will accept                   ment of storage allocation and erasure of storage be
information is simply a fail-safe mechanism to avoid                    incorporated into the system software and system op­
oversight on the part of a user. It is reasonable that                  erational features. The problem of leakage concerns
the system assist the user by asking him in turn for                    both complete and fragmentary pieces of informa­
level of classification, codewords, dissemination la­                   tion, and entire as well as partial quantities ofstor­
bels, and information labels (as applicable). Where                     age. For example, the scratch space on a magnetic
possible, the system should automatically apply any                     disc assigned to one classified job must be satisfac­
caveats, labels, etc., implied by information already                   torily sanitized before assigning it to a second job.
supplied. It is also reasonable that, on request, the                   The problem of leakage would be greatly facilitated
system provide the user with a listing oflabels so that                 if magnetic tape transports contained a rewind-and­
he can assure himself that nothing has been over­                       erase feature, and magnetic discs a read-and-erase
looked.                                                                 feature.

Information Output                                                      Residual Information
   Each user shall be notified of at least the classifi­                   A storage medium shall carry the same classifica­
cation level and special access caveats ofall informa­                  tion as the most highly classified information stored
tion being furnished him by the system. Where                           on it since the most recent sanitization. All sanitiza­
physical limitations prohibit or discourage presenta­                   tion (e.g., degaussing) shall be done in such a way as
tion of all caveats and labels associated with each                     to insure that even if the medium were removed

                                                             21

                                               ,-..~L   lr-lr""""'''.r-llrr.   1......-1   J.   I
from the computing system and subjected to tests                major changes or correction of failures.
under laboratory conditions, no residual informa­               Comment: The problem of certifying that a com­
tion could be extracted from it. The alternative to             puter system contains a properly functioning set of
sanitization is to treat the storage medium as clas­            security safeguards and is operated under an appro­
sified until destruction.                                       priate set of operational procedures is complex and
   This requirement does not imply that all infor­              difficult. The issue is considered at this point in con­
mation read from a storage device must be treated as            nection with policy and operational recommenda­
if it were classified to the highest level of any data          tions, but is also discussed later in the context of
ever recorded on the medium. Information extracted              hardware recommendations. The precise details ofan
from the device by normal means (e.g., via the com­             adequate certification procedure, including the neces­
puter system) may be properly handled at the clas­              sary inspections and tests, are difficult to define, al­
sification of the information per se, provided, how­            though it is clear that the details ofsuch procedures
ever, that all other criteria that relate to handling of        will depend, in part, on the type of computer system
information at that classification level are satisfied.         in question, and on the scope and type ofservice that
                                                                the system furnishes its users. System certification is
Sanitization Procedures                                         the crucial process in establishing the classification
                                                                level permissible in a secure system.
  The specific techniques and tests required to in­
mre sanitization ofstorage media, as required in the              Certification of an overall system, determined on
)receding paragraph, shall be at the discretion of a            the basis of inspection and test results, shall be cha­
Responsible Authority.                                          racterized in terms of the highest classification or
                                                                most restrictive specific special-access categories
Comment: Currently, there is no sanitization tech­
                                                                that may be handled. Where tests show that the
'lique or equipment generally available that will con­
                                                                overall system can effectively maintain the integrity
~istently degauss any and all media so thoro.ughly
                                                                ofboundaries between portions ofthe system, certifi­
~hat residual information cannot be extracted under
                                                                cation may differ for various portions (i.e., for "sub­
~pecialized laboratory conditions. Additional re­
                                                                systems").
~earch and testing are needed to determine the valid­
:ty of various procedures now used, and· to develop             Comment: This recommendation establishes a con­
'lew procedures, equipment, and tests. It is recom­             venient way to characterize the certification of a sys­
nended that research continue, and, to the max­                 tem or portions of it. By permitting certification to
 :mum extent possible, that duplication of efforts be           differ for portions of a system, we have in principle
 woided. Results should be made available through               permitted part of a system to function in an uncer­
 ~he Department of Defense. Meanwhile, responsible              tified condition, but subject to tests that demonstrate
 zuthorities must have leeway to select the degaussing          that the system can effectively maintain the integrity
 ~echnique proven best for the particular media under           of subsystem boundaries. It is not certain at the pre­
 ~heir control.                                                 sent time that tests can adequately establish the in­
                                                                tegrity ofboundaries, thus permitting inclusion ofan
                                                                uncertified portion in a system. In general, the more
 VIII.   SYSTEM CERTIFICATION                                   highly classified and sensitive the information in a
                                                                system, the more carefully one should consider the
    Certification is the process of measuring, testing,         risks before permitting an uncertified portion to oper­
 md evaluating the effectiveness of the security con­           ate in the overall system.
 .rol features of a system. It must be accomplished
 >efore a system can be used operationally with clas­           Tests and Inspections
 :ified information. The three types of system certifi­
 :ation are Design Certification, performed before                 Any computer system used to process classified
  md during system construction; Installation Certifi­          information shall be subjected to inspection and test
 :ation, performed prior to authorizing a system for            by expert technical personnel acting for the Respon­
  1perational use; and Recertification, performed after         sible Authority. The extent and duration of the in­

                                                           22
spections and tests shall be at the discretion of the          vironment supplements and complements hardware
Responsible Authority. The inspections and tests               and software safeguards, and that physical safe­
shall be conducted to determine the degree to which            guards are appropriate. It is anticipated that certifi­
the system conforms to the requirements here                   cation review will be most extensive and thorough at
recommended, any derivative regulations, and other             the time ofinitial installation ofthe system. Installa­
applicable regulations.                                        tion certification will probably be conducted by a
Comment: This recommendation does not specify                  special team, not necessarily under the control ofthe
the details of tests and inspections to be conducted,          Responsible Authority. Ideally, the System Security
nor does it specify when such tests and inspections are        Officer will participate in this certification so that he
necessary. Furthermore, it does not prohibit the Re­           becomes familiar with the safeguards in the system
sponsible Authority from using expert technical per­           and with the process and intent of certification in
sonnel from an external agency or department. On the           ordP.r that he can conduct subsequent certifications.
contrary, some of the tests and inspections should be             Recertification. Some level of recertification
conducted by an external group. Where the sensitivity          must be accomplished periodically, as indicated by
of the information in the system warrants, some of             operational circumstances. These instances are as
the tests, inspections, and deliberate diagnostic at­          follows:
tempts at penetration should be conducted on an                   Periodically during the operational life. It is
unannounced basis. It is not implied that the extent              desirable to recertify the system at intervals dur­
and nature of the tests and inspections necessarily be            ing its lifetime. This is in the nature of a preven­
the same for each of the types ofsystem certification.            tive procedure to establish the continuity of
                                                                  security safeguards, to make gross checks on sys­
Types of System Certification                                     tem functioning, and to search for loopholes in the
                                                                  protection. It is conceivable that some level of
    Design Certification. A series of tests and in­               recertification might be desirable at the beginning
spections that establish that the safeguards designed             of each scheduled shift of operation or on some
into the hardware and software of the system are                  other periodic basis, as dictated by the needs or
operative, function as intended, and collectively con­            sensitivity of the computing installation.
stitute acceptable controls for safeguarding clas~
sified information. Production models of a given de­              After system malfunction. Depending upon how
sign need be tested only to verify that all safeguards            the system has malfunctioned and on what
are present and properly functioning. It is recom­                remedial action has been taken, some recertifica­
mended that this certification be performed by an                 tion procedures are desirable to re-establish that
agency or a special team not part ofthe using agency              the security controls are fully functioning. The
and separate from design or maintenance groups.                   responsibility for determining which recertifica­
Specifications (procedures, tests, inspections) for               tion tests and inspections are necessary rests with
subsequent certification reviews must be produced                 the System Security Officer, although he may so­
as part of the design certification process.                      licit expert opinion from System Maintenance
   Installation Certification. A series of tests and              Personnel or the System Administrator.
inspections performed according to specifications es­             After scheduled or unscheduled hardware or soft­
tablished during the design certification phase to in­            ware maintenance or modification. As with system
sure that the required set of security safeguards                 malfunctions, some level of recertification un­
(hardware, software, and procedural) are in fact pre­             doubtedly is necessary after modifications have
sent and operational in the installed equipment, and              been made in the computing equipment or the
on all communication links that will carry classified             system software. The scope and depth of these
information to remote terminals or other computers.               tests and inspections should reflect what mainte­
This certification must also examine the operational              nance has been performed and what changes have
procedures and administrative structure of the                    been made. The ultimate judgment as to which
organization that controls the equipment, and must                recertification procedures are necessary must be
establish that the procedural and administrative en­              the responsibility of the System Security Officer,

                                                          23
  although he may solicit expert opinion. For suffi­             mation is permissible without the need for recertifi­
  ciently extensive modifications or maintenance,                cation as long as precautions (escorting, continuous
  the recertification procedure may well approxi­                surveillance to prevent tampering, etc.) are taken to
  mate the extensive set of tests and inspections                prevent subversion of the security mechanisms
  made at the time of initial installation.                      needed (and previously certified as effective) to pro­
Comment: The Task Force does not recommend any                   tect the stipulated classification of the terminal.
oarticular recertification periodicity, but suggests             Comment: The impact of this recommendation on
that initially, at least, the question ofperiodic inspec­        the clearance specified for a remote terminal is com­
tion and recertification be jointly determined by the            plex. In effect, it requires that the clearance assigned
System Security Officer and the Responsible Au­                  to a given terminal be determined by appropriate tests
thority. As each acquires confidence in the capability           and safeguards that are commensurate with the
Jf the system to maintain satisfactory security con­             highest classification of information to be handled.
trol, it is likely that the intervals between tests and          Temporary operation of the terminal with informa­
-ecertifications will be adjusted accordingly.                   tion ofa lower classification is acceptable, providing
4.utomatic internal selftesting pr~wiously described             that adequate measures are taken to maintain the
:an be regarded as a form ofrecertification that takes           integrity of the certified status of both the terminal
Jlace on a short time scale (e.g., milliseconds), as op­         and its environment. There must be safeguards that
Josed to the type discussed above which occurs on a·             insure that the system responds to each user appropri­
~ong time scale (e.g., hours, days).                             ately to his clearance, and tests must be applied dur­
                                                                 ing the various certification phases that verify the
                                                                 presence and efficacy of these protection mechanisms.
)perational Security Parameters                                  Extra precautions must be taken before and after the
                                                                 use of a terminal by an uncleared person. Following
  The necessary operational security parameters of               use of a terminal by a person not cleared to receive
he overall system, or of each portion of it, shall be            information classified equivalent to the terminal's
nserted into the system by the System Security                   maximum clearance, authentication ofa new user is
)fficer.                                                         mandatory before initiating transactions involving
":omment: This recommendation is consistent with                 higher classifications. In establishing his authen­
'he view that the security apparatus of the agency               ticity, the new user is also tacitly indicating that the
'hat operates a computing system has the necessary               former user is no longer in a position to monitor the
1verall view to be able to specify the relevant security         higher classification transactions.
 )arameters for the system. The recommendation also
·eflects the requirement that the System Security                Post-Certification Changes
 )fficer be responsible for the currency and accuracy of
 he parameters in his system. The point is included                 Changes in the hardware or software of the sys­
 ts part of certification because proper tests and in­           tem shall be installed for normal operations only by
 pections must be conducted in order to ascertain that           the designated System Maintenance Personnel or
 he security parameters have in fact been correctly              personnel operating under their observation and
 nserted into the system (and accepted by it), both              supervision, with the concurrence of the System
 nitially and each time the security parameters ofthe            Security Officer. An explicit report of all such
 ystem are modified.                                             changes shall be made to the certifying authority for
                                                                 the particular system, in addition to the normal
                                                                 manual and/or automatic logging ofsystem transac­
,rotection at Boundaries                                         tions.
  Information shall be passed to or accepted from                Comment: This recommendation requires explicit
 ny portion of the system only at a security level               reporting of all changes in system hardware or soft­
 ommensurate with the security parameter for that                ware. If such changes are sufficiently minor i17- the
 ortion of the system. The use by an uncleared per­              opinion of the System Security Officer or the System
 on of a terminal certified for highly classified infor­         Certifier, then reporting may be sufficient. However,

                                                            24
if, in the opinion of the System Certifier or the System        guard against the implantation of intelligence sen­
Security Officer, the changes are sufficiently major            sors or software changes that might aid penetration
that security safeguards may have been affected, then           ofsafeguards. Note that it does not require the items
some level of recertification tests and inspection will         to be classified, nor does it require physical protection
be essential.                                                   for all copies of an item. For example, several copies
                                                                (e.g., on card decks or magnetic tapes or discs) of the
Continuity of Physical Protection                               operating system software will usually exist. Only
                                                                that copy to be inserted into the machine for actual
   Equipment and associated materials (e.g., media              running of the system and the master copy from
containing copies of programs) used for handling                which it was made must be physically protected as
classified information must be continuously pro­                required; even then, protection need commence only
tected against unauthorized change commensurate                 after a copy has been certified to be correct. Other
with the security level at which they most recently             copies, which are for the convenience ofmaintenance
have been certified. Copies of operating ·software              personnel or system operators and which will not be
that is not itselfclassified and which is not to be used        used to make additional copies or used operationally
for actual insertion into the system or to generate             in the system when it contains classified information,
programs for insertion into the system need not be              need not be protected. This recommendation should
subject to this requirement.                                    also aid in avoiding unnecessary classification of
Comment:     This recommendation is intended to                 equipment or software.




                                                           25

                                               rll"-.ICif"'\Ct\.ITI A I
                                                  Part C
                      TECHNICAL RECOMMENDATIONS


I. INTRODUCTION                                            wholly different but realistic environments. From a
                                                           technical point of view, a secure closed system (i.e.,
    It is important to understand what present tech­       one acceptably resistant to external attack, acciden­
nology can and cannot do in protecting classified in­      tal disclosures, internal subversion, and denial ofuse
formation in a resource-sharing system. Present            to legitimate users) while presenting difficult prob­
technology offers no way to absolutely protect infor­      lems, can be provided by contemporary technology;
mation or the computer operating system itselffrom         but a secure open system cannot be provided by con­
all security threats posed by the human beings             temporary technology. In fact, there is special con­
around it. As a consequence, procedural and ad­            cern about the risk ofcompromise ofclassified infor­
ministrative safeguards must be applied in resource­       mation and the vulnerability of an open system to
sharing computer centers to supplement the protec­         potential penetrations because, as of today:
tion available in the hardware and software.
    As could be observed in the policy recommenda­           (a) It is virtually impossible to verify that a large
tions, there are two types of environments in which              software system is completely free of errors
secure computing systems operate. One is an envi­                and anomalies.
ronment consisting of only cleared users who func­           (b) The state of system design of large software
~ion at physically protected terminals connected to              systems is such that frequent changes to the
a physically protected computing central by pro­                 system can be expected.
 cected communication circuits. The main security            (c) Certification of a system is not a fully deve­
 problem in such a closed environment is largely one             loped technique nor are its details thoroughly
 )f maintaining the data and program integrity of                worked out.
 ~ach individual user. An inadvertent divergence of          (d) System failure modes are not thoroughly un­
 ~lassified information by the system is analogous to            derstood, catalogued, or protected against.
 i cleared person finding a classified document for
                                                             (e) Large hardware complexes cannot be abso­
 IY'hich he is not authorized access. The other type of          lutely guaranteed error-free.
 mvironment is one in which there is a mixture of
  mcleared users working at unprotected consoles              Since adequate controls cannot be provided by
 :onnected to the computing central by unprotected         technology alone, it is necessary to rely on a combi­
  :ommunication circuits, and cleared users with pro­      nation of hardware, software, and procedural safe­
  .ected consoles and protected communication lines.       guards. Thus, some of the recommendations below
  Phe security problem with such an open environment       refer to issues already discussed in Part B.
  s that the system must be able to withstand efforts         The precise mix ofcontrols and safeguards neces­
  o penetrate it from both inside and outside.             sary in any given case will depend on the operational
    For purposes of this Report, the terms closed sys­     environment, sensitivity of information, <;lass of us­
  ·em and open system are used to indicate security        ers, and types of service rendered, as noted above.
   ontrolled computing systems that operate in these       We believe that these recommendations are both

                                                      26
necessary and sufficient for a closed secure system.                        relevant hardware features greatly simplifies the
However, their sufficiency for an open system cannot                        achievement of isolation. It is recommended that
be guaranteed in the abstract. Only by intelligent                          hardware user-isolation mechanisms be required for
adaptation to a specific open environment utilizing                         all resource-sharing systems ofTypes I, II, and III (in
experience from closed systems and by extremely                             Fig. 2).
objective and stringent testing and evaluation can                             It is recommended that isolation hardware be
their adequacy be established for a specific open sys­                      mandatory in systems that provide extensive pro­
tem.                                                                        gramming capability to the user in any language
                                                                            and with any compiler of his choice, including the
                                                                            machine language of the computer (Type IV in Fig.
II. CENTRAL PROCESSOR                                                       2).
HARDWARE                                                                       While many contemporary machines designed
                                                                            for multiprogramming or time-sharing environ­
   Central processor hardware must provide some                             ments incorporate hardware safeguards that pro­
or all ofthe following mechanisms, depending on the                         vide user isolation, there is very little internal hard­
class of service it renders its users: user ·isolation;                     ware self-checking to guard against malfunctions.
supervisory software 1 protection; and assurance                            Older machines operating in a security controlling
against unanticipated conditions.                                           mode may not be able to fully meet these recommen­
                                                                            dations. To some extent, user isolation achieved by
User Isolation Mechanisms                                                   means of hardware mechanisms can be exchanged
                                                                            for isolation via software mechanisms. This should
    Each user (or worker) program 2 must be isolated
                                                                            be done with caution, for the protection mechanisms
 from all other programs in the computing system.
                                                                            effected by software-means must themselves be safe­
 The currently known principal hardware mech­
                                                                            guarded against collapse due to a hardware or soft­
 anisms for isolating programs include base-address­
                                                                            ware malfunction.
 ing registers and various forms of hardware check­
 ing circuits to assure that memory addresses gener­
 ated within the processor are in fact restricted to                        Supervisor Protection
 those permitted for the programs of a particular
                                                                                The objective of Supervisor protection is to deny
 user. In addition, some contemporary machines pro­
                                                                             a user program the ability to penetrate the Supervi­
 vide memory protection through length-check regis­
                                                                             sor (which contains security control safeguards)
.ters, bounds registers, and storage locks.
                                                                             without detection by the Supervisor. A user program
    The characteristics of the system software deter­
                                                                             might attempt such a subversion for the purpose of
 mine whether or not user-isolation hardware fea­
                                                                             manipulating supervisory information in such a way
 tures are required on systems that provide the user
                                                                            'as to disable security control barriers, or to pre-empt
 with a file-query capability (Type I in Fig. 2), or with
                                                                             the system and so deny service to other users.
 full programming capability through an interpre­
                                                                                It is recommended that computer systems that
 tive mode or in a restricted set of languages with
                                                                             provide for programming via interpretation or via
 checked-out compilers; (Types II and III in Fig. 2).
                                                                             limited languages and checked-out compilers, and
 Sometimes, the hardware features are not necessary
                                                                             systems that provide extensive programming
 in principle, but as a practical matter the use of
                                                                             capabilities (Types II, III, and IV in Fig. 2), incorpo­
    'Supervisory software, or the Supervisor (also called the Ex­
                                                                             rate hardware techniques that have the effect of pro­
ecutive or the Monitor) includes that portion of the software that           viding at least two distinct operating states: the user
internally manages job flow through the computer, allocates sys­             state and the supervisor state (also called worker or
tem resources to jobs, controls information flows to and from files,
etc.                                                                         slave, and master or privileged, respectively). Any
   2
     User program (or worker program) is a computer program                  hardware configuration is acceptable if it can create
that performs some task for a user of the system. The Supervisor             one internal operating state that cannot be pene­
handles scheduling of the user program into the job stream of the
system, the allocation of resources to it, control of its security
                                                                             trated by·any software that a user program can exe­
aspects, etc.                                                                cute.

                                                                       27
   In the supervisor state, the machine is able to exe­         ute, for example), but imposing a shorter delay (10
cute all instructions, including those which affect             seconds, for instance) if he has stated that he is in a
security controls. In the user state, any instruction           debug mode and this statement has been verified by
that initiates an input or output operation (such as            the System Security Officer; imposing successively
a reference to a file), that attempts to modify a regis­        longer delays on the user as the frequency of his in­
ter used to isolate users or to protect the Supervisor,         fractions increases; notifying the System Security
or that attempts to suspend or modify security con­             Officer when a user has exceeded a certain number of
trols must not be executed. Thus, in the user state,            violations.
a user program will not be able to execute certain
instructions and operations that are prohibited to it.          Assurance Against Unanticipated
Entrance to the supervisor state must be hardware
                                                                Conditions
controlled. This frequently is established by pro­
viding a facility to detect a special instruction, and             Since it is virtually impossible to determine in
creating by hardware means an interrupt signal                  every situation whether a computing system is work­
that returns the computing system to its supervisor             ing as designed, it is obvious that a machine not
state.                                                          operating properly is not only ofdoubtful utility, but
   If a user program attempts to execute a prohib­              also poses a grave risk to the security ofthe informa­
ited instruction, the attempt must be thwarted by               tion being handled by it. Thus, it is desirable to incor­
immediately suspending the user program and re­                 porate safeguards that protect the system against
turning control to the Supervisor. Furthermore, if a            unanticipated conditions that might arise. As a
user program attempts to execute an undefined in­               minimum condition, it is mandatory that the com­
struction, this too must be thwarted by immediately             puter produce a known response to all possible in­
suspending execution of the user program and re­                structions (both legal ones specifically in the ma­
turning control to the Supervisor.                              chine repertoire, and undefined ones), together with
Comment: There are two technical points involved                all possible combinations of tags or modifiers,
in this recommendation, as well as a delicate ques­             whether legal or not.
tion of balancing tight security control against user
service. A user program may accidentally attempt to             Comment: This condition is required to prevent the
execute a prohibited instruction because the user has           exploitation of undefined instruction bit patterns
made a mistake in his programming; similarly, a                 that might by-pass normal isolation and protection
sequence of instructions in a user program can inad­            mechanisms.
vertently create a "false instruction," one whose bit­
                                                                Summary Comment: There are many other hard- ·
pattern is undefined in the machine,· this can give rise
                                                                ware features that are not absolutely essential for
to unpredicted results, including bypassing security
                                                                implementing security controls, but which can help
safeguards. As an aid to the Supervisor in determin­
                                                                protect against certain threats or can increase the
ing which event has occurred, it would be convenient
                                                                assurance that controls are working properly and
for the hardware to generate unique interrupt signals
                                                                have not been inadvertently by-passed. For example:
for each. Conversely, a user program can deliberately
create either of these actions as part ofa penetration             Program-readable status switches on the hard­
attempt.                                                           ware can assure that the program is aware of the
                                                                   hardware configuration in which it resides. This
From a security point of view, the safe thing is to
                                                                   feature can protect against loading of the wrong
suspend execution of the user program whenever it
                                                                  ·software, and against some actions ofthe operator.
behaves suspiciously. However, if the user is attempt­
ing to debug a program, he is likely to have errors in            Key switches on all important peripheral-device
his program that will result in his suspension, and               controllers can protect against accidental change
consequently interfere with his work. Possibilities for           in their status or in security safeguards.
handling this conflict include imposing a time delay              Program-readable hardware clocks assist in con­
on the user before allowing him to continue (one min­             trolling and maintaining audits and recording ac­

                                                           28
  tions by date and time.                                       other errors. As recommended earlier with respect
  An interrupt system can give first priority to hard­          to hardware, language processors should provide to
  ware errors, malfunctions, and undefined instruc­             the maximum extent possible known responses for
  tion bit patterns.                                            various error conditions.
                                                                Comment: This discussion applies only to the struc­
                                                                ture of the software components. Additional safe­
III.   SOFTWARE                                                 guards against misuse ofthe software or malfunction
                                                                by it can be incorporated with appropriate procedural
   The software of a resource-sharing system in­                controls. Examination of the software is really an
cludes the Supervisor, the language processors (com­            aspect of certification and it is conceivable that, be­
pilers, assemblers, etc.), the program library, and the         cause ofthe technical expertise implied, examination
utility programs (e.g., sort programs, file copying             and testing ofsoftware can most efficiently be done by
programs, etc.). The design of a computer system                a certifying group.
must consider all software components of the sys­
tem, as well as the hardware on which the software
will run.                                                       Supervisor Program
                                                                   The detailed structure of the Supervisor for are­
Language Processors and Utility Routines
                                                                source-sharing computer system is a function of the
   While a Supervisor ofsome sort is required on all            hardware configuration and of the type of service
types of systems enumerated in Fig. 2, the broad                provided by the system to its users. Because of the
range of user software capabilities inherent in sys­            variety of Supervisors and the fact that most re­
tems of Types III and IV implies that a much more               source-sharing systems are delivered by the manu­
complex Supervisor is required for them. With re­               facturer with a Supervisor, it is difficult to specify
spect to language processors and utility programs,              requirements in detail. In general, however, the soft­
very little can be said that will be ofassistance in the        ware design should be clean, in the sense that it is
design and development of secure resource-sharing               as modular as possible. There are some aspects to
systems. In a Type III system (permitting program­              Supervisor design that are sufficiently important to
ming via limited languages and certified compilers)             qualify as requirements.
the care and thoroughness with which the language                  It is recommended that Supervisors designed for
processors are examined prior to approval can limit             a resource-sharing system include the following fea­
the threat that a user of the system might be able to           tures:
mount against the classified information it contains.
A careful analysis of all language translators, and               1.    As much of the Supervisor as possible must
particularly the assumptions that have been made                run in the user state (as opposed to the supervisor
regarding the execution environment of user pro­                state); each part of the Supervisor should have only
grams, is essential on all four types of computing              as much freedom of the machine as it needs to do its
systems.                                                        job. This should provide the Supervisor more protec­
   Assembly languages and the processors for them               tion than is given to user programs against faulty
impose a particularly difficult problem because of.             programming or machine errors. Supervisor func­
the manifold opportunities for the user to create               tions should be separated into individual, self-con­
seemingly safe instruction sequences that, in turn,             tained modules with explicit communication3 be­
construct executable instruction sequences designed             tween modules. Each module must be fully described
to disrupt service or to by-pass security controls in
the operating system. Little more can be said about
                                                                   "For example, we would discourage writing a subroutine that
language processors or utility programs except to               on its own initiative reaches into another subroutine for informa­
require that they be thoroughly tested by the user              tion without the knowledge of the second one. We would insist
                                                                that some communication require that the first module ask infor­
agency for correct operation and for detection and              mation from the second, and that the exchange take place in an
rejection of incorrect sequences of instructions or             information-exchange area within neither.


                                                           29
with flowcharts to assist in its security analysis. 4                     tures as automatic logging out of users and access
   2. The Supervisor must assure, to the extent                           closure to all files ofclassified information). Further­
technically feasible, that no classified information                      more, it must be possible for system personnel, work­
can remain as program-accessible residue in either                        ing at a control console, to pre-empt selected users or
primary or secondary storage. This includes all                           to deny access to a given user or terminal (e.g., if an
forms of secondary storage (magnetic drums, mag­                          attempt to access the system with improper authori­
netic discs, magnetic tapes), as well as the primary                      zation has been detected).
core store and all registers. One technique is to have                       4. The Supervisor must have a certified capabil­
the Supervisor erase any segment of primary (core)                        ity to control access to files. This point is so critical
storage before making that segment available to an­                       that it is treated separately below.
other program.
                                                                          Summary Comment: The detailed design of the
Comment: For systems with sufficiently small                              Supervisor and the protective safeguards that it con­
amounts of secondary storage, the requirement to                          tains and that are afforded it are vital to adequate
erase-before-reuse will not be burdensome, but sys­                       security control. Since commercially designed Super­
tems with voluminous secondary storage will suffer                        visors and operating systems have not included
in terms of efficiency. A possibility for handling the                    securlty control, it is to be expected that the average
situation (which, however, may be costly in terms of                      commercial software will not provide the standards,
system efficiency) is as follows. If the user program                     conventions, and capabilities required. A number of
requires some temporary secondary storage, the                            potential design guidelines are suggested here.
Supervisor can keep track ofhow much of the store is
assigned, and also of how much information ha8 ac­                        The Multics time-sharing software 5 utilizes the con­
tually been transferred into secondary storage. Subse­                    cept ofconcentric circles ofprotection. The most sensi­
quent read-out of such information by the user pro­                       tive part of the Supervisor (sensitive in the sense that
gram will be restricted by the Supervisor to only that                    penetration of it will open the machine completely to
volume that has been written. This procedure can be                       the user) is conceptually at the innermost circle. Sur­
applied to so-called scratch tapes or disc space. It                      rounding it in successive rings are decreasingly sensi­
should be noted, however, that tapes, drums, or discs                     tive parts of the Supervisor. A user program seeking
controlled in this fashion must be classified and pro­                    access to some portion of the Supervisor must specifi­
tected appropriately for the highest level ofclassifica­                  cally thread its way through the concentric rings un­
tion of the information written on them until erased                      til it reaches the desired portion. Thus, there is no
by an acceptable method. Any arrangement that gua­                        direct route from a user program to, for example, the
rantees that a user program cannot read secondary                         file-access control mechanism.
storage beyond material that it wrote originally                          In the case where the Supervisor is responsible for
avoids unnecessary erasure ofsecondary storage, and                       data segregation, it must check the authority of ter­
also unnecessary computer-erasure of the informa­                         minals that originate traffic, must properly label (in­
tion. This issue is one which requires attention in                       ternally) all traffic, must label all tasks whose execu- .
future machine designs; features such as bulk-eras­                       tion is required in order to service a user request, must
ure ofmagnetic discs will be valuable in maintaining                      keep track of all tasks and of the programs that exe­
system efficiency.                                                        cute them, must validate the security markings (in­
                                                                          cluding security flags) on all tasks and control access
  3. The Supervisor must have provision for bring­                        to files on the basis of the markings, and must vali­
[ng the computing system into operational status in                       date (by reference to internal tables or files) the au­
m orderly manner. There also must be provision for
>rderly shutdown of the system (including such fea­
                                                                              •v. A. Vyssotsky, F. J. Corbato, and R. M. Graham, "Structure
                                                                          of the Multics Supervisor," AFIPS Conference Proceedings, Vol.
                                                                          27, Part 1, Spartan Books, Washington, D.C., 1965, pp. 203-212;
    4
      For an example of this type of design and the level of docu­        also R. M. Graham, "Protection in an Information Processing
mentation required, see the software maintenance documenta­               Utility," Communications oftheACM, Vol.ll, No.5, May 1968,
tion for the GE 625/35 GECOS III time-sharing system.                     pp. 365-369.


                                                                     30
thority ofa remote location to receive output informa­           IV. ACCESS CONTROL
tion with a given security marking or flag.                      THROUGHOUT THE SYSTEM
The system programs that collectively form the
Supervisor must not be allowed to execute with com­                 In a resource-sharing computer system, access to
plete freedom of the machine. Ideally, such system               the system itself and access to the information (files
programs should execute only in the system's user                and programs) contained in the system must be sepa­
state; otherwise, these programs should execute with             rately controlled. Iftheresource-sharing system is a
as many restrir.tions as possible. Only the minimum              multiprogrammed computer operating with only lo­
number ofsystem programs should be allowed to exe­               cal (as opposed to remote) access, operations person­
cute without any restriction. Relaxation of this                 nel can visually ·identify an individual before grant~
philosophy in order to facilitate execution ofa system           ing him access to the system. Furthermore, the oper­
program can lead to a serious weakness in security.              ations people can perform whatever verification pro­
                                                                 cedure is necessary before releasing particular files
An essential aspect of access control is the security
                                                                 or programs to that user. Alternatively, if such user
flag that identifies the classification level of the pro­
                                                                 information as authentication words or access proto­
gram, the data, the terminal, and the user. The basic
                                                                 cols must be protected when in punchcard form, an
philosophy ofa program executing in the user state is
                                                                 arrangement can be made to have the card deck read
that it is able to process anything that it has availa­
                                                                 under the visual surveillance of its owner, and im­
ble within the region of core memory (or logical ad­
                                                                 mediately returned to him. For remote batch and
dress space) assigned to it. Thus, satisfactory security
                                                                 resource-sharing computer systems, such functions
control depends upon careful monitoring and control
                                                                 must be performed by security-controlling mech­
of what a user program brings within its memory
                                                                 anisms in the system software and hardware.
region (physical or logical). Specifically, it must not
be allowed to bring security flags into its region. Ifan
unusual program has the privilege of writing outside             User Access
its core region, it can in principle modify security
flags. Obviously, such programs must be carefully de­               In a terminal-oriented system, a user must an­
signed and must be faultless.                                    nounce himself to the system through a log-on pro­
                                                                 cedure that requires standard identification and ac­
Since system programs are very sensitive with respect            counting information, and a specific user authentica­
to security controls, they must be carefully debugged            tion step so that the computer system can verify the
before becoming resident in the permanent program                identity of the individual at the terminal. For sys­
library. Those of particularly high sensitivity, such            tems that have point-to-point permanent and pro­
as routines for controlling access to classified files,          tected communication links, physical control of ac­
must be given extraordinary attention during the                 cess to a terminal may be used in lieu of authentica­
debugging phase.                                                 tion. In this case, responsibility for authentication is
It is desirable that system programs which have                  transferred to the administrative jurisdiction which
unusually broad capabilities (such as being able to              has cognizance over the terminal. For systems that
access all permanent files in secondary storage or in            utilize dial-up communication links, or in which ·
temporary working stores) be programmed so as to                 physical access control is undesirable, a password
print console messages notifying the System Opera­               scheme or its equivalent must be used to provide
tors of the specific privileges being extended; before           authentication.
proceeding to implement such privileges, the system                 Authentication words or techniques must be clas­
should require explicit permission. All such events              sified and protected by the user in accordance with
should be logged automatically, together with the                the highest level of information to which it permits
operator's response and, when deemed necessary, the              him access. Authentication words or techniques
concurrence of the System Security Officer. This re­             must be obtained from an approved source, or, alter­
striction is a double check to prevent unauthorized              natively, must be generated and distributed under
execution of broad-capability programs with mali­                the cognizance of the System Security Officer by ap­
cious intent.                                                    proved techniques. Specifically, a user cannot gener­

                                                            31
ate his own passwords. Depending on the sensitivity             of the total security structure with which his system
ofinformation or operating conditions (circuit noise,           must deal, as well as a means for inserting security
interruptions, etc.) contained within a system, a user          parameters into the system.
may be required to reauthenticate himself from time             In addition to the security reasons for controlling
to time during a single terminal session. Authentica­           access to files, it is necessary also to control access so
tion words must be changed as frequently as pre­                that unauthorized changes cannot be made, particu­
scribed by the approved issuing source.                         larly ifthe file management responsibility is assigned
   Provided that techniques approved by the appro­              exclusively to some individual or group-e.g., the
priate cognizant agency are used, the resource-shar­            Office of Primary Responsibility. For example, even
ing system can itselfbe utilized to generate authenti­          though a given user might qualify for access to a
cation words, provided the output is available only at          particular file in terms ofproper clearance and need-·
a designated terminal and that the procedure is car­            to-know, he might be granted access to read it but
ried out under the cognizance ofthe System Security             denied the right to change the file because this privi­
Officer.                                                        lege is reserved to a designated file manager. Thus, in
   The Supervisor software must be so constructed               part, security control and file integrity overlap. Both
that user identification and authentication word                features are essential, and common software can con­
lists can be maintained as part of the normal opera­            veniently accommodate both. 6
tion of the system from the terminal designated for
the System Security Officer who has sole responsibil­
ity for such lists.                                             Denial of Access
                                                                   A user must not be able to acquire information
Information Access                                              about the security controls or the files when access
   The fact that a user is granted access to a system           is denied him for any reason. Assuming inadvert­
does not imply authorization to access classified files         ence on the part ofthe user, the system should assist
of data and programs contained in that system. For              him in identifying his mistakes or procedural errors.
example, he may be authorized to perform only on­               However, the system logs should record all unsuc­
line computation, but not on-line file processing.              cessful attempts to access classified files.
Before a user is given access to a classified file, the         Comment: The point of this prohibition is to guard
user's clearance level, need-to-know, and access                against acquiring incidental information by brow­
privileges must be checked against the access res­              sing. Thus, an improper access request must result in
trictions of that file. If information from this file is        some innocuous reply, such as, "File not found. "
to be delivered to the user's terminal or to a terminal         However, the restriction that the system not reveal
designated by him, the status of the designated ter­            the existence of a file creates a potentially awkward
minal must also be verified. To do this, the computer           situation because the user might inadvertently create
system must have an internal catalog of user clear­             a file (perhaps public and unclassified) with the same
ance levels and access privileges, as well as a catalog         name as one whose existence is unknown to him.
of the characteristics of all terminals connected to            Since different files of the same name are unaccepta­
the system. Each file must be marked with any clear­            ble in a system, the system must (1) inform the user
ance, need-to-know, or other restrictions on its use.           that his proposed name is unacceptable (without giv­
Finally, there must be an explicit and separate capa­           ing a reason), (2) prefix all file names with a user­
bility to update such an internal catalog. If the re­           unique code to guarantee dissimilarity of names, or
sponsibility for maintaining this catalog is divided            (3) use some pseudo-random process to automatically
among several people, each must be restricted to                generate file names.
only that part of it for which he is responsible.
Comment: The Appendix describes a system for im­
plementing a file-access control mechanism. It also                "For example, seeR. C. Daley and P. G. Neumann, "A Gener­
                                                                al-Purpose File System for Secondary Storage," AFIPS Confer­
discusses a scheme whereby the System Security                  ence Proceedings, Vol. 27, Part 1, Spartan Books, Washington,
Officer can describe to the computing system that part          D.C., 1965, pp. 213-229.


                                                           32
Maintenance Access                                              by the System Security Officer. In either case, the
                                                                user's action must be recorded in the system log. If
   Because systems are vulnerable to security                   the classification has been lowered or caveats have
threats posed by operations and maintenance per­                been removed, the file must not be released to other
sonnel, it is strongly recommended that for systems             users before the System Security Officer has verified
handling extremely sensitive information all soft­              that the new status is correct. In some operational
ware and hardware maintenance be performed as a                 situations, it may be prudent to limit downgrading
joint action of two or more persons. ln particular,             authorization to only those users who are entitled to
on-line debugging of the Supervisor software is ex­             write into a file.
pressly prohibited except when (1) all on-line storage             When a new file is created by combining informa­
devices containing classified files not needed in the           tion from existing files and adding interpretations of
performance of the maintenance are physically or                the combined results, it is conceivable that a purely
electrically disconnected, and (2) only fully-cleared           algorithmically determined maximum classification
maintenance personnel have access to the system.                and caveats may exceed the user's access privileges.
   In order to maintain good security control, it is            In such a case, the access control mechanism must
recommended that modification of installed system               be designed to withhold the information from the
software·currently in operation be done from specifi­           user and to bring the situation to the attention ofthe
cally designated terminals; that system software                System Security Officer.
maintenance personnel be assigned unique access
privileges, including authentication words to permit            Comment: The reason for requiring the user to
them access to test files, system functions, etc.; and          confirm or modify the computer-determined status,
that all actions from such specially privileged con­            rather than permitting the user to specify his own, is
soles be under the continuous, positive control of a            that he may not be aware of the totality of all file
responsible individual who maintains a written log              classifications and caveats that he has referenced;
ofthe console use, including positive identification of         thus, he would be unaware ofthe classification status
the individuals using it. Such special hand-main­               ofthe composite information. Classification ofa large
tained logs should be in addition to the automatic              collection of classified documentary information al­
logging performed by the system.                                ways requires extensive manual analysis and evalua­
                                                                tion; a corresponding action on large computer files
                                                                would be unreasonable.
File Classification Determination
   The system can and should be designed to assist              Input/Output Limitation
the user in determining the appropriate classifica­
tion and applicable caveats for each new file. In                 It is recommended that software traps be incor­
many cases, this can be determined algorithmically              porated to detect any input or output information
by the computer through a consideration ofthe clas­             identified by a security flag that exceeds that author­
sifications and caveats of all files referenced, pro­           ized for either the user, his terminal, or any file
grams utilized to create the files, and input~;~. 7 In          specified in his job. Such a condition must immedi­
other cases, it can only be determined by the user.             ately suspend service to the terminal, notify the Sys­
Whenever a user is notified by the system that, based           tem Security Officer, and record the event in the
on internal information, it has assigned a tentative            system log.
classification status for a newly created file, he must         Comment: This implies that all input/output oper­
indicate that he has verified and accepts this status           ations are buffered through a storage area assigned to
or desires to change it. If a user chooses to change            the Supervisor on the way to or from a user program.
the classification, either raising or lowering it, or to        For example, information from a terminal must be
add or remove caveats, the system should record the             moved into buffered storage, its security flag detected
transaction in its log and specially note it for review         and compared with the user privileges, and then it
                                                                must be moved again into the user program area.
    •see the Appendix for one such scheme.                        Typically, the Supervisor is designed to receive

                                                           33
    Clearance                        Classification

                           Input           Job        Output



    User                    >                           >


    1/0 Device              >          Independent      >



*Except for certified execute-only programs.


                            Figure 4




                                34
remote input information only from the terminal                  file data, input, and output. The question of which
that originates the job and, correspondingly, to out­            jobs a user can run in each possible circumstance can
put information only at that terminal. If operational            become very complex. Unfortunately, the Supervi­
requirements dictate otherwise, the Supervisor must              sor will have to determine user privileges algorith­
be so designed that it can identify and authenticate             mical_ly; it cannot exert judgment. Thus, the issue
terminals and users other than the originating one               must be examined carefully in each operational en­
and with which information will be exchanged.                    vironment, with appropriate rules formulated to
                                                                 match user needs and security restrictions of the
                                                                 installation.
Job Security Interaction
                                                                 Comment: A program might be intrinsically clas­
   As a user's job actually runs in the computer,. it            sified because it implements classified algorithms,
will carry a security flag that initially is determined          and, thus, its claSsification establishes a lower bound
from the security flags of the user and of the termi­            when it runs as part of a job. On the other hand, a
nal from which he works unless the user specifically             classified program might access data more highly
designates otherwise at the beginning ofthe job. In              classified, and, hence, the job classification can ex­
either case, as the job unfolds, the security flag may           ceed that of the program that is executing.
have to be modified automatically by the system to
reflect the security flags offiles ofinformation or files        Multilevel Utilization
of other programs that are used. The job flag need
not be limited by the terminal flag. For example, an                It is possible to demonstrate that many resource­
individual cleared for Top Secret might run an en­               sharing computer systems may be safe from direct
tirely Top Secret job through a Secret terminal if               user 'attacks from terminals by proving that a par­
there is to be no Top Secret input or output through             ticular hardware/software component is effective in
the terminal; the output, for example, might be di­              blocking attacks of various kinds. However, there is
rected to a Top Secret printer. A situation such as              the recurring question of the risk ofinadvertent dis­
this might be common for remotely initiated batch                closure of classified information through software,
operations, and no deception is indicated since the              hardware, or a combination of failures; in such a
user is cleared for the job even though his terminal             case; it would be necessary to prove that a single
is not. The basic point is that the security flag of the         failure or a combination of failures cannot occur.
user is the absolute limit on his access privileges,             Since a complete proofofprotection is not within the
unless the program in question has been certified to             present state of the art, particularly for existing
have access to higher security flags but to produce              computer systems, it is recommended that the sys­
information that does not exceed the flag ofthe user.            tem designer estimate the probability of occurrence
   The access control limitation just outlined can be            ofa single failure or the combination offailures that
represented as shown in Fig. 4. It is read: user (de­            could result in a disclosure of classified information.
vice) flag should be greater than or equal to ( > ) the          Based on this information, the Responsible Au­
input (job, output) flag.                                        thority can determine whether the risk probability
   It may prove too difficult in a specific case to cer­         is acceptable or not. If the decision is that the risk is
tify that a program can access highly classified infor­          too great, a segregated mode of operation should be
mation but produce results of a lower level. If so, it           used, and the system certification made accordingly.
is strongly recommended that a user's job never be                   A system functioning in a segregated mode re­
allowed to access information-either data or pro­                quires that all users are cleared to a specified level,
grams-whose security flag exceeds that of the user.              all terminals are physically protected to that level,
Since parts of the Supervisor will run in the user               and all communication lines are secure to that level.
state as a user program, access in such a case to                If, within any level of classification, special caveat
accounting and control files must be excluded from               information is introduced, a new determination
the restriction.                                                 must be made as to whether the risk and conse­
   In principle, the following items can each carry a            quences of exposure of the special caveat informa­
security flag: user, terminal, job program, job data,            tion to cleared but not authorized persons operating

                                                            35
User Clearance                               Current Classification of System

                         Special    Special           Top
                       Access "A" Access "8"         Secret     Secret    Confidential Unclassified



Special Category "A"
                            •                           •""       •""           •""         •
Special Category "B"
                                        •               •""       •""           •""         •

Top Secret
                                                        •         •             •           •
Secret
                                                                  •             •           •

Confidential
                                                                                •           •
Uncleared
                                                                                            •
   • -Access authorized.
   •"" -Access may or may not be authorized, depending on the relation
of the Special Category to the given national classification.



                                            Figure .5




                                                36
within the system warrants segregated operation of                                         formation about the specific classification
the entire system at the special caveat level. If the                                      status ofthe new mode. A change in the mode
classification level at which the system is certified to                                   of operation must be accomplished by recess­
function hierarchically subsumes other levels of                                           ing or logging off, as appropriate, all active
classification, then authorized users of the system                                        users and forcing a new log-on procedure, in­
may execute programs ofsuch lower levels ofclassifi­                                       cluding authentication, for the new level.
cation. However, if the scheduled mode for the sys­                                        A change in the operational status of the sys­
tem establishes a level of classification which is                                         tem will obviously inconvenience users. While
mutually exclusive of other levels, the users are re­                                      some will be required to terminate their work
stricted to programs classified at the current mode of                                     completely; all will be required to momen­
the system. Fig. 5 illustrates these relations.                                            tarily suspend operation until the change in
   The concept of segregated operational modes re­                                         status and the new log-on have been accom­
quires that users of various clearance levels be sche­                                     plished. To the maximum extent possible, the
duled separately. In addition, special controls are                                        procedures for changing the status of the ma­
needed to assure that highly classified or caveated                                        chine should be designed with user conven­
material does not become accessible when a lower­                                          ience in mind.
level classification or differently caveated mode be­                                  (d) Since the operational clearance status of the
gins operation. The precise procedures and mech­                                           system can change in a segregated style of
anisms necessary to change the operational status of                                       operation, any user who is granted access to
a system must be tailored to the precise hardware/­                                        the system must be informed by the system of
software configuration. The following steps are rep­                                       its current status.
resentative of the procedures necessary to maintain                                    (e) When initiating a new operational mode, ter­
segregation when system status changes.                                                    minals in work areas not cleared to receive
                                                                                           the information at the forthcoming level of
   (a) When file information is permanently resi­                                          operation must be disconnected from com­
       dent in the system (e.g., on disc files or mass                                     munication links with the computer (by cer­
       storage devices), the information must be pro­                                      tified electronic switching, unplugging, or
       tected by disconnecting such devices (by cer­                                       manual operation of switches).
       tified electronic switching, unplugging cables,                                 (f) When initiating a new operational mode, any
       or manual operation ofswitches) ifthe classifi­                                     special software relevant to the new mode
       cation or special-access categories of the file                                     must replace that of the previous mode.
       information are such that the file must not                                     (g) In the event of a failure in the Supervisor
       become accessible to unauthorized users un­                                         software or in the hardware resulting in an
       der any circumstances.                                                              operational malfunction, the system must be
   (b) Before a file device is made available to users                                     restarted at the appropriate clearance level
       with more restricted access privileges than                                         by an approved restart procedure as a part of
       those who have been using it, it must be sanit­                                     returning it to operational status in the same
       ized (and checked) by approved procedures of                                        mode. 8 Depending upon the nature ofthe mal­
       any classified information more highly clas­                                        function, it may be necessary to verify the
       sified or restricted in access than appropriate                                     security flags of on-line data files in order to
       to the new mode of operation.                                                       assure that the malfunction did not affect
   (c) Each user must be notified of any change in                                          them.
       the operational status of the system, whether
                                                                                 The recommendations above indicate in a gen­
       scheduled or not. This notification should be
                                                                               eral way what is required; additional issues, such as
       transmitted prior to the change to all active
                                                                               the following, must be considered.
       terminals that will be able to access the sys­
       tem in its new mode of operation. However, a
                                                                                       (a) Indicator lights visible to the operator may be
       terminal not authorized to access the system
       in the new mode should not be given any in­                                           "See Part D.


                                                                       37

                                               , . . . . " " ... lr""l......_.r" ...   ........   .&   •
                                            \.....VI'~riUI:l'l IIAL




      needed so that the status of on-line file media         protected in accordance with Government-approved
      is readily discernible.                                 communication security methods. They may include
  (b) The disabling of read heads of magnetic disc            provision of approved secure cable between the ter­
      devices may be required.                                minal and the central location, or of approved cryp­
  (c) Appropriate key locks may be needed so that             tographic equipment. Intelligent deception of the
      an operator is assured that certain actions             link (i.e., spoofing) must not be possible.
      have been taken; the action of these locks
      must be electrically reported."                         Emergency Communication Arrangements
  (d) Checklists are helpful to assure that system
      operating personnel methodically verify each               There may be an operational requirement to
      step of the process.                                    maintain continuity of service to a remote user in
  (e) Storage of such classified material as punch­           spite of communication circuit failure. If so, there
      cards, printed paper, magnetic tapes, etc.,             must be emergency provisions and procedures for
      must be provided.                                       establishing alternate channels to remote locations,
  (f) Printers or punchcard equipment must be sa­             and such actions must be accomplished by properly
      nitized by running out blank paper or blank             cleared and authorized individuals, in accordance
      cards; ribbons must be changed or protected.            with established operating procedures for secure
  (g) Positive control procedures should be used to           communications.
      assure that magnetic tapes or magnetic disc
      packs containing classified information ofone
      level. of classification or special category are
                                                              High-Risk Areas
      not accidentally used at some other inappro­               If the resource-sharing computer system operates
      priate level.
                                                              in an environment wherein there is a reasonable
  (h) There must be detailed instructions to the              probability ofone or more terminals being captured,
      system operating personnel for each mode,               then it is essential to employ the technique ofcrypto­
      relative to such things as console actions, on­         graphic isolation (i.e., use of a unique key for each
      line file status, memory-clear procedures,              terminal). In the event of capture, this confines the
      mode shut down, mode initiation, message in­            operational and information loss to the captured ter­
      sertion via the console typewriter, etc.
                                                              minal, and prevents the captor from intruding on
  (i) There must be continuous surveillance ofthe
                                                              other communication links in the system and inter­
      operations area by fully cleared personnel.
                                                              cepting classified information intended for other ter­
   It is not possible to consider explicitly all the          minals.
changes that must take place in a computer system
for a change in operational clearance level. In gen­
eral, the recommendations given parallel practices            VI. TERMINALS
common in existing security doctrine. At a particu­
lar installation, the System Security Officer will be
aware ofthe levels ofclassification and special access
                                                              Terminal Protection
categories in his system, and must be able to formu­            Any terminal through which a user can gain ac­
late the detailed procedures for shifting the opera­          cess to classified information in the central comput­
tional mode of the system from one to another.                ing facility must be physically protected in accord­
                                                              ance with the highest classification of information
                                                              processed through the terminal. Furthermore, if
V. COMMUNICATION LINES                                        protection requirements are specified for any crypto­
                                                              graphic equipment collocated with the terminal, the
   Any communication line that passes classified in­          physical protection must be in accordance with the
formation between a terminal and the central com­             protection requirements specified for that crypto­
puter facility or between computer systems must be            graphic equipment. In addition, if the system is

                                                         38
closed, the protection must be consistent with that             sifted information. It is almost impossible to identify
specified for the overall system.                               and protect against all possible failure modes of a
   To guard against the covert emplacement of ille­             system.
gal intelligence sensors or recorders, terminal                     Design certification is the process of measuring,
maintenance personnel must be cleared for the high­             testing, and evaluating the probable effectiveness
est level of classified information handled at the ter­         under operating conditions of the security control
minal, or the terminal maintenance must be per­                 features of a stable system-i.e., one whose software
formed under. surveillance of an appropriately                  and hardware have been completed. In order to
cleared and technically knowledgeable person.                   make the measuring process meaningful, the
                                                                security protection designed into a system must be
Terminal Identification                                         quantified to the maximum extent possible. It is
                                                                stropgly recommended that design certification be
   Because present security doctrine depends                    performed by a group other than that responsible for
heavily upon identification, it is necessary that a             the design, construction, or maintenance of an oper­
remote-access, resource-sharing system require posi­            ational system. A suggested procedure is given be­
tive identification of each terminal with which it             ·low:
communicates, and that the system be able to inter­
rogate a terminal for its identification at any time.             (a) Identify all hardware elements (such as regis­
                                                                      ters, base address registers, counters, etc.)
Comment: Terminal identification is particularly
                                                                      that provide or are depended upon for direct
important when a computing system is being brought
                                                                      operation of a security control function. Iden­
into operational status initially, or when it is being
                                                                      tify all system software features, barriers, and.
recertified as a secure configuration. This recommen­
                                                                      components that have a security control func­
dation also applies to all remote equipment, such as
                                                                      tion. For each of these determine:
other computers.
                                                                      (1) Its logic;
If remote terminals are connected into the central                    (2) Hardware failures that will cause incor­
processor via a dial-up connection rather than perma­                      rect operation and any inherent checks
nent hard wire, this requirement for terminal iden­                        that are intended to detect such failures­
tification may require a separate authentication                           e.g., a parity .check on register-to-register
method despite the use ofcryptographic equipment on                        transfer;
the circuit. This recommendation will also apply to                   (3) The probability of failure of the hard­
the situation in which a user at a terminal connected                      ware upon which a security control de­
to one system wishes to access a second system. In                         pends;
some systems it may be permissible for the user to                    (4) Possible software checks on the consist­
authenticate himself to his own system, which then                         ency of its operations and the accuracy of
passes the authentication to the second system via                         parameters, addresses, etc., used by the
their mutually authenticated and protected com­                            function;
munication link. In other cases, a unique arrange­                    (5) Combinations of data (parameters, ta­
ment may be necessary to enter the second system.                          bles, etc.) that will result in incorrect op­
                                                                           eration;
                                                                      (6) Its dependence on other functions for its
VII.    CERTIFICATION                                                      own operation;
                                                                      (7) The probable effect of its failure;
   Certifying that a resource-sharing computer sys­                   (8) Specific tests-either software or elec­
tem is secure represents a very difficult issue. It in­                    tronic-that can be made to determine
volves an examination ofthe safeguards-hardware,                           if the function really works as specified.
software, procedural, administrative-that have                    (b) Based on the determination of these factors
been provided, and, ideally, a quantitative estimate                  and test results, make an overall estimate of
of the probability of inadvertent disclosure of clas­                 the probability offailure ofthe total function.

                                                          39


                                             r{)"IJ:Jnl=t\.ITI A I
  (c)   Based on the probability of failure of each             (e) Loss of an operator console may require that
        security function, estimate the overall proba­              the associated computer must be shut off if it
        bility of a system security failure that would              cannot be properly controlled, or if alternate
        result in a compromise of classified informa­               locations for operator control are not availa­
        tion or an illegal entry into the system.                   ble.

   The matter of overall equipment configuration                 At the time of installation certification, the ad­
becomes especially important in large systems con­            ministrative and procedural environment in which
taining many computers, either collocated or geo­             the system is to function must be examined to verify
graphically distributed. The overall hardware confi­          that it supports the controls present in the hard­
guration must be examined in order to establish the           ware/software complex, and that it provides the ad­
consequences to the security controls of a total or           ditional controls on the people, paper, magnetic
partial loss of a major component in the system. For          tapes, etc., of the system, Also at installation certifi­
example, if the controller for a group of magnetic            cation, the communications arrangement must be
discs were to fail, it is necessary to determine              verified to be secure, the level of spurious emana­
whether a crucial segment of the software would be            tions must be demonstrated to be acceptable, physi­
made unavailable for security. control. Whenever              cal protection must be shown to be adequate, and all
possible, security controls should be designed so that        controls over remote equipment (physical, person­
failure of a portion of the system does not invalidate        nel, emanation) must be verified.
or weaken the controls in the balance of the system              Complete certification should be performed
remaining operational. Conversely, the design                 before changing a closed system into an open system
should permit rapid and simple physical disconnec­            even though it may be operated in a segregated
tion of an inoperative portion of the system. Follow­         mode, as previously described, when processing
ing are some other points that should be considered.          highly sensitive information. After a system has
                                                              been certified, all changes to the system must be
  (a) If the failed component (such as a magnetic             similarly examined before being incorporated. Such
      drum, a section of core, or a second computer)          an examination is required whether the changes
      contains information required for security              originate with the user-agency or with either the
      control and not available elsewhere in the sys­         hardware or software vendors.
      tem, the entire system must shut down or op­               After the general reliability of a system has been
      erate in a degraded mode. The decision should           established by operating successfully for a reasona­
      be made jointly by the System Security Officer          ble length of time, a limited recertification process
      and the System Administrator.                           should be performed at appropriate intervals, con­
  (b) The loss ofsome components may so seriously             sisting only of tests and inspections intended to re­
      affect the operational performance and ac­              veal changes surreptitiously made in the system, or
      curacy of the remainder of the system that it           to detect inadvertent changes made in the system
      should be shut down for that reason, even               during maintenance, or to validate the continuing
      though significant security controls continue           performance of system security controls.
      to function.
  (c) Loss of communciation between elements of
      the system may force it to be shut down ifdata          Audit Trails
      critical to security control in the system can­
      not be transferred.                                        The audit-trail technique can be used to verify
  (d) If the Supervisor software is designed to               that a system is operating correctly and, more im­
      monitor the operating status of each remote             portantly, that it is being used properly. For pur­
      station before sending information to it, the           poses of monitoring security controls, it is recom­
      loss of a remote station is not a security              mended that the system contain software that au­
      threat, although such incidents must be re­             tomatically records (with date and time) at least the
      ported to the System Security Officer.                  following:


                                                         40
  (aJ All user log-ons and log-offs, including each          gram, and the system reaction. In general, the log
      user's name, identification, and terminal;             should be complete enough to permit the System
  (b) All maintenance log-ons and log-offs for               Security Officer to monitor system performance on a
      whatever purpose, including the names of               real-time or periodic basis, as needed. The data col­
      maintenance personnel, the nature of the               lected by the system log can also be aggregated at
      maintenance, and any files accessed;                   intervals to provide performance statistics that indi­
  (cJ All operator-initiated functions, including            cate the efficacy of existing security safeguards, and
      his name and the function (from the point of           to develop new or improved procedures and controls.
      view of the logs, the operator should be
                                                             Comment: If a system contains unusually sensitive
      treated as a user);
                                                             information or must operate in an unusually hostile
  (dJ Each attempt by a user or his program to ac­
                                                             environment, more extensive automatic logging of
      cess files or programs for which he is not au­
                                                             system activity may be desirable. Furthermore, in
      thorized, including his name, terminal, and
                                                             some cases the presence of special machine instruc­
      an identification of his program;
                                                             tions whose execution might modify or by-pass
  (e) All program-abort incidents, including the
                                                             security controls, or the existence ofan unusual confi­
      name of the program, the user, terminal, and
                                                             guration, etc., might require logging of additional
      time of abort;
                                                             activity-e.g., any use ofa diagnostic instruction that
  (f) Any special usage of the system-e.g., gener­
                                                             can lead to subsequent errors because of change-of­
      ation of passwords, changing of the classifica­
                                                             mode in the machine.
      tion, or modifying security parameters; a re­
      cord of the type of transaction, including the
      authority or person under whose cognizance                Supplementary manual logs kept by the opera­
      the usage is conducted, and the terminal used;         tors to record such events as the following may be
  (g) Groups of output operations that the system            useful.
      performs at the request of a user, including
      those which he directs to be sent to a terminal          (a) Machine faults, failures of internal checks,
      other than the one from which the request                    power losses, environmental malfunctions;
      was made; including identification of the file           (b) Restarts of the system, including details of
      accessed and a measure of the amount of in­                  the loading of system software and by whom,
      formation read out from the file, and the re­                checking or verification of files, manual oper­
      questing and receiving terminals. Similar in­                ations taken, etc.;
      formation should be logged for all input oper­           (c) All changes to the Supervisor, the program
      ations that create or destroy files or instruc­              library, or any system files made by way ofthe
      tions, or that change file classifications or                operator console;
      security parameters.                                     (d) Each running of unusually privileged system
                                                                   programs and by whom;
   To the extent deemed necessary by the System                (e) Each instance of hardware or software
Security Officer, the log records must contain suffi­              maintenance, by whom, and for what purpose.
cient detail to permit reconstruction of events that
indicate an unsuccessful attempt to penetrate the            Comment: A system will also log much information
system or that clearly resulted in a compromise of           for purposes of accounting for resources assigned to
information or a security violation. For example, re­        users, for scheduling events and users in the system,
peated unsuccessful attempts to gain access to the           for allocating charges to users and to accounts, etc.
system software or to a file should be promptly re­          Such information may also be useful for monitoring
ported by the Supervisor software in order to alert          the security controls. Since a large volume of infor­
system operations personnel and, if necessary, the           mation will be available through the various logs, it
System Security Officer. The audit trails should ena­        is clear that special data reduction programs, event­
ble security investigation personnel to identify the         correlation programs, and data-summary programs
terminal involved, the user, the target file or pro­         will be required by the System Security Officer.

                                                        41
Self Surveillance                                                the user in an awkward position from which it may
                                                                 be difficult to restart his program or recover any com­
   As a means ofverifying the continued correct op-.
                                                                 pleted work. Similarly, it is an inconvenience to other
eration ofthe security safeguards in a resource-shar­
                                                                 users to be interrupted even briefly in order to recer•
ing computing system, a system self-inspection and
                                                                 tify the system. Obviously, the seriousness of the vio­
testing program must be inserted into the system
                                                                 lation and the potential security risk are matters that
with the status of a user program. The function of
                                                                 the System Security Officer is responsible for judging.
this program is to verify that the hardware and soft­
ware safeguards are operative. At a minimum, the
testing program should attempt to violate security
controls, and should verify that the correct response            VIII. OPEN ENVIRONMENT
was received in all cases. The security testing pro­             CONSIDERATIONS
gram must communicate with the computer system
by directing its information through a turnaround                   As stated earlier, it is simpler to create a secure
channel (i.e., one that leaves the central processor             system in a closed environment than an open one,
proper, traverses a channel controller, turns around,            largely because of inadequacies in the present state
and re-enters) in order to verify the integrity of the           of technology. The foregoing recommendations pre­
channel controllers as well.                                     sent techniques and methods relevant to protecting
   If the test program succeeds in any attempt to                information in an open environment, but which may
violate either a hardware or software safeguard, the             not as~ure security in such a situation. A few com­
system shall immediately enter a unique (degraded)               ments are in order on the practicability of reducing
operating mode, in which it withholds all informa­               the degree ofopenness as a means of coping with the
tion from the user community until the situation has             security problem. The system can be closed to un­
been assessed and appropriate action taken (see Part             cleared users when classified information is resi­
B, pp. 14-25>.                                                   dent; this is a simple and possible course of action.
                                                                 However, it may be impractical because the work­
Security Violation and Auto-Testing                              load and population of users in many installations
                                                                 will be such that a single computer system is re­
   If a user program violates any security controls              quired to economically serve both cleared and un­
while running operationally (i.e., not during debug­             cleared users.
ging), the program must be immediately suspended                     On the other hand, it might also be true that the
and the System Security Officer notified. Appropri­              volume of classified and the volume of unclassified
ate remedial action must be taken and verified                   work are such that an economic solution might be a
before the program is returned to operational status.            separate machine for each part of the workload. A
   If the violation occurs during on-line debugging              modification ofthis approach is to schedule a system
of application programs, and the program has not                 to operate alternately in uncleared .and classified
accessed files of sensitive information, it is sufficient        modes, with appropriate operational procedures to
to notify the user, alert the System Security Officer,           sanitize the system and to certify it between modes.
and record the event in the system log, while allow­             All information within the system might be ren­
ing the program to continue after the user acknowl­              dered unclassified, which implies that internal en­
edges the event and responds with any appropriate                cryption is used. Finally, it might be possible to find
remedial action. In any such conflict between a user             special configurations ofhardware that could be cer­
program and security controls, but especially in the             tified secure even in an open environment--e.g., du­
case of an open system, it may be advisable to inter­            plex-redundant processors and input/output con­
rupt all system operations at the first feasible oppor­          trols with management of the system and of the
tunity and run a security testing program to verify              security controls vested completely in a third and
correct functioning of all security controls.                    independent machine. With respect to internal en­
Comment: This situation is a delicate one in that it             cryption, it should be noted that the principal threat
reflects a compromise between user convenience and               countered is recovery of information. The threats of
security ofinformation. A complete abort could leave             system denial or intelligent deception must be coun­

                                                            42
tered by other controls. A possible benefit ofinternal          and solutions to it must be based on a system point
encryption may be that it reduces the scope of sys­             ofview. A number of problems covered in the preced­
tem certification to more manageable proportions. A             ing discussions are brought together here briefly be­
possible drawback is the possibility of a malfunction           cause of their importance to the system as a whole.
in the encryption device permanently "freezing" the
information in an encrypted, impenetrable state.
   Internal encryption could be applied not only to
                                                                Redundancy
the primary magnetic core storage, but also to sec­                Given the present state of computer hardware
ondary file stor~ge. All programs and all data resi­            and software technology, we can expect that even
dant in core storage could be in encrypted form and             the best designed systems will have relatively fre­
decrypted only as they pass from storage to the proc­           quent malfunctions. While system designers can be
essing unit for execution. As information is returned           very ingenious in attempting to arrange safeguards
from the processing unit to storage, it would be re­            so that malfunctions do not result in serious conse­
encrypted. Incorporation of this technique into a sys­          quences, nonetheless, given the present lack of ex­
tem would protect against unauthorized access to                perience with computer systems that contain
data resident in primary storage. In addition, infor­           security safeguards, it is strongly recommended that
mation in secondary storage could be protected by an            redundancy be incorporated throughout the system
encrypting mechanism connected directly to the en­              safeguards. Redundancy might take such forms as
crypted primary storage in such a way that informa­             duplicate software residing in different parts of the
tion could be transferred from primary to secondary             memory; software checks that verify hardware
storage without an intermediate plain-text stage oc­            checks, and vice versa; self-checking hardware ar­
curring. The purpose of securing secondary storage              rangements; error-detecting or error-correcting in­
in this fashion is to protect against physical access to        formation representations; duplication of procedu­
storage devices. On the other hand, encryption of               ral checks; error-correcting internal catalogs and
secondary storage greatly complicatesthe file man­              security flags; or audit processes that monitor the
agement problem.                                                performance of both software and hardware func­
                                                                tions.
                                                                   A particular point to note is that the absence of
IX.    RESEARCH NEEDED                                          a parity check in the memory or in information
   In addition to continuing research into internal             transfers can permit errors which perturb, disable,
encryption devices, as mentioned above, other re­               or mislead security controls. In the absence of parity
search requirements include special hardware confi­             checks throughout the machine configuration,
gurations to maintain absolute segregation between              equivalent error-detecting procedures must be incor­
uncleared and other users, special software for such            porated into the software.
configurations, automatic recertification procedures
to be used by the system itselfbetween configuration            Certification·
changes, comprehensive automatic monitors (hard­
ware and software) for security controls, more relia­              As system designers and system operators ac­
ble self-checking hardware architectures, me­                   quire insight into the behavior of resource-sharing
thodology for identifying failure modes and accurate            configurations, new and revised certification tests
prediction of failure probabilities, and new machine            will have to be developed to check one or another
architectures whose security controls minimally                 aspect of system behavior. Certification is a continu­
affect the efficiency or cost of the system.                    ing process. It is the experience ofdesigners ofmulti­
                                                                access, resource-sharing systems that even with the
                                                                best and most ingenious designs, users of a system
X.    OVERALL SYSTEM PROBLEMS                                   find ways of chaining together actions that were not
                                                                foreseen by the designers and which, in many cases,
   Security control in a computer system, especially            lead to undesirable or disastrous consequences.
a resource-sharing one, is a system-design problem,             Therefore, in order to establish confidence in the

                                                           43
security controls, the certification procedure must             the Supervisor tend to be subtle and not immedi­
include a phase that deliberately attempts to pene­             ately detectable; as a general principle, it is desirable
trate our best designs, and that is conducted by tech­          to design the Supervisor so that faults result in gross
nically competent individuals not part of the design            misbehavior, thus facilitating detection. However, in
group or of the operating agency, and not adminis­              practice, this principle is difficult to apply because of
tratively responsible to either.                                the complexity of the Supervisor software and be­
                                                                cause only after-the-fact operational experience will
Debugging and Testing                                           indicate the general manner in which a given soft­
                                                                ware design faults.
   During debugging of a new program or testing of
a program with new data, the likelihood of an error             Cross-checking
is much greater. It is inappropriate to levy security
violations against a user for security errors occur­               Where possible, security controls should be de­
ring during a debugging phase; but it is dangerous to           signed to cross-check each other; e.g., operator input
risk having an agent conceal his activities as debug­           actions should be recorded automatically in the log,
ging errors. Possibilities for dealing with the prob­           which is transmitted to the System Security Officer,
lem include: requiring the user to state his intention          thus minimizing the opportunity for an operator to
to be in a debugging mode and to have this fact noted           take any undetected hostile action. Also, to the max­
(and possibly authenticated to the system) by the               imum extent possible, checks between security con- -­
System Security Officer; requiring all debugging to             trois should cross system components; e.g., manual
operate through a certified interpreter; requiring all          actions should be checked by equipment records,
debugging of programs to operate on dummy and                   software checks of hardware should not depend on
unclassified data; reflecting all errors and violations­        the hardware being checked.
of security control back to the user with an enforced
delay before he can resume work.
                                                                Gradation

System Component Isolation                                         In principle, the number, type, and depth of
                                                                security controls in a system should depend on the
   Each system component-individual user, opera­                sensitivity of the information in the system, on the
tor, maintenance person, etc.-must be isolated from             class of users being served, on the geographical dis­
all other components of the system to the maximum               tribution of the system, on the nature of the service
practicable degree, except as needed to do its job.             that the system provides its users, and on the opera­
Strict adherence to the principle ofisolation is neces­         tional situation that the system supports. In several
sary in order to avoid undesirable or unpredictable             places, it has been suggested that detailed decishms
side effects in case of failure or malfunction of a             must be made by the System Security Officer, by the
particular item in the system.                                  user-agency, or through a consideration of the sen­
                                                                sitivity of the information and classification levels
Fault Detection                                                 involved. The cost of providing security controls may
                                                                turn out to be substantially independent of the fac­
  System design must be such that faults-mal­                   tors noted above, or it may strongly depend on them.
functions of either the equipment or the Supervisor             Thus, positive statements about gradation of
software-are readily detectable. The damage re­                 security controls await the design, implementation,
sulting from a fault depends upon the importance of             and operational experience with a few such systems.
the faulting element to the security control struc­             Examples of features whose presence, frequency of
ture and the length of time that the fault goes un­             operation, completeness of checking, etc., might be
detected and unremedied. Intermittent faults may                subject to gradation are:
go undetected because of error-correcting proce­
dures in the system, or because the system may au­                •    The variety and amount of information re­
tomatically repeat a faulting operation. Faults in                     corded in the system logs for audit purposes;

                                                           44
  •   The manner in which user debugging and                 ways to get around, ignore, or subvert controls.
      testing of programs is handled;
  •   The periodicity and completeness of the in­            Centralization of Vulnerability
      ternal self-testing program;
  •   The frequency with which users must au­                   Care must be exercised not to create inadvert­
      thenticate themselves;                                 ently a system weakness by centralizing too much
  •   The amount of redundancy in the security               responsibility in one individual. For example, the
      controls;                                              System Security Officer oversees all the protective ·
  •   The number of events reported to the System            features ofthe system, as well as controlling its oper­
      Security Officer for his attention;                    ational security status. Thus, he has broad and criti­
  •   The depth of operational control exerted by            cal powers, and becomes a potential target for subv­
      the System Security Officer;                           ersion. Appropriate administrative and procedural
  •   The frequency of recertification procedures;           safeguards, plus division of responsibility and power
  •   The internal events that are reported as               in the System Security Office, will be required to .
      security violations;                                   offset such a threat.
  •   The frequency with which authentication
      words must be changed.                                 Positive Alarms

User Convenience                                                A computer system can malfunction in ways that
                                                             are not readily noticeable to its operators; thus, it is
   At several places it has been indicated that the          conceivable that security controls can also malfunc­
system must be designed to aid the user or to behave         tion or fail without noticeable evidence. All security
in a way helpful and convenient to him. This point           controls must be implemented in such a way that
must not be taken lightly. User convenience is an            failure or malfunction is positively and unambigu­
important aspect of achieving security control be­           ously transmitted, preferably in a redundant fash­
cause it determines whether or not users tend to find        ion, to the System Security Officer.




                                                        45
                                                   Part D
         MANAGEMENT AND ADMINISTRATIVE CONTROL


   In addition to overall policy guidance and to tech­        fresh, certified copy of the Supervisor software, for
nical methods, there must be an effective set ofman­          verification of its correct loading, for validation of
agement and administrative controls and proce­                system security checks, for inserting relevant
dures governing the flow ofinformation to and from            security parameters, and for certification of system
the computer system and over the movement and                 security status by the System Security Officer.
actions within the system environment ofpeople and               Scheduled shutdown. The procedures for a
movable components (e.g., demountable magnetic                scheduled shutdown ofoperations must take account
tapes and discs, print-outs). An essential aspect of          of proper notification of the System Security Officer,
effective control is standardization of activities and        physical protection of demountable storage (tapes,
the need for standards throughout the system. Their           discs) as required, orderly closing of internal files,
presence will make attempts to subvert the system             validation ofthe suspension ofoperation ofall termi­
much more visible and detectable.                             nals, demounting of all copies (or required parts) of
Comment: The importance of.standards is a subtle              the Supervisor software, erasure of any parts of the
philosophical point. They are effective in many ways:         Supervisor software remaining in working storage,
with rigidly prescribed procedures, operators will be         verification of erasure of the Supervisor, disconnec­
inhibited from taking shortcuts that can result in            tion of remote communication circuits, and physical
leakage; "game players" who wish to subvert the sys­          securing of the power controls.
tem to their own ends will find it much more difficult            Unscheduled shutdown. An unscheduled shut­
in a highly standardized environment; records ofsys­          down must initiate procedures for immediate sur­
tem performance and human activities will be avail-·          veillance and recording of all indicators to help as­
able so that the system can be tuned for improved             certain what happened; any needed emergency ac­
service; etc.                                                 tions in case of fire, water hazard, etc.; special sur­
                                                              veillance or physical protection measures to guaran­
   The discussion below presents typical procedures           tee that no demountable items are removed; immedi­
that are required, and suggests some details of each.         ate notification of the System Security Officer; and
For each, it is necessary to provide forms for record­        special security controls (for example, protecting all
ing, initiating, and controlling events; definitions          printouts, including those at terminals, in accord­
and documentation of procedures; checklists for aid­          ance with protection rules for the highest classifica­
ing in the execution of procedures; training aids;            tion handled in the system until the situation can be
periodic and archival summaries of activities; spe­           resolved).
cifications and limitations of personnel responsibili­            Restart after unscheduled shutdown. If a
ties; etc.                                                    trouble condition has caused the system to shut
                                                              down, it is necessary that there be procedures to
   Operational start-up. Procedures must be es­               handle restart, including the loading of a new, cer­
tablished for putting a resource-sharing system into          tified copy of the Supervisor software, clearing the
operation, and must include provisions for loading a          internal state of the equipment in order to clean up

                                                         46
 memory untidiness resulting from the shutdown,                rigid control and protection of certified copies of the
 verifying correct loading of the Supervisor, validat­         Supervisor and other software bearing on system
 ing security controls and security parameters, and            security or threat to the system, for loading the
 certifying the system security status by the System           Supervisor, for making changes to it, and for verify­
 Security Officer.                                              ing the changes.
     File control. File control procedures include                 Maintenance. All maintenance to be per­
 those for identifying the cognizant agency of each            formed on hardware or software must be covered by
 file, scheduling changes for files, modifying access           appropriate procedures, including measures for sur­
 restrictions of files, giving operators access to de­          veillance of maintenance personnel by properly
 mountable files, moving files into and out ofthe com­          cleared personnel, for verifying with the System Ad­
 puting area, pre-operator handling offiles (including          ministrator any iidjustments made to the system's
 mounting and demounting of tapes and discs), and               configuration, and for manually logging all changes
 sanitization of files.                                         and adjustments made or errors discovered.
     Control of magnetic tapes and discs. These                    Certification. Certification procedures should
 procedures must account for and control the circula­           embrace various personnel responsibilities, tests
 tion and storage of tapes and discs; their use, reuse,         and inspections to be performed and their conduct,
 and sanitization; and their classification markings            the responsibilities of the System Security Officer,
 and entrance to and release from the area.                     etc.
     Control of paper-based media. Procedures for                  User aids. The production, distribution, and
 punchcards, forms, papertape, and printouts must               document control of manuals, guides, job procedure
 cover their accountability, classification marking,            write-ups, etc., must be covered by appropriate
 storage, and entrance to and release from the area.            procedures; there must be approved ways ofconduct­
·Additionally, manuals, guides, and various system              ing personnel training.
 documents must be covered.                                        Change of mode. These procedures include the
     Personnel control. Personnel control proce­                provision of checklists for actions requiredin chang­
 dures include measures for verifying clearances and           ing mode, removal and storage of paper media and
.special-access authorization for personnel ent~y to           demountable files, physical and electronic surveil­
 each area of the system, visual surveillance of oper~         lance of the machine area, purging of printers by
 ating and maintenance areas, and logging and es­              running out the paper, purging ofpunchcard equip­
 corting of uncleared visitors. The reporting ofsuspi­         ment by running out cards, removal or erasure of
 cious behavior and security infractions is included           Supervisor software from the previous mode and
 among the personnel control procedures.                       proper verification thereof, loading ofthe Supervisor
     Terminal control. Various procedures are re­              for the new mode and proper verification thereof,
 quired with respect to the operation of remote termi­         clearing of all storage devices so that residual infor­
 nals. These include provisions for logging user entry         mation from the previous mode does not carry for­
 to the terminal area, removal of hardcopy, proper             ward, removal of print ribbons from printers and
 marking of hardcopy not marked by the system,                 terminal typewriters for storage or destruction,
 clearing of displays, and securing as required during         mounting of files for the new mode, and certification
 orderly shutdown.                                             of the security status of the new mode.
     Security parameter control. Procedures must                  Assurance of security control. Security control
 be provided for authorizing security parameters to            assurance includes procedures for reporting anoma­
 be entered into the system; for verifying correct en­         lous behavior of the system or security infractions;
 try; for changing them on the basis of shift, day of          for monitoring security controls, including those on
 the week, etc.; for receiving and processing requests         communications; for assuring continuity of security
 to modify them; and for actions to be taken in case           control; for devolution of responsibility in case of
 of a system emergency or an external crisis.                  personnel nonavailability; and for auditing user and
     Software control. These include procedures for            system behavior.




                                                          47
                                                   Appendix
       AUTOMATION OF A MULTILEVEL SECURITY SYSTEM


INTRODUCTION                                                                                    permits input/output for any user only after
                                                                                                authorization by the security system.
   The basic multilevel security problem consists of
determining whether an individual with a particu­                                 Since the operating environment is not discussed
lar clearance and need-to-know can have access to a                            in further detail, the implementation of the security
quantum of classified information in a given physi­                            system is specified only at the level of the logical
cal environment. While this problem exists in­                                 processing that insures the integrity of the security
dependently of computer systems, the introduction                              system. The details of a monitoring system with
of an automated decision process requires a formal                             which the System Security Officer can observe ac­
specification ofthe decision rules used to answer this                         tivity within the security system are also not treated
question. This Appendix addresses itself to one solu­                          here.
tion to that problem, detailing a language for defin­                             One important implementation issue that is cov­
ing security clearance structures, and a system that,                          ered, however, is the table-driven nature of the
given such a definition, will automate it and protect                          security system, facilitating on-line modification of
its integrity. This system provides for the classifica­                        system security parameters and minimizing the
tion and protection of information through a series                            problem of separate certification of the system at
ofauthorization checks which verify that an impend­                            each installation. Because of the complexity of the
ing user action is permissible to the user in his cur­                         overall scheme for controlling access to classified in­
rent operational context.                                                      formation, it may be that the full range of security
   The operating environment in which the                                      control mechanisms will not be necessary at each
proposed system will exist is not discussed, and will                          installation. Furthermore, as a matter ofprecaution,
certainly vary depending on the equipment configu­                             it would be undesirable to divulge unnecessarily to
ration ofthe installation. It is assumed, though, that                         programming personnel the details of the security
the operating environment possess the following fea­                           control methods. Therefore, the approach has been
tures:                                                                         to conceive a scheme in which only the structure of
                                                                               the security control procedures need be described to
  •    Integrity for both itself and the security sys­                         programming personnel. The specific security
       tem;                                                                    parameters should not be available to such program­
  •    Multiprogramming and/or on-line, interac­                               mers, and must be inserted by the local System
       tive capability;                                                        Security Officer.
  •    A basic file system;                                                       It is proposed that a multi-access, remote-termi­
  •    Protection (read, write, and execute) for users                         nal computer system contain the following informa­
       from each other;                                                        tion:
  •    A secure method of identifying and authen­
       ticating users;                                                                 •        For each user, a list of certain parameters
   •   An interface with the security system that                                               relevant to him;

                                                                       48

                                             ~,.........   ...   lr-'lr""'''o.r- ...   1-.- •   .i.   I
  •     For each file, a list of certain access parame­              cess) only to the Secret level. This is regarded
        ters relevant to the information contained in                as an illegal use ofthe clearance control struc­
        that file;                                                   ture. For the purposes of the computer re­
  •     For each terminal connected to the system, a                 cords, an individual granted (say) a national
        list of certain parameters relevant to it.                   Top Secret clearance and access to informa­
  The details ofthese parameters and how they are                    tion of Type A is automatically assumed to be
used are developed below.                                            cleared for all Type A information through
  Certain assumptions and definitions have been                      the Top Secret level; this does not imply, how­
made for the purposes of this discussion:                            ever, that he is automatically authorized ac­
                                                                     cess to all levels ofType A information. Thus,
  (a) The System Security Officer must be aware of                   it can be said that a national clearance factors
      the structure of that portion of the total                     or distributes over all special information
      security system that is ofconcern to his instal­               types. The phrase Type A can refer to a special
      lation.                                                        clearance system, a compartment or special
  (b) Access authorizations must be verified by ex­                  grouping that may be within a special clear­
      plicit reference to a name check, organization                 ance system, or any major or minor segment
      check, other check, or combination of checks,                  of any clearance system that may have to be
      etc., as may be required by security proce­                    specified.
      dures. This is in addition to verification of the
      clearance status of the user requesting access           Comment: The above-mentioned special situation
      to a given file.                                         was ruled out for two reasons. First, discussion with
  (c) A clearance 1 status must be associated with             several security officers indicated that it is, in fact, a
      both a user and a terminal; a classification 1           misuse ofthe security system. Second, the inclusion of
      status must be associated with a file of infor­          this case would introduce a logical inconsistency in
      mation.                                                  the security control processing described herein,
  (d) The word accesses, when used below as part of            thereby making it possible to circumvent the system.
      the security structure language, is defined to           While this could be corrected, the cost, in terms of
      be semantically equivalent to permits access             computer processing, would be prohibitively high,
                                                               and the first reason makes it unnecessary.
       to information labelled as.
  (e) The phrase national clearances is taken to
                                                                 (g) As a consequence of the above, the computer
      mean the normal defense clearances of Top                      algorithm which matches the parameters of
      Secret, Secret, Confidential, and Uncleared,                   the user against the parameters of the file to
      which are hierarchical in that order. The na­
                                                                     be accessed will first compare the user's na­
      tional clearance status ofan individual will be                tional clearance and the file's national classifi­
      taken as the major parameter in controlling                    cation. If a user is to be granted access to a
      his access to classified information.                          given file, then his national clearance level
  (f) If an individual is authorized to have access
                                                                     must equal or exceed the national classifica­
      to information of Type A at one or more na­
                                                                     tion level of the file. Note that this is a neces­
      tional clearance levels, then it is assumed that
                                                                     sary but not sufficient condition for access.
      he is (in principle) granted access to Type A
                                                                     Additional controls, such as code words, spe­
      information up through the level of his na­
                                                                     cial access categories or compartments, etc.,
      tional clear~nce. This is intended to rule out
                                                                     will be regarded as controlling access to spe­
      the following case, which we believe is com­
                                                                     cific information types within the framework
      mon in present manual practice. An in­
                                                                     of the national clearance structure.
      dividual with a national clearance of Top Se­
                                                                 (h) A dissemination label is regarded as an addi­
      cret is authorized access to (say) crypto­                     tional means of access control, and will re­
      graphic information (i.e., is granted Crypto ac­
                                                                     quire verification against the user's status.
                                                                     Examples of such labels are "No Foreign Dis­
      'These terms are defined on p. 12.                             semination" and "Not Releasable Outside the

                                                          49
      Department of Defense."                                    (d) His citizenship.
  (i) An information label is regarded as not con­               (e) His agency assignment(s).
      trolling access to information, but rather giv­            (f) His permanent identification number (Social
      ing guidance to the user on how the informa­                   Security or other).
      tion may be further disseminated, controlled,              (g) Special need-to-know designators other than
      utilized, etc. Examples of such labels are                     those explicitly contained in the first and
      "Limited Distribution," "Special Handling                      third items.
      Required," "Downgrading Group 1."
                                                                  The computer system will maintain the following
  G) All names, code words, etc., are assumed to be
      unique.                                                  information for each file:

                                                                 (a) Its national classification level.
                                                                 (b) Special names, such as code words, compart­
COMPUTER SYSTEM CATALOGS
                                                                     ment names, handling labels, etc., that serve
   The computer system will maintain a catalog of                    to control access to the file.
all terminals that may be connected to it. For each              (c) Access authorization lists, including one or
terminal, it will maintain the following information:                more of the following as may be required:
                                                                     • Universal authorization lists (i.e., every­
  (a) The highest classification level of informa­                       one is authorized access);
      tion that may be transmitted to or from the                    • Name lists;
      terminal-i.e., the terminal clearance level.                   • Group designator authorizations (group
  (b) Special code words, group names, or other                          membership information is maintained by
      names that modify the clearance level of the                       the system in support of access authoriza­
      terminal to receive other classes of informa­                      tion processing);
      tion.                                                          • Specific exclusions from access authoriza­
  (c) A list ofthe users authorized to use the termi­                    tion by such things as groups, names, ex­
      nal (this may be "ALL").                                           plicit lists of names.
  (d) The electrical address.                                    (d) Dissemination labels.
  (e) The permanent identification number.                       (e) Information labels.
  (f) Physical location, including building loca­                (f) Background information on the file; exam­
      tion, room number, and the cognizant agency.                   ples ofinformation that might be desired are:
  (g) Person responsible for the terminal and (per­                  • Its date of creation;
      haps) his telephone number.                                    • Its downgrading group, and any downgrad­
   The first three items above may be time and date                      ing actions applied to it;
dependent; different parameters may be specified for                 • Name of individual who created the file
different periods, such as normal working hours,                       · and his agency;
holidays, weekends, and night shifts.                                • Predecessor files (if any) from which the
   The computer system will maintain a catalog of                        file was created.
all users authorized to have access to it, and for each
user will maintain the following information:
                                                               SECURITY CONTROL SYSTEM
  (a) His national clearance level, its date of expi­          GENERATION
      ration, and its granting agency. (If necessary,
      its date of issuance can be included.)                      The system for automating multilevel security
  (b) Special code words and groupings or other                classification and control here described is entirely
      words that extend his access to other classes            table driven. As such, the same software implemen­
      of information, and the date of expiration of            tation can be used at all installations using the same
      each such special name.                                  machine. The generation process described below
  (c) His agency affiliation.                                  creates the tables used by the system, but does not

                                                          50
affect the software or any ofits built-in checks. Thus,        tion specifies the dissemination labels and the way
installation personnel need not know about or imple­           they are processed. It is not discussed here because
ment any part of the security control system; nor              we have been unable to determine any standardized,
should they be expected or allowed to modify it. Each          rigorous order in the current practice of using such
installation, through the security control system              labels: We recommend that this area be further ex­
generation process, particularizes the security tables         plored. Note that the processing ofthe dissemination
to its environment (with built-in validity and consist­        labels will depend upon the Personnel Definition.
ency checks), and thus can minimize recertification            For example, a "DoD Only" file will necessitate the
of the security control system.                                ability to determine the agency that the individual
. The card deck (or magnetic tape ot1magnetic disc)            represents.
detailing the security control system and the tables              The other four specifications of the Security Con­
produced during the geil'eration proceSl(> contain the         trol Definition are discussed below. The reader is
most sensitive information resident in the computer            directed to Annex A for the formal System Access
system. As such, no proyision is made for directly             Specification in a slightly modified Backus-Naur
classifying or accessing this information via the file         Form (BNF). In addition to the language specifica­
system; rather, special mechanisms must be pro­                tion, it is necessary to specify the algorithms for
vided to limit access to this information to only the          processing this information. These are discussed be­
responsible authorities.                                       low in all but the obvious cases. The reader should
   System Access Definition is the vehicle for de­             reference the Annexes as he reads the remainder of
scribing to the computer system those parameters               the discussion, particularly Annex B, which contains
that will affect an individual's access to information.        examples of Security Component Definitions.
This consists ofa Personnel Definition, describing all
relevant parameters for the individuals permitted to
use the system, except information dealing with                SECURITY STRUCTURE DEFINITION
security; a Terminal Definition, describing all rele­
vant parameters for any terminals that may be con­                The Security Structure Definition formally
nected to the system, except information dealing               defines the structure of that portion of the security
with security; and a Security Control Definition, d~­          classification and control system that is applicable to
scribing all relevant security parameters. The Per­            the particular installation in question. The language
sonnel and Terminal Definitions are not discussed              presented in Annex A is sufficient to describe all
here, since they are installation dependent and are            special clearances and compartments with which we
not within the scope of this Report.                           are familiar, although actual examples demonstrat­
   Security control system generation is the process           ing the completeness of this approach cannot be pre­
whereby the System Security Officer (or other re­              sented at this level of classification.
sponsible authority) specifies the Security Control               The Security Structure Definition consists ofany
Definition to the computer system. The computer                number of Security Component Definitions, followed
system will process this information, doing such               by any merge rules relating different components. A
things as validity checking and internal table stor­           component may be a compartment, a special cate­
age generation, and thus render the system ready for           gory, or a special access. It is reasonable to expect
actual use. After the initial security system has been         that changes to the Security Structure Definition
generated, changes to the Security Control Defini­             will necessitate a new system generation.
tion can (in almost all cases) be handled directly by             The security structure language formally defines
the system without cause for regenerating the                  a set of relations among entities, including names of
security control system.                                       clearances or classifications, code words, labels, etc.
   The Security Control Definition consists of five            The structure below can be thought of as defining a
separate specifications: Security Structure Defini­            set of decision rules that the computer system can
tion, Personnel Security Definition, Authorization             consult when it wishes to make a decision concern­
Group Definition, Terminal Security Definition, and            ing security parameters. It is immaterial as to how
Releasability Definition. The Releasability Defini­            these decision rules are actually stored in the com­

                                                          51
puter, and this is (for the present) left to the in­           nent, respectively. This is interpreted to mean that
dividual software system designers.                            access authorized by a given clearance implies the
   Following is an example ofa Security Component              automatic access (unless otherwise limited) author­
Definition: 2                                                  ized by other clearances lower in the hierarchy. For
                                                               example, ifan individual has a Top Secret clearance,
  DEFINE: NATIONAL CLEARANCES;
                                                               Top Secret implies Secret (TS IMPLIES S) in the
  CLEARANCES: TOP SECRET, SECRET, CON­                         sense that an individual cleared for Top Secret also
  FIDENTIAL, UNCLEARED;                                        has access to information to which an irtdividual
  SYNONYMS: TOP SECRET = TS, SECRET =                          cleared for Secret has access.
  S, CONFIDENTIAL = C, UNCLEARED = UR,                            Under ACCESS RULES, there is only one opera­
  UNCLASSIFIED= U;                                             tor, called accesses, which has been previously
  INTERNAL STRUCTURE:TS IMPLIES S, S IM­                       defined as permits access to information labelled as.
  PLIES C, C IMPLIES UR;                                       These rules explicitly state the relation between the
                                                               names of the clearances in the security component
  ACCESS RULES: TS ACCESSES TS, S AC­                          being defined and the labels on the information to
  CESSES S, C ACCESSES C, UR ACCESSES U;                       which that security clearance permits access. In
  REQUIRED LABELS: NONE;                                       many cases, the same word is used to specify a clear­
  EXTERNAL STRUCTURE: NONE;                                    ance and a label indicating classification of informa­
                                                               tion (as in the example above).
  REQUIREMENTS: NONE;
                                                                  The REQUIRED LABELS are those other than
  MERGE RULES: TS AND (S OR C OR U)                            the normal classification labels on a file. For exam­
  YIELDS TS, SAND (COR U) YIELDS S, C AND                      ple, certain security components require all informa­
  U YIELDS C;                                                  tion within the component to be handled via special
  END;                                                         channels, and this fact is explicitly stated on any
                                                               piece of information protected by the component. In
   The component name (as specified in the DE­                 effect, a required label can be regarded as a pseudo­
FINE statement) is the name normally applied to a              classification, accessed by any of the clearances
classification system, compartment, or special cate­           listed in the Security Component Definition (or their
gory. It, and all CLEARANCES within the compo­                 synonyms). The necessity ofthis view is indicated in
nent, are listed· in the definition. Note that a compo­        the Crypto example of Annex B (Example 1), where
nent name and a clearance name may be the same.                administrative traffic not having the Crypto classifi­
SYNONYMS allows for commonly used abbrevia­                    cation label, but still confined to Crypto-authorized
tions or synonyms.                                             people, must be recognized by the system.
   The INTERNAL and EXTERNAL STR UC­                            · Note that information and dissemination labels,
TURE statements (i.e., internal and external to the            although required on information, are not included
particular component in question) are handled the              here as REQUIRED LABELS because at present
same way by the system software. They are stipu­               their usage is neither standardized nor logically con­
lated separately in the definition merely to assist the        sistent. When their usage becomes standardized, it
System Security Officer in organizing his thoughts             will be possible to revise slightly the scheme here
as he defines the security structure. A possible use of        described to accommodate them and handle them
the EXTERNAL STRUCTURE statement is to cre­                    automatically.
ate Universal Privileges, as discussed below; its use             The REQUIREMENTS statement is the vehicle
is also illustrated in Example 4 of Annex B. These             for describing situations in which a particular clear­
statements describe hierarchical relationships that            ance requires the simultaneous existence or non­
exist between one of the clearances being defined in           existence of other clearances or access authoriza­
the component, and either another clearance within             tions (see Examples 2-4 in Annex B). Note that clas­
that component or a clearance from another compo­              sification labels are not mentioned, since the particu­
                                                               lar labels accessed by a given clearance can always
   2
       Additional examples are found in Annex B.               be determined.

                                                          52
   MERGE RULES, discussed more fully below,                               clearance from being accepted before the Secret
contain the information that allows the system to                         clearance is deleted.)
determine automatically the classification of infor­
mation that results from merging information of                           Consistency Check of the Security
various classifications. Standard logical relation­                       Structure Definition
ships (utilizing the Boolean connectives AND and
ORJ are permitted.                                                          After all Security Component Definitions have
   The operator YIELDS means that the combina­                            been entered into the computer and preprocessing
tion of classifications (or labels) on the left requires                  has been completed, two consistency checks are
the classification (or labels) on the right to be placed                  made. The first insures that all clearances refe­
on the merged information.                                                renced have been defined and that no clearance is
                                                                          multiply-defined. The second insures that no chains
Security Structure Preprocessing for                                      exist that lead to contradictions. For example, A re­
Minimization of Clearances                                                quires B, B requires C, C requires NOT A, would form
                                                                          an inconsistent set of clearances in which clearance
   Afte:r the complete Security Structure Definition                      A could never be granted.
has been entered into the computer, an augmented                            The consistency check is performed as follows for
set of Requirement statements will be automatically                       each clearance in the Security Structure Definition:
constructed as follows. For each implication state­                          (a) Form an expression, called the consistency ex­
ment ofthe form A IMPLIES Bin either an Internal                                 pression, consisting of the clearance being
or an External Structure statement, the Require­                                 tested.
ment statement of Bwill be modified by the conjunc­                          (b) Moving through this consistency expression
tion of NOT A. If there is no previous Requirement                               from left to right, pick up the next clearance
statement for B, then one must be created.                                       in the expression and replace it by itself con­
   The purpose of this is to provide for consistency                             juncted with the right-hand side of the Re­
in the minimization of the user's clearance set. For                             quirements statement for that clearance
example, if an individual is to be granted a Top Se­                             (from its Security Component Definition), all
cret clearance after already possessing ·a Secret                                enclosed in parentheses.
clearance, the system should rightfully expect that                          (c) Repeat step (b) above, each time moving to
his Secret clearance be removed when the Top Se­                                 the next clearance appearing in the consist­
cret is granted. Similarly, there are instances of in­                           ency expression (i.e., the next one to the right
terrelated components where it is mandatory that a                               of the one just processed), until all clearances
clearance not mutually coexist with another clear­                               in the consistency expression have been proc­
ance that implies it (see Example 4 in Annex B). The                             essed.
system includes this capability, and this results in                         (d) Assign the value of TRUE to the next (left­
the following rule:                                                              most) clearance in the consistency expression
                                                                                 (i.e., to the one being tested for consistency
   When upgrading any user clearance that is                                     with the rest of the security structure).
   hierarchical, the security officer must first
                                                                             (e) If any set of assignments of TRUE and
   remove the lower clearance and then add the
   higher clearance. 3                                                           FALSE can be made to the other Clearances in
                                                                                 the consistency expression which result in a
  In the example just given, this means that the                                 value of TRUE (when the expression is eva­
security officer must remove the user's Secret clear­                            luated according to the normal rules of Boo­
ance before adding the user's Top Secret status to the                           lean expression evaluation), then the clear­
system. (The system's consistency checking mech­                                 ance being tested is consistent with the rest of
anism described below will prevent the Top Secret                                the Security Structure Definition.
                                                                             (f) If no such assignment can be found to make
   3
     As described below, the user is not allowed to be logged onto
the system while his clearance status is being modified, nor can                 the consistency expression TRUE, then the
his status be changed while he is logged on the system.                          clearance being tested is inconsistent with the

                                                                     53
      rest of the Security Structure Definition. The                     side of the rule. (Treat the left-hand side
      consistency expression and the inconsistent                        of the merge as a Boolean expression and
      clearance must be output by the system to                          evaluate according to the normal rules. If
      facilitate the correction of the inconsistency.                   ·a label appears in the concatenated label
      The consistency check should continue to look                      set, consider it TRUE in the expression;
      for further inconsistencies, but .the particular                   otherwise, FALSE. Hence, the right side
      Security Structure Definition cannot be ac­                        is substituted for the left side of a merge
      cepted by the system. (The system cannot al­                       rule when the left side is TRUE.)
      low any type of error in the Security Struc­                  In attempting to apply steps (1) and (2) above,
      ture Definition.) After correcting the incon­                 the labels can be freely reordered to promote
      sistency, the entire process of Security Struc­               a simplification.
      ture Definition must be restarted from the be­            (c) If any simplification results from step (b),
      ginning. Also, because ofthe complex process­                 then repeat steps (b) and (c).
      ing described above, there is no provision for
      on-line definition of new clearances.
  (g) Repeat steps (d), (e), and (f) above, each time
      moving to the next clearance appearing in the
                                                              PERSONNEL SECURITY DEFINITION
      consistency expression (i.e., the next one to
                                                              AND USER CLEARANCE UPDATE
      the right of the one just processed), until all           The next step in system generation is Personnel
      clearances in the consistency expression have           Security Definition. It is possible to modify this infor­
      been processed.                                         mation subsequently through the on-line use of the
                                                              user clearance update language. The processing in­
Merge Rules                                                   volved is the same for both initial system generation
                                                              and subsequent updates, and is as follows:
   Merge rules are provided to permit automatic                 (a) Update of a user's clearance status by the
determination of the classification of information                  security officer can be done if and only if the
that has been produced by the combination of infor­                 user is not logged onto the system.
mation of dissimilar classifications (see the example           (b) The granting agency and expiration date
above of National Clearances, and also Examples 2-4                 may be specified for clearances and put into
in Annex B). Note that all relationships, including                 the user's information, but are not presently
hierarchical ones, must be explicitly stated in terms               utilized. The cognizant agency is neither spe­
of classification labels; the software cannot be ex­                cified nor stored. This implies that within this
pected to infer that one classification subsumes an­                automated security system, a Top Secret
other.                                                              clearance granted from one agency also im­
                                                                    plies access to Top Secret information from
Merge Rule Processing                                               another agency, unless additional labels that
                                                                    deny such access have been applied to this
  The actual merge rule processing is as follows:                   information.
  (a) Concatenate (i.e., conjunct) all the labels of            (c) On each addition or deletion of a user clear­
      each file accessed during the merge process                    ance, a check will be made that the user ex­
      (this includes required labels).                              ists; that (on addition) the clearance exists
  (b) Simplify resultant merge label by the follow­                  and has not already been granted to the user;
      ing rules:                                                     and (on deletion) that the user does, in fact,
      (1) Identity transformation. A AND A yields                    have the clearance to be deleted.
           A for all A;                                         (d) At the time of Personnel Security Definition,
      (2) Apply merge rules; i.e., if the left-hand                  and at the time of granting an additional
          side of a special merge rule matches the                   clearance to (or removing an existing clear­
          concatenated labels or a portion thereof,                  ance from) a user, a consistency check is made
           replace that portion by the right-hand                    to insure that the Requirements statement for

                                                         54
         each of the user's clearances is still satisfied          information to which he has in fact been granted
         after the addition (deletion) of the new (old)            access. In the usual context, need-to-know is really
         clearance; this is accomplished as follows:               need-to-know for reading. We have simply extended
         OJ Generate the set of access privileges spe­             that concept to allow separate need-to-know groups
             cified by the user's explicit clearances;             for reading, changing, etc., and we call this extended
             this can be done as follows:                          concept "authorization groups" in order to avoid con­
             • Form the set of all the user's explicit             fusion.
                  clearances (called the clearance set);
             • For each clearance in the clearance
                  set, add all clearances implied by this .        UNIVERSAL PRIVILEGES
                  particular clearance in either Inter­
                  nal or External Structure statements                Under emergency conditions, it may be necessary
                  within the Security Component Defi­              to grant a user or a group of users unrestricted ac­
                  nition;                                          cess to all files in the system or to a set offiles regard­
             • Apply identity transformation (A                    less of clearances, special access categories, and/or
                  [AN_D] A yields A) to the clearance set          need-to-know restrictions. Rather than turning off
                  (i.e., remove all duplicates).                   th~ file safeguards in the system, necessitating con­

             Notice that this is the algorithm used in             cern for user identification, protection of terminals,
             generating the set of all labels to which             etc. (especially under emergency conditions), a spe­
             the user's clearance permits access (ex­              cial capability is provided within the system so that
             plained below in "File Access Processing")            the system security controls are not impaired.
             with steps (b), (c)(l), and (c)(3) deleted.              The System Security Officer in a normal Security
         (2) For each explicit clearance the user has
                                                                   Component Definition can define a universal or
             been granted, including the new one being             emergency clearance, which implies all other clear­
             added (or excluding the old one being de­             ances or special-access categories in the system and
             leted), check to see ifthe requirements as            which has no external requirements. It can be
             stated in the Requirements statem~nt(s)               granted to a given user by first removing all his
             in the Security Component Definition are              clearances (to prevent a clearance inconsistency
             satisfied by the occurrence or absence of             check) and then granting the universal or emer­
             the clearances in the clearance set just              gency clearance. (Obviously, any number of such
             generated according to the normal rules               emergency clearances could be set up for any subsets
             of Boolean expression evaluation.                     of the overall security system by simply listing the
                                                                   desired ones in the External Structure statement.)
                                                                      Universal authorization groups can be defined to
  AUTHORIZATION GROUP                                              handle the problem of overriding the system's file
  DEFINITION                                                       manipulation and access authorization restrictions.
                                                                   Membership in such a group authorizes the in­
         Authorization Group Definition occurs at system           dividual to take some action on the files to which he
     generation time, but, like Personnel Definition, also         is permitted access, either on a standing or an emer­
      may be updated on-line. There is no special process­         gency basis. Examples of universal authorizations
      ing explicitly required for authorization groups. A          are: universal right-to-read, universal right-to­
      user does not have to be authorized to use the system        change, etc .
... . for his name to be in an authorization group. Up­            Comment: The word "emergency" is used here in a
      dates are made via the authorization group update            limited sense; i.e., we refer mainly to the numerous
      language.                                                    unanticipated special situations that always seem to
   Comment: Our concept ofan authorization group is                arise at any computer installation. Through appro­
   more general than the normal need-to-know concept               priate forethought and predefinition, these situations
   associated with classified information. It also ad­             can be hlLndled routinely as they arise. Still, however,
   dresses the question of what a person can do to the             there may arise a true emergency (such as an enemy

                                                              55
attack) where there is no time to do anything but               may therefore specify authorizations and an access
respond. The techniques discussed here are not in­              list to be assnciated with each authorization.
tended to address that problem. Rather, we would                   If not specified, default access lists are assumed
assume some sort of fail-safe, joint-key mechanism              as follows:
whereby appropriately authorized individuals could
turn off all access controls of the system in time of             All authorization access lists have the default
dire emergency.                                                   condition of null (i.e., unless otherwise spe­
                                                                  cified, they are empty) except those associated
   Mechanisms such as described above should be                   with the following actions: unrestricted access,
sufficient for accommodating any specific situations              right-to-change authorization lists, and right­
that may arise, assuming the appropriate universal                to-change file classifications. The access lists as­
groups have been predefined. In addition, they allow              sociated with these particular authorization
                                                                  types must be initialized by the system to con­
routine handling of two situations normally requir­
                                                                  tain the name of the author of the file.
ing special provisions. These are the privileges ofthe
System Security Officer and the file-backup mech­                 It should be noted that the syntax of the authori­
anism. The System Security Officer should have, in              zation specification provides capability for the re­
addition to his normal clearance status, universal              moval ofthe author's name from an access list. Un­
authorizations for read-only, right-to-change author­           less this is explicitly done, however, the author of a
ization lists, and right-to-change file classifications.        file will be permitted unrestricted access to the file,
The file backup program can be given the clearance              as well as the privilege ofchanging the authorization
status to handle all files for which it is to provide           specification and classification of the file.
backup and universal authorization for read-only to                 At present, it is not deemed necessary to provide
enable it to read any of these files.                           the capability to be able to syntactically distinguish
                                                                between authorization group identifiers and user
                                                                identifiers. Rather, it is assumed that the processing
TERMINAL SECURITY DEFINITION                                    algorithms  will  have to check the identifier in ques­
AND UPDATE                                                      tion against master lists, and that the semantics will
                                                                be obvious from the context.
    Terminal Security Definition is handled in a man­               Anyone who has the ability to write in a file can,
ner similar to personnel security information. There            in principle, add to it information ofa higher classifi­
exists the capability to update this information on­            cation than the file. Therefore, he must have some
line. In the present specification, the capability to           way of altering the classification status of the file.
specify a terminal access list has not been included;           Whether this is provided by allowing anyone with
i.e., a list ofthe authorized users ofa given terminal.         write privilege to alter the file classification directly,
It appears, for the present, that this is an unneces­           or by requesting the original author of the file to
sary complexity to add to an already burdened sys­              alter the classification, or by requesting the System
tem, and we expect that physical access to terminals            Security Offic~ to alter the classification, is an oper­
processing classified information will normally be              ational policy decision. The first alternative is simpl­
controlled. Further control seems unnecessary, but              est, but it may be operationally desirable to have a
should it be desired, mechanisms similar to those               second person involved in change of classification.
already specified can be used. For.example, a special           The mechanisms in the overall scheme provide capa­
clearance status can be defined, access to which is             bility to specify a separate group of individuals who
permitted only for a particular terminal.                       can only alter the classification of a file.

Specification of File Authorizations
  Each time a file is created, the creator may                  FILE ACCESS PROCESSING
specify which individuals or groups of individuals
are permitted to access the file, as well as how they              The system must follow certain procedures when
may do so; e.g., read-only. For each file, the author           attempting to determine whether or not a given user

                                                           56
may reference a particular file of information. First,           ofmanipulation he is allowed for the file in question.
the user's clearance must be sufficient to permit ac­            The proce.ss for carrying this out is as follows:
cess to the file classification, and this is determined
as follows:                                                        (a) Copy the user's universal authorization privi­
                                                                       leges (which are explicitly specified at log-on
  (a) Obtain the file classification labels.                           time by the universal authorization algorithm
  (b) Obtain the set of labels to which user clear­                    described below) into a memory area called
      ances permit access. This set may be cal­                        his file-access rights block. If he has universal
      culated as needed at log-on time or at security                  unrestricted access after specifying this in the
      system update time (if the latter is used, on­                   file-access-rights block as explained in step
      line updating of a user's clearance by the Sys­                  (b)(2) below, then processing can stop (i.e.,
      tem Security Officer cannot be allowed).                         there is nothing that can be added to his ac­
  (c) If the set of labels to which the user's clear­                  cess rights).
      ance status permits him access contains all                  (b) For each authorization type (starting with
      the labels in the file classification status, then               unrestricted access):
      the formal security accessing requirements                       (1) If the user is in the access list either ex­
      have been satisfied.                                                  plicitly (by name) or implicitly (either by
                                                                            membership in a group specified in the list
   The method of generating the set of labels to                            or because the universal set was specified),
which a user's clearance status permits him access                          grant the user the specified type of access;
is as follows:                                                         (2) If the authorization is for unrestricted ac­
                                                                            cess and the user qualifies for it, grant
  (a) Form the set of all user's clearances and spe­                        him (in his file-access-rights block for this
      cial access categories (called clearance set).                        file) all the other authorization types, and
  (b) Initialize to null the set oflabels to which the                      stop processing these rights.
      user's clearance status permits him access
      (called the accessible label set).                            The file-access-rights information (in the file­
  (c) For each entry in the clearance set:                       access-rights block) is consulted by the Supervisor on
      (1) Add to the accessible label set all labels to          everyinput/output operation in order to determine
          which the particular entry permits access.             whether or not the operation on the file is legal.
          These are obtained fro~. the access rules              Thus, the authorization processing occurs during the
          in the Security Componenr Definition.                  linkage of a user to a file after clearance status
          Also, add all required labels for this par­            checks have been made, and results only in the crea­
          ticular clearance entry.                               tion ofthe file-access-rights data, which is later used
      (2) Add to the clearance set all clearances or             by the Supervisor for controlling access to the file.
          special-access categories implied by this                 The universal authorization aigorithm consists of
           particular clearance entry in either Inter­           checking each universal group for the presence of
          nal or External Structure statements                   the user in the set, either explicitly by name or im­
          within the Security Component Defini­                  plicitly by membership in another group specified as
           tion.                                                 a member of the universal group. If the user is pre­
      (3) Delete this entry from the clearance set.              sent in the set, then grant him the associated univer­
  (d) Apply identity transformation (A AND A                     sal access privilege.
      yields A) to the accessible label set (i.e., delete
      all duplicates).                                           Comment: When access control labels are standard­
                                                                 ized and any precedence or combinatorial relations
  After a user's clearance status has been checked               among them have been specified, the algorithms for
and successfully permits access to a file, the security          handling them can be developed, and the restrictions
system must determine whether the user satisfies                 resulting from the operation of such algorithms
the authorization limitations for the file. This check           would be examined at this point in file access process­
determines the user rights and specifies what types              ing.

                                                            57
                               Annex A:
        FORMAL SYSTEM ACCESS SPECIFICATION


Notation: Standard Backus-Naur Form (BNF), plus:
• [x] means one or more occurrences ofx separated by commas, with no
   initial or terminal comma.
• Also, if any <STRING:> contains one of the fixed words appearing in
   the following BNF rules that could lead to an ambiguity, the <STRING>
   should be enclosed in parentheses.


System Access Definition

<SYSTEM ACCESS DEFINITION> ::=<PERSONNEL DEFINITION>
     <TERMINAL DEFINITION> <SECURITY CONTROL DEFINITION>
<PERSONNEL DEFINITION> ::=     Not part of this specification.
<TERMINAL DEFINITION> ::=      ~art      of this soecification.
<SECURITY CONTROL DEFINITION> : := <SECURITY STRUCTURE DEFINITION>
     <PERSONNEL SECURITY DEFINITION> <AUTHORIZATION GROUP DEFINITION>
     <TERMINAL SECURITY DEFINITION> <RELEASABILITY DEFINITION>
<RELEASABILITY DEFINITION> ::=Not part of this specification.

Security Structure Definition

<SECURITY STRUCTURE·DEFINITION> ::=
     <SECURITY COMPONENT DEFINITION> <MERGE RULES> I
     <SECURITY COMPONENT DEFINITION> <SECURITY STRUCTURE DEFINITION>
<SECURITY COMPONENT DEFINITION> ::=<DEFINE STATEMENT>
     <CLEARANCE STATEMENT> <SYNONYM STATEMENT>
     <INTERNAL STRUCTURE STATEMENT> <ACCESS RULE STATE~1ENT>
     <REQUIRED LABEL STATEMENT> <EXTERNAL STRUCTURE STATEr~ENT>
     <REQUIREMENT STATEMENT> END;
<DEFINE STATEMENT> ::=DEFINE: <COMPONENT NAME>;
<CLEARANCE STATEMENT> ::=CLEARANCES: [<CLEARANCE NAME>];
<SYNONYM STATEMENT> : := SYNONYt1S: NONE; I SYNONn1S: [<SYNONYM PAIR>];
<INTERNAL STRUCTURE STATEMENT> : := INTERNAL STRUCTURE: NONE;
      INTERNAL STRUCTURE: [<CLEARANCE NAME> <BLANKS> IMPLIES
      <BLANKS> <CLEARANCE NAt1E>];
<ACCESS RULE STATEf·HlT > : : = ACCESS RULES: NONE; I
     ACCESS RULES: [<CLEARANCE NAME> <BLANKS> ACCESSES <BLANKS>
     <LABEL>];
<REQUIRED LABEL STATEMENT> ::=REQUIRED LABELS: NONE; I
     REQUIRED LABELS: [<REQUIRED LABEL>];

                                   58
<EXTERNAL STRUCTURE STATEMENT> ::=EXTERNAL STRUCTURE: NONE;
     EXTERNAL STRUCTURE: [<CLEARN~CE NAME> <BLANKS> IMPLIES
     <BLANKS> <EXTERNAL CLEARANCE NAME>];
<REQUIREMENT STATEMENT> ::=REQUIREMENTS: NONE; I
     REQUIREMENTS: [<CLEARANCE NAME> <BLANKS> REQUIRES <BLANKS>
     <CLEARANCE EXPRESSION>];
<CLEARANCE EXPRESSION> ::=<PRIMARY> I <PRIMARY> <BOOLEAN OPERATOR>
     <PRIMARY>
<PRIMARY> : := (<CLEARANCE EXPRESS.I.Otb} I <CLEARANCE NAME> I
     <BLANKS> NOT <BLANKS> <PRIMARY>
<BOOLEAN OPERATOR> ::=<BLANKS> AND <BLANKS> I <BLANKS> OR <BLANKS>
<SYNONYM PAIR> ::=<BASIC NAME>= <SYNONYM NAME>
<BASIC NAME> ::=<COMPONENT NAME> I <CLEARANCE NAME> I <LABEL NAME>
<LABEL NAME> ::=<LABEL> I <REQUIRED LABEL>
<SYNONYM NAME> ::=<STRING>
<EXTERNAL CLEARANCE NAME> ::=<STRING>
<COMPONENT NAME> ::=<STRING>
<CLEARANCE NAME> : := <STRING>
<LABEL> ::=<STRING>
<REQUIRED LABEL> ::=<STRING>
<STRING> ::=<LETTER> I <LETTER>·, <CHARACTER STRING>
<CHARACTER STRING> ::= <NONBLANK CHARACTER>· I <CHARACTER>
     <CHARACTER STRING>
<CHARACTER> ::= <NONBLANK CHARACTER> I <SPACE> I <HYPHEN>
<NONBLANK CHARACTER> ::=<LETTER> I <DIGIT>
<LETTER> : := A I B I c I . . . I y I z
<DIGIT> : := 0 I 1 I 2 I ... I 8 I 9
<BLANKS> ::=<SPACE> I <SPACE> <BLANKS>
<MERGE RULES> ::=<MERGE RULE STATEMENT> END;
<MERGE RULE STATEMENT> : := :·iERGE RULES: NONE;
     MERGE RULES: [<MERGE RULE>];
<MERGE RULE> ::=<MERGE CONDITION EXPRESSION> <BLANKS> YIELDS
     <BLANKS> <RESULTANT STRING>
<MERGE CONDITION EXPRESSION> : := <MERGE PRIM~RY> I <~4ERGE PRH·1ARY>
     <BOOLEAN OPERATOR> <~·1ERGE PR1t4ARY>
<MERGE PRIMARY> : := (<MERGE CONDITION EXPRESS·ION>) I <LABEL NAME> I
     <BLANKS> NOT <BLANKS> <MERGE PRIMARY>

                                    59
<RESULTANT STRING> : := <LABEL NAME> I <LABEL NAME> <BLANKS> AND
     <BLANKS> <RESULTANT STRING>

Personnel Security Definition

<PERSONNEL SECURITY DEFINITION> ::=END; I <USER CLEARANCE STATEMENT>
      <PERSONNEL SECURITY DEFINITION>
<USER CLEARANCE STATE~1ENT> : := [<USER ID>]:
     [(<CLEARANCE NAr·1E>, <GRANTING AGENCY>, <EXPIRATION DATE>)];
<USER ID> ::= <NONBLANK CHARACTER> I <NONBLANK CHARACTER> <USER ID>
<GRANTING AGENCY> ::=<LETTER> I <LETTER> <GRANTING AGENCY>
<EXPIRATION DATE> ::=<MONTH> I <DAY> I <YEAR>
<r'ONTH> : := <DIGIT> <DIGIT>
<DAY> ::= <DIGIT> <DIGIT>
<YEAR> ::=<DIGIT> <DIGIT>

User Clearance Update Language

<USER CLEARANCE UPDATE LANGUAGE> : := <GRANT USER CLEARANCE STATEMENT>
     <REMOVE USER CLEARANCE STATEMENT>
<GRANT USER CLEARANCE STATEMENT> : := GRANT [(<CLEARANCE NAME>,
     <GRANTING AGENCY>, <EXPIRATION DATE>)] TO USER [<USER ID>]
<REMOVE USER CLEARANCE STATEt1ENT> : := REMOVE <CLEARANCE SET> FROM USER
     [<USER ID>]
<CLEARANCE SET> ::=ALL CLEARANCES I ([<CLEARANCE NAME>])

Authorization Group Definition

<AUTHORIZATION GROUP DEFINITION> ::=END;
     <AUTHORIZATION GROUP SPECIFICATION>
     <AUTHORIZATION GROUP DEFINITION>
<AUTHORIZATION GROUP SPECIFICATION> ::=<AUTHORIZATION GROUP NAME>:
     [<AUTHORIZATION TYPE>]
     ([<AUTHORIZATION GROUP ELEMENT>]);
<AUTHORIZATION GROUP NAME> ::=UNIVERSAL <AUTHORIZATION TYPE>
     <AUTHORIZATION GROUP IDENTIFIER>
<AUTHORIZATION TYPE> ::=READ ONLY I CHANGE ONLY I
     APPEND ONLY I EXECUTE ONLY I U~JRESTRICTED ACCESS
     RIGHT-TO-CHANGE AUTHORIZATION SPECIFICATION I
     RIGHT-TO-CHANGE FILE CLASSIFICATION
<AUTHORIZATION GROUP ELEMENT> : := <AUTHORIZATION GROUP IDENTIFIER> I
     <USER ID>

                                  60
<AUTHORIZATION GROUP IDENTIFIER> ::= <NONBLANK CHARACTER>
     <NONBLANK CHARACTER> <AUTHORIZATION GROUP IDENTIFIER>

Authorization Group Update Language

<AUTHORIZATION GROUP UPDATE LANGUAGE> : := <DEFINE GROUP STATEMENT>
     <ADD MEMBER STATEMENT> I <REMOVE t~EMElER STATEMENT>
<DEFINE GROUP STATEMENT> : := DEFINE GROUP <AUTHORIZATION GROUP NAME>:
     [<AUTHORIZATION TYPE>]
      ([<AUTHORIZATION GROUP ELEMENT>])
<ADD MEMBER STATEMENT> ::=ADD ([<AUTHORIZATION GROUP ELEMENT>])
     TO GROUP [<AUTHORIZATION GROUP NAME>]
<REMOVE Mn1BER STATEMENT> : := REMOVE ([<AUTHORIZATION GROUP ELEMENT>])
     FROM GROUP [<AUTHORIZATION GROUP NAME>]

Terminal Security Definition

<TERMINAL SECURITY DEFINITION> ::= END; I
     <TERMINAL CLEARANCE STATEr1ENT> <TERMINAL SECURITY DEFINITION>
<TERMINAL CLEARANCE STATEMENT> ::=[<TERMINAL ID>]: <CLEARANCE SET>;
<TERMINAL ID> ::= Installation de endent--not soecified here
                  not include comma, colon, or semicolon .


Terminal Clearance Update Language

<TERMINAL CLEARANCE UPDATE LANGUAGE> ::=
     <GRANT TERMINAL CLEARANCE STATEMENT> I
     <REMOVE TERMINAL CLEARANCE STATEMENT>
<GRANT TERt4INAL CLEARANCE STATEMENT> : := GRANT <CLEARANCE SET>
     TO TERMINAL <TERMINAL ID>
<REMOVE TERMINAL CLEARANCE STATEMENT> ::=REMOVE <CLEARANCE SET>
     FROM TERMINAL <TERMINAL ID>

File Authorization Specification

<FILE AUTHORIZATION SPECIFICATION> : := <FILE NAME>:
     [(<AUTHORIZATION TYPE>
     <AUTHORIZATION ACCESS LIST>)]
<AUTHORIZATION ACCESS LIST> ::=UNIVERSAL I UNIVERSAL
     <SET SUBTRACTION OPERATOR> <AUTHORIZATION EXPRESSION>
     <AUTHORIZATION EXPRESSION>
<AUTHORIZATION EXPRESSION> ::=<AUTHORIZATION GROUP>
     <AUTHORIZATION GROUP> <AUTHORIZATION OPERATOR>
     <AUTHORIZATION EXPRESSION>

                                  61
 <AUTHORIZATION GROUP> ::= ([<AUTHORIZATIDN IDENTIFIER>])
 <AUTHORIZATION IDENTIFIER> ::=<AUTHORIZATION GROUP IDENTIFIER>
      <USER ID> I AUTHOR
 <AUTHORIZATION OPERATOR> : := <SET ADDITION OPERATOR> I
      <SET SUBTRACTION OPERATOR>
 <SET ADDITION OPERATOR> ::= +
 <SET SUBTRACTION OPERATOR> ::=­
 <FILE NAME>                                            s ecified here rna




                                   Annex B
        SECURITY COMPONENT DEFINITION EXAMPLES

Example I
     Consider a class ofinformation.called Crypto, which is to be regarded as
a further restriction on access under the national clearance system. Since
Crypto information is to be transmitted via special channels, and is labelled as
such, administrative traffic without the classification label Crypto can still be
confined to Crypto-authorized personnel by regarding the required label on the
file as a pseudo-classification accessed by any of the clearances listed in the
definition.    ·
DEFINE: CRYPTO;

CLEARANCES: CRYPTO;

SYNONYMS: CRYPTO = CRP;

INTERNAL STRUCTURE: NONE;

ACCESS RULES: CRP ACCESSES CRP;

REQUIRED LABELS: HANDLE VIA SPECIAL CHANNELS;
EXTERNAL STRUCTURE: NONE;

REQUIREMENTS: CRP REQUIRES TS OR S;

MERGE RULES: NONE;
END;


                                       62
Example 2
    Consider a hypothetical refinement of the national clearance system
called DATATEL as follows:
DEFINE: DATATEL;

CLEARANCES: III, II, I;

SYNONYMS: NONE;

INTERNAL STRUCTURE: III IMPLIES II, II IMPLIES I;

ACCESS RULES: III ACCESSES ABLE, II ACCESSES BAKER, I ACCESSES CHARLIE;

REQUIRED LABELS: HANDLE VIA DATATEL CHANNELS ONLY;

EXTERNAL STRUCTURE: NONE;

REQUIREMENTS: III REQUIRES TS, II REQUIRES S, I REQUIRES C;

MERGE RULES: ABLE AND (BAKER OR CHARLIE) YIELDS ABLE, BAKER AND CHARLIE
YIELDS BAKER;

END;


Example 3
    Now consider a hypothetical compartment of information within the
DATATEL structure. It has been assumed that APPLE information is not
labelled as such, but is to carry the codeword ALICE. The APPLE definition
below relates APPLE to III; the DATATEL definition relates III to ABLE and
also to Top Secret. Thus, the system can correctly determine that the proper
classification labe,l for APPLE information is TOP SECRET ABLE ALICE.
Note also that such information has two required labels; some rule of prece­
dence must be specifi~d to handle such situations.
DEFINE: APPLE;

CLEARANCES: APPLE;

SYNONYMS: NONE;

INTERNAL STRUCTURE: NONE;

ACCESS RULES: APPLE ACCESSES ALICE;

REQUIRED LABELS: HANDLE VIA APPLE CHANNELS ONLY;

EXTERNAL STRUCTURE: NONE;

REQUIREMENTS: APPLE REQUIRES III;

MERGE RULES: NONE;

END;


Example 4
    Consider a hypothetical example (named ROUND ROBIN) in which it is
assumed that at the Secret levelthere are two categories ofinformation, called


                                      63
AGILE and BANANA, accessing information labelled respectively as ANN
and BETTY. Further assume that an individual cannot be concurrently au­
thorized access to both AGILE and BANANA information. Rather, assume
that in order to have access to both, an individual must be cleared to Top
Secret, in which case he will be said to have access to CHERRY information
labelled CHICO, as well as to all AGILE and BANANA information. Further­
more, assume that having a CHERRY access also allows an individual to access
all information that a person who has a III access authorization (see Example
2) may access.
DEFINE: ROUND ROBIN;
CLEARANCES: CHERRY, AGILE, BANANA;
SYNONYMS: NONE;
INTERNAL STRUCTURE: CHERRY IMPLIES AGILE. CHERRY IMPLIES BANANA;
ACCESS RULES: CHERRY ACCESSES CHICO, AGILE ACCESSES ANN, BANANA ACCESSES
BETI'Y;

REQUIRED LABELS: NONE;

EXTERNAL STRUCTURE: CHERRY IMPLIES III;
REQUIREMENTS: AGILE REQUIRES NOT BANANA AND SECRET, BANANA REQUIRES
NOT AGILE AND SECRET, CHERRY REQUIRES TOP SECRET;

MERGE RU~S: ANN AND BETTY YIELDS TOP SECRET AND CHICO;
END;




                                     64
                                                         )
The typographical format used in this report represents a practical application
of current computer-associated technology to decrease the time and expense
usually involved in manuscript preparation and typesetting. The copy is key­
boarded on an IBM Magnetic Selectric Typewriter (MT/STJ, an office machine
designed to reduce the time required for correctin(J and editing of written
material. After correction, the MT/ST tape is processed through an IBM 2495
Converter multiplexed to Rand's IBM 360165 computer, producing a standard
computer-readable magnetic tape. This tape is processed on an RCA Spectra
70145 and an RCA Videocomp, operated by Auto-Graphics, Inc., of Monterey
Park, California, to produce phototypeset galleys which are then pasted up for
reproduction. The RCA system also does the line justification and hyphenation,
according to standard algorithms. This process results in a substantial reduc­
tion in the author-to-reader costs normally associated with graphics quality
publications.
'-:UNt-IUENTIAL                                 c



                                                •




~~ . .   ..................   ·-   ?'   /
                                            /
```
