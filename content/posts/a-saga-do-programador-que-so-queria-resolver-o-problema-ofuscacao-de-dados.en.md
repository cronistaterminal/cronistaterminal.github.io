+++
title = 'The saga of the programmer who just wanted to solve the problem: Data obfuscation'
slug = 'the-saga-of-the-programmer-who-just-wanted-to-solve-the-problem-data-obfuscation-tb04'
date = 2026-11-19
draft = false
traducao = 'maquina'
num = '0000'
epoca = 'c. 1900 BC–2026'
tldr = "From strange hieroglyphs to Brazil's data protection law: why do we hide information, and how does a dev fix the bug without knowing whose data it is?"
tldr_long = 'For as long as there has been language, someone has wanted to hide something. I pass through Egypt, Mesopotamia and Aeneas Tacticus, arrive at the Enigma and the pillars of security - until the LGPD shows up with the question: how do I solve the problem without knowing who the user is?'
tags = ['security', 'cryptography', 'lgpd', 'python']
+++

## A light INTRODUCTION


I dare say that, very likely, from the moment language develops and the first societies take shape, the need to hide information arises. Maybe someone found a tree especially full of fruit and didn't want to share it, maybe someone knew of a better hunting ground. Either way, at some point, human beings felt the need to hide things from other humans.

That creates a problem, doesn't it? After all, I don't want the neighboring tribe to know where we catch so many fish, but at the same time I want to be able to talk about it with whoever I choose. How do we do that?

By inventing codes: maybe, instead of saying north, I say "where the sun gets lost", pointing to a mountain that blocks the sun, or maybe I simply call it "the sacred place".

The problem with what is passed on only by word of mouth is that the words get lost. But once we write them down, they gain the ability to cross generation after generation.

## Cryptography through the ages

Cryptography is easy for programmers to understand, but if we look at it through the lens of **history**, everything gets stranger and grayer: if we count the transformation of writing and "unusual writing" as a cryptographic act, the oldest case I found was reported by [David Kahn](https://en.wikipedia.org/wiki/David_Kahn_(writer)) in *The Codebreakers - The Story of Secret Writing*: the tomb of [Khnumhotep II](https://en.wikipedia.org/wiki/Khnumhotep_II) contained altered hieroglyphs that made it harder to understand[^kahn]. Nothing suggests, however, that the intent was to hide the meaning of the writing[^stauder]. Playfully, I see a lot of resemblance to the slang and memes of our own era.

{{< figure src="posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/khnumhotep-ii-hieroglifos.jpg"
    alt="Painting on the wall of the tomb of Khnumhotep II: a man in a patterned robe carries an ibex, next to hieroglyphs painted in red and black."
    cap="Detail of a painting from the tomb of Khnumhotep II, at Beni Hasan (c. 1900 BC), for illustration only: these are not the altered hieroglyphs cited by Kahn. Photo: Macquarie University, public domain, via Wikimedia Commons." >}}

If we assume that cryptography aims to hide its content, **setting aside the intent to protect that content**, we can look at Mesopotamia in the 17th century BC[^gadd] - [Gadd](https://en.wikipedia.org/wiki/C._J._Gadd) and [Thompson](https://en.wikipedia.org/wiki/Reginald_Campbell_Thompson) published a glazed tablet with a recipe that was later read as "enciphered" text by other researchers, such as [Caubet](https://www.idref.fr/026772639)[^caubet] and [Mollin](https://orcid.org/0000-0002-8750-883X)[^mollin]; however, [Diepenbroek](https://orcid.org/0000-0002-7804-7226), when citing that reading, warns of the bias in that interpretation, pointing out that the purpose may have been ritual rather than security[^diep-meso].

But if we bring intent and technique together, ciphers in this case, the oldest I found was by the Greek [Aeneas Tacticus](https://en.wikipedia.org/wiki/Aeneas_Tacticus), who describes in his book *On the Defence of Fortified Positions* (original: *Poliorkētiká*, Πολιορκητικά) a cipher that replaces vowels with dots, hiding the original message[^eneias]. I chose to leave out the scytale of [Lysander](https://en.wikipedia.org/wiki/Lysander) (late 5th century BC)[^plutarco] because of the dispute over whether it is just a myth or a proven reality[^kelly].

## We banged a rock until it threw sparks and started thinking. Now what?

When we talk about cryptography in computing, it's impossible not to talk about the Enigma. A feat of German mechanical and electrical engineering that changed how the world saw cryptography. Not long after, we would have computers, processes and specialized technologies that came as a consequence of the Enigma's existence.

{{< figure src="posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/enigma-bundesarchiv.jpg"
    alt="Black-and-white photo: hands typing on the keyboard of an Enigma machine, with the letters of the keys and of the lamp board visible."
    cap="A German air force signals auxiliary operating an Enigma, c. 1943. Photo: Bundesarchiv, Bild 183-2007-0705-502, CC BY-SA 3.0 DE." >}}

But as these machines stop being weapons of war and become both product and means of production, we start needing to encrypt data - whether because only some people may have access, because other systems will have access, or because legislation started to standardize its use. The *Ware Report* (1970), by [Willis Ware](https://en.wikipedia.org/wiki/Willis_Ware), already mentions the need to "[resist] accidental disclosures, internal subversion, and denial of use to legitimate users"[^ware]. But only in the early 1990s do we get the definition of the famous Pillars of Security, first documented (at least as far as I could find) by [ITSEC](https://en.wikipedia.org/wiki/Information_Technology_Security_Evaluation_Criteria).

> In this context, IT security means:
>
> - confidentiality - prevention of the unauthorised disclosure of information;
> - integrity - prevention of the unauthorised modification of information;
> - availability - prevention of the unauthorised withholding of information or resources.[^itsec]

These pillars are the first domino on the way to Brazil's General Data Protection Law (*Lei Geral de Proteção de Dados*, LGPD), from 2018[^lgpd].

But a problem arises: how can I, a developer, solve my system's problems without knowing a person's data?

## Mask of a Thousand Faces

> Instead of disappearing, the vampire who uses this power can pass as any stranger, someone ordinary in the area. Unlike other Obfuscate powers, this one lets its user interact and communicate with those they meet.[^vampiro]

The LGPD, in Article 5, item I[^lgpd], establishes that, whatever the information, if it can be used to identify a single user, it must be protected.

But think about it: how can I know a problem is happening to a user if I don't know who that user is?

I won't talk about observability, NDAs, or legal and approved agreements. I'll focus here on the obfuscation technique.

The Michaelis dictionary defines *ofuscação* (obfuscation) as:

> ***ofuscação***: The act or effect of obfuscating (oneself); obfuscation.
>
> ***ofuscar***: To make something lose its shine; to prevent from seeing or being seen; to cover (oneself), to darken (oneself), to cloud (oneself).[^michaelis]

In my professional life, what helped the most was, without a doubt, obfuscating data in an isolated environment. In practice: a protected production database, with no human access, is replicated, with its data altered, *ids* and financial information included, into a troubleshooting/staging environment. That database is recreated every day. The developer/support person receives the ticket, which already contains the obfuscated id (calculated automatically).

If we consider a simplified *serverless* environment, nothing stops the system itself, when a ticket comes in, from firing the trigger and adding the data to the troubleshooting environment, lowering the cost and the load of that environment. There must be a secret, an agreement between the environments, but it must be impossible to trace your way back to a person in production.

And the pillars are all there: nobody sees the real data (**confidentiality**), whoever investigates never changes production data (**integrity**), and support doesn't weigh on the production database (**availability**).

Separation of responsibilities is the key. For a system, what it does with a person matters more than who that person is.

{{< diagrama src="posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/fluxo-ofuscacao.en.svg" >}}

1. The application writes the data to the production database.
2. The production database sends a trigger (an event, not a database trigger).
3. The serverless function receives the trigger and obfuscates the data.
4. The obfuscated data is saved to the troubleshooting database.

And if we look at the database obfuscation, we can think of it like this Python pseudocode, showing how to obfuscate the id and the amount.

```python
import hashlib
import hmac
from decimal import Decimal

SECRET: bytes = read_secret("obfuscation")


def obfuscate_id(original_id: int) -> str:
    return hmac.new(SECRET, str(original_id).encode(), hashlib.sha256).hexdigest()[:16]


def obfuscate_amount(original_id: int, amount: Decimal) -> Decimal:
    factor = Decimal(int(obfuscate_id(original_id), 16) % 100 + 50) / 100
    return (amount * factor).quantize(Decimal("0.01"))


def on_trigger(event: Event) -> None:
    record = event.data
    troubleshooting_db.save(
        id=obfuscate_id(record.id),
        customer_id=obfuscate_id(record.customer_id),
        amount=obfuscate_amount(record.id, record.amount),
        status=record.status,
    )
```

In the end, the premise holds: since the beginning of time, the secret has never been in stopping people from reading, but in making sure only the right people understand.


[^kahn]: KAHN, David. *The Codebreakers: The Story of Secret Writing*. Macmillan, 1967,
    ch. 2. Cited via PINEAU, Roger. Review of *The Codebreakers*. *Studies in
    Intelligence*, vol. 12, no. 3, 1968. Available at
    [cia.gov](https://www.cia.gov/resources/csi/static/Review-The-Codebreakers.pdf).

[^stauder]: STAUDER, Andréas. "Introduction". In: KLOTZ, David; STAUDER, Andréas (eds.).
    *Enigmatic Writing in the Egyptian New Kingdom I*. 2020, pp. 1–5. Available at
    [web.archive.org](https://web.archive.org/web/20240909060622/https://archiv.ub.uni-heidelberg.de/propylaeumdok/5400/1/Stauder_Introduction_Enigmatic_Writing.pdf).

[^gadd]: GADD, C. J.; THOMPSON, R. Campbell. "A Middle-Babylonian Chemical Text".
    *Iraq*, vol. 3, no. 1, 1936, pp. 87–96. Available at
    [cambridge.org](https://cambridge.org/core/journals/iraq/article/middlebabylonian-chemical-text/F4B01DC7752095019833F30BE77CD2BD).

[^caubet]: CAUBET, Annie. "Vitreous Materials". In: ARUZ, J.; BENZEL, K.; EVANS, J. (eds.).
    *Beyond Babylon: Art, Trade, and Diplomacy in the Second Millennium B.C.* New York:
    The Metropolitan Museum of Art; New Haven: Yale University Press, 2008, pp. 419–434
    (read as a cipher on p. 421). Cited via DIEPENBROEK, 2020, p. 53, note 82.

[^mollin]: MOLLIN, Richard A. *Codes: The Guide to Secrecy From Ancient to Modern Times*.
    Boca Raton: Chapman & Hall/CRC, 2005, p. 5. Cited via DIEPENBROEK, 2020, p. 53,
    note 82.

[^diep-meso]: DIEPENBROEK, Martine L. M. *Myths and Histories of the Spartan scytale*.
    PhD thesis — University of Bristol, 2020, § 1.1, pp. 52–53. Available at
    [research-information.bris.ac.uk](https://research-information.bris.ac.uk/ws/files/263833703/Myths_and_Histories_of_the_Spartan_scytale_29_11_2020.pdf).

[^eneias]: AENEAS TACTICUS. *On the Defence of Fortified Positions*, 31.30–31.
    Trans. Illinois Greek Club, 1928. Available at
    [penelope.uchicago.edu](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Aeneas_Tacticus/E*.html).

[^plutarco]: PLUTARCH. *Life of Lysander*, 19.4–7. Trans. Bernadotte Perrin, 1916.
    Available at
    [penelope.uchicago.edu](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives/Lysander*.html).

[^kelly]: DIEPENBROEK, Martine L. M. *Myths and Histories of the Spartan scytale*.
    PhD thesis — University of Bristol, 2020, pp. 23–24, on KELLY, Thomas.
    "The Myth of the Skytale". *Cryptologia*, vol. 22, no. 3, 1998, pp. 244–260.
    Available at
    [research-information.bris.ac.uk](https://research-information.bris.ac.uk/ws/files/263833703/Myths_and_Histories_of_the_Spartan_scytale_29_11_2020.pdf).

[^ware]: WARE, Willis H. (ed.). *Security Controls for Computer Systems: Report of
    Defense Science Board Task Force on Computer Security*. RAND, R-609, 1970, p. vi.
    Available at
    [csrc.nist.gov](https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf).

[^itsec]: FRANCE; GERMANY; NETHERLANDS; UNITED KINGDOM. *Information Technology
    Security Evaluation Criteria (ITSEC)*, v. 1.2, 28 Jun. 1991, § 0.2. Available at
    [wiretapped.mirrorservice.org](https://wiretapped.mirrorservice.org/info/reference/cesg-publications/Information-Technology-Security-Evaluation-Criteria.pdf).

[^lgpd]: BRAZIL. Law No. 13,709, of August 14, 2018. General Personal Data Protection
    Law (*Lei Geral de Proteção de Dados Pessoais*, LGPD). In Portuguese. Available at
    [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).

[^vampiro]: *Vampiro: A Máscara*. 5th ed. Core book, p. 262. Brazilian edition of
    *Vampire: The Masquerade 5th Edition*, White Wolf, 2018. Quoted passage translated
    by us from the Brazilian edition.

[^michaelis]: MICHAELIS. "Ofuscação" and "ofuscar". *Michaelis — Dicionário Brasileiro
    da Língua Portuguesa*. Melhoramentos, online. In Portuguese; definitions translated
    by us. Available at
    [michaelis.uol.com.br](https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/ofusca%C3%A7%C3%A3o/)
    and [michaelis.uol.com.br](https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/ofuscar/).
