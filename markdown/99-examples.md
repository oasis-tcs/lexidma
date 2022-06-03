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

```xml
<entry id="aardvark-noun">
    <headword>aardvark</headword>
    <pronunciation>
        <transcription>a:rdva:rk</transcription>
    </pronunciation>
    <sense>...</sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "aardvark-noun",
    "headword": "aardvark",
    "pronunciations": [{
        "transcriptions": [{"text": "a:rdva:rk"}]
    }],
    "senses": [...]
}
```


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

```xml
<entry id="aardvark-noun">
    <headword>aardvark</headword>
    <pronunciation soundFile="aardvark.mp3"/>
    <sense>...</sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "aardvark-noun",
    "headword": "aardvark",
    "pronunciations": [{
        "soundFile": "aardvark.mp3"
    }],
    "senses": [...]
}
```


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

```xml
<entry id="aardvark-noun">
    <headword>aardvark</headword>
    <pronunciation soundFile="aardvark.mp3">
        <transcription>a:rdva:rk</transcription>
    </pronunciation>
    <sense>...</sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "aardvark-noun",
    "headword": "aardvark",
    "pronunciations": [{
        "soundFile": "aardvark.mp3",
        "transcriptions": [{"text": "a:rdva:rk"}]
    }],
    "senses": [...]
}
```


## How to use `tag` {#ex05}

This is an entry from a hypothetical Irish dictionary for the headword "folúsghlantóir" ("vacuum cleaner"). The meaning of the various tags used in this entry is explained in the `tag` objects.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: my-irish-dictionary
    language: ga
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

```xml
<lexicographicResource id="my-irish-dictionary" language="ga">
    <entry id="folúsghlantóir-n">
        <headword>folúsghlantóir</headword>
        <partOfSpeech value="n-masc"/>
        <inflectedForm inflectedTag="sg-gen">folúsghlantóra</inflectedForm>
        <inflectedForm inflectedTag="pl">folúsghlantóirí</inflectedForm>
        <sense>...</sense>
    </entry>
    <tag value="n-masc">
        <description>noun, masculine</description>
        <target value="partOfSPeech"/>
    </tag>
    <tag value="n-fem">
        <description>noun, feminine</description>
        <target value="partOfSPeech"/>
    </tag>
    <tag value="sg-gen">
        <description>singular genitive</description>
        <target value="inflectedTag"/>
        <partOfSpeechConstraint value="n-masc"/>
        <partOfSpeechConstraint value="n-fem"/>
    </tag>
    <tag value="pl">
        <description>plural</description>
        <target value="inflectedTag"/>
        <partOfSpeechConstraint value="n-masc"/>
        <partOfSpeechConstraint value="n-fem"/>
    </tag>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-irish-dictionary",
    "language": "ga",
    "entries": [{
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
    }],
    "tags": [{
        "value": "n-masc",
        "description": "noun, masculine",
        "targets": ["partOfSpeech"]
    }, {
        "value": "n-fem",
        "description": "noun, feminine",
        "targets": ["partOfSpeech"]
    }, {
        "value": "sg-gen",
        "description": "singular genitive",
        "targets": ["inflectedTag"],
        "partOfSpeechConstraints": ["n-masc", "n-fem"]
    }, {
        "value": "pl",
        "description": "plural",
        "targets": ["inflectedTag"],
        "partOfSpeechConstraints": ["n-masc", "n-fem"]
    }]
}
```


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

```xml
<tag value="n-masc">
    <description>noun, masculine</description>
    <target value="partOfSPeech"/>
    <sameAs uri="http://www.lexinfo.net/ontology/3.0/lexinfo#noun"/>
    <sameAs uri="http://www.lexinfo.net/ontology/3.0/lexinfo#masculine"/>
</tag>
<tag value="n-fem">
    <description>noun, feminine</description>
    <target value="partOfSPeech"/>
    <sameAs uri="http://www.lexinfo.net/ontology/3.0/lexinfo#noun"/>
    <sameAs uri="http://www.lexinfo.net/ontology/3.0/lexinfo#feminine"/>
</tag>
```

### JSON {.unnumbered .unlisted}

```json
{
    "tags": [{
        "value": "n-masc",
        "description": "noun, masculine",
        "targets": ["partOfSpeech"],
        "sameAs": [
            "http://www.lexinfo.net/ontology/3.0/lexinfo#noun",
            "http://www.lexinfo.net/ontology/3.0/lexinfo#masculine"
        ]
    }, {
        "value": "n-fem",
        "description": "noun, feminine",
        "targets": ["partOfSpeech"],
        "sameAs": [
            "http://www.lexinfo.net/ontology/3.0/lexinfo#noun",
            "http://www.lexinfo.net/ontology/3.0/lexinfo#feminine"
        ]
    }]
}
```


## Defining a bilingual lexicographic resource {#ex07}

This defines a lexicographic resource where the source language is German and the translation language is English and the English translations are going to come with pronunciation transcriptions in English IPA.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: deueng
    title: My German-English Dictionary
    language: de
    translationLanguage: en
```

### XML {.unnumbered .unlisted}

```xml
<lexicographicResource id="deueng" language="de">
    <title>My German-English Dictionary</title>
    <translationLanguage langCode="en"/>
    ...
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "deueng",
    "title": "My German-English Dictionary",
    "language": "de",
    "translationLanguages": ["en"],
    ...
}
```


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

```xml
<lexicographicResource id="irish-multilingual" language="ga">
    <title>My Irish-Multilingual Dictionary</title>
    <translationLanguage langCode="en"/>
    <translationLanguage langCode="de"/>
    <translationLanguage langCode="cs"/>
    ...
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "irish-multilingual",
    "title": "My Irish-Multilingual Dictionary",
    "language": "ga",
    "translationLanguages": ["en", "de", "cs"],
    ...
}
```


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

```xml
<entry id="doctor-n">
    <headword>doctor</headword>
    <sense id="doctor-n-1">
        <indicator>medical doctor</indicator>
        <headwordTranslation>
            <text>Arzt</text>
            <partOfSpeech value="n-masc"/>
        </headwordTranslation>
        <headwordTranslation>
            <text>Ärztin</text>
            <partOfSpeech value="n-fem"/>
        </headwordTranslation>
    </sense>
    <sense id="doctor-n-2">
        <indicator>academic title</indicator>
        <headwordTranslation>
            <text>Doktor</text>
            <partOfSpeech value="n-masc"/>
        </headwordTranslation>
        <headwordTranslation>
            <text>Doktorin</text>
            <partOfSpeech value="n-fem"/>
        </headwordTranslation>
    </sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "doctor-n",
    "headword": "doctor",
    "senses": [{
        "id": "doctor-n-1",
        "indicator": "medical doctor",
        "headwordTranslations": [{
            "text": "Arzt",
            "partsOfSpeech": ["n-masc"]
        }, {
            "text": "Ärztin",
            "partsOfSpeech": ["n-fem"]
        }]
    }, {
        "id": "doctor-n-2",
        "indicator": "academic title",
        "headwordTranslations": [{
            "text": "Doktor",
            "partsOfSpeech": ["n-masc"]
        }, {
            "text": "Doktorin",
            "partsOfSpeech": ["n-fem"]
        }]
    }]
}
```


## How to use `headwordTranslation` in a multilingual lexicographic resource {#ex11}

This is an entry from a hypothetical Irish-multilingual dictionary.

### NVH {.unnumbered .unlisted}

```yaml
entry: fómhar-n
    headword: fómhar
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

```xml
<entry id="fómhar-n">
    <headword>fómhar</headword>
    <sense id="fómhar-n-1">
        <headwordTranslation language="en">
            <text>autumn</text>
        </headwordTranslation>
        <headwordTranslation language="en">
            <text>fall</text>
        </headwordTranslation>
        <headwordTranslation language="de">
            <text>Herbst</text>
        </headwordTranslation>
        <headwordTranslation language="cs">
            <text>podzim</text>
        </headwordTranslation>
    </sense>
    <sense id="fómhar-n-2">
        <headwordTranslation language="en">
            <text>harvest</text>
        </headwordTranslation>
        <headwordTranslation language="de">
            <text>Ernte</text>
        </headwordTranslation>
        <headwordTranslation language="cs">
            <text>sklizeň</text>
        </headwordTranslation>
    </sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "fómhar-n",
    "headword": "fómhar",
    "senses": [{
        "id": "fómhar-n-1",
        "headwordTranslations": [{
            "language": "en",
            "text": "autumn"
        }, {
            "language": "en",
            "text": "fall"
        }, {
            "language": "de",
            "text": "Herbst"
        }, {
            "language": "cs",
            "text": "podzim"
        }]
    }, {
        "id": "fómhar-n-2",
        "headwordTranslations": [{
            "language": "en",
            "text": "harvest"
        }, {
            "language": "de",
            "text": "Ernte"
        }, {
            "language": "cs",
            "text": "sklizeň"
        }]
    },]
}
```


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

```xml
<entry id="treppenwitz">
    <headword>Treppenwitz</headword>
    <partOfSpeech value="n-masc"/>
    <sense id="treppenwitz-1">
        <headwordExplanation>
            belated realisation of what one could have said
        </headwordExplanation>
        <headwordTranslation>
            <text>staircase wit</text>
        </headwordTranslation>
    </sense>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "treppenwitz",
    "headword": "Treppenwitz",
    "partsOfSpeech": ["n-masc"],
    "senses": [{
        "id": "treppenwitz-1",
        "headwordExplanations": [{
            "text": "belated realisation of what one could have said"
        }],
        "headwordTranslations": [{
            "text": "staircase wit"
        }]
    }]
}
```


## Modelling parts and wholes {#ex12}

We have three entries with one sense each: "glasses", "microscope" and "lens". We want to represent the fact that "lens" is a meronym of both "glasses" and "microscope", and simultanously that "glasses" and "microscope" are both holonyms of "lens".

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: my-dictionary
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

```xml
<lexicographicResource id="my-dictionary" language="en">
    <entry id="glasses">
        <headword>glasses</headword>
        <sense id="glasses-1">
            <definition>an optical seeing aid</definition>
        </sense>
    </entry>
    <entry id="microscope">
        <headword>microscope</headword>
        <sense id="microscope-1">
            <definition>equipment for looking at very small things</definition>
        </sense>
    </entry>
    <entry id="lens">
        <headword>lens</headword>
        <sense id="lens-1">
            <definition>curved glass that makes things seem bigger</definition>
        </sense>
    </entry>
    <relation type="meronymy">
        <member idref="glasses-1" role="whole"/>
        <member idref="lens-1" role="part"/>
    </relation>
    <relation type="meronymy">
        <member idref="microscrope-1" role="whole"/>
        <member idref="lens-1" role="part"/>
    </relation>
    <relationType type="meronomy">
        <description>used for modelling part-whole relationships</description>
        <memberRole role="whole" memberType="sense"  min="1" max="1" action="navigate">
            <description>the whole</description>
        </memberRole>
        <memberRole role="part" memberType="sense" min="1" max="1" action="navigate">
            <description>the part</description>
        </memberRole>
    </relationType>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-dictionary",
    "language": "en",
    "entries": [{
        "id": "glasses",
        "headword": "glasses",
        "senses": [{
            "id": "glasses-1",
            "definition": "an optical seeing aid"
        }, {
        "id": "microscope",
        "headword": "microscope",
        "senses": [{
            "id": "microscope-1",
            "definition": "equipment for looking at very small things"
        }, {
        "id": "lens",
        "headword": "lens",
        "senses": [{
            "id": "lens-1",
            "definition": "curved glass that makes things seem bigger"
        }]
    }],
    "relations": [{
        "type": "meronymy",
        "members": [{
            "idref": "glasses-1",
            "role": "whole"
        }, {
            "idref": "lens-1",
            "role": "part"
        }]
    }, {
        "type": "meronymy",
        "members": [{
            "idref": "microscope-1",
            "role": "whole"
        }, {
            "idref": "lens-1",
            "role": "part"
        }]
    }],
    "relationTypes": [{
        "type": "meronymy",
        "description": "used for modelling part-whole relationships",
        "memberRoles": [{
            "role": "whole",
            "description": "the whole",
            "memberType": "sense",
            "min": 1,
            "max": 1,
            "action": "navigate"
        }, {
            "role": "part",
            "description": "the part",
            "memberType": "sense",
            "min": 1,
            "max": 1,
            "action": "navigate"
        }]
    }]
}
```

### Suggested rendering for human users {.unnumbered .unlisted}

> **lens**
> 
> -  curved glass that makes things seem bigger  
>     _things that contain lens:_ **glasses**, **microscope**


## Modelling antonyms {#ex13}

We have two entries for the verbs "buy" and "sell" with one sense each. We want to express the fact that the senses are antonyms.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: my-dictionary
    language: en
    entry: buy
        headword: buy
        sense: buy-1
            definition: get something by paying money for it
    entry: sell
        headword: sell
        sense: sell-1
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

```xml
<lexicographicResource id="my-dictionary" language="en">
    <entry id="buy">
        <headword>buy</headword>
        <sense id="buy-1">
            <definition>get something by paying money for it</definition>
        </sense>
    </entry>
    <entry id="sell">
        <headword>sell</headword>
        <sense id="sell-1">
            <definition>exchange something for money</definition>
        </sense>
    </entry>
    <relation type="ants">
        <member idref="buy-1"/>
        <member idref="sell-1"/>
    </relation>
    <relationType type="ants">
        <description>antonyms</description>
        <memberRole memberType="sense" min="2" max="2" action="navigate"/>
    </relationType>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-dictionary",
    "language": "en",
    "entries": [{
        "id": "buy",
        "headword": "buy",
        "senses": [{
            "id": "buy-1",
            "definition": "get something by paying money for it"
        }, {
        "id": "sell",
        "headword": "sell",
        "senses": [{
            "id": "sell-1",
            "definition": "exchange something for money"
        }]
    }],
    "relations": [{
        "type": "ants",
        "members": [
            {"idref": "buy-1"},
            {"idref": "sell-1"}
        ]
    }],
    "relationTypes": [{
        "type": "ants",
        "description": "antonyms",
        "memberRoles": [{
            "memberType": "sense",
            "min": 2,
            "max": 2,
            "action": "navigate"
        }]
    }]
}
```

### Suggested rendering for human users {.unnumbered .unlisted}

> **buy**
> 
> -  get something by paying money for it   
>     _opposite meaning:_ **sell**


## Modelling synonyms {#ex14}

We have three German entries with one sense each, two which mean "sea" and one which means "ocean". We want to set up a relation which brings these three sense together as near-synonyms.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: my-dictionary
    language: de
    translationLanguage: en
    entry: die-see
        headword: See
        partOfSpeech: n-fem	
        sense: die-see-1
            headwordTranslation: sea
    entry: das-meer
        headword: Meer
        partOfSpeech: n-neut
        sense: das-meer-1
            headwordTranslation: sea
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

```xml
<lexicographicResource id="my-dictionary" language="en">
    <translationLanguage langCode="de"/>
    <entry id="die-see">
        <headword>See</headword>
        <partOfSpeech value="n-fem"/>
        <sense id="die-see-1">
            <headwordTranslation><text>sea</text></headwordTranslation>
        </sense>
    </entry>
    <entry id="das-meer">
        <headword>Meer</headword>
        <partOfSpeech value="n-neut"/>
        <sense id="das-meer-1">
            <headwordTranslation><text>sea</text></headwordTranslation>
        </sense>
    </entry>
    <entry id="der-ozean">
        <headword>Ozean</headword>
        <partOfSpeech value="n-masc"/>
        <sense id="der-ozean-1">
            <headwordTranslation><text>ocean</text></headwordTranslation>
        </sense>
    </entry>
    <relation type="syns">
        <description>words that mean sea and ocean</description>
        <member idref="die-see-1"/>
        <member idref="das-meer-1"/>
        <member idref="der-ozean-1"/>
    </relation>
    <relationType type="syns">
        <description>synonyms and near synonyms</description>
        <memberRole memberType="sense" min="2" action="navigate"/>
    </relationType>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-dictionary",
    "language": "de",
    "translationLanguages": ["en"],
    "entries": [{
        "id": "die-see",
        "headword": "See",
        "partsOfSpeech": ["n-fem"],
        "senses": [{
            "id": "die-see-1",
            "headwordTranslations": [{"text": "sea"}]
        }]
    }, {
        "id": "das-meer",
        "headword": "Meer",
        "partsOfSpeech": ["n-neut"],
        "senses": [{
            "id": "das-meer-1",
            "headwordTranslations": [{"text": "sea"}]
        }]
    }, {
        "id": "der-ozean",
        "headword": "OZean",
        "partsOfSpeech": ["n-masc"],
        "senses": [{
            "id": "der-ozean-1",
            "headwordTranslations": [{"text": "ocean"}]
        }]
    }],
    "relations": [{
        "type": "syns",
        "description": "words that mean sea and ocean",
        "members": [
          {"idref": "die-see-1"},
          {"idref": "das-meer-1"},
          {"idref": "der-ozean-1"}
        ]
    }],
    "relationTypes": [{
        "type": "syns",
        "description": "synonyms and near synonyms",
        "memberRoles": [{
            "memberType": "sense",
            "min": 2,
            "action": "navigate"
        }]
    }]
}
```

### Suggested rendering for human users {.unnumbered .unlisted}

> **See** _feminine noun_
> 
> -  sea   
>     _same or similar meaning:_ **Meer**, **Ozean**


## Modelling variants {#ex15}

We have two entries in our lexicographic resource, one for the headword "colour" and one for the headword "color". We want to create a relation to represent the fact that these are spelling variants.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: my-dictionary
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

```xml
<lexicographicResource id="my-dictionary" language="en">
    <entry id="colour">
        <headword>colour</headword>
        <partOfSpeech value="n"/>
        <label value="europeanSpelling"/>
        <sense id="colour-1">
            <definition>red, blue, yellow etc.</definition>
            <example><text>What is your favourite colour?</text></example>
        </sense>
    </entry>
    <entry id="color">
        <headword>color</headword>
        <partOfSpeech value="n"/>
        <label value="americanSpelling"/>
    </entry>
    <relation type="vars">
        <member idref="colour"/>
        <member idref="color"/>
    </relation>
    <relationType type="vars">
        <description>variants, words which differ only in spelling</description>
        <memberRole memberType="entry" min="2" action="navigate"/>
    </relationType>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-dictionary",
    "language": "en",
    "entries": [{
        "id": "colour",
        "headword": "colour",
        "partsOfSpeech": ["n"],
        "labels": ["europeanSpelling"],
        "senses": [{
            "id": "colour-1",
            "definitions": [{"text": "red, blue, yellow etc."}],
            "examples": [{"text": "What is your favourite colour?"}]
        }]
    }, {
        "id": "color",
        "headword": "color",
        "partsOfSpeech": ["n"],
        "labels": ["americanSpelling"]
    }],
    "relations": [{
        "type": "vars",
        "members": [
          {"idref": "colour"},
          {"idref": "color"}
        ]
    }],
    "relationTypes": [{
        "type": "vars",
        "description": "variants, words which differ only in spelling",
        "memberRoles": [{
            "memberType": "entry",
            "min": 2,
            "action": "navigate"
        }]
    }]
}
```

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
lexicographicResource: my-dictionary
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

```xml
<lexicographicResource id="my-dictionary" language="en">
    <entry id="colour">
        <headword>colour</headword>
        <sense id="colour-1">
            <definition>red, blue, yellow etc.</definition>
            <example><text>What is your favourite colour?</text></example>
        </sense>
        <sense id="colour-2">
            <definition>not being black and white</definition>
            <example><text>Back then owning a colour TV meant you were rich.</text></example>
        </sense>
        <sense id="colour-3">
            <definition>a sign of a person's race</definition>
            <example><text>We welcome people of all creeds and colours.</text></example>
        </sense>
        <sense id="colour-4">
            <definition>interest or excitement</definition>
            <example><text>Examples add colour to your writing.</text></example>
        </sense>
    </entry>
    <relation type="subsensing">
        <member idref="colour-1" role="supersense"/>
        <member idref="colour-2" role="subsense"/>
    </relation>
    <relation type="subsensing">
        <member idref="colour-1" role="supersense"/>
        <member idref="colour-3" role="subsense"/>
    </relation>
    <relationType type="subsensing" scope="sameEntry">
        <description>
            expresses the fact that a sense is a subsense of another sense
        </description>
        <memberRole role="supersense" memberType="sense" min="1" max="1"
                    action="none"/>
        <memberRole role="subsense" memberType="sense" min="1" max="1"
                    action="embed"/>
    </relationType>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-dictionary",
    "language": "en",
    "entries": [{
        "id": "colour",
        "headword": "colour",
        "senses": [{
            "id": "colour-1",
            "definitions": [{"text": "red, blue, yellow etc."}],
            "examples": [{"text": "What is your favourite colour?"}]
        }, {
            "id": "colour-2",
            "definitions": [{"text": "not being black and white"}],
            "examples": [{"text": "Back then owning a colour TV meant you were rich."}]
        }, {
            "id": "colour-3",
            "definitions": [{"text": "a sign of a person's race"}],
            "examples": [{"text": "We welcome people of all creeds and colours."}]
        }, {
            "id": "colour-4",
            "definitions": [{"text": "interest or excitement"}],
            "examples": [{"text": "Examples add colour to your writing."}]
        }]
    }],
    "relations": [{
        "type": "subsensing",
        "members": [
          {"role": "supersense", "idref": "colour-1"},
          {"role": "subsense", "idref": "colour-2"}
        ]
    }, {
        "type": "subsensing",
        "members": [
          {"role": "supersense", "idref": "colour-1"},
          {"role": "subsense", "idref": "colour-3"}
        ]
    }],
    "relationTypes": [{
        "type": "subsensing",
        "description": "expresses the fact that a sense is a subsense of another sense",
        "scope": "sameEntry",
        "memberRoles": [{
            "role": "supersense",
            "memberType": "sense",
            "min": 1,
            "max": 1,
            "action": "none"
        }, {
            "role": "subsense",
            "memberType": "sense",
            "min": 1,
            "max": 1,
            "action": "embed"
        }]
    }]
}
```

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
lexicographicResource: my-dictionary
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
        sense: better-safe-1
            definition: you should be careful even if it seems unnecessary
    relation: subentrying
        membership: safe-1
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

```xml
<lexicographicResource id="my-dictionary" language="en">
    <entry id="safe">
        <headword>safe</headword>
        <sense id="safe-1">
            <indicator>protected from harm</indicator>
            <example><text>It isn't safe to park here.</text></example>
        </sense>
        <sense id="safe-2">
            <indicator>not likely to cause harm</indicator>
            <example><text>Is the ride safe for a small child?</text></example>
        </sense>
    </entry>
    <entry id="better-safe">
        <headword>better safe than sorry</headword>
        <sense id="better-safe-1">
            <definition>
                <text>you should be careful even if it seems unnecessary</text>
            </definition>
        </sense>
    </entry>
    <relation type="subentrying">
        <member idref="safe-1" role="container"/>
        <member idref="better-safe" role="subentry"/>
    </relation>
    <relationType type="subentrying" scope="sameResource">
        <memberRole role="container" memberType="sense" min="1" max="1"
                    action="navigate"/>
        <memberRole role="subentry" memberType="entry" min="1" max="1"
                    action="embed"/>
    </relationType>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-dictionary",
    "language": "en",
    "entries": [{
        "id": "safe",
        "headword": "safe",
        "senses": [{
            "id": "safe-1",
            "indicator": "protected from harm",
            "examples": [{"text": "It isn't safe to park here."}]
        }, {
            "id": "safe-2",
            "indicator": "not likely to cause harm",
            "examples": [{"text": "Is the ride safe for a small child?"}]
        }]
    }, {
        "id": "better-safe",
        "headword": "better safe than sorry",
        "senses": [{
            "id": "better-safe-1",
            "definitions": [{
                "text": "you should be careful even if it seems unnecessary"
            }]
        }]
    }],
    "relations": [{
        "type": "subentrying",
        "members": [
          {"role": "container", "idref": "safe-1"},
          {"role": "subentry", "idref": "better-safe"}
        ]
    }],
    "relationTypes": [{
        "type": "subentrying",
        "scope": "sameResource",
        "memberRoles": [{
            "role": "container",
            "memberType": "sense",
            "min": 1,
            "max": 1,
            "action": "navigate"
        }, {
            "role": "subentry",
            "memberType": "entry",
            "min": 1,
            "max": 1,
            "action": "embed"
        }]
    }]
}
```

### Suggested rendering for human users {.unnumbered .unlisted}

> **safe**
> 
> 1.  protected from harm: _It isn't safe to park here._
>     -  **better safe than sorry** you should be careful even if it seems unnecessary
> 2.  not likely to cause harm:  _Is the ride safe for a small child?_

> **better safe than sorry**
> 
> - you should be careful even if it seems unnecessary
> 
> see also: safe


## Modelling subentries (at sense level) {#ex18}

We have an entry for the word "bible" and another entry for the expression "the Bible". We want to make sure that, when a human user is viewing the entry for "bible", the entry for "the Bible" is shown as a subentry of it, as if it were its first sense.

### NVH {.unnumbered .unlisted}

```yaml
lexicographicResource: my-dictionary
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

```xml
<lexicographicResource id="my-dictionary" language="en">
    <entry id="the-bible">
        <headword>the Bible</headword>
        <sense id="the-bible-1">
            <definition>
                <text>the book considered holy by Christians</text>
            </definition>
        </sense>
    </entry>
    <entry id="bible">
        <headword>bible</headword>
        <sense id="bible-1"/>
        <sense id="bible-2">
            <definition>
                <text>a book considered important for a subject</text>
            </definition>
        </sense>
    </entry>
    <relation type="subentrying">
        <member idref="bible-1" role="container"/>
        <member idref="the-bible" role="subentry"/>
    </relation>
    <relationType type="subentrying" scope="sameResource">
        <memberRole role="container" memberType="sense" min="1" max="1"
                    action="navigate"/>
        <memberRole role="subentry" memberType="entry" min="1" max="1"
                    action="embed"/>
    </relationType>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "my-dictionary",
    "language": "en",
    "entries": [{
        "id": "the-bible",
        "headword": "the Bible",
        "senses": [{
            "id": "the-bible-1",
            "definitions": [{"text": "the book considered holy by Christians"}]
        }]
    }, {
        "id": "bible",
        "headword": "bible",
        "senses": [{
            "id": "bible-1"
        }, {
            "id": "bible-2",
            "definitions": [{"text": "a book considered important for a subject"}]
        }]
    }],
    "relations": [{
        "type": "subentrying",
        "members": [
          {"role": "container", "idref": "bible-1"},
          {"role": "subentry", "idref": "the-bible"}
        ]
    }],
    "relationTypes": [{
        "type": "subentrying",
        "scope": "sameResource",
        "memberRoles": [{
            "role": "container",
            "memberType": "sense",
            "min": 1,
            "max": 1,
            "action": "navigate"
        }, {
            "role": "subentry",
            "memberType": "entry",
            "min": 1,
            "max": 1,
            "action": "embed"
        }]
    }]
}
```

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
entry: continue-studies
    headword: continue your studies
        placeholderMarker: your
    sense: ...
```

### XML {.unnumbered .unlisted}

```xml
<entry id="continue-studies">
    <headword>
        continue <placeholderMarker>your</placeholderMarker> studies
    </headword>
    <sense.../>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
  "id": "continue-studies",
  "headword": "continue your studies",
  "placeholderMarkers": [
     {"startIndex": 9, "endIndex": 13}
  ],
  "senses": [...]
}
```


## Using `placeholderMarker` in a bilingual lexicographic resource {#ex20}

### NVH {.unnumbered .unlisted}

```yaml
entry: beat-up
    headword: beat sb. up
        placeholderMarker: sb.
    sense: beat-up-1
        headwordTranslation: jemanden verprügeln
            placeholderMarker: jemanden
```

### XML {.unnumbered .unlisted}

```xml
<entry id="beat-up">
    <headword>
        beat <placeholderMarker>sb.</placeholderMarker> up
    </headword>
    <sense id="beat-up-1">
      <headwordTranslation>
        <text>
            <placeholderMarker>jemanden</placeholderMarker> verprügeln
        </text>
      </headwordTranslation>
    </sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
  "id": "beat-up",
  "headword": "beat sb. up",
  "placeholderMarkers": [
      {"startIndex": 5, "endIndex": 8}
  ],
  "senses": [{
    "id": "beat-up-1",
    "headwordTranslations": [{
      "text": "jemanden verprügeln",
      "placeholderMarkers": [
          {"startIndex": 0, "endIndex": 8}
      ],
    }]
  }]
}
```


## Using `headwordMarker` {#ex21}

### NVH {.unnumbered .unlisted}

```yaml
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

```xml
<entry id="autopsy">
    <headword>autopsy</headword>
    <sense id="autopsy-1">
        <headwordTranslation><text>pitva</text></headwordTranslation>
        <example>
            <text>
                The coroner performed an <headwordMarker>autopsy</headwordMarker>.
            </text>
            <exampleTranslation>
                <text>
                    Koroner provedl <headwordMarker>pitvu</headwordMarker>.
                </text>
            </exampleTranslation>
        </example>
    </sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
  "id": "autopsy",
  "headword": "autopsy",
  "senses": [{
    "id": "autopsy-1",
    "headwordTranslations": [{"text": "pitva"}],
    "examples": [{
      "text": "The coroner performed an autopsy.",
      "headwordMarkers": [
        {"startIndex": 25, "endIndex": 32}
      ],
      "exampleTranslations": [{
        "text": "Koroner provedl pitvu.",
        "headwordMarkers": [
          {"startIndex": 16, "endIndex": 21}
        ]
      }]
    }]
  }]
}
```


## Using `itemMarker` {#ex22}

### NVH {.unnumbered .unlisted}

```yaml
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

```xml
<entry id="autopsy">
    <headword>autopsy</headword>
    <sense id="autopsy-1">
        <headwordTranslation><text>pitva</text></headwordTranslation>
        <example>
            <text>
                The coroner <itemMarker lemma="perform">performed</itemMarker>
                an <headwordMarker>autopsy</headwordMarker>.
            </text>
            <exampleTranslation>
                <text>
                    Koroner <itemMarker lemma="provést">provedl</itemMarker>
                    <headwordMarker>pitvu</headwordMarker>.
                </text>
            </exampleTranslation>
        </example>
    </sense>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
  "id": "autopsy",
  "headword": "autopsy",
  "senses": [{
    "id": "autopsy-1",
    "headwordTranslations": [{"text": "pitva"}],
    "examples": [{
      "text": "The coroner performed an autopsy.",
      "headwordMarkers": [
        {"startIndex": 25, "endIndex": 32}
      ],
      "itemMarkers": [
        {"startIndex": 12, "endIndex": 21, "lemma": "perform"}
      ],
      "exampleTranslations": [{
        "text": "Koroner provedl pitvu.",
        "headwordMarkers": [
          {"startIndex": 16, "endIndex": 21}
        ],
        "itemMarkers": [
          {"startIndex": 8, "endIndex": 15, "lemma": "provést"}
        ],
      }]
    }]
  }]
}
```
