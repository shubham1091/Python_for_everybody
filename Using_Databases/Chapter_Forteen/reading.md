# <span style="color:#f6fc2d">Welcome to Using Databases with Python</span>

# <span style="color:#f6fc2d">Object Oriented Definitions and Terminology</span>

## <span style="color:#b5473f">Warning</span>

- This lecture is very much about definitions and mechanics for objects
- This lecture is a lot more about "how it works" and less about "how you use it"
- You won't get the entire picture until this is all looked at in the context of a real problem
- So please suspend disbelief and learn technique

## <span style="color:#f6fc2d">Lets Start with Programs</span>

```mermaid
flowchart LR
    a[Input] ==>B[Process]==>c[Output]
```

## <span style="color:#f6fc2d">Object</span>

- <span style="color: #94ed1f">An Object is a bit of self-contained Code and Data</span>
- A key aspect of the Object approach is to break the problem into<br>
  smaller understandable parts (divide and conquer)
- Objects have boundaries that allow us to ignore un-needed detail
- We have been using objects all along: String Objects, Integer Objects,<br>
  Dictionary Objects, List Objects...

```mermaid
flowchart LR
    ip[Input] ==> A
    D ==> op[Output]
    subgraph object
    B --> A
    A --> D[Code/Data]
    C --> A
    A --> C[Code/Data]
    A[Code/Data] --> B[Code/Data]
    end
```

## <span style="color:#f6fc2d">Definitions</span>

- <span style="color:#ed971f">Class</span> - a template
- <span style="color:#ed971f">Method or Message</span> - A defined capability of a class
- <span style="color:#ed971f">Field or attribute</span> - A bit of data in a class
- <span style="color:#ed971f">Object or Instance</span> - A particular instance of a class

### Terminology: <span style="color:#ed971f">Class</span>

Defines the abstract characteristics of a thing (object), including the<br>
thing's characteristics (its attributes, <span style="color: #94ed1f">fields</span> or <span style="color: #94ed1f">properties</span>) and the<br>
thing's behaviors (the things it can do, or <span style="color: #94ed1f">methods</span>, operations or<br>
features). One might say that a <span style="color:#ed971f">class</span> is a <span style="color:#ed971f">blueprint</span> or factory that<br>
describes the nature of something. For example, the <span style="color:#ed971f">class</span> Dog would<br>
consist of traits shared by all dogs, such as breed and fur color<br>
(characteristics), and the ability to bark and sit (behavior)

### Terminology: <span style="color:#ae1fd1">Instance</span>

One can have an <span style="color:#ae1fd1">instance</span> of a class or a particular object.<br>
The <span style="color:#ae1fd1">instance</span> is the actual object created at runtime. In<br>
programmer jargon, the Lassie object is an <span style="color:#ae1fd1">instance</span> of the<br>
Dog class. The set of values of the attributes of a particular <br>
<span style="color:#ae1fd1">object</span> is called its <span style="color:#94ed1f">state</span>. The <span style="color:#ae1fd1">object</span> consists of state and the <br>
behavior that's defined in the object's class.

<span style="color:#f6fc2d">Object and instance are often used interchangeably</span>

### Terminology: <span style="color:#94ed1f">Method</span>

An object's abilities. In language, <span style="color:#94ed1f">Method</span> ae verbs. Lassie, being a<br>
Dog's has the ability to bark. So bark() is one of Lassie's methods.<br>
She may have other <span style="color:#94ed1f">Method</span> as well, for example sit() or eat() or<Br>
walk() or save_timmy(). Within the program, using a <span style="color:#94ed1f">Method</span> usually <br>
affects only one particular object; all Dogs can bark, but you need<br>
only one particular dog to do the barking

<span style="color:#f6fc2d">Method and Message are often used interchangeably</span>

# <span style="color:#f6fc2d">Object Lifecycle</span>

- Objects are created, used and discarded
- We have special blocks of code (methods) that get called
  - At the moment of creation (constructor)
  - At the moment of destruction (destructor)
- Constructors are used a lot
- Destructors are seldom used

## <span style="color:#f6fc2d">Constructor</span>

- The primary purpose of the constructor is to set up some instance variables<br>
  to have the proper initial values when the object is created
- In Object oriented programming, a constructor in a class is a special block<br>
  of statements called when an object is created

## Many <span style="color:#ed971f">Instances</span>

- We can create <span style="color:#ed971f">lots of objects</span> - th class is the template for the object
- We can store each <span style="color:#ed971f">distinct</span> object in its own variable
- We call this having multiple <span style="color:#ed971f">instances</span> of the same class
- Each <span style="color:#ed971f">instance</span> has its own copy ot the <span style="color:#f6fc2d">instance variables</span>

<span style="color:#ae1fd1">Constructors</span> can have additional <span style="color:#94ed1f">parameters</span>. These can be used to set up <br>
<span style="color:#ed971f">instance variables</span> for the particular instance of the class (i.e., for the particular object)

# <span style="color:#f6fc2d">Object Inheritance</span>

- When we make a new class - we can reuse an existing <br>
  class and <span style="color:#ed971f">inherit</span> all the capabilities of an existing class and<br>
  then add our own little bit to make our new class
- Another form of store and reuse
- Write once - reuse many times
- The new class (child) has all the capabilities of the old class<br>
  (parent) - and then some more

### Terminology: <span style="color:#ed971f">Inheritance</span>

"Subclasses" are more specialized versions of a class, which <br>
<span style="color:#ed971f">inherit</span> attributes and behaviors from their parent classes, and<br>
can introduce their own
