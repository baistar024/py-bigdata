# Python 基本数据类型

    Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
    可以使用全局type()显示出变量的数据类型
    Python 3中有六个标准的数据类型：Numbers（数字）、String（字符串）、List（列表）、Tuple（元组）、Sets（集合）、Dictionaries（字典）
    以下是 Python 内置类型的列表。扩展模块 (具体实现会以 C, Java 或其他语言编写) 可以定义更多的类型。未来版本的 Python 可能会加入更多的类型 (例如有理数、高效存储的整型数组等等)，不过新增类型往往都是通过标准库来提供的。

## 标准类型层级结构
    numbers.Number
    此类对象由数字字面值创建，并会被作为算术运算符和算术内置函数的返回结果。数字对象是不可变的；一旦创建其值就不再改变。
    Python 中的数字当然非常类似数学中的数字，但也受限于计算机中的数字表示方法。
### Python数字类型 
    1. 区分整型数、浮点型数和复数:
    numbers.Integral
    此类对象表示数学中整数集合的成员 (包括正数和负数)。    
    整型数可细分为两种类型:    
    整型 (int)    
    此类对象表示任意大小的数字，仅受限于可用的内存 (包括虚拟内存)。在变换和掩码运算中会以二进制表示，负数会以 2 的补码表示，看起来像是符号位向左延伸补满空位。
    布尔型 (bool)
    此类对象表示逻辑值 False 和 True。代表 False 和 True 值的两个对象是唯二的布尔对象。
    布尔类型是整型的子类型，两个布尔值在各种场合的行为分别类似于数值 0 和 1，例外情况只有在转换为字符串时分别返回字符串 "False" 或 "True"。
    整型数表示规则的目的是在涉及负整型数的变换和掩码运算时提供最为合理的解释。
    2.实数型
    numbers.Real (float)
    此类对象表示机器级的双精度浮点数。其所接受的取值范围和溢出处理将受制于底层的机器架构 (以及 C 或 Java 实现)。Python 不支持单精度浮点数；支持后者通常的理由是节省处理器和内存消耗，但这点节省相对于在 Python 中使用对象的开销来说太过微不足道，因此没有理由包含两种浮点数而令该语言变得复杂。
    3.复数型
    numbers.Complex (complex)
    此类对象以一对机器级的双精度浮点数来表示复数值。有关浮点数的附带规则对其同样有效。一个复数值 z 的实部和虚部可通过只读属性 z.real 和 z.imag 来获取。

### 序列
    此类对象表示以非负整数作为索引的有限有序集。
    内置函数 len() 可返回一个序列的条目数量。
    当一个序列的长度为 n 时，索引集包含数字 0, 1, ..., n-1。序列 a 的条目 i 可通过 a[i] 选择。    
    序列还支持切片: a[i:j] 选择索引号为 k 的所有条目，i <= k < j。当用作表达式时，序列的切片就是一个与序列类型相同的新序列。新序列的索引还是从 0 开始。
    有些序列还支持带有第三个 "step" 形参的 "扩展切片": a[i:j:k] 选择 a 中索引号为 x 的所有条目，x = i + n*k, n >= 0 且 i <= x < j。
    序列可根据其可变性来加以区分:    
    不可变序列
    不可变序列类型的对象一旦创建就不能再改变。
    (如果对象包含对其他对象的引用，其中的可变对象就是可以改变的；但是，一个不可变对象所直接引用的对象集是不能改变的。)    
    
#### 以下类型属于不可变对象:
    字符串
    字符串是由 Unicode 码位值组成的序列。范围在 U+0000 - U+10FFFF 之内的所有码位值都可在字符串中使用。Python 没有 char 类型；而是将字符串中的每个码位表示为一个长度为 1 的字符串对象。内置函数 ord() 可将一个码位由字符串形式转换成一个范围在 0 - 10FFFF 之内的整型数；chr() 可将一个范围在 0 - 10FFFF 之内的整型数转换为长度为 1 的对应字符串对象。str.encode() 可以使用指定的文本编码将 str 转换为 bytes，而 bytes.decode() 则可以实现反向的解码。
    元组
    一个元组中的条目可以是任意 Python 对象。包含两个或以上条目的元组由逗号分隔的表达式构成。只有一个条目的元组 ('单项元组') 可通过在表达式后加一个逗号来构成 (一个表达式本身不能创建为元组，因为圆括号要用来设置表达式分组)。一个空元组可通过一对内容为空的圆括号创建。
    字节串
    字节串对象是不可变的数组。其中每个条目都是一个 8 位字节，以取值范围 0 <= x < 256 的整型数表示。字节串字面值 (例如 b'abc') 和内置的 bytes() 构造器可被用来创建字节串对象。字节串对象还可以通过 decode() 方法解码为字符串。
    
#### 可变序列
    可变序列在被创建后仍可被改变。下标和切片标注可被用作赋值和 del (删除) 语句的目标。    
    目前有两种内生可变序列类型:    
    列表
    列表中的条目可以是任意 Python 对象。列表由用方括号括起并由逗号分隔的多个表达式构成。(注意创建长度为 0 或 1 的列表无需使用特殊规则。)    
    字节数组
    字节数组对象属于可变数组。可以通过内置的 bytearray() 构造器来创建。除了是可变的 
    (因而也是不可哈希的)，在其他方面字节数组提供的接口和功能都于不可变的 bytes 对象一致。
    扩展模块 array 提供了一个额外的可变序列类型示例，collections 模块也是如此。

### 集合类型
    此类对象表示由不重复且不可变对象组成的无序且有限的集合。因此它们不能通过下标来索引。但是它们可被迭代，也可用内置函数 len() 返回集合中的条目数。
    集合常见的用处是快速成员检测，去除序列中的重复项，以及进行交、并、差和对称差等数学运算。
    
    对于集合元素所采用的不可变规则与字典的键相同。注意数字类型遵循正常的数字比较规则: 如果两个数字相等 (例如 1 和 1.0)，则同一集合中只能包含其中一个。    
    目前有两种内生集合类型:    
    集合
    此类对象表示可变集合。它们可通过内置的 set() 构造器创建，并且创建之后可以通过方法进行修改，例如 add()。    
    冻结集合
    此类对象表示不可变集合。它们可通过内置的 frozenset() 构造器创建。由于 frozenset 对象不可变且 hashable，它可以被用作另一个集合的元素或是字典的键。

#### 映射
    此类对象表示由任意索引集合所索引的对象的集合。
    通过下标 a[k] 可在映射 a 中选择索引为 k 的条目；这可以在表达式中使用，也可作为赋值或 del 语句的目标。内置函数 len() 可返回一个映射中的条目数。
    目前只有一种内生映射类型:

    字典
    此类对象表示由几乎任意值作为索引的有限个对象的集合。
    不可作为键的值类型只有包含列表或字典或其他可变类型，通过值而非对象编号进行比较的值，其原因在于高效的字典实现需要使用键的哈希值以保持一致性。
    用作键的数字类型遵循正常的数字比较规则: 如果两个数字相等 (例如 1 和 1.0) 则它们均可来用来索引同一个字典条目。    
    字典会保留插入顺序，这意味着键将以它们被添加的顺序在字典中依次产生。 替换某个现有的键不会改变其顺序，但是移除某个键再重新插入则会将其添加到末尾而不会保留其原有位置。    
    字典是可变的；它们可通过 {...} 标注来创建 (参见 字典显示 小节)。    
    扩展模块 dbm.ndbm 和 dbm.gnu 提供了额外的映射类型示例，collections 模块也是如此。

## 字符串数据类型
    在Python中处理文本数据是使用 str 对象，也称为字符串。 字符串是由 Unicode 码位构成的不可变序列。 字符串字面值有多种不同的写法：
### 字符串数据类型表示    
    字符串由成对的单引号、双引号和三对单引号或双引号括起的字一串字符 
    为了避免歧义，使用\符号转义特定意义的字符，我们称为转义符号，如果使用三个双引号和三个单引号括起来的字符不用转义字符，原样输出。
    字符串是可以被索引的，字符串的第一个字符的索引为 0。没有单独的字符类型；一个字符就是长度为一的字符串。
    字符串也可以通过使用 str 构造器从其他对象创建。
### 字符型常量
    字符型常量就是字符的字面值，字符串共有两一种是字节串另外一种是字符串，两种字面值都可以用成对单引号 (') 或双引号 (") 来标示首尾。反斜杠 (\) 字符被用来对特殊含义的字符进行转义，
    它们也可以用成对的连续三个单引号或双引号来标示首尾 (这通常被称为 三引号字符串)。
    字节串前缀为b或b表示这是一个字节串，r和R前缀表示原始字符串，其中的反斜杠会被当作其本身的字面字符来处理。f或F表示格式化字符串， u或U表示是unicode编码字段串
     
### 字符串数据的运算符号
    
    + 将两个字符串原样连接    str1 + str2
    * 重复前一个字符串多少次  str1 * 5
    
### 字符串的格式化
     格式化字符串常量， 是带有 'f' 或 'F' 前缀的字符串字面值。这种字符串可包含替换字段，即以 {} 标示的表达式。
     我们可以认为{}是占位符，格式化字符串字面值实际上是会在运行时被求值的表达式。
     字符串在花括号以外的部分按其字面值处理，
     支持的转换旗标有三种:对花括号内使用 '!s' 会对值调用 str()，'!r' 调用 repr() 而 '!a' 则调用 ascii()执行不同字面求值。 
     
### 格式说明 
    [[fill] align] [sign] [#] [0] [width] [grouping_option] [.precision] [type] 
    -------------  -----
        1            2     3   4     5            6              7          8
```
    1. 对齐格式     
    对齐选项的含义如下：
    选项      含义
    '<'     强制字段在可用空间内左对齐（这是大多数对象的默认值）。
    '>'     强制字段在可用空间内右对齐（这是数字的默认值）。
    '='     强制将填充放置在符号（如果有）之后但在数字之前。这用于以“+000000120”形式打印字段。此对齐选项仅对数字类型有效。当'0'紧接在字段宽度之前时，它成为默认值。
    '^'     强制字段在可用空间内居中。
    2. sign 选项仅对数字类型有效，可以是以下之一：
    选项      含义
    '+'     表示标志应该用于正数和负数。
    '-'     表示标志应仅用于负数（这是默认行为）。
    space   表示应在正数上使用前导空格，在负数上使用减号。
    3. '#' 选项
    可以让“替代形式”被用于转换。 替代形式可针对不同类型分别定义。 此选项仅对整数、浮点、复数和 Decimal 类型有效。 
    对于整数类型，当使用二进制、八进制或十六进制输出时，此选项会为输出值添加相应的 '0b', '0o' 或 '0x' 前缀。 
    对于浮点数、复数和 Decimal 类型，替代形式会使得转换结果总是包含小数点符号，即使其不带小数。 通常只有在带有小数的情况下，此类转换的结果中才会出现小数点符号。 
    对于 'g' 和 'G' 转换，末尾的零不会从结果中被移除。
    4. [0]选项
    当未显式给出对齐方式时，在 width 字段前加一个零 ('0') 字段将为数字类型启用感知正负号的零填充。 这相当于设置 fill 字符为 '0' 且 alignment 类型为 '='。
    5. width选项
    width 是一个定义最小总字段宽度的十进制整数，包括任何前缀、分隔符和其他格式化字符。 如果未指定，则字段宽度将由内容确定。    
    6. grouping_option选项
        ','或'_' 选项表示使用逗号作为千位分隔符。 对于感应区域设置的分隔符，
    7. .precision选项
    是一个十进制数字，表示对于以 'f' and 'F' 格式化的浮点数值要在小数点后显示多少个数位，
    或者对于以 'g' 或 'G' 格式化的浮点数值要在小数点前后共显示多少个数位。 
    对于非数字类型，该字段表示最大字段大小 —— 换句话说就是要使用多少个来自字段内容的字符。 
    对于整数值则不允许使用 precision。
    8.type 选项
        "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
    's'     字符串格式。这是字符串的默认类型，可以省略。    
    'b'		二进制格式。 输出以 2 为基数的数字。
    'c'     字符。在打印之前将整数转换为相应的unicode字符。
    'd'     十进制整数。 输出以 10 为基数的数字。
    'o'     八进制格式。 输出以 8 为基数的数字。
    'x'     十六进制格式。 输出以 16 为基数的数字，使用小写字母表示 9 以上的数码。
    'X'     十六进制格式。 输出以 16 为基数的数字，使用大写字母表示 9 以上的数码。
    'n'     数字。 这与 'd' 相似，不同之处在于它会使用当前区域设置来插入适当的数字分隔字符。
    None    和 'd' 相同。
    'e'     指数表示。 以使用字母 'e' 来标示指数的科学计数法打印数字。 默认的精度为 6。
    'E'     指数表示。 与 'e' 相似，不同之处在于它使用大写字母 'E' 作为分隔字符。
    'f'     定点表示。 将数字显示为一个定点数。 默认的精确度为 6。
    'F'     定点表示。 与 'f' 相似，但会将 nan 转为 NAN 并将 inf 转为 INF。
    'g'     常规格式。 对于给定的精度 p >= 1，这会将数值舍入到 p 位有效数字，再将结果以定点格式或科学计数法进行格式化，具体取决于其值的大小。
            准确的规则如下：假设使用表示类型 'e' 和精度 p-1 进行格式化的结果具有指数值 exp。 
            那么如果 m <= exp < p，其中 m 以 -4 表示浮点值而以 -6 表示 Decimal 值，该数字将使用类型 'f' 和精度 p-1-exp 进行格式化。 
            否则的话，该数字将使用表示类型 'e' 和精度 p-1 进行格式化。 
            在两种情况下，都会从有效数字中移除无意义的末尾零，如果小数点之后没有余下数字则小数点也会被移除，除非使用了 '#' 选项。
            正负无穷，正负零和 nan 会分别被格式化为 inf, -inf, 0, -0 和 nan，无论精度如何设定。
            精度 0 会被视为等同于精度 1。 默认精度为 6。
    'G'     常规格式。 类似于 'g'，不同之处在于当数值非常大时会切换为 'E'。 无穷与 NaN 也会表示为大写形式。
    'n'     数字。 这与 'g' 相似，不同之处在于它会使用当前区域设置来插入适当的数字分隔字符。
    '%'     百分比。 将数字乘以 100 并显示为定点 ('f') 格式，后面带一个百分号。
    None    类似于 'g'，不同之处在于当使用定点表示法时，小数点后将至少显示一位。 默认精度与表示给定值所需的精度一样。
            整体效果为与其他格式修饰符所调整的 str() 输出保持一致。         
     

```
### 字符串函数 
    字符串实现了所有一般序列的操作，还额外提供了以下列出的一些附加方法。 
    str.capitalize()  返回原字符串的副本，其首个字符大写，其余为小写。
    str.casefold()  返回原字符串消除大小写的副本。 消除大小写的字符串可用于忽略大小写的匹配。消除大小写类似于转为小写，但是更加彻底一些，
                    因为它会移除字符串中的所有大小写变化形式。 例如，德语小写字母 'ß' 相当于 "ss"。 
                    由于它已经是小写了，lower() 不会对 'ß' 做任何改变；而 casefold() 则会将其转换为 "ss"。
    str.center(width[, fillchar]) 返回长度为 width 的字符串，原字符串在其正中。 
                    使用指定的 fillchar 填充两边的空位（默认使用 ASCII 空格符）。 如果 width 小于等于 len(s) 则返回原字符串的副本。
    str.count(sub[, start[, end]]) 返回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。
                    可选参数 start 与 end 会被解读为切片表示法。                
    str.encode(encoding="utf-8", errors="strict") 返回原字符串编码为字节串对象的版本。 默认编码为 'utf-8'。
     可以给出 errors 来设置不同的错误处理方案。 errors 的默认值为 'strict'，表示编码错误会引发 UnicodeError。 
     其他可用的值为 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及任何其他通过 codecs.register_error() 注册的值。
    str.endswith(suffix[, start[, end]])  如果字符串以指定的 suffix 结束返回 True，否则返回 False。 
    suffix 也可以为由多个供查找的后缀构成的元组。 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较。
    str.expandtabs(tabsize=8)   返回字符串的副本，其中所有的制表符会由一个或多个空格替换，具体取决于当前列位置和给定的制表符宽度。
     每 tabsize 个字符设为一个制表位（默认值 8 时设定的制表位在列 0, 8, 16 依次类推）。 
     要展开字符串，当前列将被设为零并逐一检查字符串中的每个字符。 如果字符为制表符 (\t)，则会在结果中插入一个或多个空格符，直到当前列等于下一个制表位。 
     （制表符本身不会被复制。） 如果字符为换行符 (\n) 或回车符 (\r)，它会被复制并将当前列重设为零。 
     任何其他字符会被不加修改地复制并将当前列加一，不论该字符在被打印时会如何显示。
    str.find(sub[, start[, end]])   返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引。
     可选参数 start 与 end 会被解读为切片表示法。 如果 sub 未被找到则返回 -1。
     注解 find() 方法应该只在你需要知道 sub 所在位置时使用。 要检查 sub 是否为子字符串，请使用 in 操作符:
    str.format(*args, **kwargs) 执行字符串格式化操作。 
    调用此方法的字符串可以包含字符串字面值或者以花括号 {} 括起来的替换域。
     每个替换域可以包含一个位置参数的数字索引，或者一个关键字参数的名称。 
     返回的字符串副本中每个替换域都会被替换为对应参数的字符串值。
    注解 当使用 n 类型 (例如: '{:n}'.format(1234)) 来格式化数字 (int, float, complex, decimal.Decimal 及其子类) 的时候，
    该函数会临时性地将 LC_CTYPE 区域设置为 LC_NUMERIC 区域以解码 localeconv() 的 decimal_point 和 thousands_sep 字段，
    如果它们是非 ASCII 字符或长度超过 1 字节的话，并且 LC_NUMERIC 区域会与 LC_CTYPE 区域不一致。 这个临时更改会影响其他线程。
    str.format_map(mapping) 类似于 str.format(**mapping)，不同之处在于 mapping 会被直接使用而不是复制到一个 dict。
     适宜使用此方法的一个例子是当 mapping 为 dict 的子类的情况：
    str.index(sub[, start[, end]])  类似于 find()，但在找不到子类时会引发 ValueError。    
    str.isalnum()       如果字符串中的所有字符都是字母或数字且至少有一个字符，则返回 True ， 否则返回 False 。 
    如果 c.isalpha() ， c.isdecimal() ， c.isdigit() ，或 c.isnumeric() 之中有一个返回 True ，则字符``c``是字母或数字。
    str.isalpha()   如果字符串中的所有字符都是字母，并且至少有一个字符，返回 True ，否则返回 False 。
    字母字符是指那些在 Unicode 字符数据库中定义为 "Letter" 的字符，即那些具有 "Lm"、"Lt"、"Lu"、"Ll" 或 "Lo" 之一的通用类别属性的字符。 
    注意，这与 Unicode 标准中定义的"字母"属性不同。
    str.isascii()       如果字符串为空或字符串中的所有字符都是 ASCII ，返回 True ，否则返回 False 。ASCII 字符的码点范围是 U+0000-U+007F 。
    str.isdecimal()     如果字符串中的所有字符都是十进制字符且该字符串至少有一个字符，则返回 True ， 否则返回 False 。
    十进制字符指那些可以用来组成10进制数字的字符，例如 U+0660 ，即阿拉伯字母数字0 。 严格地讲，十进制字符是 Unicode 通用类别 "Nd" 中的一个字符。
    str.isdigit()       如果字符串中的所有字符都是数字，并且至少有一个字符，返回 True ，否则返回 False 。 
    数字包括十进制字符和需要特殊处理的数字，如兼容性上标数字。这包括了不能用来组成十进制数的数字，如 Kharosthi 数。 
    严格地讲，数字是指属性值为 Numeric_Type=Digit 或 Numeric_Type=Decimal 的字符。
    str.isidentifier()  如果字符串是有效的标识符，返回 True ，依据语言定义， 标识符和关键字。
    调用 keyword.iskeyword() 来检测字符串 s 是否为保留标识符，例如 def 和 class。
    str.isnumeric()     如果字符串中至少有一个字符且所有字符均为数值字符则返回 True ，否则返回 False 。 
    数值字符包括数字字符，以及所有在 Unicode 中设置了数值特性属性的字符，例如 U+2155, VULGAR FRACTION ONE FIFTH。 
    正式的定义为：数值字符就是具有特征属性值 Numeric_Type=Digit, Numeric_Type=Decimal 或 Numeric_Type=Numeric 的字符。
    str.isprintable()   如果字符串中所有字符均为可打印字符或字符串为空则返回 True ，否则返回 False 。 
    不可打印字符是在 Unicode 字符数据库中被定义为 "Other" 或 "Separator" 的字符，例外情况是 ASCII 空格字符 (0x20) 被视作可打印字符。 
    （请注意在此语境下可打印字符是指当对一个字符串发起调用 repr() 时不必被转义的字符。 它们与字符串写入 sys.stdout 或 sys.stderr 时所需的处理无关。）
    str.isspace()   如果字符串中只有空白字符且至少有一个字符则返回 True ，否则返回 False 。
    str.istitle()   如果字符串中至少有一个字符且为标题字符串则返回 True ，例如大写字符之后只能带非大写字符而小写字符必须有大写字符打头。 否则返回 False 。
    str.isupper()   如果字符串中至少有一个区分大小写的字符 4 且此类字符均为大写则返回 True ，否则返回 False 。
    str.join(iterable)  返回一个由 iterable 中的字符串拼接而成的字符串。 
    如果 iterable 中存在任何非字符串值包括 bytes 对象则会引发 TypeError。 调用该方法的字符串将作为元素之间的分隔。
    str.ljust(width[, fillchar])    返回长度为 width 的字符串，原字符串在其中靠左对齐。 
    使用指定的 fillchar 填充空位 (默认使用 ASCII 空格符)。 如果 width 小于等于 len(s) 则返回原字符串的副本。
    str.lower()     返回原字符串的副本，其所有区分大小写的字符均转换为小写。
    str.lstrip([chars]) 返回原字符串的副本，移除其中的前导字符。
     chars 参数为指定要移除字符的字符串。 如果省略或为 None，则 chars 参数默认移除空格符。 实际上 chars 参数并非指定单个前缀；而是会移除参数值的所有组合:
    str.partition(sep)  在 sep 首次出现的位置拆分字符串，返回一个 3 元组，其中包含分隔符之前的部分、分隔符本身，以及分隔符之后的部分。
     如果分隔符未找到，则返回的 3 元组中包含字符本身以及两个空字符串。
    str.replace(old, new[, count])  返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。 如果给出了可选参数 count，则只替换前 count 次出现。
    str.rfind(sub[, start[, end]])  返回子字符串 sub 在字符串内被找到的最大（最右）索引，这样 sub 将包含在 s[start:end] 当中。 
    可选参数 start 与 end 会被解读为切片表示法。 如果未找到则返回 -1。
    str.rindex(sub[, start[, end]]) 类似于 rfind()，但在子字符串 sub 未找到时会引发 ValueError。
    str.rjust(width[, fillchar])    返回长度为 width 的字符串，原字符串在其中靠右对齐。 
    使用指定的 fillchar 填充空位 (默认使用 ASCII 空格符)。 如果 width 小于等于 len(s) 则返回原字符串的副本。
    str.rpartition(sep) 在 sep 最后一次出现的位置拆分字符串，返回一个 3 元组，其中包含分隔符之前的部分、分隔符本身，以及分隔符之后的部分。 
    如果分隔符未找到，则返回的 3 元组中包含两个空字符串以及字符串本身。
    str.rsplit(sep=None, maxsplit=-1)   返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。 
    如果给出了 maxsplit，则最多进行 maxsplit 次拆分，从 最右边 开始。 如果 sep 未指定或为 None，任何空白字符串都会被作为分隔符。 
    除了从右边开始拆分，rsplit() 的其他行为都类似于下文所述的 split()。
    str.rstrip([chars]) 返回原字符串的副本，移除其中的末尾字符。 chars 参数为指定要移除字符的字符串。 
    如果省略或为 None，则 chars 参数默认移除空格符。 实际上 chars 参数并非指定单个后缀；而是会移除参数值的所有组合:
    str.split(sep=None, maxsplit=-1)    返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。 
    如果给出了 maxsplit，则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）。 
    如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）。
    如果给出了 sep，则连续的分隔符不会被组合在一起而是被视为分隔空字符串 
    (例如 '1,,2'.split(',') 将返回 ['1', '', '2'])。 sep 参数可能由多个字符组成 
    (例如 '1<>2<>3'.split('<>') 将返回 ['1', '2', '3'])。 使用指定的分隔符拆分空字符串将返回 ['']。
    不同于 split()，当给出了分隔字符串 sep 时，对于空字符串此方法将返回一个空列表，而末尾的换行不会令结果中增加额外的行:
    str.strip([chars])  返回原字符串的副本，移除其中的前导和末尾字符。 chars 参数为指定要移除字符的字符串。
     如果省略或为 None，则 chars 参数默认移除空格符。 实际上 chars 参数并非指定单个前缀或后缀；而是会移除参数值的所有组合:
    str.title() 返回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写。
    str.translate(table)    返回原字符串的副本，其中每个字符按给定的转换表进行映射。 
    转换表必须是一个使用 __getitem__() 来实现索引操作的对象，通常为 mapping 或 sequence。 
    当以 Unicode 码位序号（整数）为索引时，转换表对象可以做以下任何一种操作：返回 Unicode 序号或字符串，将字符映射为一个或多个字符；返回 None，
    将字符从结果字符串中删除；或引发 LookupError 异常，将字符映射为其自身。你可以使用 str.maketrans() 基于不同格式的字符到字符映射来创建一个转换映射表。
    str.upper() 返回原字符串的副本，其中所有区分大小写的字符均转换为大写。
     请注意如果 s 包含不区分大小写的字符或者如果结果字符的 Unicode 
     类别不是 "Lu" (Letter, uppercase) 而是 "Lt" (Letter, titlecase) 则 s.upper().isupper() 有可能为 False。
    str.zfill(width)    返回原字符串的副本，在左边填充 ASCII '0' 数码使其长度变为 width。 
    正负值前缀 ('+'/'-') 的处理方式是在正负符号 之后 填充而非在之前。 如果 width 小于等于 len(s) 则返回原字符串的副本。

### 二进制序列类型 --- bytes, bytearray, memoryview
    操作二进制数据的核心内置类型是 bytes 和 bytearray。
    它们由 memoryview 提供支持，该对象使用 缓冲区协议 来访问其他二进制对象所在内存，不需要创建对象的副本。
    array 模块支持高效地存储基本数据类型，例如 32 位整数和 IEEE754 双精度浮点值。

#### bytes 对象
    bytes 对象是由单个字节构成的不可变序列。 由于许多主要二进制协议都基于 ASCII 文本编码，因此 bytes 对象提供了一些仅在处理 ASCII 兼容数据时可用，并且在许多特性上与字符串对象紧密相关的方法。
    1. 定义
    class bytes([source[, encoding[, errors]]])
    首先，表示 bytes 字面值的语法与字符串字面值的大致相同，只是添加了一个 b 前缀：
    单引号: b'同样允许嵌入 "双" 引号'。
    双引号: b"同样允许嵌入 '单' 引号"。
    三重引号: b'''三重单引号''', b"""三重双引号"""
    bytes 字面值中只允许 ASCII 字符（无论源代码声明的编码为何）。 任何超出 127 的二进制值必须使用相应的转义序列形式加入 bytes 字面值。
    像字符串字面值一样，bytes 字面值也可以使用 r 前缀来禁用转义序列处理。 
    虽然 bytes 字面值和表示法是基于 ASCII 文本的，但 bytes 对象的行为实际上更像是不可变的整数序列，
    序列中的每个值的大小被限制为 0 <= x < 256 (如果违反此限制将引发 ValueError)。 
    这种限制是有意设计用以强调以下事实，虽然许多二进制格式都包含基于 ASCII 的元素，可以通过某些面向文本的算法进行有用的操作，
    但情况对于任意二进制数据来说通常却并非如此（盲目地将文本处理算法应用于不兼容 ASCII 的二进制数据格式往往将导致数据损坏）。
    
    除了字面值形式，bytes 对象还可以通过其他几种方式来创建：
    指定长度的以零值填充的 bytes 对象: bytes(10)
    通过由整数组成的可迭代对象: bytes(range(20))
    通过缓冲区协议复制现有的二进制数据: bytes(obj)
    由于两个十六进制数码精确对应一个字节，因此十六进制数是描述二进制数据的常用格式。 相应地，bytes 类型具有从此种格式读取数据的附加类方法：
    2. classmethod fromhex(string)
    此 bytes 类方法返回一个解码给定字符串的 bytes 对象。 字符串必须由表示每个字节的两个十六进制数码构成，其中的 ASCII 空白符会被忽略。
    bytes.fromhex('2Ef0 F1f2  ')
    b'.\xf0\xf1\xf2'
    存在一个反向转换函数，可以将 bytes 对象转换为对应的十六进制表示。
    hex([sep[, bytes_per_sep]])
    返回一个字符串对象，该对象包含实例中每个字节的两个十六进制数字。
#### bytearray 对象
    bytearray是 bytes 对象的可变对应物。
    1. 定义  class bytearray([source[, encoding[, errors]]])
    bytearray 对象没有专属的字面值语法，它们总是通过调用构造器来创建：
    2. 创建bytearray对象
        创建一个空实例: bytearray()
        创建一个指定长度的以零值填充的实例: bytearray(10)
        通过由整数组成的可迭代对象: bytearray(range(20))
        通过缓冲区协议复制现有的二进制数据: bytearray(b'Hi!')
    3. bytearray对象的操作
    由于 bytearray 对象是可变的，该对象除了 bytes 和 bytearray 操作中所描述的 bytes 和 bytearray 共有操作之外，还支持可变序列操作。
    由于两个十六进制数码精确对应一个字节，因此十六进制数是描述二进制数据的常用格式。 相应地，bytearray 类型具有从此种格式读取数据的附加类方法：
    classmethod fromhex(string)
        bytearray 类方法返回一个解码给定字符串的 bytearray 对象。 字符串必须由表示每个字节的两个十六进制数码构成，其中的 ASCII 空白符会被忽略。
        存在一个反向转换函数，可以将 bytearray 对象转换为对应的十六进制表示。
        hex([sep[, bytes_per_sep]])
        返回一个字符串对象，该对象包含实例中每个字节的两个十六进制数字。
    bytes 和 bytearray 对象都支持通用序列操作。 它们不仅能与相同类型的操作数，也能与任何 bytes-like object 进行互操作。 
    由于这样的灵活性，它们可以在操作中自由地混合而不会导致错误。 但是，操作结果的返回值类型可能取决于操作数的顺序。
    注解 bytes 和 bytearray 对象的方法不接受字符串作为其参数，就像字符串的方法不接受 bytes 对象作为其参数一样。 例如，你必须使用以下写法:
    a = "abc" 
    b = a.replace("a", "f")
    和:    
    a = b"abc"
    b = a.replace(b"a", b"f")
    某些 bytes 和 bytearray 操作假定使用兼容 ASCII 的二进制格式，因此在处理任意二进数数据时应当避免使用。 这些限制会在下文中说明。
    注解 使用这些基于 ASCII 的操作来处理未以基于 ASCII 的格式存储的二进制数据可能会导致数据损坏。
    bytes 和 bytearray 对象的下列方法可以用于任意二进制数据。

    bytes.count(sub[, start[, end]])
    bytearray.count(sub[, start[, end]])
    返回子序列 sub 在 [start, end] 范围内非重叠出现的次数。 可选参数 start 与 end 会被解读为切片表示法。
    bytes.decode(encoding="utf-8", errors="strict")
    bytearray.decode(encoding="utf-8", errors="strict")
    返回从给定 bytes 解码出来的字符串。 默认编码为 'utf-8'。 可以给出 errors 来设置不同的错误处理方案。 
    errors 的默认值为 'strict'，表示编码错误会引发 UnicodeError。 
    其他可用的值为 'ignore', 'replace' 以及任何其他通过 codecs.register_error() 注册的名称。
    注解 将 encoding 参数传给 str 允许直接解码任何 bytes-like object，无须创建临时的 bytes 或 bytearray 对象。
    
    bytes.endswith(suffix[, start[, end]])
    bytearray.endswith(suffix[, start[, end]])
    如果二进制数据以指定的 suffix 结束则返回 True，否则返回 False。 suffix 也可以为由多个供查找的后缀构成的元组。 
    如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较。要搜索的后缀可以是任意 bytes-like object。
    
    bytes.find(sub[, start[, end]])
    bytearray.find(sub[, start[, end]])
    返回子序列 sub 在数据中被找到的最小索引，sub 包含于切片 s[start:end] 之内。 可选参数 start 与 end 会被解读为切片表示法。 
    如果 sub 未被找到则返回 -1。要搜索的子序列可以是任意 bytes-like object 或是 0 至 255 范围内的整数。
    注解 find() 方法应该只在你需要知道 sub 所在位置时使用。 要检查 sub 是否为子串，请使用 in 操作符
    
    bytes.index(sub[, start[, end]])
    bytearray.index(sub[, start[, end]])
    类似于 find()，但在找不到子序列时会引发 ValueError。
    要搜索的子序列可以是任意 bytes-like object 或是 0 至 255 范围内的整数。
    
    bytes.join(iterable)
    bytearray.join(iterable)
    返回一个由 iterable 中的二进制数据序列拼接而成的 bytes 或 bytearray 对象。 如果 iterable 中存在任何非 字节类对象 包括存在 str 对象值则会引发 TypeError。 
    提供该方法的 bytes 或 bytearray 对象的内容将作为元素之间的分隔。
    
    static bytes.maketrans(from, to)
    static bytearray.maketrans(from, to)
    此静态方法返回一个可用于 bytes.translate() 的转换对照表，它将把 from 中的每个字符映射为 to 中相同位置上的字符；from 与 to 必须都是 字节类对象 并且具有相同的长度。
    
    bytes.partition(sep)
    bytearray.partition(sep)
    在 sep 首次出现的位置拆分序列，返回一个 3 元组，其中包含分隔符之前的部分、分隔符本身或其 bytearray 副本，以及分隔符之后的部分。 如果分隔符未找到，则返回的 3 元组中包含原序列以及两个空的 bytes 或 bytearray 对象。
    
    要搜索的分隔符可以是任意 bytes-like object。
    
    bytes.replace(old, new[, count])
    bytearray.replace(old, new[, count])
    返回序列的副本，其中出现的所有子序列 old 都将被替换为 new。 如果给出了可选参数 count，则只替换前 count 次出现。
    要搜索的子序列及其替换序列可以是任意 bytes-like object。
    
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    bytes.rfind(sub[, start[, end]])
    bytearray.rfind(sub[, start[, end]])
    返回子序列 sub 在序列内被找到的最大（最右）索引，这样 sub 将包含在 s[start:end] 当中。 可选参数 start 与 end 会被解读为切片表示法。 如果未找到则返回 -1。
    要搜索的子序列可以是任意 bytes-like object 或是 0 至 255 范围内的整数。
    
    
    bytes.rindex(sub[, start[, end]])
    bytearray.rindex(sub[, start[, end]])
    类似于 rfind()，但在子序列 sub 未找到时会引发 ValueError。
    要搜索的子序列可以是任意 bytes-like object 或是 0 至 255 范围内的整数。
    
    bytes.rpartition(sep)
    bytearray.rpartition(sep)
    在 sep 最后一次出现的位置拆分序列，返回一个 3 元组，其中包含分隔符之前的部分，分隔符本身或其 bytearray 副本，以及分隔符之后的部分。 如果分隔符未找到，则返回的 3 元组中包含两个空的 bytes 或 bytearray 对象以及原序列的副本。
    要搜索的分隔符可以是任意 bytes-like object。
    
    bytes.startswith(prefix[, start[, end]])
    bytearray.startswith(prefix[, start[, end]])
    如果二进制数据以指定的 prefix 开头则返回 True，否则返回 False。 
    prefix 也可以为由多个供查找的前缀构成的元组。 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较。
    要搜索的前缀可以是任意 bytes-like object。
    
    bytes.translate(table, /, delete=b'')
    bytearray.translate(table, /, delete=b'')
    返回原 bytes 或 bytearray 对象的副本，移除其中所有在可选参数 delete 中出现的 bytes，其余 bytes 将通过给定的转换表进行映射，该转换表必须是长度为 256 的 bytes 对象。
    你可以使用 bytes.maketrans() 方法来创建转换表。
    对于仅需移除字符的转换，请将 table 参数设为 None:
    
    以下 bytes 和 bytearray 对象的方法的默认行为会假定使用兼容 ASCII 的二进制格式，但通过传入适当的参数仍然可用于任意二进制数据。
    请注意本小节中所有的 bytearray 方法都 不是 原地执行操作，而是会产生新的对象。
    
    bytes.center(width[, fillbyte])
    bytearray.center(width[, fillbyte])
    返回原对象的副本，在长度为 width 的序列内居中，使用指定的 fillbyte 填充两边的空位（默认使用 ASCII 空格符）。 对于 bytes 对象，如果 width 小于等于 len(s) 则返回原序列的副本。
    
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    bytes.ljust(width[, fillbyte])
    bytearray.ljust(width[, fillbyte])
    反回原对象的副本，在长度为 width 的序列中靠左对齐。 使用指定的 fillbyte 填充空位（默认使用 ASCII 空格符）。 对于 bytes 对象，如果 width 小于等于 len(s) 则返回原序列的副本。
    
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    bytes.lstrip([chars])
    bytearray.lstrip([chars])
    返回原序列的副本，移除指定的前导字节。 chars 参数为指定要移除字节值集合的二进制序列 —— 这个名称表明此方法通常是用于 ASCII 字符。
    如果省略或为 None，则 chars 参数默认移除 ASCII 空白符。 chars 参数并非指定单个前缀；而是会移除参数值的所有组合:
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    bytes.rjust(width[, fillbyte])
    bytearray.rjust(width[, fillbyte])
    返回原对象的副本，在长度为 width 的序列中靠右对齐。 使用指定的 fillbyte 填充空位（默认使用 ASCII 空格符）。
    对于 bytes 对象，如果 width 小于等于 len(s) 则返回原序列的副本。
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    
    bytes.rsplit(sep=None, maxsplit=-1)
    bytearray.rsplit(sep=None, maxsplit=-1)
    将二进制序列拆分为相同类型的子序列，使用 sep 作为分隔符。 如果给出了 maxsplit，则最多进行 maxsplit 次拆分，从 最右边 开始。
     如果 sep 未指定或为 None，任何只包含 ASCII 空白符的子序列都会被作为分隔符。 除了从右边开始拆分，rsplit() 的其他行为都类似于下文所述的 split()。
    
    bytes.rstrip([chars])
    bytearray.rstrip([chars])
    返回原序列的副本，移除指定的末尾字节。 chars 参数为指定要移除字节值集合的二进制序列 —— 这个名称表明此方法通常是用于 ASCII 字符。 
    如果省略或为 None，则 chars 参数默认移除 ASCII 空白符。 chars 参数并非指定单个后缀；而是会移除参数值的所有组合:
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    
    bytes.split(sep=None, maxsplit=-1)
    bytearray.split(sep=None, maxsplit=-1)
    将二进制序列拆分为相同类型的子序列，使用 sep 作为分隔符。 
    如果给出了 maxsplit 且非负值，则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）。
    如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）。
    如果给出了 sep，则连续的分隔符不会被组合在一起而是被视为分隔空子序列 (例如 b'1,,2'.split(b',') 将返回 [b'1', b'', b'2'])。 
    sep 参数可能为一个多字节序列 (例如 b'1<>2<>3'.split(b'<>') 将返回 [b'1', b'2', b'3'])。 
    使用指定的分隔符拆分空序列将返回 [b''] 或 [bytearray(b'')]，具体取决于被拆分对象的类型。 sep 参数可以是任意 bytes-like object。
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    以下 bytes 和 bytearray 对象的方法会假定使用兼容 ASCII 的二进制格式，不应当被应用于任意二进制数据。 
    请注意本小节中所有的 bytearray 方法都 不是 原地执行操作，而是会产生新的对象。
    
    bytes.capitalize()
    bytearray.capitalize()
    返回原序列的副本，其中每个字节将都将被解读为一个 ASCII 字符，并且第一个字节的字符大写而其余的小写。 非 ASCII 字节值将保持原样不变。
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    
    bytes.expandtabs(tabsize=8)
    bytearray.expandtabs(tabsize=8)
    返回序列的副本，其中所有的 ASCII 制表符会由一个或多个 ASCII 空格替换，具体取决于当前列位置和给定的制表符宽度。 
    每 tabsize 个字节设为一个制表位（默认值 8 时设定的制表位在列 0, 8, 16 依次类推）。 要展开序列，当前列位置将被设为零并逐一检查序列中的每个字节。 
    如果字节为 ASCII 制表符 (b'\t')，则并在结果中插入一个或多个空格符，直到当前列等于下一个制表位。 （制表符本身不会被复制。） 
    如果当前字节为 ASCII 换行符 (b'\n') 或回车符 (b'\r')，它会被复制并将当前列重设为零。 任何其他字节会被不加修改地复制并将当前列加一，不论该字节值在被打印时会如何显示:
    
    bytes.isdigit()
    bytearray.isdigit()
    如果序列中所有字节都是 ASCII 十进制数码并且序列非空则返回 True ，否则返回 False 。 ASCII 十进制数码就是字节值包含在序列 b'0123456789' 中的字符。
    
    bytes.isspace()
    bytearray.isspace()
    如果序列中所有字节都是 ASCII 空白符并且序列非空则返回 True ，否则返回 False 。 ASCII 空白符就是字节值包含在序列 b' \t\n\r\x0b\f'
     (空格, 制表, 换行, 回车, 垂直制表, 进纸) 中的字符。
    
    bytes.istitle()
    bytearray.istitle()
    如果序列为 ASCII 标题大小写形式并且序列非空则返回 True ，否则返回 False 。 请参阅 bytes.title() 了解有关“标题大小写”的详细定义。
    
    bytes.lower()
    bytearray.lower()
    返回原序列的副本，其所有大写 ASCII 字符均转换为对应的小写形式。
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    
    bytes.splitlines(keepends=False)
    bytearray.splitlines(keepends=False)
    返回由原二进制序列中各行组成的列表，在 ASCII 行边界符的位置拆分。 此方法使用 universal newlines 方式来分行。 结果列表中不包含换行符，除非给出了 keepends 且为真值。
    不同于 str.swapcase()，在些二进制版本下 bin.swapcase().swapcase() == bin 总是成立。 大小写转换在 ASCII 中是对称的，即使其对于任意 Unicode 码位来说并不总是成立。
    
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    bytes.title()
    bytearray.title()
    返回原二进制序列的标题版本，其中每个单词以一个大写 ASCII 字符为开头，其余字母为小写。 不区别大小写的字节值将保持原样不变。
    
    注解 此方法的 bytearray 版本 并非 原地操作 —— 它总是产生一个新对象，即便没有做任何改变。
    bytes.zfill(width)
    bytearray.zfill(width)
    返回原序列的副本，在左边填充 b'0' 数码使序列长度为 width。 正负值前缀 (b'+'/ b'-') 的处理方式是在正负符号 之后 填充而非在之前。 
    对于 bytes 对象，如果 width 小于等于 len(seq) 则返回原序列。
