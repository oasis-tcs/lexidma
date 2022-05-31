# DMLex Linking Module

DMLex's Linking Module can be used to construct _relations_ between objects which "break out" of the tree-like parent-and-child hierarchy constructed from datatypes from the Core and from other modules. The Linking Module can be used to create relations between senses which are synonyms or antonyms, between entries whose headwords are homonyms or spelling variants, between senses which represent superordinate and subordinate concepts (eg. hypernyms and hyponyms, holonyms and meronyms), between entries and subentries, between senses and subsenses, and many others.

Each relation is represented in DMLex by an instance of the `relation` datatype. A relation brings two or more _members_ together. The fact that an object (such as a sense or an entry) is a member of a relation is represented in DMLex by an instance of the `member` datatype.

The Linking Module can be used to set up relations between objects inside the same lexicographic resource, or between objects residing in different lexicographic resources.

Relations themselves can be members of other relations.

See Examples ref{ex12}, \ref{ex13}, \ref{ex14}, \ref{ex15}, \ref{ex16}, \ref{ex17}, \ref{ex18}.

## Extensions to `lexicographicResource`

Additional children:

```yaml
lexicographicResource: ...
    relation: (0..n)
    relationType: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<lexicographicResource ...>
    ...
    <relation.../>
    <relationType.../>
</lexicographicResource>
```

### JSON {.unnumbered .unlisted}

```json
{
    ...,
    "relations": [...],
    "relationTypes": [...]
}
```

### SQL {.unnumbered .unlisted}

No changes needed.


## `relation`

Represents the fact that a relation exists between two or more objects.

```yaml
relation: <string>
    description: (0..1) <string>
    member: (2..n)
```

### XML {.unnumbered .unlisted}

```xml
<relation type="...">
    <description>...</description>
    <member.../>
</relation>
```

### JSON {.unnumbered .unlisted}

```json
{
    "type": "...",
    "description": "...",
    "members": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table relations (
    id int primary key,
    type varchar(10),
    description nvarchar(255)
)
```

Comments

- The value of a relation specifies what type of relation it is, for example a relation between synonyms or a relation between a sense and a subsense. Optionally, you can use `relationType` objects to explain those types and to constrain which types of relations are allowed to exist in your lexicographic resource.

- `description` is an optional human-readable explanation of this relation.

## `member`

Represents the fact that an object is a member of a relation.

```yaml
member: <idref>
    role: (0..1) <string>
    listingOrder: (1..1) <number>
    reverseListingOrder: (1..1) <number>
```

### XML {.unnumbered .unlisted}

```xml
<member idref="..." role="..." reverseListingOrder="..."/>
```

### JSON {.unnumbered .unlisted}

```json
{
    "idref": "...",
    "role": "...",
    "reverseListingOrder": "..."
}
```

### SQL {.unnumbered .unlisted}

```sql
create table members (
    lexicographicResourceID int foreign key references lexicographicResources(id),
    relationID int foreign key references relations(id),
    memberEntryID int foreign key references entries(id),
    memberSenseID int foreign key references senses(id),
    memberCollocateMarkerID int foreign key references collocateMarkers(id),
    role nvarchar(50),
    listingOrder int,
    reverseListingOrder int,
    id int primary key
)
```

Comments

- The value of `member` is the ID of an object, such as an entry or a sense.

- `role` is an indication of the role the member has in this relation: whether it is the hypernym or the hyponym (in a hyperonymy/hyponymy relation), or whether it is one of the synonyms (in a synonymy relation), and so on. You can use `membershipRole` objects to explain those roles and to constrain which relations are allowed to contain which roles, what their object types are allowed to be (eg. entries or senses) and how many members with this role each relation is allowed to have.

- `listingOrder` is the position of this member among other members of the same relation. It should be respected when showing members of the relation to human users. This can be implicit from the serialization.

- `reverseListingOrder` is the position of this relation among other relations this member is involved in. It should be respected when showing the relations of this member to a human user. This can be implicit from the serialization.

## `relationType`

Represents one of possible values for `relation`.

```yaml
relationType: <string>
    description: (0..1) <string>
    scope: (0..1) <symbol>
    sameAs: (0..n)
    memberRole: <0..n>
```

### XML {.unnumbered .unlisted}

```xml
<relationType type="..." scope="...">
    <description>...</description>
    <sameAs.../>
    <memberRole.../>
</relationType>
```

### JSON {.unnumbered .unlisted}

```json
{
    "type": "...",
    "scope": "...",
    "sameAs": ["..."],
    "memberRoles": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table relationTypes (
    lexicographicResourceID int foreign key references lexicographicResources(id),
    type varchar(10),
    scope varcar(50),
    id int primary key
);
alter table sameAs (
    add relationTypeID int foreign key references relationTypes(id)
)
```

Comments

- `description` is a human-readable explanation of this relation type.

- `scope` specifies restrictions on member of relations of this type. The possible values are:
    - `sameEntry`: members must be within of the same `entry`
    - `sameResource`: members must be within the same `lexicographicResource`
    - `any`: no restriction

- `memberRole` objects define roles for members of relations of this type.

## `memberRole`

```yaml
memberRole: <stringOrEmpty>
    description: (1..1) <string>
    memberType: (1..1) <symbol>
    min: (0..1) <number>
    max: (0..1) <number>
    action: (1..1) <symbol>
    sameAs: (0..n)
```

### XML {.unnumbered .unlisted}

```xml
<memberRole role="..." memberType="..." min="..." max="..." action="...">
    <description></description>
    <sameAs.../>
</memberRole>
```

### JSON {.unnumbered .unlisted}

```json
{
    "role": "...",
    "description": "...",
    "memberType": "...",
    "min": "...",
    "max": "...",
    "action": "...",
    "sameAs": [...]
}
```

### SQL {.unnumbered .unlisted}

```sql
create table memberRoles (
    relationTypeID int foreign key references relationTypes(id),
    role varchar(50),
    description varchar(255),
    memberType varchar(50),
    min int,
    max int,
    action varchar(50)
);
alter table sameAs (
    add memberRoleID int foreign key references memberRoles(id)
)
```

Comments

- If the value is empty, then members having this role do not need to have a `role` property.

- `description` is a human-readable explanation of this member role.

- `memberType` is a restrictions on the types of objects that can have this role. The possible values are:
    - `sense`: the object that has this role must be a `sense`. 
    - `entry`: the object that has this role must be an `entry`. 
    - `itemMarker`: the object that has this role must be a `itemMarker`.

- `min` is a number which says that relations of this type must have at least this many members with this role. If omitted then there is no lower limit (effectively, zero).

- `max` is a number which says that relations of this type may have at most this many members with this role. If omitted then there is no upper limit.

- `action` gives instructions on what machine agents should do when showing this relation to a human user (either on its own or in the context of one of its members). The possibe values are:
    - `embed`: Members that have this role should be shown in their entirety, i.e. the entire entry or the entire sense. This is suitable for the relation between entries and subentries, or senses and subsenses.
    - `navigate`: Members that have this role should not be shown in their entirety, but a navigable (e.g. clickable) link should be provided. This is suitable for the relation between synonyms, for example.
    - `none`: Members that have this role should not shown.

