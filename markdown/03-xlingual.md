# DMLex Crosslingual Module

DMLex's Multilingual Module extends the Core and turns a monolingual lexicographic resource into a bilingual or multilingual one. A bilingual or multilingual lexicographic resource is a lexicographic resource with multiple (two or more) languages: the headwords and the examples are in one language (called the _headword language_ in DMLex) and their translations are in one or more other languages (called the _translation languages_ in DMLex).

## Extensions to `lexicographicResource`

Additional children:

```yaml
lexicographicResource: ...
    translationLanguage: (1...n)
```

### XML {.unnumbered .unlisted}

```xml
<lexicographicResource ...>
    ...
    <translationLanguage.../>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    ...,
    "translationLanguages": [...]
}
```

### SQL {.unnumbered .unlisted}

No changes needed.

## `translationLanguage`

Represents one of the languages in which translations are given in this lexicographic resource. See Examples \ref{ex07}, \ref{ex10}.

```yaml
translationLanguage: <langCode>
    listingOrder: (1..1) <number>
```

### XML {.unnumbered .unlisted}

```xml
<translationLanguage langCode=""/>
```

### JSON {.unnumbered .unlisted}

```json
"..."
```

### SQL {.unnumbered .unlisted}

```sql
create table translationLanguage (
    lexicographicResourceID int foreign key references lexicographicResources(id),
    langCode varchar(10) primary key,
    listingOrder int,
)
```

Comments

- `listingOrder` sets the order in which translations (of headwords and examples) should be shown. It outranks the listing order given in `headwordTranslation`, `headwordExplanation` and `exampleTranslation` objects.

## Extensions to `sense`

Additional children:

```yaml
sense: ...
    headwordExplanation: (0..n)
    headwordTranslation: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<sense ...>
    ...
    <headwordExplanation.../>
    <headwordTranslation.../>
    ...
</sense>
```

### JSON {.unnumbered .unlisted}

```json
{
    ...
    "headwordExplanations": {...},
    "headwordTranslations": {...},
    ...
}
```

### SQL {.unnumbered .unlisted}

No changes needed.

## `headwordTranslation`

Represents one of possibly multiple translations of a headword. See Examples \ref{ex08}, \ref{ex11}.

```yaml
headwordTranslation: <string>
    language: (0..1) <langCode>
    listingOrder: (1..1) <number>
    partOfSpeech: (0..n) <string>
    label: (0..n)
    pronunciation: (0..n)
    inflectedForm: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<headwordTranslation language="...">
    <text>...</text>
    <partOfSpeech.../>
    <label.../>
    <pronunciation.../>
    <inflectedForm.../>
</headwordTranslation>
```

### JSON {.unnumbered .unlisted}

```json
"headwordTranslations": {
    <language>: [{
        "text": "...",
        "partsOfSpeech": [...],
        "labels": [...],
        "pronunciations": [...],
        "inflectedForms": [...]
    }], 
    ...
}
```

### SQL {.unnumbered .unlisted}

```sql
create table headwordTranslations (
    senseID int foreign key references senses(id),
    language nvarchar(10) foreign key references translationLanguage(langCode),
    text nvarchar(255),
    listingOrder int,
    id int primary key
);
alter table partsOfSpeech (
    add headwordTranslationID int foreign key references headwordTranslations(id)
);
alter table labels (
    add headwordTranslationID int foreign key references headwordTranslations(id)
);
alter table pronunciations (
    add headwordTranslationID int foreign key references headwordTranslations(id)
);
alter table inflectedForms (
    add headwordTranslationID int foreign key references headwordTranslations(id)
)
```

Comments

- `language` indicates the language of this translation. You can use the `translationLanguage` datatype to explain the meaning of the language codes that appear here and/or to constrain which language codes are allowed.

- If ony one translation language exists in your lexicographic resource, then `language` can be left out.

- For more comments see comments under `headwordTranslation` in the Bilingual Module.

## `headwordExplanation`

Represents a statement in the target language which explains (but does not translate) the meaning of the headword. See Example \ref{ex09}.

```yaml
headwordExplanation: <string>
    language: (1..1) <langCode>
```

### XML {.unnumbered .unlisted}

```xml
<headwordExplanation language="...">...</headwordExplanation>
```

### JSON {.unnumbered .unlisted}

```json
"headwordExplanations": {
    <language>: "...", 
    ...
}
```

### SQL {.unnumbered .unlisted}

```sql
create table headwordExplanations (
    senseID int foreign key references senses(id),
    language nvarchar(10) foreign key references translationLanguage(langCode),
    text nvarchar(255),
    id int primary key
)
```

Comments

- `language` indicates the language of this explanation. You can use the `translationLanguage` datatype to explain the meaning of the language codes that appear here and/or to constrain which language codes are allowed.

- If ony one translation language exists in your lexicographic resource, then `language` can be left out.

- It is assume that there will always be a maximum of one `headwordExplanation` per translation language.

## Extensions to `example`

Additional children:

```yaml
sense: ...
    exampleTranslation: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<example ...>
    ...
    <exampleTranslation.../>
</example>
```

### JSON {.unnumbered .unlisted}

```json
{
    ...,
    "exampleTranslations": {...}
}
```

### SQL {.unnumbered .unlisted}

No changes needed.

## `exampleTranslation`

Represents the translation of an example.

```yaml
exampleTranslation: <string>
    language: (1..1) <langCode>
    soundFile: (0..1) <uri>
    listingOrder: (1..1) <number>
```
### XML {.unnumbered .unlisted}

```xml
<exampleTranslation language="..." soundFile="...">
    <text>...</text>
    <label.../>
</exampleTranslation>
```

### JSON {.unnumbered .unlisted}

```json
"exampleTranslations": {
    <language>: [{
        "text": "...",
        "labels": [...],
        "soundFile": "..."
    }],
    ...
}
```

### SQL {.unnumbered .unlisted}

```sql
create table exampleTranslations (
    exampleID int foreign key references examples(id),
    language varchar(10) foreign key references translationLanguage(langCode),
    text varchar(255),
    soundFile varchar(255),
    listingOrder int,
    id int primary key
);
alter table labels (
    add exampleTranslationID foreign key references exampleTranslations(id) 
)
```

Comments

- `language` indicates the language of this translation. You can use the `translationLanguage` datatype to explain the meaning of the language codes that appear here and/or to constrain which language codes are allowed.

- If ony one translation language exists in your lexicographic resource, then `language` can be left out.

- For more comments see commens under `exampleTranslation` in the Bilingual Module.

## Extensions to `tag`

Redefinition of  `partOfSpeechConstraint`:

- If present, says that:
    - If this tag is used inside a `headwordTranslation`, then it is intended to be used only inside a `headwordTranslation` labelled with this part of speech.
    - If this tag is used outside a `headwordTranslation`, then it is intended to be used only inside entries that are labelled with this part of speech.

Additional child:

```yaml
tag: ...
    translationLanguageConstraint: (0..n) <langCode>
```

### XML {.unnumbered .unlisted}

```xml
<tag ...>
    ...
    <translationLanguageConstraint langCode="..."/>
</tag>
```

### JSON {.unnumbered .unlisted}

```json
{
    ...,
    "translationLanguageConstraint": ["..."]
}
```

### SQL {.unnumbered .unlisted}

```sql
alter table tags (
    add translationLanguageConstraints varchar(255), --comma-separated list
)
```

Comments

- `translationLanguageConstraint`, if present, says that if this tag is being used inside a `headwordTranslation` or an `exampleTranslation`, then it is intended to be used only inside `headwordTranslation` and `exampleTranslation` objects labelled with this language.

- For a redefinition of  `partOfSpeechConstraint`, see see `tag` in the Bilingual Module.

