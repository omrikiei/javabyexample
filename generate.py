#!/usr/bin/env python3
"""Generate Java by Example static site."""

import os
import html

# ─── Example definitions ───────────────────────────────────────────
# Each example: (slug, title, sections, output_sections)
# sections: list of (comment, code) pairs for the code table
# output_sections: list of (comment, code) pairs for the shell output table

EXAMPLES = []

def ex(slug, title, sections, output_sections=None):
    EXAMPLES.append((slug, title, sections, output_sections or []))

# ────────────────────────────────────────────────────────────────────
# 1. Hello World
# ────────────────────────────────────────────────────────────────────
ex("hello-world", "Hello World", [
    ("Our first program will print the classic &ldquo;hello world&rdquo;\nmessage. Here&rsquo;s the full source code.",
     'public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("hello world");\n    }\n}'),
], [
    ("To run the program, put the code in <code>HelloWorld.java</code>\nand use <code>javac</code> to compile, then <code>java</code> to run.",
     "$ javac HelloWorld.java\n$ java HelloWorld\nhello world"),
    ("Starting with Java 11, you can also run single-file\nprograms directly.",
     "$ java HelloWorld.java\nhello world"),
    ("Now that we can run and build basic Java programs,\nlet&rsquo;s learn more about the language.", None),
])

# ────────────────────────────────────────────────────────────────────
# 2. Values
# ────────────────────────────────────────────────────────────────────
ex("values", "Values", [
    ("Java has various value types including strings,\nintegers, floats, booleans, etc. Here are a few\nbasic examples.", None),
    ("Strings, which can be concatenated with <code>+</code>.",
     'System.out.println("java" + "lang");'),
    ("Integers and floats.",
     "System.out.println(1 + 1);\nSystem.out.println(7.0 / 3.0);"),
    ("Booleans, with boolean operators as you&rsquo;d expect.",
     "System.out.println(true && false);\nSystem.out.println(true || false);\nSystem.out.println(!true);"),
], [
    ("", "$ java Values.java\njavalang\n2\n2.3333333333333335\nfalse\ntrue\nfalse"),
])

# ────────────────────────────────────────────────────────────────────
# 3. Variables
# ────────────────────────────────────────────────────────────────────
ex("variables", "Variables", [
    ("In Java, variables are explicitly typed. Since Java 10,\n<code>var</code> can be used for local variable type inference.",
     'String a = "initial";\nSystem.out.println(a);'),
    ("You can declare multiple variables at once.",
     "int b = 1, c = 2;\nSystem.out.println(b + \" \" + c);"),
    ("Java will infer the type of initialized variables\nusing <code>var</code> (Java 10+).",
     'var d = true;\nSystem.out.println(d);'),
    ("Variables declared without initialization get\ndefault values. For instance, the default for\n<code>int</code> is <code>0</code>.",
     "int e;\ne = 0;\nSystem.out.println(e);"),
    ("<code>final</code> declares a variable that cannot be\nreassigned after initialization.",
     'final String f = "constant";\nSystem.out.println(f);'),
], [
    ("", "$ java Variables.java\ninitial\n1 2\ntrue\n0\nconstant"),
])

# ────────────────────────────────────────────────────────────────────
# 4. Constants
# ────────────────────────────────────────────────────────────────────
ex("constants", "Constants", [
    ("Java supports constants using the <code>final</code> keyword.\n<code>final</code> can be used with fields, local variables,\nand method parameters.",
     'public class Constants {\n    // Class-level constants are typically\n    // declared as static final.\n    static final String S = "constant";\n    static final int N = 500000000;'),
    ("A constant expression can be used anywhere\na value of its type is expected.",
     '    public static void main(String[] args) {\n        System.out.println(S);'),
    ("Constant expressions perform arithmetic\nwith arbitrary precision at compile time.",
     "        double d = 3e20 / N;\n        System.out.println(d);"),
    ("A numeric constant has no type until it&rsquo;s\ngiven one, such as by a cast or assignment.",
     "        System.out.println((long) d);\n    }\n}"),
], [
    ("", "$ java Constants.java\nconstant\n6.0E11\n600000000000"),
])

# ────────────────────────────────────────────────────────────────────
# 5. For
# ────────────────────────────────────────────────────────────────────
ex("for", "For", [
    ("<code>for</code> is Java&rsquo;s only looping construct. Here are\nsome basic types of <code>for</code> loops.", None),
    ("The most basic type, with a single condition.",
     'int i = 1;\nwhile (i <= 3) {\n    System.out.println(i);\n    i = i + 1;\n}'),
    ("A classic initial/condition/after <code>for</code> loop.",
     "for (int j = 0; j < 3; j++) {\n    System.out.println(j);\n}"),
    ("<code>for</code> without a condition (like Go&rsquo;s <code>for {}</code>)\nuses <code>while (true)</code> in Java. You can\n<code>break</code> out of it.",
     'while (true) {\n    System.out.println("loop");\n    break;\n}'),
    ("You can also <code>continue</code> to the next iteration\nof the loop.",
     "for (int n = 0; n < 6; n++) {\n    if (n % 2 == 0) {\n        continue;\n    }\n    System.out.println(n);\n}"),
], [
    ("", "$ java For.java\n1\n2\n3\n0\n1\n2\nloop\n1\n3\n5"),
])

# ────────────────────────────────────────────────────────────────────
# 6. If/Else
# ────────────────────────────────────────────────────────────────────
ex("if-else", "If/Else", [
    ("Branching with <code>if</code> and <code>else</code> in Java\nis straightforward.", None),
    ("Here&rsquo;s a basic example.",
     'if (7 % 2 == 0) {\n    System.out.println("7 is even");\n} else {\n    System.out.println("7 is odd");\n}'),
    ("You can have an <code>if</code> statement without an else.",
     'if (8 % 4 == 0) {\n    System.out.println("8 is divisible by 4");\n}'),
    ("Logical operators like <code>&&</code> and <code>||</code>\nare often useful in conditions.",
     'if (8 % 2 == 0 || 7 % 2 == 0) {\n    System.out.println("either 8 or 7 are even");\n}'),
    ("A statement can precede conditionals; any variables\ndeclared in this statement are available in the\ncurrent and all subsequent branches (unlike Go, you\njust declare them before the <code>if</code>).",
     'int num = 9;\nif (num < 0) {\n    System.out.println(num + " is negative");\n} else if (num < 10) {\n    System.out.println(num + " has 1 digit");\n} else {\n    System.out.println(num + " has multiple digits");\n}'),
], [
    ("Note that you don&rsquo;t need parentheses around conditions\nin Java&hellip; wait, actually you do! Unlike Go, Java\n<em>requires</em> parentheses around conditions.",
     "$ java IfElse.java\n7 is odd\n8 is divisible by 4\neither 8 or 7 are even\n9 has 1 digit"),
    ("There is no ternary <code>if</code> in Java&rsquo;s statement form,\nbut the ternary operator <code>? :</code> works for expressions.\n<code>int x = (a > b) ? a : b;</code>", None),
])

# ────────────────────────────────────────────────────────────────────
# 7. Switch
# ────────────────────────────────────────────────────────────────────
ex("switch", "Switch", [
    ("<code>switch</code> statements express conditionals across\nmany branches. Java&rsquo;s traditional switch uses\n<code>break</code> to prevent fall-through. Since Java 14,\n<em>switch expressions</em> with arrow syntax are available.", None),
    ("Here&rsquo;s a basic <code>switch</code>.",
     'int i = 2;\nswitch (i) {\n    case 1:\n        System.out.println("one");\n        break;\n    case 2:\n        System.out.println("two");\n        break;\n    case 3:\n        System.out.println("three");\n        break;\n}'),
    ("You can use commas to separate multiple expressions\nin the same <code>case</code> (Java 14+ arrow syntax). This\nalso works as an expression.",
     'var day = java.time.LocalDate.now().getDayOfWeek();\nvar type = switch (day) {\n    case MONDAY, TUESDAY, WEDNESDAY,\n         THURSDAY, FRIDAY -> "weekday";\n    case SATURDAY, SUNDAY -> "weekend";\n};  \nSystem.out.println(type);'),
    ("<code>switch</code> without a variable is not directly\nsupported in Java, but you can achieve the same\nwith if/else chains or switch expressions on\nbooleans (Java 21+).",
     'var t = java.time.LocalTime.now();\nif (t.getHour() < 12) {\n    System.out.println("It\'s before noon");\n} else {\n    System.out.println("It\'s after noon");\n}'),
], [
    ("", "$ java Switch.java\ntwo\nweekday\nIt's before noon"),
])

# ────────────────────────────────────────────────────────────────────
# 8. Arrays
# ────────────────────────────────────────────────────────────────────
ex("arrays", "Arrays", [
    ("In Java, an <em>array</em> is a fixed-size sequence\nof elements of a specific type.",
     '// Create an array that holds exactly 5 ints.\n// By default, elements are zero-valued.\nint[] a = new int[5];\nSystem.out.println("emp: " + java.util.Arrays.toString(a));'),
    ("We can set a value at an index and get a value\nwith the standard <code>array[index]</code> syntax.",
     'a[4] = 100;\nSystem.out.println("set: " + java.util.Arrays.toString(a));\nSystem.out.println("get: " + a[4]);'),
    ("The built-in <code>length</code> field returns the length of an array.",
     'System.out.println("len: " + a.length);'),
    ("Use this syntax to declare and initialize an array\nin one line.",
     'int[] b = {1, 2, 3, 4, 5};\nSystem.out.println("dcl: " + java.util.Arrays.toString(b));'),
    ("Multi-dimensional arrays are also supported.",
     'int[][] twoD = new int[2][3];\nfor (int i = 0; i < 2; i++) {\n    for (int j = 0; j < 3; j++) {\n        twoD[i][j] = i + j;\n    }\n}\nSystem.out.println("2d: " + java.util.Arrays.deepToString(twoD));'),
], [
    ("Note that arrays are printed in <code>[a, b, c]</code> form when\nusing <code>Arrays.toString</code>.",
     "$ java Arrays.java\nemp: [0, 0, 0, 0, 0]\nset: [0, 0, 0, 0, 100]\nget: 100\nlen: 5\ndcl: [1, 2, 3, 4, 5]\n2d: [[0, 1, 2], [1, 2, 3]]"),
])

# ────────────────────────────────────────────────────────────────────
# 9. Lists (ArrayList)
# ────────────────────────────────────────────────────────────────────
ex("lists", "Lists", [
    ("<em>Lists</em> in Java (via <code>ArrayList</code>) are resizable\nsequences, similar to Go&rsquo;s slices. They are one of\nthe most commonly used data structures.",
     'import java.util.ArrayList;\nimport java.util.List;\n\npublic class Lists {\n    public static void main(String[] args) {'),
    ("To create an empty list of strings, use\n<code>new ArrayList&lt;&gt;()</code>.",
     '        var s = new ArrayList<String>();\n        System.out.println("emp: " + s);'),
    ("We can <code>add</code> elements to the list.",
     '        s.add("a");\n        s.add("b");\n        s.add("c");\n        System.out.println("add: " + s);'),
    ("Individual elements can be accessed with <code>get</code>.\nThe <code>size()</code> method gives the list length.",
     '        System.out.println("get: " + s.get(2));\n        System.out.println("len: " + s.size());'),
    ("Lists support many operations like <code>subList</code>\n(similar to Go&rsquo;s slicing).",
     '        System.out.println("sub: " + s.subList(1, 3));'),
    ("<code>List.of()</code> creates an immutable list inline\n(Java 9+).",
     '        var t = List.of("a", "b", "c");\n        System.out.println("dcl: " + t);\n    }\n}'),
], [
    ("", "$ java Lists.java\nemp: []\nadd: [a, b, c]\nget: c\nlen: 3\nsub: [b, c]\ndcl: [a, b, c]"),
])

# ────────────────────────────────────────────────────────────────────
# 10. Maps
# ────────────────────────────────────────────────────────────────────
ex("maps", "Maps", [
    ("<em>Maps</em> (via <code>HashMap</code>) are Java&rsquo;s built-in\nassociative data type (sometimes called\n<em>hashes</em> or <em>dicts</em> in other languages).",
     'import java.util.HashMap;\nimport java.util.Map;\n\npublic class Maps {\n    public static void main(String[] args) {'),
    ("To create an empty map, use <code>new HashMap&lt;&gt;()</code>.",
     '        var m = new HashMap<String, Integer>();'),
    ("Set key/value pairs using <code>put()</code>.",
     '        m.put("k1", 7);\n        m.put("k2", 13);\n        System.out.println("map: " + m);'),
    ("Get a value for a key with <code>get()</code>.",
     '        System.out.println("v1: " + m.get("k1"));'),
    ("The <code>size()</code> method returns the number of\nkey/value pairs.",
     '        System.out.println("len: " + m.size());'),
    ("The <code>remove()</code> method deletes key/value pairs.",
     '        m.remove("k2");\n        System.out.println("map: " + m);'),
    ("<code>containsKey()</code> checks for the presence of a key.",
     '        System.out.println("has: " + m.containsKey("k2"));'),
    ("<code>Map.of()</code> creates an immutable map inline\n(Java 9+).",
     '        var n = Map.of("foo", 1, "bar", 2);\n        System.out.println("map: " + n);\n    }\n}'),
], [
    ("", '$ java Maps.java\nmap: {k1=7, k2=13}\nv1: 7\nlen: 2\nmap: {k1=7}\nhas: false\nmap: {bar=2, foo=1}'),
])

# ────────────────────────────────────────────────────────────────────
# 11. Functions
# ────────────────────────────────────────────────────────────────────
ex("functions", "Functions", [
    ("<em>Functions</em> (methods) are central to Java.\nWe&rsquo;ll learn about them with a few examples.",
     '// In Java, functions are always methods of a class.\npublic class Functions {\n\n    // Here\'s a method that takes two ints and\n    // returns their sum as an int.\n    static int plus(int a, int b) {\n        return a + b;\n    }'),
    ("Java requires explicit return types. Unlike Go,\nJava does not support multiple return values\nnatively (use a class or record instead).",
     '    // Methods can take multiple parameters of\n    // the same or different types.\n    static int plusPlus(int a, int b, int c) {\n        return a + b + c;\n    }'),
    ("Call a method as you&rsquo;d expect, with <code>name(args)</code>.",
     '    public static void main(String[] args) {\n        int res = plus(1, 2);\n        System.out.println("1+2 = " + res);\n\n        res = plusPlus(1, 2, 3);\n        System.out.println("1+2+3 = " + res);\n    }\n}'),
], [
    ("", "$ java Functions.java\n1+2 = 3\n1+2+3 = 6"),
])

# ────────────────────────────────────────────────────────────────────
# 12. Method Overloading
# ────────────────────────────────────────────────────────────────────
ex("method-overloading", "Method Overloading", [
    ("Java supports <em>method overloading</em>: multiple\nmethods with the same name but different parameter\nlists. This is a form of compile-time polymorphism.", None),
    ("Here we define two <code>add</code> methods &mdash; one for\n<code>int</code> and one for <code>double</code>.",
     'public class MethodOverloading {\n\n    static int add(int a, int b) {\n        return a + b;\n    }\n\n    static double add(double a, double b) {\n        return a + b;\n    }'),
    ("You can also overload on the number of parameters.",
     '    static int add(int a, int b, int c) {\n        return a + b + c;\n    }'),
    ("Java selects the correct method based on\nthe argument types at compile time.",
     '    public static void main(String[] args) {\n        System.out.println(add(1, 2));\n        System.out.println(add(1.5, 2.5));\n        System.out.println(add(1, 2, 3));\n    }\n}'),
], [
    ("", "$ java MethodOverloading.java\n3\n4.0\n6"),
])

# ────────────────────────────────────────────────────────────────────
# 13. Varargs
# ────────────────────────────────────────────────────────────────────
ex("varargs", "Varargs", [
    ("<a href=\"https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html\">Varargs</a>\n(variable-length arguments) let methods accept\nany number of arguments of a given type.",
     'public class Varargs {\n\n    // This method takes an arbitrary number\n    // of ints.\n    static int sum(int... nums) {\n        int total = 0;\n        for (int n : nums) {\n            total += n;\n        }\n        return total;\n    }'),
    ("Varargs methods can be called with individual\narguments or an array.",
     '    public static void main(String[] args) {\n        System.out.println(sum(1, 2));\n        System.out.println(sum(1, 2, 3));\n\n        int[] nums = {1, 2, 3, 4};\n        System.out.println(sum(nums));\n    }\n}'),
], [
    ("", "$ java Varargs.java\n3\n6\n10"),
])

# ────────────────────────────────────────────────────────────────────
# 14. Lambdas
# ────────────────────────────────────────────────────────────────────
ex("lambdas", "Lambdas", [
    ("Java supports <em>lambda expressions</em> (since Java 8),\nwhich are anonymous functions. They are commonly\nused with functional interfaces.",
     'import java.util.function.IntBinaryOperator;\nimport java.util.function.IntUnaryOperator;\n\npublic class Lambdas {'),
    ("This method takes a function (functional interface)\nas a parameter.",
     '    static int apply(IntBinaryOperator op, int a, int b) {\n        return op.applyAsInt(a, b);\n    }'),
    ("Lambdas can capture variables from their\nenclosing scope (effectively final variables).",
     '    public static void main(String[] args) {\n        // A simple lambda\n        IntBinaryOperator add = (a, b) -> a + b;\n        System.out.println(apply(add, 1, 2));'),
    ("You can also use lambdas inline.",
     '        System.out.println(apply((a, b) -> a * b, 3, 4));'),
    ("Lambdas can be used to create closures.\nThis function returns a lambda that adds\n<code>x</code> to its argument.",
     '        int x = 5;\n        IntUnaryOperator addX = n -> n + x;\n        System.out.println(addX.applyAsInt(10));\n    }\n}'),
], [
    ("", "$ java Lambdas.java\n3\n12\n15"),
])

# ────────────────────────────────────────────────────────────────────
# 15. Recursion
# ────────────────────────────────────────────────────────────────────
ex("recursion", "Recursion", [
    ("Java supports <em>recursive methods</em>: methods that\ncall themselves.",
     'public class Recursion {\n\n    // This fact method calls itself until it\n    // reaches the base case of fact(0).\n    static int fact(int n) {\n        if (n == 0) {\n            return 1;\n        }\n        return n * fact(n - 1);\n    }'),
    ("Unlike some languages, Java doesn&rsquo;t support\ntail call optimization. For deep recursion,\nconsider iterative approaches.",
     '    public static void main(String[] args) {\n        System.out.println(fact(7));\n\n        // Lambdas can also be recursive via\n        // method references or by using a\n        // wrapper.\n    }\n}'),
], [
    ("", "$ java Recursion.java\n5040"),
])

# ────────────────────────────────────────────────────────────────────
# 16. Strings
# ────────────────────────────────────────────────────────────────────
ex("strings", "Strings", [
    ("Java <code>String</code> is an immutable sequence of\ncharacters. The standard library provides\na rich set of string methods.",
     'public class Strings {\n    public static void main(String[] args) {\n        // String literals\n        var s = "Hello, World";\n        System.out.println(s);'),
    ("Common string operations.",
     '        System.out.println("Contains:  " + s.contains("World"));\n        System.out.println("Count:     " + s.chars().filter(c -> c == \'l\').count());\n        System.out.println("StartsWith:" + s.startsWith("Hello"));\n        System.out.println("EndsWith:  " + s.endsWith("World"));\n        System.out.println("IndexOf:   " + s.indexOf("World"));\n        System.out.println("Length:    " + s.length());'),
    ("String transformation methods return new strings\nsince Strings are immutable.",
     '        System.out.println("ToUpper:   " + s.toUpperCase());\n        System.out.println("ToLower:   " + s.toLowerCase());\n        System.out.println("Replace:   " + s.replace("World", "Java"));\n        System.out.println("Substring: " + s.substring(0, 5));\n        System.out.println("Trim:      " + "  hi  ".trim());'),
    ("Text blocks (Java 13+) for multi-line strings.",
     '        var tb = """\n                Hello,\n                Java!\n                """;\n        System.out.println(tb);\n    }\n}'),
], [
    ("", "$ java Strings.java\nHello, World\nContains:  true\nCount:     3\nStartsWith:true\nEndsWith:  true\nIndexOf:   7\nLength:    12\nToUpper:   HELLO, WORLD\nToLower:   hello, world\nReplace:   Hello, Java\nSubstring: Hello\nTrim:      hi\nHello,\nJava!"),
])

# ────────────────────────────────────────────────────────────────────
# 17. Classes
# ────────────────────────────────────────────────────────────────────
ex("classes", "Classes", [
    ("Java is an object-oriented language.\n<em>Classes</em> are the fundamental building blocks\nfor structuring code.",
     '// A simple class with fields and methods.\nclass Rect {\n    double width;\n    double height;\n\n    Rect(double width, double height) {\n        this.width = width;\n        this.height = height;\n    }\n\n    double area() {\n        return width * height;\n    }\n\n    double perimeter() {\n        return 2 * width + 2 * height;\n    }\n}'),
    ("Use <code>new</code> to create instances of a class.",
     'public class Classes {\n    public static void main(String[] args) {\n        var r = new Rect(3, 4);\n        System.out.println("area: " + r.area());\n        System.out.println("perim: " + r.perimeter());\n    }\n}'),
], [
    ("", "$ javac Classes.java\n$ java Classes\narea: 12.0\nperim: 14.0"),
])

# ────────────────────────────────────────────────────────────────────
# 18. Records
# ────────────────────────────────────────────────────────────────────
ex("records", "Records", [
    ("<em>Records</em> (Java 16+) are a concise way to create\nimmutable data classes. They automatically generate\n<code>equals()</code>, <code>hashCode()</code>, <code>toString()</code>,\nand accessor methods.",
     '// A record automatically creates a constructor,\n// accessors, equals, hashCode, and toString.\nrecord Point(int x, int y) {}'),
    ("Records can have custom methods.",
     'record Rect(double width, double height) {\n    double area() {\n        return width * height;\n    }\n}'),
    ("Using records.",
     'public class Records {\n    public static void main(String[] args) {\n        var p = new Point(3, 4);\n        System.out.println(p);\n        System.out.println("x: " + p.x());\n\n        var r = new Rect(3, 4);\n        System.out.println("area: " + r.area());\n\n        // Records implement equals based on values\n        var p2 = new Point(3, 4);\n        System.out.println("equal: " + p.equals(p2));\n    }\n}'),
], [
    ("", "$ javac Records.java\n$ java Records\nPoint[x=3, y=4]\nx: 3\narea: 12.0\nequal: true"),
])

# ────────────────────────────────────────────────────────────────────
# 19. Interfaces
# ────────────────────────────────────────────────────────────────────
ex("interfaces", "Interfaces", [
    ("<em>Interfaces</em> are named collections of method\nsignatures. Unlike Go, Java classes must\nexplicitly declare that they implement an\ninterface.",
     '// A basic interface for geometric shapes.\ninterface Geometry {\n    double area();\n    double perimeter();\n}'),
    ("Classes implement interfaces explicitly with\nthe <code>implements</code> keyword.",
     'class Circle implements Geometry {\n    double radius;\n\n    Circle(double radius) {\n        this.radius = radius;\n    }\n\n    public double area() {\n        return Math.PI * radius * radius;\n    }\n\n    public double perimeter() {\n        return 2 * Math.PI * radius;\n    }\n}'),
    ("If a variable has an interface type, you can\ncall methods from that interface.",
     'public class Interfaces {\n    static void measure(Geometry g) {\n        System.out.println(g);\n        System.out.println("area: " + g.area());\n        System.out.println("perim: " + g.perimeter());\n    }\n\n    public static void main(String[] args) {\n        var c = new Circle(5);\n        measure(c);\n    }\n}'),
], [
    ("", "$ javac Interfaces.java\n$ java Interfaces\nCircle@<hash>\narea: 78.53981633974483\nperim: 31.41592653589793"),
])

# ────────────────────────────────────────────────────────────────────
# 20. Enums
# ────────────────────────────────────────────────────────────────────
ex("enums", "Enums", [
    ("<em>Enum types</em> in Java are full classes that represent\na fixed set of constants. They can have fields,\nmethods, and constructors.",
     '// A basic enum.\nenum Direction {\n    NORTH, SOUTH, EAST, WEST\n}'),
    ("Enums can have fields and methods.",
     'enum Planet {\n    MERCURY(3.303e+23, 2.4397e6),\n    VENUS(4.869e+24, 6.0518e6),\n    EARTH(5.976e+24, 6.37814e6);\n\n    final double mass;\n    final double radius;\n\n    Planet(double mass, double radius) {\n        this.mass = mass;\n        this.radius = radius;\n    }\n\n    double surfaceGravity() {\n        final double G = 6.67300E-11;\n        return G * mass / (radius * radius);\n    }\n}'),
    ("Using enums.",
     'public class Enums {\n    public static void main(String[] args) {\n        var d = Direction.NORTH;\n        System.out.println(d);\n\n        // Enums work with switch\n        switch (d) {\n            case NORTH -> System.out.println("Going up!");\n            case SOUTH -> System.out.println("Going down!");\n            default -> System.out.println("Going sideways!");\n        }\n\n        // Enum methods\n        System.out.printf("Earth gravity: %.2f m/s²%n",\n            Planet.EARTH.surfaceGravity());\n\n        // Iterate over all values\n        for (var p : Planet.values()) {\n            System.out.println(p.name());\n        }\n    }\n}'),
], [
    ("", "$ javac Enums.java\n$ java Enums\nNORTH\nGoing up!\nEarth gravity: 9.80 m/s²\nMERCURY\nVENUS\nEARTH"),
])

# ────────────────────────────────────────────────────────────────────
# 21. Inheritance
# ────────────────────────────────────────────────────────────────────
ex("inheritance", "Inheritance", [
    ("Java supports class <em>inheritance</em> via <code>extends</code>.\nThis is one of the fundamental OOP principles.",
     '// Base class\nclass Animal {\n    String name;\n\n    Animal(String name) {\n        this.name = name;\n    }\n\n    void speak() {\n        System.out.println(name + " makes a sound");\n    }\n}'),
    ("Subclasses extend the parent and can override\nmethods using <code>@Override</code>.",
     'class Dog extends Animal {\n    Dog(String name) {\n        super(name);\n    }\n\n    @Override\n    void speak() {\n        System.out.println(name + " barks");\n    }\n}'),
    ("Polymorphism: a parent reference can point\nto a child object.",
     'public class Inheritance {\n    public static void main(String[] args) {\n        Animal a = new Animal("Generic Animal");\n        Animal d = new Dog("Rex");\n\n        a.speak();\n        d.speak();\n\n        // instanceof check\n        System.out.println("d is Dog: " + (d instanceof Dog));\n    }\n}'),
], [
    ("", "$ javac Inheritance.java\n$ java Inheritance\nGeneric Animal makes a sound\nRex barks\nd is Dog: true"),
])

# ────────────────────────────────────────────────────────────────────
# 22. Generics
# ────────────────────────────────────────────────────────────────────
ex("generics", "Generics", [
    ("Starting with Java 5, <em>generics</em> let you write\nclasses, interfaces, and methods that work with\nany type while providing compile-time type safety.",
     '// A generic class that can hold any type.\nclass Box<T> {\n    private T value;\n\n    Box(T value) {\n        this.value = value;\n    }\n\n    T get() {\n        return value;\n    }\n}'),
    ("Generic methods can also be defined independently.",
     'import java.util.List;\n\npublic class Generics {\n\n    // A generic method\n    static <T extends Comparable<T>> T max(T a, T b) {\n        return a.compareTo(b) >= 0 ? a : b;\n    }'),
    ("Using generic classes and methods.",
     '    public static void main(String[] args) {\n        var intBox = new Box<>(42);\n        System.out.println("int box: " + intBox.get());\n\n        var strBox = new Box<>("hello");\n        System.out.println("str box: " + strBox.get());\n\n        System.out.println("max(3,5): " + max(3, 5));\n        System.out.println("max(a,z): " + max("a", "z"));\n    }\n}'),
], [
    ("", "$ javac Generics.java\n$ java Generics\nint box: 42\nstr box: hello\nmax(3,5): 5\nmax(a,z): z"),
])

# ────────────────────────────────────────────────────────────────────
# 23. Sealed Classes
# ────────────────────────────────────────────────────────────────────
ex("sealed-classes", "Sealed Classes", [
    ("<em>Sealed classes</em> (Java 17+) restrict which classes\ncan extend them. This enables exhaustive pattern\nmatching and better domain modeling.",
     '// A sealed interface can only be implemented\n// by permitted classes.\nsealed interface Shape permits Circle, Rectangle {\n    double area();\n}'),
    ("Each permitted subclass must be <code>final</code>,\n<code>sealed</code>, or <code>non-sealed</code>.",
     'final class Circle implements Shape {\n    double radius;\n    Circle(double r) { this.radius = r; }\n    public double area() { return Math.PI * radius * radius; }\n}\n\nfinal class Rectangle implements Shape {\n    double w, h;\n    Rectangle(double w, double h) { this.w = w; this.h = h; }\n    public double area() { return w * h; }\n}'),
    ("Pattern matching with sealed types (Java 21+).",
     'public class SealedClasses {\n    static String describe(Shape s) {\n        return switch (s) {\n            case Circle c -> "Circle with radius " + c.radius;\n            case Rectangle r -> "Rectangle " + r.w + "x" + r.h;\n        };\n    }\n\n    public static void main(String[] args) {\n        Shape c = new Circle(5);\n        Shape r = new Rectangle(3, 4);\n        System.out.println(describe(c));\n        System.out.println(describe(r));\n        System.out.println("area: " + c.area());\n    }\n}'),
], [
    ("", "$ javac SealedClasses.java\n$ java SealedClasses\nCircle with radius 5.0\nRectangle 3.0x4.0\narea: 78.53981633974483"),
])

# ────────────────────────────────────────────────────────────────────
# 24. Exceptions
# ────────────────────────────────────────────────────────────────────
ex("exceptions", "Exceptions", [
    ("Java uses <em>exceptions</em> for error handling.\nExceptions are objects that represent errors and\ncan be thrown and caught.",
     '// Custom exception by extending Exception.\nclass ValidationException extends Exception {\n    private final int value;\n\n    ValidationException(String msg, int value) {\n        super(msg);\n        this.value = value;\n    }\n\n    int getValue() {\n        return value;\n    }\n}'),
    ("Methods declare checked exceptions with <code>throws</code>.",
     'public class Exceptions {\n\n    static int divide(int a, int b) throws ArithmeticException {\n        return a / b;\n    }\n\n    static void validate(int age) throws ValidationException {\n        if (age < 0) {\n            throw new ValidationException("negative age", age);\n        }\n    }'),
    ("Use <code>try/catch/finally</code> to handle exceptions.",
     '    public static void main(String[] args) {\n        // Catching a runtime exception\n        try {\n            divide(10, 0);\n        } catch (ArithmeticException e) {\n            System.out.println("error: " + e.getMessage());\n        }\n\n        // Catching a custom exception\n        try {\n            validate(-5);\n        } catch (ValidationException e) {\n            System.out.println("invalid: " + e.getMessage()\n                + " (value=" + e.getValue() + ")");\n        }\n\n        // try-with-resources for auto-closeable resources\n        // (similar to Go\'s defer)\n        System.out.println("done");\n    }\n}'),
], [
    ("", "$ java Exceptions.java\nerror: / by zero\ninvalid: negative age (value=-5)\ndone"),
])

# ────────────────────────────────────────────────────────────────────
# 25. Threads
# ────────────────────────────────────────────────────────────────────
ex("threads", "Threads", [
    ("Java has built-in support for concurrent execution\nvia <em>threads</em>.",
     'public class Threads {\n\n    static void task(String name) {\n        for (int i = 0; i < 3; i++) {\n            System.out.println(name + ": " + i);\n        }\n    }'),
    ("Start a new thread using <code>Thread.start()</code> or\n<code>Thread.ofVirtual()</code> (Java 21+).",
     '    public static void main(String[] args) throws Exception {\n        // Traditional thread\n        var t1 = new Thread(() -> task("thread1"));\n        t1.start();\n\n        // Virtual thread (Java 21+)\n        var t2 = Thread.ofVirtual().start(() -> task("thread2"));\n\n        // Run in the main thread too\n        task("main");\n\n        // Wait for threads to finish\n        t1.join();\n        t2.join();\n        System.out.println("done");\n    }\n}'),
], [
    ("When we run this program, we see the output\nof the threads interleaved. The exact ordering\nmay vary between runs.",
     "$ java Threads.java\nmain: 0\nmain: 1\nmain: 2\nthread1: 0\nthread1: 1\nthread1: 2\nthread2: 0\nthread2: 1\nthread2: 2\ndone"),
])

# ────────────────────────────────────────────────────────────────────
# 26. Virtual Threads
# ────────────────────────────────────────────────────────────────────
ex("virtual-threads", "Virtual Threads", [
    ("<em>Virtual threads</em> (Java 21+) are lightweight threads\nmanaged by the JVM, similar to goroutines. They allow\nmassive concurrency without the overhead of OS threads.",
     'import java.util.concurrent.Executors;\nimport java.util.concurrent.atomic.AtomicInteger;\n\npublic class VirtualThreads {\n    public static void main(String[] args) throws Exception {\n        var counter = new AtomicInteger(0);'),
    ("You can create thousands (or millions) of virtual\nthreads efficiently.",
     '        // Create 10,000 virtual threads\n        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {\n            for (int i = 0; i < 10_000; i++) {\n                executor.submit(() -> {\n                    counter.incrementAndGet();\n                });\n            }\n        } // executor.close() waits for all tasks'),
    ("All 10,000 tasks complete efficiently.",
     '        System.out.println("count: " + counter.get());\n    }\n}'),
], [
    ("Virtual threads have minimal memory overhead and\nare ideal for I/O-bound workloads.",
     "$ java VirtualThreads.java\ncount: 10000"),
])

# ────────────────────────────────────────────────────────────────────
# 27. Synchronization
# ────────────────────────────────────────────────────────────────────
ex("synchronization", "Synchronization", [
    ("Java provides several mechanisms for synchronizing\naccess to shared data across threads.",
     'import java.util.concurrent.locks.ReentrantLock;\n\npublic class Synchronization {\n    static int counter = 0;\n    static final Object lock = new Object();'),
    ("The <code>synchronized</code> keyword is the simplest\nway to achieve mutual exclusion.",
     '    static synchronized void incrementSync() {\n        counter++;\n    }'),
    ("You can also synchronize on specific objects\nor use <code>ReentrantLock</code> for more control.",
     '    static final ReentrantLock rLock = new ReentrantLock();\n\n    static void incrementWithLock() {\n        rLock.lock();\n        try {\n            counter++;\n        } finally {\n            rLock.unlock();\n        }\n    }'),
    ("Example usage with multiple threads.",
     '    public static void main(String[] args) throws Exception {\n        counter = 0;\n        var threads = new Thread[1000];\n        for (int i = 0; i < threads.length; i++) {\n            threads[i] = new Thread(() -> {\n                for (int j = 0; j < 1000; j++) {\n                    incrementSync();\n                }\n            });\n            threads[i].start();\n        }\n        for (var t : threads) t.join();\n        System.out.println("count: " + counter);\n    }\n}'),
], [
    ("The count will always be exactly 1,000,000\nthanks to synchronization.",
     "$ java Synchronization.java\ncount: 1000000"),
])

# ────────────────────────────────────────────────────────────────────
# 28. Atomic Counters
# ────────────────────────────────────────────────────────────────────
ex("atomic-counters", "Atomic Counters", [
    ("For managing simple shared state, Java provides\n<code>java.util.concurrent.atomic</code> package with\nlock-free thread-safe operations.",
     'import java.util.concurrent.atomic.AtomicLong;\n\npublic class AtomicCounters {\n    public static void main(String[] args) throws Exception {\n        var ops = new AtomicLong(0);'),
    ("We&rsquo;ll start 50 threads that each increment\nthe counter 1000 times.",
     '        var threads = new Thread[50];\n        for (int i = 0; i < threads.length; i++) {\n            threads[i] = new Thread(() -> {\n                for (int j = 0; j < 1000; j++) {\n                    ops.incrementAndGet();\n                }\n            });\n            threads[i].start();\n        }'),
    ("Wait for all threads and read the final value.",
     '        for (var t : threads) t.join();\n\n        System.out.println("ops: " + ops.get());\n    }\n}'),
], [
    ("We expect exactly 50,000 operations. Atomics are\noften preferred over locks for simple counters.",
     "$ java AtomicCounters.java\nops: 50000"),
])

# ────────────────────────────────────────────────────────────────────
# 29. Sorting
# ────────────────────────────────────────────────────────────────────
ex("sorting", "Sorting", [
    ("Java&rsquo;s <code>Collections.sort()</code> and\n<code>Arrays.sort()</code> provide sorting for\ncollections and arrays.",
     'import java.util.*;\n\npublic class Sorting {\n    public static void main(String[] args) {\n        // Sorting a list of strings\n        var strs = new ArrayList<>(List.of("c", "a", "b"));\n        Collections.sort(strs);\n        System.out.println("Strings: " + strs);'),
    ("Sorting integers.",
     '        var ints = new ArrayList<>(List.of(7, 2, 4));\n        Collections.sort(ints);\n        System.out.println("Ints:    " + ints);'),
    ("You can check if a list is already sorted.",
     '        // No built-in isSorted, but easy to check\n        boolean sorted = true;\n        for (int i = 0; i < ints.size() - 1; i++) {\n            if (ints.get(i) > ints.get(i + 1)) {\n                sorted = false;\n                break;\n            }\n        }\n        System.out.println("Sorted:  " + sorted);\n    }\n}'),
], [
    ("", "$ java Sorting.java\nStrings: [a, b, c]\nInts:    [2, 4, 7]\nSorted:  true"),
])

# ────────────────────────────────────────────────────────────────────
# 30. Sorting by Comparator
# ────────────────────────────────────────────────────────────────────
ex("sorting-by-comparator", "Sorting by Comparator", [
    ("Sometimes we want to sort a collection by something\nother than its natural order. Use a <code>Comparator</code>.",
     'import java.util.*;\n\npublic class SortingByComparator {\n    public static void main(String[] args) {\n        // Sort strings by length\n        var fruits = new ArrayList<>(List.of(\n            "peach", "kiwi", "apple"));\n\n        fruits.sort(Comparator.comparingInt(String::length));\n        System.out.println(fruits);'),
    ("You can also sort with a custom lambda comparator.",
     '        // Sort by last character\n        fruits.sort((a, b) -> {\n            char lastA = a.charAt(a.length() - 1);\n            char lastB = b.charAt(b.length() - 1);\n            return Character.compare(lastA, lastB);\n        });\n        System.out.println(fruits);\n    }\n}'),
], [
    ("", "$ java SortingByComparator.java\n[kiwi, peach, apple]\n[peach, apple, kiwi]"),
])

# ────────────────────────────────────────────────────────────────────
# 31. String Formatting
# ────────────────────────────────────────────────────────────────────
ex("string-formatting", "String Formatting", [
    ("Java offers several ways to format strings.\n<code>String.format</code>, <code>printf</code>, and the\nnewer <code>formatted()</code> method (Java 15+).",
     'public class StringFormatting {\n\n    record Point(int x, int y) {}\n\n    public static void main(String[] args) {\n        var p = new Point(1, 2);'),
    ("General formatting with <code>printf</code> / <code>format</code>.",
     '        // Print a representation of the object\n        System.out.printf("struct1: %s%n", p);\n\n        // String formatting\n        System.out.printf("string: %s%n", "hello");\n\n        // Integer formatting\n        System.out.printf("int:     %d%n", 42);'),
    ("Float formatting and width control.",
     '        System.out.printf("float:   %.2f%n", 3.14159);\n        System.out.printf("float:   %e%n", 100000.0);\n\n        // Right-justify in a 10-char wide field\n        System.out.printf("right:   |%10d|%n", 42);\n        // Left-justify\n        System.out.printf("left:    |%-10d|%n", 42);'),
    ("<code>String.format</code> returns a string without\nprinting it.",
     '        String s = String.format("format: %s has %d points", "Java", 100);\n        System.out.println(s);\n    }\n}'),
], [
    ("", "$ java StringFormatting.java\nstruct1: Point[x=1, y=2]\nstring: hello\nint:     42\nfloat:   3.14\nfloat:   1.000000e+05\nright:   |        42|\nleft:    |42        |\nformat: Java has 100 points"),
])

# ────────────────────────────────────────────────────────────────────
# 32. Regular Expressions
# ────────────────────────────────────────────────────────────────────
ex("regular-expressions", "Regular Expressions", [
    ("Java provides built-in support for\n<a href=\"https://docs.oracle.com/javase/tutorial/essential/regex/\">regular expressions</a>\nvia the <code>java.util.regex</code> package.",
     'import java.util.regex.*;\n\npublic class RegularExpressions {\n    public static void main(String[] args) {\n        // Test whether a pattern matches a string\n        boolean match = Pattern.matches("p([a-z]+)ch", "peach");\n        System.out.println(match);'),
    ("Compile a pattern for reuse.",
     '        var p = Pattern.compile("p([a-z]+)ch");\n\n        // Find a match\n        System.out.println(p.matcher("peach punch").find());\n\n        // Find the matching string\n        var m = p.matcher("peach punch");\n        if (m.find()) {\n            System.out.println("match: " + m.group());\n        }'),
    ("Find all matches.",
     '        // Find all matches\n        m = p.matcher("peach punch pinch");\n        while (m.find()) {\n            System.out.print(m.group() + " ");\n        }\n        System.out.println();\n    }\n}'),
], [
    ("", "$ java RegularExpressions.java\ntrue\ntrue\nmatch: peach\npeach punch pinch"),
])

# ────────────────────────────────────────────────────────────────────
# 33. JSON
# ────────────────────────────────────────────────────────────────────
ex("json", "JSON", [
    ("Java doesn&rsquo;t have built-in JSON support in the\nstandard library, but common libraries like\n<em>Jackson</em> and <em>Gson</em> are widely used.\nHere we show a simple approach using\nthe built-in <code>javax.json</code> or manual\nparsing concepts.",
     'import java.util.*;\n\n// For simple cases, you can represent JSON\n// with Maps and Lists. For real projects,\n// use Jackson or Gson.\npublic class Json {\n    public static void main(String[] args) {\n        // Building a JSON-like structure\n        var person = new LinkedHashMap<String, Object>();\n        person.put("name", "Alice");\n        person.put("age", 30);'),
    ("Nested structures and arrays.",
     '        person.put("hobbies", List.of("reading", "coding"));\n\n        // Simple serialization (not real JSON,\n        // but demonstrates the concept)\n        System.out.println(person);'),
    ("For proper JSON, use a library like Jackson:",
     '        // With Jackson (pseudo-code):\n        // ObjectMapper mapper = new ObjectMapper();\n        // String json = mapper.writeValueAsString(person);\n        // Person p = mapper.readValue(json, Person.class);\n        System.out.println("name: " + person.get("name"));\n    }\n}'),
], [
    ("For production use, add Jackson or Gson\nto your project dependencies.",
     "$ java Json.java\n{name=Alice, age=30, hobbies=[reading, coding]}\nname: Alice"),
])

# ────────────────────────────────────────────────────────────────────
# 34. Time
# ────────────────────────────────────────────────────────────────────
ex("time", "Time", [
    ("Java 8+ provides the <code>java.time</code> package for\ncomprehensive date/time support.",
     'import java.time.*;\nimport java.time.format.*;\nimport java.time.temporal.*;\n\npublic class Time {\n    public static void main(String[] args) {\n        var now = Instant.now();\n        System.out.println("now: " + now);'),
    ("Creating specific times and dates.",
     '        var dt = LocalDateTime.of(2023, 6, 15, 14, 30, 0);\n        System.out.println("date: " + dt);\n        System.out.println("year: " + dt.getYear());\n        System.out.println("month: " + dt.getMonth());\n        System.out.println("day: " + dt.getDayOfMonth());'),
    ("Duration and period calculations.",
     '        var earlier = LocalDateTime.of(2023, 1, 1, 0, 0);\n        var diff = Duration.between(earlier, dt);\n        System.out.println("diff: " + diff);\n        System.out.println("hours: " + diff.toHours());'),
    ("Formatting and parsing.",
     '        var fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");\n        System.out.println("formatted: " + dt.format(fmt));\n\n        var parsed = LocalDateTime.parse(\n            "2023-06-15 14:30", fmt);\n        System.out.println("parsed: " + parsed);\n    }\n}'),
], [
    ("", "$ java Time.java\nnow: 2024-01-15T10:30:00Z\ndate: 2023-06-15T14:30\nyear: 2023\nmonth: JUNE\nday: 15\ndiff: PT3942H30M\nhours: 3942\nformatted: 2023-06-15 14:30\nparsed: 2023-06-15T14:30"),
])

# ────────────────────────────────────────────────────────────────────
# 35. Random Numbers
# ────────────────────────────────────────────────────────────────────
ex("random-numbers", "Random Numbers", [
    ("Java&rsquo;s <code>java.util.Random</code> and\n<code>ThreadLocalRandom</code> (or <code>RandomGenerator</code>\nin Java 17+) provide pseudo-random number generation.",
     'import java.util.Random;\nimport java.util.concurrent.ThreadLocalRandom;\n\npublic class RandomNumbers {\n    public static void main(String[] args) {\n        // Random integers in [0, 100)\n        var rng = new Random();\n        System.out.println(rng.nextInt(100));\n        System.out.println(rng.nextInt(100));'),
    ("Random floats in [0.0, 1.0).",
     '        System.out.printf("%.4f%n", rng.nextDouble());'),
    ("Using ThreadLocalRandom for concurrent scenarios.\nSeeding for reproducible results.",
     '        // Seeded random for reproducibility\n        var seeded = new Random(42);\n        System.out.println(seeded.nextInt(100));\n        System.out.println(seeded.nextInt(100));\n    }\n}'),
], [
    ("Some of the generated numbers may differ on\nyour machine. Seeded generators always produce\nthe same sequence.",
     "$ java RandomNumbers.java\n68\n41\n0.6591\n0\n68"),
])

# ────────────────────────────────────────────────────────────────────
# 36. Streams
# ────────────────────────────────────────────────────────────────────
ex("streams", "Streams", [
    ("<em>Streams</em> (Java 8+) provide a functional-style API\nfor processing sequences of elements. They support\nmap, filter, reduce, and more.",
     'import java.util.*;\nimport java.util.stream.*;\n\npublic class Streams {\n    public static void main(String[] args) {\n        var nums = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);'),
    ("Filter, map, and collect.",
     '        // Filter even numbers and double them\n        var result = nums.stream()\n            .filter(n -> n % 2 == 0)\n            .map(n -> n * 2)\n            .collect(Collectors.toList());\n        System.out.println("result: " + result);'),
    ("Reduce to a single value.",
     '        // Sum all elements\n        int sum = nums.stream()\n            .reduce(0, Integer::sum);\n        System.out.println("sum: " + sum);'),
    ("Other useful stream operations.",
     '        // Count, min, max\n        long count = nums.stream().filter(n -> n > 5).count();\n        System.out.println("count>5: " + count);\n\n        // Collecting to different types\n        String joined = nums.stream()\n            .map(String::valueOf)\n            .collect(Collectors.joining(", "));\n        System.out.println("joined: " + joined);\n\n        // Grouping\n        var grouped = nums.stream()\n            .collect(Collectors.groupingBy(n -> n % 2 == 0 ? "even" : "odd"));\n        System.out.println("grouped: " + grouped);\n    }\n}'),
], [
    ("", "$ java Streams.java\nresult: [4, 8, 12, 16, 20]\nsum: 55\ncount>5: 5\njoined: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\ngrouped: {odd=[1, 3, 5, 7, 9], even=[2, 4, 6, 8, 10]}"),
])

# ────────────────────────────────────────────────────────────────────
# 37. Optional
# ────────────────────────────────────────────────────────────────────
ex("optional", "Optional", [
    ("<code>Optional</code> (Java 8+) is a container that may\nor may not contain a value. It helps avoid\n<code>NullPointerException</code> and makes APIs clearer.",
     'import java.util.Optional;\n\npublic class Optionals {\n\n    // A method that may or may not return a value.\n    static Optional<String> findUser(int id) {\n        if (id == 1) {\n            return Optional.of("Alice");\n        }\n        return Optional.empty();\n    }'),
    ("Using Optional values.",
     '    public static void main(String[] args) {\n        // Present value\n        var user = findUser(1);\n        System.out.println("present: " + user.isPresent());\n        System.out.println("value: " + user.get());\n\n        // Absent value with default\n        var missing = findUser(99);\n        System.out.println("absent: " + missing.orElse("unknown"));'),
    ("Chaining operations on Optional.",
     '        // Map and flatMap\n        var upper = findUser(1)\n            .map(String::toUpperCase);\n        System.out.println("mapped: " + upper.orElse("N/A"));\n\n        // ifPresent\n        findUser(1).ifPresent(u ->\n            System.out.println("found: " + u));\n    }\n}'),
], [
    ("", "$ java Optionals.java\npresent: true\nvalue: Alice\nabsent: unknown\nmapped: ALICE\nfound: Alice"),
])

# ────────────────────────────────────────────────────────────────────
# 38. Reading Files
# ────────────────────────────────────────────────────────────────────
ex("reading-files", "Reading Files", [
    ("Reading files is a common task. Java provides\nseveral ways to read files.",
     'import java.io.*;\nimport java.nio.file.*;\n\npublic class ReadingFiles {\n    public static void main(String[] args) throws Exception {\n        // Read an entire file into a string (Java 11+)\n        String content = Files.readString(Path.of("/tmp/dat"));\n        System.out.println(content);'),
    ("Reading all lines into a list.",
     '        // Read all lines\n        var lines = Files.readAllLines(Path.of("/tmp/dat"));\n        for (var line : lines) {\n            System.out.println("line: " + line);\n        }'),
    ("Reading with a BufferedReader for large files.",
     '        // Buffered reading\n        try (var reader = Files.newBufferedReader(Path.of("/tmp/dat"))) {\n            String line;\n            while ((line = reader.readLine()) != null) {\n                System.out.println("buf: " + line);\n            }\n        }\n    }\n}'),
], [
    ("", "$ echo -e \"hello\\njava\" > /tmp/dat\n$ java ReadingFiles.java\nhello\njava\nline: hello\nline: java\nbuf: hello\nbuf: java"),
])

# ────────────────────────────────────────────────────────────────────
# 39. Writing Files
# ────────────────────────────────────────────────────────────────────
ex("writing-files", "Writing Files", [
    ("Writing files in Java follows similar patterns\nto reading them.",
     'import java.io.*;\nimport java.nio.file.*;\n\npublic class WritingFiles {\n    public static void main(String[] args) throws Exception {\n        // Write a string directly (Java 11+)\n        Files.writeString(Path.of("/tmp/dat1"), "hello\\njava\\n");'),
    ("Writing with more control using BufferedWriter.",
     '        // Buffered writing\n        try (var writer = Files.newBufferedWriter(\n                Path.of("/tmp/dat2"))) {\n            writer.write("buffered\\n");\n            writer.write("writes\\n");\n        } // auto-flushes and closes'),
    ("Appending to files.",
     '        // Append to an existing file\n        Files.writeString(\n            Path.of("/tmp/dat1"),\n            "appended\\n",\n            StandardOpenOption.APPEND);\n\n        // Verify\n        System.out.print(Files.readString(Path.of("/tmp/dat1")));\n        System.out.print(Files.readString(Path.of("/tmp/dat2")));\n    }\n}'),
], [
    ("", "$ java WritingFiles.java\nhello\njava\nappended\nbuffered\nwrites"),
])

# ────────────────────────────────────────────────────────────────────
# 40. HTTP Client
# ────────────────────────────────────────────────────────────────────
ex("http-client", "HTTP Client", [
    ("Java 11+ includes a modern <code>HttpClient</code>\nin the standard library.",
     'import java.net.URI;\nimport java.net.http.*;\nimport java.net.http.HttpResponse.BodyHandlers;\n\npublic class HttpClientExample {\n    public static void main(String[] args) throws Exception {\n        var client = HttpClient.newHttpClient();'),
    ("Simple GET request.",
     '        // GET request\n        var request = HttpRequest.newBuilder()\n            .uri(URI.create("https://httpbin.org/get"))\n            .build();\n\n        var response = client.send(request,\n            BodyHandlers.ofString());\n        System.out.println("status: " + response.statusCode());\n        System.out.println("body length: " + response.body().length());'),
    ("POST request with a body.",
     '        // POST request\n        var postReq = HttpRequest.newBuilder()\n            .uri(URI.create("https://httpbin.org/post"))\n            .header("Content-Type", "application/json")\n            .POST(HttpRequest.BodyPublishers\n                .ofString("{\\\"key\\\": \\\"value\\\"}"))\n            .build();\n\n        var postRes = client.send(postReq,\n            BodyHandlers.ofString());\n        System.out.println("post status: " + postRes.statusCode());\n    }\n}'),
], [
    ("", "$ java HttpClientExample.java\nstatus: 200\nbody length: 256\npost status: 200"),
])

# ────────────────────────────────────────────────────────────────────
# 41. HTTP Server
# ────────────────────────────────────────────────────────────────────
ex("http-server", "HTTP Server", [
    ("Java includes a simple built-in HTTP server via\n<code>com.sun.net.httpserver</code>. For production,\nuse frameworks like Spring Boot or Javalin.",
     'import com.sun.net.httpserver.*;\nimport java.io.*;\nimport java.net.InetSocketAddress;\n\npublic class HttpServer {\n\n    static void hello(HttpExchange exchange) throws IOException {\n        var response = "hello\\n";\n        exchange.sendResponseHeaders(200, response.length());\n        try (var os = exchange.getResponseBody()) {\n            os.write(response.getBytes());\n        }\n    }'),
    ("Setting up request handlers.",
     '    static void headers(HttpExchange exchange) throws IOException {\n        var headers = exchange.getRequestHeaders();\n        var sb = new StringBuilder();\n        headers.forEach((key, values) ->\n            sb.append(key).append(": ")\n              .append(String.join(", ", values)).append("\\n"));\n        var response = sb.toString();\n        exchange.sendResponseHeaders(200, response.length());\n        try (var os = exchange.getResponseBody()) {\n            os.write(response.getBytes());\n        }\n    }'),
    ("Starting the server.",
     '    public static void main(String[] args) throws Exception {\n        var server = com.sun.net.httpserver.HttpServer\n            .create(new InetSocketAddress(8090), 0);\n        server.createContext("/hello", HttpServer::hello);\n        server.createContext("/headers", HttpServer::headers);\n        server.start();\n        System.out.println("Server on :8090");\n    }\n}'),
], [
    ("Run the server in the background and test with curl.",
     "$ java HttpServer.java &\n$ curl localhost:8090/hello\nhello"),
])

# ────────────────────────────────────────────────────────────────────
# 42. Command-Line Arguments
# ────────────────────────────────────────────────────────────────────
ex("command-line-arguments", "Command-Line Arguments", [
    ("<a href=\"https://docs.oracle.com/javase/tutorial/essential/environment/cmdLineArgs.html\">Command-line arguments</a>\nare available in the <code>String[] args</code>\nparameter of the <code>main</code> method.",
     'public class CommandLineArgs {\n    public static void main(String[] args) {\n        // args contains all arguments (no program name)\n        System.out.println("args: " + java.util.Arrays.toString(args));\n        System.out.println("count: " + args.length);\n\n        if (args.length >= 3) {\n            System.out.println("3rd: " + args[2]);\n        }\n    }\n}'),
], [
    ("Note that unlike Go/C, the program name is NOT\nincluded in <code>args</code>.",
     "$ java CommandLineArgs.java a b c d\nargs: [a, b, c, d]\ncount: 4\n3rd: c"),
])

# ────────────────────────────────────────────────────────────────────
# 43. Environment Variables
# ────────────────────────────────────────────────────────────────────
ex("environment-variables", "Environment Variables", [
    ("<a href=\"https://docs.oracle.com/javase/tutorial/essential/environment/env.html\">Environment variables</a>\nare read using <code>System.getenv()</code>.",
     'public class EnvironmentVariables {\n    public static void main(String[] args) {\n        // Get a specific variable\n        System.out.println("HOME: " + System.getenv("HOME"));\n        System.out.println("FOO:  " + System.getenv("FOO"));'),
    ("List all environment variables.",
     '        // All environment variables\n        System.out.println();\n        System.getenv().forEach((key, val) -> {\n            if (key.startsWith("JAVA")) {\n                System.out.println(key + "=" + val);\n            }\n        });\n    }\n}'),
], [
    ("", "$ FOO=bar java EnvironmentVariables.java\nHOME: /home/user\nFOO:  bar\n\nJAVA_HOME=/usr/lib/jvm/java-21"),
])

# ────────────────────────────────────────────────────────────────────
# 44. Logging
# ────────────────────────────────────────────────────────────────────
ex("logging", "Logging", [
    ("Java includes <code>java.util.logging</code> in the\nstandard library. In practice, many projects use\n<em>SLF4J</em> with <em>Logback</em> or <em>Log4j2</em>.",
     'import java.util.logging.*;\n\npublic class LoggingExample {\n    static final Logger logger = Logger.getLogger(\n        LoggingExample.class.getName());\n\n    public static void main(String[] args) {\n        // Default log levels\n        logger.info("This is an info message");\n        logger.warning("This is a warning");\n        logger.severe("This is severe");'),
    ("Configuring log format.",
     '        // Custom format\n        var handler = new ConsoleHandler();\n        handler.setFormatter(new SimpleFormatter() {\n            @Override\n            public String format(LogRecord r) {\n                return String.format("[%s] %s: %s%n",\n                    r.getLevel(), r.getLoggerName(),\n                    r.getMessage());\n            }\n        });\n        logger.addHandler(handler);\n        logger.setUseParentHandlers(false);\n\n        logger.info("Custom formatted message");\n    }\n}'),
], [
    ("", "$ java LoggingExample.java\nJan 15, 2024 10:30:00 AM LoggingExample main\nINFO: This is an info message\nJan 15, 2024 10:30:00 AM LoggingExample main\nWARNING: This is a warning\nJan 15, 2024 10:30:00 AM LoggingExample main\nSEVERE: This is severe\n[INFO] LoggingExample: Custom formatted message"),
])

# ────────────────────────────────────────────────────────────────────
# 45. Processes
# ────────────────────────────────────────────────────────────────────
ex("processes", "Processes", [
    ("Java can spawn external processes using\n<code>ProcessBuilder</code>.",
     'import java.io.*;\n\npublic class Processes {\n    public static void main(String[] args) throws Exception {\n        // Simple command\n        var process = new ProcessBuilder("date")\n            .start();\n        var output = new String(\n            process.getInputStream().readAllBytes());\n        System.out.println("output: " + output.trim());\n        System.out.println("exit: " + process.waitFor());'),
    ("Running commands with arguments and handling stderr.",
     '        // Command with arguments\n        var p2 = new ProcessBuilder("ls", "-la", "/tmp")\n            .redirectErrorStream(true)\n            .start();\n        var lines = new BufferedReader(\n            new InputStreamReader(p2.getInputStream()))\n            .lines().limit(3).toList();\n        lines.forEach(System.out::println);\n        p2.waitFor();\n    }\n}'),
], [
    ("", "$ java Processes.java\noutput: Thu Jan 15 10:30:00 UTC 2024\nexit: 0\ntotal 48\ndrwxrwxrwt 12 root root 4096 Jan 15 10:30 .\ndrwxr-xr-x 19 root root 4096 Jan 10 00:00 .."),
])

# ────────────────────────────────────────────────────────────────────
# 46. Exit
# ────────────────────────────────────────────────────────────────────
ex("exit", "Exit", [
    ("Use <code>System.exit()</code> to immediately exit with\na given status code.",
     'public class Exit {\n    public static void main(String[] args) {\n        // This will be printed\n        System.out.println("starting");\n\n        // Exit with status 3\n        // Note: finally blocks and shutdown hooks\n        // may or may not run depending on the JVM\n        System.exit(3);\n\n        // This will never be reached\n        System.out.println("unreachable");\n    }\n}'),
], [
    ("If you run <code>exit</code>, it will exit with\nstatus 3. The shell will show the exit code.",
     "$ java Exit.java\nstarting\n$ echo $?\n3"),
    ("Note that unlike Go, the <code>main</code> method\nreturning normally exits with status 0.\nUse <code>System.exit(code)</code> for non-zero exits.", None),
])


# ─── HTML Generation ───────────────────────────────────────────────

def esc(s):
    """Escape code for HTML but preserve already-escaped entities."""
    if s is None:
        return None
    return html.escape(s).replace("&amp;lt;", "&lt;").replace("&amp;gt;", "&gt;").replace("&amp;amp;", "&amp;")

def highlight_java(code):
    """Simple regex-based Java syntax highlighting."""
    import re
    
    keywords = {'abstract','assert','boolean','break','byte','case','catch',
                'char','class','const','continue','default','do','double',
                'else','enum','extends','final','finally','float','for',
                'goto','if','implements','import','instanceof','int',
                'interface','long','native','new','package','permits',
                'private','protected','public','record','return','sealed',
                'short','static','strictfp','super','switch','synchronized',
                'this','throw','throws','transient','try','var','void',
                'volatile','while','yield'}
    
    kw_constants = {'true', 'false', 'null'}
    builtins = {'System', 'Math', 'String', 'Integer', 'Long', 'Double',
                'Boolean', 'Object', 'Thread', 'Optional', 'List', 'Map',
                'Set', 'Arrays', 'Collections', 'Collectors', 'Path',
                'Files', 'Pattern', 'Matcher'}
    
    # Regex tokenizer: order matters
    token_re = re.compile(
        r'(//[^\n]*)'           # line comment
        r'|("(?:[^"\\]|\\.)*")' # string literal
        r"|('(?:[^'\\]|\\.)*')" # char literal
        r'|(\b\d[\d_.eExXabcdefABCDEFL]*\b)' # number
        r'|(\b[a-zA-Z_@][a-zA-Z0-9_]*\b)' # word
        r'|([^\s\w"\']+|\s+)'  # punctuation / whitespace
    )
    
    def replace_token(m):
        comment, string, char, number, word, other = m.groups()
        if comment:
            return f'<span class="c1">{html.escape(comment)}</span>'
        if string:
            return f'<span class="s">{html.escape(string)}</span>'
        if char:
            return f'<span class="sc">{html.escape(char)}</span>'
        if number:
            return f'<span class="mi">{html.escape(number)}</span>'
        if word:
            if word in keywords:
                return f'<span class="k">{word}</span>'
            if word in kw_constants:
                return f'<span class="kc">{word}</span>'
            if word in builtins:
                return f'<span class="nb">{word}</span>'
            return f'<span class="nx">{html.escape(word)}</span>'
        if other:
            return f'<span class="p">{html.escape(other)}</span>'
        return html.escape(m.group(0))
    
    return token_re.sub(replace_token, code)


def highlight_shell(code):
    """Highlight shell output."""
    lines = code.split('\n')
    out = []
    for line in lines:
        if line.startswith('$ '):
            out.append(f'<span class="gp">$</span><span class="go">{html.escape(line[1:])}</span>')
        else:
            out.append(f'<span class="go">{html.escape(line)}</span>')
    return '\n'.join(out)


def make_code_html(code, is_shell=False):
    if is_shell:
        return highlight_shell(code)
    return highlight_java(code)


def gen_example_page(idx, slug, title, sections, output_sections):
    prev_link = '../' + EXAMPLES[idx-1][0] if idx > 0 else None
    next_link = '../' + EXAMPLES[idx+1][0] if idx < len(EXAMPLES)-1 else None
    next_title = EXAMPLES[idx+1][1] if idx < len(EXAMPLES)-1 else None
    
    # Key navigation script
    nav_script = "  <script>\n      window.onkeydown = (e) => {\n          if (e.ctrlKey || e.altKey || e.shiftKey || e.metaKey) {\n              return;\n          }\n"
    if prev_link:
        nav_script += f"          if (e.key == \"ArrowLeft\") {{\n              window.location.href = '{prev_link}';\n          }}\n"
    if next_link:
        nav_script += f"          if (e.key == \"ArrowRight\") {{\n              window.location.href = '{next_link}';\n          }}\n"
    nav_script += "      }\n  </script>\n"
    
    h = f'''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Java by Example: {title}</title>
    <link rel=stylesheet href="../site.css">
  </head>
{nav_script}  <body>
    <div class="example" id="{slug}">
      <h2><a href="../">Java by Example</a>: {title}</h2>
      
      <table>
'''
    
    # Code sections
    for i, (comment, code) in enumerate(sections):
        is_leading = "leading" if i < len(sections) - 1 else ""
        docs_html = f"<p>{comment}</p>" if comment else ""
        
        if code is not None:
            code_html = make_code_html(code, False)
            code_cell = f'''          <pre class="chroma"><code>{code_html}</code></pre>'''
            h += f'''        <tr>
          <td class="docs">
            {docs_html}
          </td>
          <td class="code {is_leading}">
            <img title="Copy code" src="../clipboard.png" class="copy" onclick="copyCode(this)" />
{code_cell}
          </td>
        </tr>
        
'''
        else:
            h += f'''        <tr>
          <td class="docs">
            {docs_html}
          </td>
          <td class="code empty {is_leading}">
            
          </td>
        </tr>
        
'''
    
    h += '''      </table>
'''
    
    # Output sections
    if output_sections:
        h += '''      
      <table>
'''
        for i, (comment, code) in enumerate(output_sections):
            is_leading = "leading" if i < len(output_sections) - 1 else ""
            docs_html = f"<p>{comment}</p>" if comment else ""
            
            if code is not None:
                code_html = make_code_html(code, True)
                h += f'''        <tr>
          <td class="docs">
            {docs_html}
          </td>
          <td class="code {is_leading}">
          <pre class="chroma"><code>{code_html}</code></pre>
          </td>
        </tr>
        
'''
            else:
                h += f'''        <tr>
          <td class="docs">
            {docs_html}
          </td>
          <td class="code empty">
            
          </td>
        </tr>
        
'''
        h += '''      </table>
'''
    
    # Navigation
    if next_link:
        h += f'''      
      <p class="next">
        Next example: <a href="{next_link}" rel="next">{next_title}</a>.
      </p>
      
'''
    
    h += f'''      <p class="footer">
        <a href="https://github.com/omrieival/javabyexample">source</a> |
        inspired by <a href="https://gobyexample.com/">Go by Example</a>
      </p>
      
    </div>
    <script>
    function copyCode(btn) {{
      const pre = btn.parentElement.querySelector("pre");
      navigator.clipboard.writeText(pre.textContent);
    }}
    </script>
  </body>
</html>
'''
    return h


def gen_index():
    h = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Java by Example</title>
    <link rel=stylesheet href="site.css">
  </head>
  <body>
    <div id="intro">
      <h2><a href="./">Java by Example</a></h2>
      <p>
        <a href="https://dev.java">Java</a> is a
        widely-used, object-oriented programming language
        designed for building robust, secure, and
        high-performance applications.
        Please read the
        <a href="https://dev.java/learn/">official documentation</a>
        to learn more.
      </p>

      <p>
        <em>Java by Example</em> is a hands-on introduction
        to Java using annotated example programs. Check out
        the <a href="hello-world">first example</a> or
        browse the full list below.
      </p>

      <p>
        Unless stated otherwise, examples here assume
        <a href="https://jdk.java.net/21/">Java 21+</a>
        and may use newer language features like records,
        sealed classes, pattern matching, and virtual threads.
      </p>

      <ul>
'''
    for slug, title, _, _ in EXAMPLES:
        h += f'        <li><a href="{slug}">{title}</a></li>\n'
    
    h += '''      </ul>

      <p class="footer">
        <a href="https://github.com/omrieival/javabyexample">source</a> |
        inspired by <a href="https://gobyexample.com/">Go by Example</a>
      </p>
    </div>
  </body>
</html>
'''
    return h


def main():
    out_dir = "docs"
    os.makedirs(out_dir, exist_ok=True)
    
    # Generate index
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(gen_index())
    print(f"Generated index.html")
    
    # Generate example pages
    for i, (slug, title, sections, output_sections) in enumerate(EXAMPLES):
        page = gen_example_page(i, slug, title, sections, output_sections)
        page_dir = os.path.join(out_dir, slug)
        os.makedirs(page_dir, exist_ok=True)
        with open(os.path.join(page_dir, "index.html"), "w") as f:
            f.write(page)
        print(f"Generated {slug}/index.html")
    
    print(f"\nTotal: {len(EXAMPLES)} examples generated in {out_dir}/")


if __name__ == "__main__":
    main()
