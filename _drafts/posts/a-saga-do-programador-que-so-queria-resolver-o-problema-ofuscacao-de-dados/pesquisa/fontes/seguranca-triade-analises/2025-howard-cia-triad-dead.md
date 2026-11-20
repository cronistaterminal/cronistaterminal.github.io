---
title: "Howard. Part I: Is the CIA Triad Dead? 2025"
type: fonte
formato: html
url: "https://diffuser.substack.com/p/is-the-cia-triad-dead"
wayback: "https://web.archive.org/web/20261119141838/https://diffuser.substack.com/p/is-the-cia-triad-dead"
acessado: 2026-11-19
conversor: trafilatura
---

> [!info] Cópia para leitura
> Original: <https://diffuser.substack.com/p/is-the-cia-triad-dead>
> Wayback: <https://web.archive.org/web/20261119141838/https://diffuser.substack.com/p/is-the-cia-triad-dead>
> Capturado em 2026-11-19 com `trafilatura`. Em caso de dúvida, vale o original.

Last month, Loris Gutic wrote a piece for CSO Online proclaiming that the CIA Triad was dead. He proposed the infosec community should adopt his own 3C Model as a modern “hierarchical system designed to map today’s threats and obligations.”

I mostly agree with Loris that the CIA Triad is dead as a first principle. It’s not that the ideas of Confidentiality, Integrity, and Availability are bad. They aren’t. They represent sound strategic concepts. Because of those strong ideas, the Triad has endured as the overriding best practice security philosophy from the early days (1970s) throughout today. In 2020, the U.S. National Institute of Standards and Technology (NIST) published “NIST SPECIAL PUBLICATION 1800-25.” They declared that “The CIA triad represents the three pillars of information security.” NIST believes that security practitioners should use the Triad as the baseline for protecting all U.S. government systems.

I think that’s misguided and I made the strong case in my *Cybersecurity First Principles* book as to why that is so.

But I want to revisit the question. Should infosec practitioners continue to adopt the CIA Triad as their baseline strategy? I’m, launching a three part mini-series to find out.

- Part I: Why has CIA Triad Endured?
- Part II: Why it’s inadequate as a first principle strategy?
- Part III: Should we adopt Gutic’s 3C model as a replacement?

This essay is Part I.

# The Origin Story of Cybersecurity

It all began in 1967. The U.S. Department of Defense was shifting from batch processing to time-sharing systems like CTSS and MULTICS. These new systems allowed dozens of users to log into the same computer simultaneously. That was great for collaboration but security issues started to emerge. Researchers at MIT, RAND, and other labs were already demonstrating that clever programmers could bypass rudimentary access controls and read files belonging to other users. They also discovered that these time-sharing systems stored both classified and unclassified data.

The U.S. Director of Defense Research and Engineering was Dr. John S. Foster Jr. He was responsible for R&D during the most innovative period of the Cold War; things like missile defense, early computing research, and the first discussions of ARPANET.

He realized that no DoD policy or technical standard addressed these emerging risks and established the Task Force on Computer Security in 1967, led by Willis H. Ware of the RAND Corporation, to study the problem, define what “secure computing” meant, and recommend a national R&D program.

Foster charged the group to:

- Assess vulnerabilities of shared-resource computer systems.
- Identify required safeguards for classified information.
- Recommend new technologies, policies, and training to ensure secure multi-level operation.

## The Ware Report

Ware published his 110 page report in 1970 and concluded that securing computer systems was a system design problem. He recommended the creation of certification standards, security accreditation, and funneling research dollars to encryption, fail-safe architectures, and data sanitization.

## The Anderson Report

After the Task Force on Computer Security published the Ware report, the U.S. Air Force’s Electronic Systems Division, its central command for developing information and control systems, hired James P. Anderson to turn the Ware Report’s ideas into an actual engineering plan. Anderson published it in 1972.

The Ware Report identified the problem. The Anderson Report was the first blueprint on how fix it. It identified the Insider Threat as the most important problem. It proposed that security must be designed into operating systems from inception. It outlined the concept of a reference monitor (what we would refer to as Identity and Access Management today) and a security kernel. Anderson proposed a secure open-use multilevel system, supported by engineering projects like secure terminals, encryption devices, and crypto concentrators. It also recommended interim fixes for legacy systems and an ongoing research program on security models, operating system architecture, and certification methods.

The Anderson Report picked up where Ware left off: instead of just describing the problem, it laid out the architecture, models, and development path for certifiably secure, multilevel systems and became the foundation for the later Trusted Computer System Evaluation Criteria (TCSEC / Orange Book) in the 1980s.

## The Saltzer and Schroeder Paper

In 1975, Saltzer and Schroeder published their research paper, “The Protection of Information in Computer Systems” in the Fourth ACM Symposium on Operating System Principles. This was the first public paper that tackled the same issues that the Ware Report and the Anderson Report did in a classified setting for the U.S. Government. It outlines eight core design principles that guide secure system architecture. Modern day Zero Trust fans will recognize four of them:

1. Least privilege
2. Complete mediation (Continuously check, not one and done)
3. Separation of privilege
4. Least common mechanism (Only share what is necessary)

The remaining four are basic design principles that could be applied to anything but here are called out specifically for securing systems.

1. Fail-safe defaults
2. Economy of mechanism (Keep it simple)
3. Open design
4. Psychological acceptability (Don’t annoy the user)

They emphasize that security must be built into system design rather than added later, and that usability and simplicity are essential for effective protection.

The paper is also the first appearance of what would become the CIA Triad.

# The CIA Triad Begins to Form in the 1970s

Jennifer Reed, a 20-year security and technology veteran and a friend of mine, in an exchange with me back in August 2022, made the case that the Saltzer and Schroeder paper might be the first public statement about the CIA triad: the idea that to make a system secure, architects have to provide confidentiality, integrity, and availability. She says that Saltzer and Schroeder don’t use the phrase CIA triad and don’t mention the specific terms (confidentiality, integrity, and availability), but they “referred to three types of invasion from the perspectives of security specialists” known as

1. Unauthorized information release (confidentiality)
2. Unauthorized information modification (integrity)
3. Unauthorized denial of use (availability).

# The CIA Triad” wasn’t a thing until the 1990s

But, as a phrase, “The CIA Triad” wasn’t a thing yet. Members of the security community at the time were aware of the ideas, but they hadn’t coalesced them into a coherent concept that depended on each other.

Donn B. Parker was a peer to Ware and Anderson (although he didn’t work on their papers). He hated the idea of Confidentiality, Integrity, and Availability as a baseline security framework. In his 1998 book “Fighting Computer Crime: A New Framework for Protecting Information,” he strongly condemns the elements in the CIA Triad as being inadequate. Although he never mentions the phrase “CIA Triad,” he proposed adding three other items (Possession or control, Authenticity, and Utility) to the list that eventually became known as the Parkerian Hexad. The idea never really caught on but I suspect his three additional elements are close to what Gutic is proposing with his 3C Model. We will explore that in Part 3 of this series.

The point is that between the Saltzer and Schroeder Paper (1975) and the Parker book (1998), the “CIA Triad” phrase wasn’t in common usage by the emerging security community.

That said, in 1991, John McCumber published “Information Systems Security: A Comprehensive Model at the 14th Annual National Computer Security Conference (NCSC). He doesn’t coin the phrase “CIA Triad” in the paper but he does say that the three elements are a triad.

I think this is the origin story of the phrase.

I reached out to John to see if he thought he was the originator. He was quick to point out that the “CIA Triad” idea was in the air. At the time, he was working for the NSA with a bunch of very smart people: Dr Paul Peters, Bob Morris, Steve LaFountain and other pioneers at Trusted Information Systems. His boss was Bob Morris Sr., father to Robert Tappan Morris junior, the guy that destroyed the internet for a week back in 1988 with the Morris worm. John said that he had learned of the triad concept from Dr Steve LaFountain.

But, because John was the first guy to get the idea published, by the laws of the Royal Society of “Who Gets Credit” (that I just made up), I hereby dub John as the originator of the “CIA Triad” phrase. We need some awards music playing in the background and an official parchment signed by somebody with a British accent.

But, like I said, the phrase wasn’t in common use. I believe that started to change in the late 1990s. (ISC)² codified the Common Body of Knowledge (CBK) in 1997 and the “Official Guide to the CISSP” began using the phrase explicitly. Exam questions using the phrase started appearing soon after; sometime around the 1998–1999 exam cycle. Before 1997, CISSP certification seekers were tested on confidentiality, integrity, availability), but not the acronym. From \~1998 onward, they had to recognize and correctly use the term “CIA Triad” to pass.

And that’s how an idea becomes a best practice.

# Take Away

This was Part I of a three part series. Now that we know where the idea came from, I will take a look at the notion that the CIA Triad is the cybersecurity’s first principle strategy as indicated by the CISSP exam, or, if Donn Parker and Loris Gutic were on to something, it’s not adequate at all.

# Source

Loris Gutic, 2025. **The CIA triad is dead — stop using a Cold War relic to fight 21st century threats** \[Analysis\]. CSO Online. URL https://www.csoonline.com/article/4070548/the-cia-triad-is-dead-stop-using-a-cold-war-relic-to-fight-21st-century-threats.html

# Reference

James Anderson, Eldred Nelson, Melvin Conway, Bruce Peters, Daniel Edwards, Charles Rose, Hilda Faust, Clark Weissman, Steven Lipner, October 1972, **Computer Security Technology Planning Study, Volume 1 - Executive Summary** \[Contracted Research Paper\] US Air Force Information Systems Technology Division (Command and Management Systems) - Computer Security Resource Center - NIST. URL [https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ande72a.pdf](https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ande72a.pdf)

James Anderson, Eldred Nelson, Clark Weissman, Bruce Peters, E. L. Glaser Steven Lipner, October 1972, **Computer Security Technology Planning Study, Volume 2 - Executive Summary** \[Contracted Research Paper\] US Air Force Information Systems Technology Division (Command and Management Systems) - Computer Security Resource Center - NIST. URL [https://csrc.nist.rip/publications/history/ande72.pdf](https://csrc.nist.rip/publications/history/ande72.pdf)

Rick Howard, 2023. **Cybersecurity First Principles: A Reboot of Strategy and Tactics** \[Book\]. Amazon. URL https://www.amazon.com/Cybersecurity-First-Principles-Strategy-Tactics-ebook/dp/B0C35HQFC3/ref=sr\_1\_1

Donn Parker, 1983. **Fighting Computer Crime: A New Framework for Protecting Information** \[Book\]. Goodreads. URL https://www.goodreads.com/book/show/605372.Fighting\_Computer\_Crime

John R. McCumber, October 1991. **Information Systems Security: A Comprehensive Model** \[Proceedings\] 14th Annual National Computer Security Conference (NCSC), National Institute of Standards and Technology (NIST) / National Computer Security Center (NCSC), Baltimore, Maryland, 1–4 October 1991, pp. 328–337. URL https://people.cs.georgetown.edu/\~clay/classes/spring2009/555/papers/McCumber91.pdf

Jennifer Cawthra (NIST), Michael Ekstrom (MITRE), Lauren Lusty (MITRE), Julian Sexton (MITRE), John Sweetnam (MITRE), 2020. **NIST SPECIAL PUBLICATION 1800-25: Data Integrity: Identifying and Protecting Assets Against Ransomware and Other Destructive Events** \[Report\] Computer Security Resource Center - NIST. URL: https://csrc.nist.gov/pubs/sp/1800/25/final

JEROME H. SALTZER and  MICHAEL D. SCHROEDER, 1974. **The Protection of Information in Computer Systems** \[Journal Article\]. Fourth ACM Symposium on Operating System Principles (October 1973). Revised version in Communications of the ACM 17, 7 (July 1974). University of Virginia. URL www.cs.virginia.edu/\~evans/cs551/saltzer/

Willis H. Ware et al, 11 February 1970. **The Ware Report: SECURITY CONTROLS FOR  COMPUTER SYSTEMS (U): Report of Defense Science Board** \[Study\] Defense Science Board - Task Force on Computer System Security - The Rand Corporation - Computer Security Resource Center - NIST. URL [https://csrc.nist.gov/csrc/media/publications/conference-paper/1998/10/08/proceedings-of-the-21st-nissc-1998/documents/early-cs-papers/ware70.pdf](https://csrc.nist.gov/csrc/media/publications/conference-paper/1998/10/08/proceedings-of-the-21st-nissc-1998/documents/early-cs-papers/ware70.pdf)
