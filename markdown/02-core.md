# DMLex Core

The DMLex Core provides data types for modelling monolingual dictionaries (called _lexicographic resources_ in DMLex) where headwords, definitions and examples are all in one and the same language. DMLex Core gives you the tools you need to model simple dictionary entries which consist of headwords, part-of-speech labels, senses, definitions and so on.

## `lexicographicResource`

Represents a dictionary. A lexicographic resource is a dataset which can be used, viewed and read by humans as a dictionary and – simultaneously – ingested, processed and understood by software agents as a machine-readable database. Note that the correct name of this data type in DMLex is _lexicographic_, not _lexical_, resource.

```yaml
lexicographicResource: <id>
    title: (0..1) <string>
    uri: (0..1) <uri>
    language: (1..1) <langCode>
    entry: (0..n)
    tag: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<lexicographicResource id="..." uri="..." language="...">
    <title>...</title>
    <entry.../>
    <tag.../>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "...",
    "title": "...",
    "language": "...",
    "entries": [...],
    "tags": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table lexicographicResources (
    id int primary key,
    title varchar(255),
    language varchar(10)
)
```

### Comments {.unnumbered .unlisted}

- `language` identifies the language of headwords, definitions and examples in this dictionary. DMLex is based on the assumption that all headwords in a lexicographic resource are in the same language, and that definitions and examples, if any occur in the lexicographic resource, are in that language too. The `language` child object of `lexicographicResource` informs potential users of the lexicographic resource which language that is.

- The main role of a lexicographic resource is to contain entries (`entry` objects). The other two object types that can optionally occur as children of a `lexicographicResource`, especially `tag`, are for lists of look-up values such as part-of-speech labels.

## `entry`

Represents a dictionary entry. An entry contains information about one headword.

```yaml
entry: <id>
    headword: (1..1) <string>
    homographNumber: (0..1) <number>
    partOfSpeech: (0..n)
    label: (0..n)
    pronunciation: (0..n)
    inflectedForm: (0..n)
    sense: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<entry id="..." homographNumber="...">
    <headword>...</headword>
    <partOfSpeech.../>
    <label.../>
    <pronunciation.../>
    <inflectedForm.../>
    <sense.../>
</entry>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "...",
    "headword": "...",
    "labels": [...],
    "pronunciations": [...],
    "inflectedForms": [...],
    "senses": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table entries (
    lexicographicResourceID int foreign key references lexicographicResource(id),
    id int primary key,
    headword varchar(255),
    homographNumber int
)
```

### Comments {.unnumbered .unlisted}

- `headword` contains entry's headword. The headword can be a single word, a multi-word expression, or any expression in the source language which is being described by the entry.

- Entries in DMLex do not have an explicit listing order. An application can imply a listing order from a combination of the headword and the homograph number.

- DMLex Core does not have a concept of 'subentry'. If you wish to have subentries (ie. entries inside entries) in your lexicographic resource you can use types from the Linking Module for that.

## `partOfSpeech`

Represents a part-of-speech label.

```yaml
partOfSpeech: <string>
    listingOrder: (1..1) <number>
```

### XML {.unnumbered .unlisted}

```xml
<partOfSpeech value="..."/>
```

### JSON {.unnumbered .unlisted}

```json
"..."
```

### SQL {.unnumbered .unlisted}

```sql
create table partsOfSpeech (
    entryID int foreign key references entries(id),
    value varchar(10),
    listingOrder int,
    id int primary key
)
```

### Comments {.unnumbered .unlisted}

- `partOfSpeech` is an abbreviation, a code or some other string of text which identifies the part-of-speech label, for example `n` for noun,  `v` for verb, `adj` for adjective. You can use the `tag` datatype to explain the meaning of the part-of-speech tags, to constrain which part-of-speech tags are allowed to occur in your lexicographic resource, and to map them onto external inventories and ontologies.

- If you want to model other grammatical properties of the headword besides part of speech, such as gender (of nouns) or aspect (of verbs), the way to do that in DMLex is to conflate them to the part-of-speech label, for example `noun-masc` and `noun-fem`, or `v-perf` and `v-imperf`. 

- `listingOrder` is the position of this part-of-speech label among other part-of-speech labels of the same entry. This can be implicit from the serialization.

## `sense`

Represents one of possibly many meanings (or meaning potentials) of the headword.

```yaml
sense: <id>
    listingOrder: (1..1) <number>
    indicator: (0..1) <string>
    label: (0..n)
    definition: (0..n)
    example: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<sense id="...">
    <indicator>...</indicator>
    <label.../>
    <definition.../>
    <example.../>
</sense>
```

### JSON {.unnumbered .unlisted}

```json
{
    "id": "...",
    "indicator": "...",
    "labels": [...],
    "definitions": [...],
    "examples": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table senses (
    entryID int foreign key references entries(id),
    id int primary key,
    indicator nvarchar(50),
    listingOrder int
)
```

### Comments {.unnumbered .unlisted}

- `listingOrder` represents the position of this sense among other senses of the same entry. Can be implicit from the serialization.

- `indicator` is a short statement, in the same language as the headword, that gives an indication of the meaning of a sense and permits its differentiation from other senses in the entry. Indicators are sometimes used in dictionaries instead of or in addition to definitions.

- `definition` is a statement, in the same language as the headword, that describes and/or explains the meaning of a sense. In DMLex, the term definition encompasses not only formal definitions, but also less formal explanations.

### Note {.unnumbered .unlisted} 

An **entry** is a container for formal properties of the headword such as orthography, morphology, syntax and pronunciation. A **sense** is a container for statements about the headword's semantics. DMLex deliberately makes it impossible to include morphological information at sense level. If you have an entry where each sense has slightly different morphological properties (eg. a noun has a weak plural in one sense and a strong plural in another) then, in DMLex, you need to treat it as two entries (homographs), and you can use the Linking Module two link the two entries together and to make sure they are always shown together to human users.

## `definition`

Represents one of possibly several definitions of a sense.

```yaml
definition: <string>
    definitionType: (0..1) <string>
    listingOrder: (1..1) <number>
```

### XML {.unnumbered .unlisted}

```xml
<definition definitionType="...">...</definition>
```

### JSON {.unnumbered .unlisted}

```json
{
    "text": "....",
    "definitionType": "..."
}
```

### SQL {.unnumbered .unlisted}

```sql
create table definitions (
    senseID int foreign key references sense(id),
    text nvarchar(255),
    definitionType nvarchar(10),
    listingOrder int,
    id int primary key
)
```

### Comments {.unnumbered .unlisted}

- If you have multiple definitions inside a single sense, you can use `definitionType` to indicate the difference between them, for example that they are intended for different audiences. Optionally, you can use the `tag` data type to constrain and/or explain the definition types that occur in your lexicographic resource.

- `listingOrder` is the position of this definition among other definitions of the same sense. This can be implicit from the serialization.


## `inflectedForm`

Represents one (of possibly many) inflected forms of the headword. See Example \ref{ex01}.

```yaml
inflectedForm: <string>
    inflectedTag: (0..1) <string>
    listingOrder: (1..1) <number>
    label: (0..n)
    pronunciation: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<inflectedForm inflectedTag="...">
    <text>...</text>
    <label.../>
    <pronunciation.../>
</inflectedTag>
```

### JSON {.unnumbered .unlisted}

```json
{
    "inflectedTag": "...",
    "text": "...",
    "labels": [...],
    "pronunciations": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table inflectedForms (
    entryID int foreign key references entries(id),
    inflectedTag varchar(10),
    text varchar(255),
    listingOrder int,
    id int primary key
)
```

### Comments {.unnumbered .unlisted}

- `inflectedTag` is an abbreviation, a code or some other string of text which identifies the inflected form, for example `pl` for plural,  `gs` for genitive singular, `com` for comparative. You can use the `tag` datatype to explain the meaning of the inflection tags, to constrain which inflection tags are allowed to occur in your lexicographic resource, and to map them onto external inventories and ontologies.

- The value of the `inflectedForm` object is the text of the inflected word itself.

- `listingOrder` is the position of this inflected form among other inflected forms of the same entry. This can be implicit from the serialization.

- The `inflectedForm` object is intended to model the **inflectional morphology** of a headword. To model derivational morphology, for example feminine forms of maculine nouns, the recommended way to do that in DMLex is to create separate entries for the two words, and link them using the Linking Module.

## `label`

Represents a restriction on its parent such as temporal (old-fashioned, neologism), regional (dialect), register (formal, colloquial), domain (medicine, politics) or grammar (singular-only).

```yaml
label: <string>
    listingOrder: (1..1) <number>
```

### XML {.unnumbered .unlisted}

```xml
<label value="..."/>
```

### JSON {.unnumbered .unlisted}

```json
"..."
```

### SQL {.unnumbered .unlisted}

```sql
create table labels (
    entryID int foreign key references entries(id),
    senseID int foreign key references senses(id),
    inflectedFormID int foreign key references inflectedForms(id),
    pronunciationID int foreign key references pronunciations(id),
    exampleID int foreign key references examples(id),
    value varchar(10),
    listingOrder int,
    id int primary key
)
```

### Comments {.unnumbered .unlisted}

- The value of the label object is an abbreviation, a code or some other string of text which identifies the label, for example `neo` for neologism,  `colloq` for colloquial, `polit` for politics. You can use the `tag` datatype to explain the meaning of the label tags, to constrain which label tags are allowed to occur in your lexicographic resource, and to map them onto external inventories and ontologies.

- `listingOrder` is the position of this label among other labels of the same entry. This can be implicit from the serialization.

- A label applies to the object that it is a child of. When the label is a child of `entry`, then it applies to the headword in all its senses. When the label is a child of `sense`, then it applies to the headword in that sense only (**not** including any subsenses linked to it using the Linking Module). When the label is a child of `inlectedForm`, then it applies only to that inflected form of the headword (in all senses). When the label is a child of `pronunciation`, then it applies only to that pronuciation of the headword (in all senses).

## `pronunciation`

Represents the pronunciation of its parent. See Examples \ref{ex02}, \ref{ex03}, \ref{ex04}.

```yaml
pronunciation: <empty>
    soundFile: (0..1) <uri>
    transcription: (0..n)
    listingOrder: (1..1) <number>
    label: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<pronunciation soundFile="...">
    <transcription.../>
    <label.../>
</pronunciation>
```

### JSON {.unnumbered .unlisted}

```json
{
    "soundFile": "...",
    "transcriptions": [...],
    "labels": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table pronunciations (
    entryID int foreign key references entries(id),
    soundFile varchar(255),
    listingOrder int,
    id int primary key
)
```

### Comments {.unnumbered .unlisted}

- `transcription` is the  transcription of the pronuciation in some notation, such as IPA. If more than transcription is present in a single pronuncuation object, then they must be different transcriptions (in different schemes) of the same pronunciation, eg. one in IPA and one in SAMPA.

- `soundFile` is a pointer to a file containing a sound recording of the pronunciation. 

- `listingOrder` is the position of this `pronunciation` object among other `pronunciation` objects of the same parent. This can be implicit from the serialization.

## `transcription`

Represents the transcription of a pronunciation in some notation such as IPA.

```yaml
transcription: <string>
    scheme: (0..1) <langCode>
    listingOrder: (1..1) <number>
```

### XML {.unnumbered .unlisted}

```xml
<transcription scheme="...">...</transcription>
```

### JSON {.unnumbered .unlisted}

```json
{
    "text": "...",
    "scheme": "..."
}
```

### SQL {.unnumbered .unlisted}

```sql
create table transcriptions (
    pronunciationID int foreign key references pronunciation(id),
    text varchar(255),
    scheme varchar(10),
    listingOrder int,
    id int primary key
) 
```

### Comments {.unnumbered .unlisted}

- `scheme` object identifies the transcription scheme used here. Example: `en-fonipa` for English IPA. This can be implicit if the lexicographic resource uses only one transcription scheme throughout.

- `listingOrder` is the position of this `transcription` object among other `transcription` objects of the same pronunciation. This can be implicit from the serialization.


## `example`

Represents a sentence or other text fragment which illustrates the headword being used.

```yaml
example: <string>
    sourceIdentity: (0..1) <string>
    sourceElaboration: (0..1) <string>
    label: (0..n)
    soundFile: (0..1) <uri>
    listingOrder: (1..1) <number>
```

### XML {.unnumbered .unlisted}

```xml
<example sourceIdentity="..." sourceElaboration="..." soundFile="...">
    <text>...</text>
    <label.../>
</example>
```

### JSON {.unnumbered .unlisted}

```json
{
    "text": "...",
    "sourceIdentity": "...",
    "sourceElaboration": "...",
    "labels": [...],
    "soundFile": "..."
}
```

### SQL {.unnumbered .unlisted}

```sql
create table examples (
    senseID int foreign key references senses(id),
    text varchar(255),
    sourceIdentity varchar(50),
    sourceElaboration varchar(255),
    soundFile varchar(255),
    id int primary key
) 
```

### Comments {.unnumbered .unlisted}

- `sourceIdentity` is an abbreviation, a code or some other string of text which identifies the source. You can use the `tag` datatype to explain the meaning of the source identifiers and to constrain which source identifiers are allowed to occur in your lexicographic resource.

- `sourceElaboration` is a free-form statement about the source of the example. If `source` is present, then `sourceElaboration` can be used for information where in the source the example can be found: page number, chapter and so on. If `sourceIdentity` is absent then `sourceElaboration` can be used to fully name the source.

- `soundFile` is a pointer to a file containing a sound recording of the example.

- `listingOrder` is the position of this example among other examples in the same sense. This can be implicit from the serialization.

## `tag`

Represents one (of many) possible values for `partOfSpeech`, `inflectedTag`, `label`, and `source`. See Example \ref{ex05}.

```yaml
tag: <string>
    description: (0..1) <string>
    target: (0..n) <symbol>
    partOfSpeechConstraint: (0..n) <string>
    sameAs: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<tag value="...">
    <description>...</description>
    <target value="..."/>
    <partOfSpeechConstraint value="..."/>
    <sameAs.../>
</tag>
```

### JSON {.unnumbered .unlisted}

```json
{
    "value": "...",
    "description": "...",
    "targets": ["..."],
    "partOfSpeechConstraints": ["..."],
    "sameAs": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table tags (
    lexicographicResourceID int foreign key references lexicographicResource(id),
    value varchar(10),
    description varchar(255),
    targets varchar(255), --comma-separated list
    partOfSpeechConstraints varchar(255), --comma-separated list
    id int primary key
)
```

### Comments {.unnumbered .unlisted}

- The value is an abbreviation, a code or some other string of text which identifies the source. If you want, you can design your implementation to enforce referential integrity between `tag` values on the one hand and  `partOfSpeech`, `inflectedTag` etc. objects on the other hand. In other words, you can make it so that the tags you define in `tag` objects are the only values allowed for `partOfSpeech`, `inflectedTag` etc. However, doing this is optional in DMLex. An implementation of DMLex is compliant regardless of whether it enforces referential integrity on `tag` values.

- `description` is a human-readable description of what the tag means.

- `target` tells us where exactly the tag is expected to be used. If omitted, then all four. The possible values are:
    - `partOfSpeech`: as the value of a `partOfSpeech` object
    - `inflectedTag`: as the value of an `inflectedTag` object
    - `sourceIdentity`: as the value of a `sourceIdentity` object
    - `label`: as the value of a `label` object
    - `definitionType`: as the value of a `definitionType` object
    - `collocateRole`: as the value of a `collocateRole` object

- `partOfSpeechConstraint`, if present, says that this tag is only intended to be used inside entries that are labelled with this part of speech. You can us this to constrain that, for example, only nouns and adjectives can have plurals but other parts of speech cannot.  

- `target` and `partOfSpeechConstraint` allow you to specify constraints on which tags are expected to appear where throughout the lexicographic resource. Enforcing these constraints in your implementation is optional.

## `sameAs`

Represents the fact that the parent object is equivalent to an item available from an external authority. See Example \ref{ex06}.

```yaml
sameAs: <uri>
```

### XML {.unnumbered .unlisted}

```xml
<sameAs uri="..."/>
```

### JSON {.unnumbered .unlisted}

```json
"..."
```

### SQL {.unnumbered .unlisted}

```sql
create table sameAs (
    tagID int foreign key references tags(id),
    uri varchar(255),
    id int primary key
)
```

### Comments {.unnumbered .unlisted}

- The value is the URI of an item in an external inventory.
