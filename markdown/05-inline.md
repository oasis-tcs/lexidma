# DMLex Inline Markup Module

This module makes it possible to mark up substrings inside the string values of certain objects and to attach properties to them.

It is up to the implementer to decide how to implement inline markup in an implementation of the DMLex Inline Markup module, whether _in-place_ (as XML) or as _stand-off_ markup (for example through start and end indexes).

## Extensions to `headword`

Additional children:

```yaml
headword: ...
    placeholderMarker: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<headword>
    ...<placeholderMarker>...</placeholderMarker>...
</headword>
```

### JSON {.unnumbered .unlisted}

```json
{
    ...,
    "headword": "...",
    "placeholderMarkers": [...],
    ...
}
```

### SQL {.unnumbered .unlisted}

No changes needed.

## Extensions to `headwordTranslation`

Additional children:

```yaml
headwordTranslation: ...
    placeholderMarker: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<headwordTranslation>
    <text>
        ...<placeholderMarker>...</placeholderMarker>...
    </text>
</headwordTranslation>
```

### JSON {.unnumbered .unlisted}

```json
{
    ...,
    "headwordTranslations": {
        <language>: [{
            "text": "...",
            "placeholderMarkers": [...],
            ...
        }], 
        ...
    },
    ...
}
```

### SQL {.unnumbered .unlisted}

No changes needed.

## Extensions to `example`

Additional children:

```yaml
example: ...
    headwordMarker: (0..n)
    itemMarker: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<example>
    <text>
        ...
        <headwordMarker>...</headwordMarker>
        ...
        <itemMarker...>...</itemMarker>
        ...
    </text>
</example>
```

### JSON {.unnumbered .unlisted}

```json
{
    "text": "...",
    "headwordMarkers": [...],
    "itemMarkers": [...],
    ...
}
```

### SQL {.unnumbered .unlisted}

No changes needed.

## Extensions to `exampleTranslation`

Additional children:

```yaml
exampleTranslation: ...
    headwordMarker: (0..n)
    itemMarker: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<exampleTranslation>
    <text>
        ...
        <headwordMarker>...</headwordMarker>
        ...
        <itemMarker...>...</itemMarker>
        ...
    </text>
</exampleTranslation>
```

### JSON {.unnumbered .unlisted}

```json
{
    "text": "...",
    "headwordMarkers": [...],
    "itemMarkers": [...],
    ...
}
```

### SQL {.unnumbered .unlisted}

No changes needed.

## Extensions to `definition`

Additional children:

```yaml
definition: ...
    headwordMarker: (0..n)
    itemMarker: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<definition...>
    ...
    <headwordMarker>...</headwordMarker>
    ...
    <itemMarker...>...</itemMarker>
    ...
</definition>
```

### JSON {.unnumbered .unlisted}

```json
{
    "text": "...",
    "headwordMarkers": [...],
    "itemMarkers": [...],
    ...
}
```

### SQL {.unnumbered .unlisted}

No changes needed.

## `placeholderMarker`

Marks up a substring inside a headword or inside a headword translation which is not part of the expression itself but stands for things that can take its place. An application can use the inline markup to format the placeholders differently from the rest of the text, to ignore the placeholder in full-text search, and so on. See Examples \ref{ex19}, \ref{ex20}.

```yaml
placeholderMarker: <string>
```

### XML {.unnumbered .unlisted}

```xml
<placeholderMarker>...</placeholderMarker>
```

### JSON {.unnumbered .unlisted}

```json
{
    "startIndex": ...,
    "endIndex": ...
}
```

### SQL {.unnumbered .unlisted}

```sql
create table placeholderMarkers (
    entryID int foreign key references entries(id),
    startIndex int,
    endIndex int,
    id int primary key
)
```

## `headwordMarker`

Marks up a substring inside an example, inside an example translation or inside a definition which corresponds to the headword (or to a translation of the headword). An application can use the inline markup to highlight the occurence of the headword for human readers through formatting. See Example \ref{ex21}.

```yaml
headwordMarker: <string>
```

### XML {.unnumbered .unlisted}

```xml
<headwordMarker>...</headwordMarker>
```

### JSON {.unnumbered .unlisted}

```json
{
    "startIndex": ...,
    "endIndex": ...
}
```

### SQL {.unnumbered .unlisted}

```sql
create table headwordMarkers (
    entryID int foreign key references entries(id),
    headwordTranslationID int foreign key references headwordTranslations(id),
    definitionID int foreign key references definitions(id),
    startIndex int,
    endIndex int,
    id int primary key
)
```

## `itemMarker`

Marks up a substring other than the headword inside an example, inside an example translation or inside a definition. An application can use the inline markup to highlight collocates or constituents. See Example \ref{ex22}.

```yaml
itemMarker: <string>
    lemma: (0..1) <string>
    itemRole: (0..n) <string>
```

### XML {.unnumbered .unlisted}

```xml
<itemMarker lemma="...">
    ...
    <itemRole value="..."/>
</itemMarker>
```

### JSON {.unnumbered .unlisted}

```json
{
    "startIndex": ...,
    "endIndex": ...,
    lemma: "...",
    itemRoles: ["..."]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table itemMarkers (
    entryID int foreign key references entries(id),
    headwordTranslationID int foreign key references headwordTranslations(id),
    definitionID int foreign key references definitions(id),
    startIndex int,
    endIndex int,
    lemma varchar(50),
    id int primary key
);
create table itemMarkerRoles (
    itemMarkerID int foreign key references itemMarkers(id),
    role: "...",
    id int primary key
)
```

### Comments {.unnumbered .unlisted}

- `lemma` is the lemmatized form of the collocate. An application can use it to provide a clickable link for the user to search for the lemma in the rest of the lexicographic resource or on the web. (If you want to link the collocate explicitly to a specific entry or to a specific sense in your lexicographic resource, or even in an external lexicographic resource, you can use the Linking Module for that.)

- `itemRole` can be used to communicate facts about the role of the item in the sentence, for example its syntactic role (subject, direct object etc.), its semantic role (agent, affected etc) or its semantic type (human, institution etc.) Optionally, you use the `tag` datatype to explain and/or constrain the item types that are allowed to appear in your lexicographic resource. 
