# Introduction

DMLex is a data model for modelling dictionaries (here called _lexicographic resources_) in computer applications such as dictionary writing systems.

DMLex is a data model, not an encoding format. DMLex is abstract, independent of any markup language or formalism. At the same time, DMLex has been designed to be easily and straightforwardly implementable in XML, JSON, as a relational database, and as a Semantic Web triplestore.

## Modular structure of DMLex

The DMLex specification is divided into a core with several optional modules.

- **DMLex Core** allows you to model the basic entries-and-sense structure if a monolingual lexicographic resource.

- **DMLex Crosslingual Module** extends DMLex Core to model bilingual and multilingual lexicographic resources.

- **DMLex Linking Module** extends DMLex Core and allows you to model various kinds of relations between entries, senses and other objects, including semantic relations such as synonymy and antonymy and presentational relations such as subentries and subsenses, both within a single lexicographic resource and across multiple lexicographic resources.

- **DMLex Inline Markup Module** extends DMLex Core to allow the modelling of inline markup on various objects such as example sentences, including the modelling of collocations and corpus patterns.

## Schema formalism

DMLex models a lexicographic resource as a **hierarchical list of objects**. Each object has a name, a value and an optional list of child objects, each of which can in turn also have a **name**, a **value** and an optional list of child objects.

The data model is defined in this standard through the means of a formalism which defines, for each object: (1) what its name is, (2) what its value is supposed to be (from a list of predefined primitive types) and (3) which child objects it may contain, with what arities.

The arities of child objects are indicated with the following codes:

- `(0..1)` zero or one
- `(0..n)` zero or one or more
- `(1..1)` exactly one
- `(1..n)` one or more
- `(2..n)` two or more

The primitive types of the values of objects are given with the following codes:

- `<string>` a non-empty string
- `<stringOrEmpty>` a string which may be empty
- `<number>` a positive integer number
- `<id>` an alphanumeric identifier
- `<idref>` a reference to something through its alphanumeric identifier
- `<uri>` a URI
- `<langCode>` an IETF language code
- `<empty>` nothing: the object serves only as a container for child objects
- `<symbol>` one of a specified finite number of values

When the primitive type of a child object is absent, this means that the schema for objects of that name is defined elsewhere in the code.

## Implementing DMLex

DMLex is an abstract data model which can be implemented in many different programming environments and serialization languages. In this document, we give recommended implementations in XML, JSON and SQL. Examples of what such implementations look like with real-world data are given in Section \ref{examples}.

### Implementing DMLex in XML

The XML implementation of DMLex shown in this document follows these priciples:

- The top-level `lexicographicResource` object is implemented as an XML element.

- All other objects are implemented as XML attributes of their parents, unless:

    - the object has an arity other than `(0..1)` and `(1..1)`
    - or the object can have child objects
    - or the object's value is human-readable text, such as a headword or a definition.
    
   In such cases the object is implemented as a child XML element of its parent.

### Implementing DMLex in JSON

The XML implementation of DMLex shown in this document follows these priciples:

- The top-level `lexicographicResource` object is implemented as a JSON object: `{...}`.

- All other objects are implemented as JSON name-value pairs inside their parent JSON object: `{"name": ...}`. 

- The values of objects are implemented:
    - If the object has an arity of `(0..1)` or `(1..1)`:
        - If the object cannot have any child objects: as a string or number.
        - If the object can have child objects: as a JSON object.
    - If the object has any other arity:
        - If the object cannot have any child objects: as an array of strings or numbers.
        - If the object can have child objects: as an array of JSON objects.

### Implementing DMLex as a relational database

The SQL implementation of DMLex shown in this document follows these priciples:

- The `lexicographicResource` object is implemented as table. (Alternatively, it can left unimplemented if the database is going to contain only one lexicographic resource.)

- Other objects with an arity other than `(0..1)` and `(1..1)` are implemented as tables.

- The values of objects, and objects with an arity of `(0..1)` or `(1..1)` are implemented as columns in those tables.

- The parent-child relation is implemented as a one-to-many relation between tables.


