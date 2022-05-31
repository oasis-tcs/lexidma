# Examples {#examples}

This section gives examples which show how to use DMLex to model lexicographic resources. The examples are shown in three formalisms: ### NVH {.unnumbered .unlisted}, ### XML {.unnumbered .unlisted} and ### JSON {.unnumbered .unlisted}.

Each example is shown in NVH first. NVH (Name-Value Hierarchy)[^1] is a concise serialization language designed for lexicographic data. ### NVH {.unnumbered .unlisted} encodes data as a hierarchical list of names, values and children, which corresponds exactly to DMLex’s own data model. We use NVH here in order to demonstrate the object model at an abstract level.

[^1]: [https://www.namevaluehierarchy.org/](https://www.namevaluehierarchy.org/)

After that, each example is shown in ### XML {.unnumbered .unlisted} and ### JSON {.unnumbered .unlisted}, two popular serialization languages. The ### XML {.unnumbered .unlisted} and ### JSON {.unnumbered .unlisted} encoding shown here follows DMLex’s own implementation guidance for ### XML {.unnumbered .unlisted} and ### JSON {.unnumbered .unlisted}.


## A basic entry {#ex00}

This is a basic, beginner-level example of how to use DMLex to represent a simple monolingual lexicographic resource consisting of one entry with two senses. It demonstrates some of the basic features of DMLex Core: how to subdivide a entry into senses, how attach various data such as definition, part-of-speech labels to entries and senses, and how to add labels to various objects such as senses and examples.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: my-dictionary
    entry: abandon-verb
        headword: abandon
        partOfSpeech: verb
        sense: abandon-verb-1
            definition: to suddenly leave a place or a person
            example: I'm sorry I abandoned you like that.
            example: Abandon ship!
                label: idiom
        sense: abandon-verb-2
            label: mostly-passive
            definition: to stop supporting an idea
            example: That theory has been abandoned.
```

### XML {.unnumbered .unlisted}

```xml
<lexicographicResource id="my-dictionary">
    <entry id="abandon-verb">
        <headword>abandon</headword>
        <partOfSpeech value="verb"/>
        <sense id="abandon-verb-1">
            <definition>to suddenly leave a place or a person</definition>
            <example>
                <text>I'm sorry I abandoned you like that.</text>
            </example>
            <example>
                <text>Abandon ship!</text>
                <label value="idiom"/>
            </example>
        <sense id="abandon-verb-2">
            <label value="mostly-passive"/>
            <definition>to stop supporting an idea</definition>
            <example>
                <text>That theory has been abandoned.</text>
            </example>
        </sense>
    </entry>
<lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-dictionary",
    "entry": {
        "id": "abandon-verb",
        "headword": "abandon",
        "partsOfSpeech": ["verb"],
        "senses": [{
            "id": "abandon-verb-1",
            "definitions": [{
                "text": "to suddenly leave a place or a person"
            }],
            "examples": [{
                "text": "I'm sorry I abandoned you like that."
            }, {
                "text": "Abandon ship!",
                "labels": ["idiom"]
            }]
        }, {
            "id": "abandon-verb-2",
            "labels": ["mostly-passive"],
            "definitions": ["to stop supporting an idea"],
            "examples": [{
                "text": "That theory has been abandoned."
            }]
        }]
    }
}
```


## How to use `inflectedForm` {#ex01}

This is an entry from a hypothetical Irish dictionary for the headword "folúsghlantóir" ("vacuum cleaner") which gives its two inflected forms, the singular genitive and the plural.

### NVH {.unnumbered .unlisted}

```yaml
entry: folúsghlantóir-n
    headword: folúsghlantóir
    partOfSpeech: n-masc
    inflectedForm: folúsghlantóra
        inflectedTag: sg-gen
    inflectedForm: folúsghlantóirí
        inflectedTag: pl
    sense: ...
```

### XML {.unnumbered .unlisted}

```xml
<entry id="folúsghlantóir-n">
    <headword>folúsghlantóir</headword>
    <partOfSpeech value="n-masc"/>
    <inflectedForm inflectedTag="sg-gen">folúsghlantóra</inflectedForm>
    <inflectedForm inflectedTag="pl">folúsghlantóirí</inflectedForm>
    <sense>...</sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "folúsghlantóir-n",
    "headword": "folúsghlantóir",
    "partsOfSpeech": ["n-masc"],
    "inflectedForms": [{
        "text": "folúsghlantóra",
        "inflectedTag": "sg-gen",
    }, {
        "text": "folúsghlantóirí",
        "inflectedTag": "pl",
    }],
    "senses": [...]
}
```


## Pronunciation given as transcription {#ex02}

### NVH {.unnumbered .unlisted}

```yaml
entry: aardvark-noun
    headword: aardvark
    pronunciation:
        transcription: a:rdva:rk
    sense: ...
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Pronunciation given as a sound file {#ex03}

### NVH {.unnumbered .unlisted}

```yaml
entry: aardvark-noun
    headword: aardvark
    pronunciation:
        soundFile: aardvark.mp3
    sense: ...
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Pronunciation given both ways {#ex04}

### NVH {.unnumbered .unlisted}

```yaml
entry: aardvark-noun
    headword: aardvark
    pronunciation:
        transcription: a:rdva:rk
        soundFile: aardvark.mp3
    sense: ...
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## How to use `tag` {#ex05}

This is an entry from a hypothetical Irish dictionary for the headword "folúsghlantóir" ("vacuum cleaner"). The meaning of the various tags used in this entry is explained in the `tag` objects.

### NVH {.unnumbered .unlisted}

```yaml
entry: folúsghlantóir-n
    headword: folúsghlantóir
    partOfSpeech: n-masc
    inflectedForm: folúsghlantóra
        inflectedTag: sg-gen
    inflectedForm: folúsghlantóirí
        inflectedTag: pl
    sense: ...
    
tag: n-masc
    description: noun, masculine
    target: partOfSpeech
tag: n-fem
    description: noun, feminine
    target: partOfSpeech

tag: sg-gen
    description: singular genitive
    target: inflectedTag
    partOfSpeechConstraint: n-masc
    partOfSpeechConstraint: n-fem
tag: pl
    description: plural
    target: inflectedTag
    partOfSpeechConstraint: n-masc
    partOfSpeechConstraint: n-fem
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Mapping `tag` to external inventories {#ex06}

This shows how to map the value of a tag such as `n-masc` and `n-fem` to items in an external inventory such as LexInfo.

### NVH {.unnumbered .unlisted}

```yaml
tag: n-masc
    description: noun, masculine
    target: partOfSpeech
    sameAs: http://www.lexinfo.net/ontology/3.0/lexinfo#noun
    sameAs: http://www.lexinfo.net/ontology/3.0/lexinfo#masculine
tag: n-fem
    description: noun, feminine
    target: partOfSpeech
    sameAs: http://www.lexinfo.net/ontology/3.0/lexinfo#noun
    sameAs: http://www.lexinfo.net/ontology/3.0/lexinfo#feminine
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Defining a bilingual lexicographic resource {#ex07}

This defines a lexicographic resource where the source language is German and the translation language is English and the English translations are going to come with pronunciation transcriptions in English IPA.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: deueng
    description: My German-English Dictionary
    language: de
    translationLanguage: en
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Defining a multilingual lexicographic resource {#ex10}

This defines a lexicographic resource where the source language is Irish and the translation languages are English, German and Czech.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: irish-multilingual
    description: My Irish-Multilingual Dictionary
    language: ga
    translationLanguage: en
    translationLanguage: de
    translationLanguage: cs
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## How to use `headwordTranslation` in a bilingual lexicographic resource {#ex08}

This is an entry from a hypothetical English-German dictionary for English-speaking learners of German.

### NVH {.unnumbered .unlisted}

```yaml
entry: doctor-n
    headword: doctor
    sense: doctor-n-1
        indicator: medical doctor
        headwordTranslation: Arzt
            partOfSpeech: n-masc
        headwordTranslation: Ärztin
            partOfSpeech: n-fem
    sense: doctor-n-2
        indicator: academic title
        headwordTranslation: Doktor
            partOfSpeech: n-masc
        headwordTranslation: Doktorin
            partOfSpeech: n-fem
            label: rare
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## How to use `headwordTranslation` in a multilingual lexicographic resource {#ex11}

This is an entry from a hypothetical Irish-multilingual dictionary.

### NVH {.unnumbered .unlisted}

```yaml
entry: fómhar-n
    headword: fómhar
    partOfSpeech: n-masc
    inflectedForm: fómhair
        inflectedTag: genitive-case
    sense: fómhar-n-1
        headwordTranslation: autumn
            language: en
        headwordTranslation: fall
            language: en
        headwordTranslation: Herbst
            language: de
        headwordTranslation: podzim
            language: cs
    sense: fómhar-n-2
        headwordTranslation: harvest
            language: en
        headwordTranslation: Ernte
            language: de
        headwordTranslation: sklizeň
            language: cs
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## How to use `headwordExplanation` {#ex09}

### NVH {.unnumbered .unlisted}

```yaml
entry: treppenwitz
    headword: Treppenwitz
    partOfSpeech: n-masc
    sense: treppenwitz-1
        headwordExplanation: belated realisation of what one could have said
        headwordTranslation: staircase wit
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Modelling parts and wholes {#ex12}

We have three entries with one sense each: "glasses", "microscope" and "lens". We want to represent the fact that "lens" is a meronym of both "glasses" and "microscope", and simultanously that "glasses" and "microscope" are both holonyms of "lens".

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en

    entry: glasses
        headword: glasses
        sense: glasses-1
            definition: an optical seeing aid
    entry: microscope
        headword: microscope
        sense: microscope-1
            definition: equipment for looking at very small things
    entry: lens
        headword: lens
        sense: lens-1
            definition: curved glass that makes things seem bigger
        
    relation: meronymy
        member: glasses-1
            role: whole
        member: lens-1
            role: part
    relation: meronymy
        member: microscrope-1
            role: whole
        member: lens-1
            role: part
        
    relationType: meronomy
        description: used for modelling part-whole relationships 
        memberRole: whole
            description: the whole
            memberType: sense
            min: 1
            max: 1
            action: navigate
        memberRole: part
            description: the part
            memberType: sense
            min: 1
            max: 1
            action: navigate
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD

### Suggested rendering for human users {.unnumbered .unlisted}

> **lens**
> 
> -  curved glass that makes things seem bigger  
>     _things that contain lens:_ **glasses**, **microscope**


## Modelling antonyms {#ex13}

We have two entries for the verbs "buy" and "sell" with one sense each. We want to express the fact that the senses are antonyms.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en
    entry: buy
        headword: buy
        sense: buy-1
            definition: get something by paying money for it
    entry: sell
        headword: sell
        sense: see-1
            definition: exchange something for money
        
    relation: ants
        member: buy-1
        member: sell-1
        
    relationType: ants
        description: antonyms
        memberRole:
            memberType: sense
            min: 2
            max: 2
            action: navigate
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD

### Suggested rendering for human users {.unnumbered .unlisted}

> **buy**
> 
> -  get something by paying money for it   
>     _opposite meaning:_ **sell**


## Modelling synonyms {#ex14}

We have three German entries with one sense each, two which mean "sea" and one which means "ocean". We want to set up a relation which brings these three sense together as near-synonyms.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: de
    translationLanguage: en

    entry: die-see
        headword: See
        partOfSpeech: n-fem	
        sense: die-see-1
            headwordTranslation: see

    entry: das-meer
        headword: Meer
        partOfSpeech: n-neut
        sense: das-meer-1
            headwordTranslation: see

    entry: der-ozean
        headword: Ozean
        partOfSpeech: n-masc
        sense: der-ozean-1
            translation: ocean
            
    relation: syns
        description: words that mean sea and ocean
        member: die-see-1
        member: das-meer-1
        member: der-ozean-1
        
    relationType: syns
        description: synonyms and near synonyms
        memberRole:
            memberType: sense
            min: 2
            action: navigate
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD

### Suggested rendering for human users {.unnumbered .unlisted}

> **See** _feminine noun_
> 
> -  sea   
>     _same or similar meaning:_ **Meer**, **Ozean**


## Modelling variants {#ex15}

We have two entries in our lexicographic resource, one for the headword "colour" and one for the headword "color". We want to create a relation to represent the fact that these are spelling variants.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en
    entry: colour
        headword: colour
        partOfSpeech: n
        label: europeanSpelling
        sense: colour-1
            definition: red, blue, yellow etc.
            example: What is your favourite colour?
    entry: color
        headword: color
        partOfSpeech: n
        label: americanSpelling
        
    relation: vars
        member: colour
        member: color
        
    relationType: vars
        description: variants, words which differ only in spelling
        memberRole:
            memberType: entry
            min: 2
            action: navigate
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD

### Suggested rendering for human users {.unnumbered .unlisted}

> **colour** _noun, European spelling_
> 
> -  red, blue, yellow etc.   
>     _What is your favourite colour?_
>
> see also: color


## Modelling subsenses {#ex16}

We have an entry for the noun "colour" with four senses. We want to express the fact that senses number two and three are subsenses of sense number one, and should be displayed as such to human users.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en
    
    entry: colour
        headword: colour
            sense: colour-1
                definition: red, blue, yellow etc.
                example: What is your favourite colour?
            sense: colour-2
                definition: not being black and white
                example: Back then owning a colour TV meant you were rich.
            sense: colour-3
                definition: a sign of a person's race
                example: We welcome people of all creeds and colours.
            sense: colour-4
                definition: interest or excitement
                example: Examples add colour to your writing.
                
    relation: subsensing
        member: colour-1
            role: supersense
        member: colour-2
            role: subsense
    relation: subsensing
        member: colour-1
            role: supersense
        member: colour-3
            role: subsense
            
    relationType: subsensing
        description: expresses the fact that a sense is a subsense of another sense
        scope: sameEntry
        memberRole: supersense
            memberType: sense
            min: 1
            max: 1
            action: none
        memberRole: subsense
            memberType: sense
            min: 1
            max: 1
            action: embed
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD

### Suggested rendering for human users {.unnumbered .unlisted}

> **colour**
> 
> 1.  red, blue, yellow etc.   
>     _What is your favourite colour?_
>     a.  not being black and white   
>         _Back then owning a colour TV meant you were rich._
>     b.  a sign of a person's race   
>         _We welcome people of all creeds and colours._
> 2.  interest or excitement   
>     _Examples add colour to your writing._


## Modelling subentries (at subsense level) {#ex17}

We have an entry for the adjective "safe" with two senses, and an entry for the multi-word expression "better safe than sorry" with one sense. We want to express the fact that the multi-word entry should appear under the first sense of "safe" as a subentry.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en

    entry: safe
        headword: safe
        sense: safe-1
            indicator: protected from harm
            example: It isn't safe to park here.
        sense: safe-2
            indicator: not likely to cause harm
            example: Is the ride safe for a small child?
    
    entry: better-safe
        headword: better safe than sorry
        sense:
            definition: you should be careful even if it seems unnecessary
    
    relation: subentrying
        membership: safe-2
            role: container
        membership: better-safe
            role: subentry
        
    relationType: subentrying
        scope: sameResource
        memberRole: container
            memberType: sense
            min: 1
            max: 1
            action: navigate
        memberRole: subentry
            memberType: entry
            min: 1
            max: 1
            action: embed
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD

### Suggested rendering for human users {.unnumbered .unlisted}

> **safe**
> 
> 1.  protected from harm: _It isn't safe to park here._
>     -  **better safe than sorry** you should be careful even if it seems unnecessary
> 2.  not likely to cause harm:  _Is the ride safe for a small child?_

Suggeted rendering of the entry "better safe than sorry" for human users:

> **better safe than sorry**
> 
> - you should be careful even if it seems unnecessary
> 
> see also: safe


## Modelling subentries (at sense level) {#ex18}

We have an entry for the word "bible" and another entry for the expression "the Bible". We want to make sure that, when a human user is viewing the entry for "bible", the entry for "the Bible" is shown as a subentry of it, as if it were its first sense.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en

    entry: the-bible
        headword: the Bible
        Sense: the-bible-1
            definition: the book considered holy by Christians

    entry: bible
        headword: bible 
        sense: bible-1
        sense: bible-2
            definition: a book considered important for a subject
    
    relation: subentrying
        member: bible-1
            role: container
        member: the-bible
            role: subentry
        
    relationType: subentrying
        scope: sameResource
        memberRole: container
            memberType: sense
            min: 1
            max: 1
            action: navigate
        memberRole: subentry
            memberType: entry
            min: 1
            max: 1
            action: embed
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD

### Suggested rendering for human users {.unnumbered .unlisted}

> **bible**
> 
> 1.  **the Bible** the book considered holy by Christians
> 2.  a book considered important for a subject

Suggeted rendering of the entry "the Bible" for human users:

> **the Bible**
> 
> - the book considered holy by Christians
> 
> see also: bible


## Using `placeholderMarker` {#ex19}

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en
    entry: continue-studies
        headword: continue your studies
            placeholderMarker: your
        sense: ...
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Using `placeholderMarker` in a bilingual lexicographic resource {#ex20}

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en
    translationLanguage: de
    entry: beat-up
        headword: beat sb. up
            placeholderMarker: sb.
        sense: beat-up-1
            headwordTranslation: jemanden verprügeln
                placeholderMarker: jemanden
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Using `headwordMarker` {#ex21}

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en
    translationLanguage: cs
    entry: autopsy
        headword: autopsy
        sense: autopsy-1
            headwordTranslation: pitva
            example: The coroner performed an autopsy.
                headwordMarker: autopsy
                exampleTranslation: Koroner provedl pitvu.
                    headwordMarker: pitvu
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD


## Using `itemMarker` {#ex22}

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource:
    language: en
    translationLanguage: cs
    entry: autopsy
        headword: autopsy
        sense: autopsy-1
            headwordTranslation: pitva
            example: The coroner performed an autopsy.
                headwordMarker: autopsy
                itemMarker: performed
                    lemma: perform
                exampleTranslation: Koroner provedl pitvu.
                    headwordMarker: pitvu
                    itemMarker: provedl
                        lemma: provést
```

### XML {.unnumbered .unlisted}

TBD

### JSON {.unnumbered .unlisted}

TBD
