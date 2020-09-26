# 序列类型 
    python中的序列共有三种基本序列类型：list, tuple 和 range 对象。   

## 通用序列操作
    大多数序列类型，包括可变类型和不可变类型都支持下表中的操作。 collections.abc.Sequence ABC 被提供用来更容易地在自定义序列类型上正确地实现这些操作。
    此表按优先级升序列出了序列操作。 在表格中，s 和 t 是具有相同类型的序列，n, i, j 和 k 是整数而 x 是任何满足 s 所规定的类型和值限制的任意对象。    
    
    运算              结果：                                         注释
    x in s          如果 s 中的某项等于 x 则结果为 True，否则为 False    (1)    
    x not in s      如果 s 中的某项等于 x 则结果为 False，否则为 True    (1)    
    s + t           s 与 t 相拼接                                   (6)(7)
    s * n 或 n * s  相当于 s 与自身进行 n 次拼接                      (2)(7)    
    s[i]            s 的第 i 项，起始为 0                            (3)    
    s[i:j]          s 从 i 到 j 的切片                             (3)(4)    
    s[i:j:k]        s 从 i 到 j 步长为 k 的切片                     (3)(5)    
    len(s)          s 的长度
    min(s)          s 的最小项    
    max(s)          s 的最大项
    s.index(x[, i[, j]])    x 在 s 中首次出现项的索引号（索引号在 i 或其后且在 j 之前） (8)    
    s.count(x)      x 在 s 中出现的总次数    
    in 和 not in 操作具有与比较操作相同的优先级。 + (拼接) 和 * (重复) 操作具有与对应数值运算相同的优先级。    
    
    (1) 虽然 in 和 not in 操作在通常情况下仅被用于简单的成员检测，某些专门化序列 (例如 str, bytes 和 bytearray) 也使用它们进行子序列检测:  
    小于 0 的 n 值会被当作 0 来处理 (生成一个与 s 同类型的空序列)。 
    请注意序列 s 中的项并不会被拷贝；它们会被多次引用。 这一点经常会令 Python 编程新手感到困扰；例如:
    lists = [[]] * 3   
    >>> lists[0].append(3)   
    (2)具体的原因在于 [[]] 是一个包含了一个空列表的单元素列表，所以 [[]] * 3 结果中的三个元素都是对这一个空列表的引用。 
    修改 lists 中的任何一个元素实际上都是对这一个空列表的修改。 你可以用以下方式创建以不同列表为元素的列表:
    lists = [[] for i in range(3)]  
    (3) 如果 i 或 j 为负值，则索引顺序是相对于序列 s 的末尾: 索引号会被替换为 len(s) + i 或 len(s) + j。 但要注意 -0 仍然为 0。    
    (4) s 从 i 到 j 的切片被定义为所有满足 i <= k < j 的索引号 k 的项组成的序列。 如果 i 或 j 大于 len(s)，则使用 len(s)。 
    如果 i 被省略或为 None，则使用 0。 如果 j 被省略或为 None，则使用 len(s)。 如果 i 大于等于 j，则切片为空。    
    (5) s 从 i 到 j 步长为 k 的切片被定义为所有满足 0 <= n < (j-i)/k 的索引号 x = i + n*k 的项组成的序列。 
    换句话说，索引号为 i, i+k, i+2*k, i+3*k，以此类推，当达到 j 时停止 (但一定不包括 j)。 当 k 为正值时，i 和 j 会被减至不大于 len(s)。
    当 k 为负值时，i 和 j 会被减至不大于 len(s) - 1。 
    如果 i 或 j 被省略或为 None，它们会成为“终止”值 (是哪一端的终止值则取决于 k 的符号)。 请注意，k 不可为零。 如果 k 为 None，则当作 1 处理。    
    (6) 拼接不可变序列总是会生成新的对象。 这意味着通过重复拼接来构建序列的运行时开销将会基于序列总长度的乘方。 想要获得线性的运行时开销，你必须改用下列替代方案之一：    
    如果拼接 str 对象，你可以构建一个列表并在最后使用 str.join() 或是写入一个 io.StringIO 实例并在结束时获取它的值    
    (7) 如果拼接 bytes 对象，你可以类似地使用 bytes.join() 或 io.BytesIO，或者你也可以使用 bytearray 对象进行原地拼接。
     bytearray 对象是可变的，并且具有高效的重分配机制.
     如果拼接 tuple 对象，请改为扩展 list 类       
    某些序列类型 (例如 range) 仅支持遵循特定模式的项序列，因此并不支持序列拼接或重复。    
    (8)当 x 在 s 中找不到时 index 会引发 ValueError。 不是所有实现都支持传入额外参数 i 和 j。 这两个参数允许高效地搜索序列的子序列。 
    传入这两个额外参数大致相当于使用 s[i:j].index(x)，但是不会复制任何数据，并且返回的索引是相对于序列的开头而非切片的开头。
        
### 不可变序列类型¶
    不可变序列类型普遍实现而可变序列类型未实现的唯一操作就是对 hash() 内置函数的支持。
    这种支持允许不可变类型，例如 tuple 实例被用作 dict 键，以及存储在 set 和 frozenset 实例中。
    尝试对包含有不可哈希值的不可变序列进行哈希运算将会导致 TypeError。

### 可变序列类型
    以下表格中的操作是在可变序列类型上定义的。 collections.abc.MutableSequence ABC 被提供用来更容易地在自定义序列类型上正确实现这些操作。
    表格中的 s 是可变序列类型的实例，t 是任意可迭代对象，而 x 是符合对 s 所规定类型与值限制的任何对象 (例如，bytearray 仅接受满足 0 <= x <= 255 值限制的整数)。
    运算                      结果：                                             注释
    s[i] = x        将 s 的第 i 项替换为 x
    s[i:j] = t      将 s 从 i 到 j 的切片替换为可迭代对象 t 的内容
    del s[i:j]      等同于 s[i:j] = []
    s[i:j:k] = t    将 s[i:j:k] 的元素替换为 t 的元素                             (1)
    del s[i:j:k]    从列表中移除 s[i:j:k] 的元素
    s.append(x)     将 x 添加到序列的末尾 (等同于 s[len(s):len(s)] = [x])
    s.clear()       从 s 中移除所有项 (等同于 del s[:])                           (5)
    s.copy()        创建 s 的浅拷贝 (等同于 s[:])                                (5)
    s.extend(t) 或 s += t    用 t 的内容扩展 s (基本上等同于 s[len(s):len(s)] = t)
    s *= n          使用 s 的内容重复 n 次来对其进行更新                           (6)
    s.insert(i, x)  在由 i 给出的索引位置将 x 插入 s (等同于 s[i:i] = [x])     
    s.pop([i])      提取在 i 位置上的项，并将其从 s 中移除                          (2)
    s.remove(x)     删除 s 中第一个 s[i] 等于 x 的项目。                            (3)
    s.reverse()     就地将列表中的元素逆序。                                        (4)
    注释:
    (1)t 必须与它所替换的切片具有相同的长度。
    (2) 可选参数 i 默认为 -1，因此在默认情况下会移除并返回最后一项。
    (3) 当在 s 中找不到 x 时 remove() 操作会引发 ValueError。
    (4) 当反转大尺寸序列时 reverse() 方法会原地修改该序列以保证空间经济性。 
    为提醒用户此操作是通过间接影响进行的，它并不会返回反转后的序列。
    (5) 包括 clear() 和 copy() 是为了与不支持切片操作的可变容器 (例如 dict 和 set) 的接口保持一致。 
    copy() 不是 collections.abc.MutableSequence ABC 的一部分，但大多数具体的可变序列类都提供了它。
    (6) n 值为一个整数，或是一个实现了 __index__() 的对象。 n 值为零或负数将清空序列。 
    序列中的项不会被拷贝；它们会被多次引用，正如 通用序列操作 中有关 s * n 的说明。
## 列表
列表是可变序列，通常用于存放同类项目的集合（其中精确的相似程度将根据应用而变化）。
### 列表创建
    class list([iterable])
#### 可以用多种方式构建列表：
    （1）使用一对方括号来表示空列表: []
    （2） 使用方括号，其中的项以逗号分隔: [a], [a, b, c]
    （3） 使用列表推导式: [x for x in iterable]
    （4） 使用类型的构造器: list() 或 list(iterable)
    构造器将构造一个列表，其中的项与 iterable 中的项具有相同的的值与顺序。 iterable 可以是序列、支持迭代的容器或其它可迭代对象。 
    如果 iterable 已经是一个列表，将创建并返回其副本，类似于 iterable[:]。 
    例如，list('abc') 返回 ['a', 'b', 'c'] 而 list( (1, 2, 3) ) 返回 [1, 2, 3]。 如果没有给出参数，构造器将创建一个空列表 []。
    （5）其它许多操作也会产生列表，包括 sorted() 内置函数。
    列表实现了所有 一般 和 可变 序列的操作。 列表还额外提供了以下方法：
    sort(*, key=None, reverse=False)
    此方法会对列表进行原地排序，只使用 < 来进行各项间比较。 异常不会被屏蔽 —— 如果有任何比较操作失败，整个排序操作将失败（而列表可能会处于被部分修改的状态）。
    sort() 接受两个仅限以关键字形式传入的参数 (仅限关键字参数):
    key 指定带有一个参数的函数，用于从每个列表元素中提取比较键 (例如 key=str.lower)。
    对应于列表中每一项的键会被计算一次，然后在整个排序过程中使用。 默认值 None 表示直接对列表项排序而不计算一个单独的键值。
    reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。
    当顺序大尺寸序列时此方法会原地修改该序列以保证空间经济性。 为提醒用户此操作是通过间接影响进行的，它并不会返回排序后的序列（请使用 sorted() 显示地请求一个新的已排序列表实例）。
    sort() 方法确保是稳定的。 如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的 --- 这有利于进行多重排序（例如先按部门、再接薪级排序）。

## 元组
元组是不可变序列，通常用于储存异构数据的多项集（例如由 enumerate() 内置函数所产生的二元组）。 元组也被用于需要同构数据的不可变序列的情况（例如允许存储到 set 或 dict 的实例）。

### 元组类定义class tuple([iterable])
### 可以用多种方式构建元组：
    （1）使用一对圆括号来表示空元组: ()
    （2）使用一个后缀的逗号来表示单元组: a, 或 (a,)
    （3）使用以逗号分隔的多个项: a, b, c or (a, b, c)
    （4）使用内置的 tuple(): tuple() 或 tuple(iterable)
    构造器将构造一个元组，其中的项与 iterable 中的项具有相同的值与顺序。 iterable 可以是序列、支持迭代的容器或其他可迭代对象。 
    如果 iterable 已经是一个元组，会不加改变地将其返回。 例如，tuple('abc') 返回 ('a', 'b', 'c') 而 tuple( [1, 2, 3] ) 返回 (1, 2, 3)。
    如果没有给出参数，构造器将创建一个空元组 ()。
    请注意决定生成元组的其实是逗号而不是圆括号。 圆括号只是可选的，生成空元组或需要避免语法歧义的情况除外。 
    例如，f(a, b, c) 是在调用函数时附带三个参数，而 f((a, b, c)) 则是在调用函数时附带一个三元组。
### 元组的操作 
    元组实现了所有 一般 序列的操作。
    对于通过名称访问相比通过索引访问更清晰的异构数据多项集，collections.namedtuple() 可能是比简单元组对象更为合适的选择。

## range 对象
range 类型表示不可变的数字序列，通常用于在 for 循环中循环指定的次数。
### range对象的构造
    class range(stop)
    class range(start, stop[, step])
    range 构造器的参数必须为整数（可以是内置的 int 或任何实现了 __index__ 特殊方法的对象）。 如果省略 step 参数，其默认值为 1。 如果省略 start 参数，其默认值为 0，如果 step 为零则会引发 ValueError。
    如果 step 为正值，确定 range r 内容的公式为 r[i] = start + step*i 其中 i >= 0 且 r[i] < stop。
    如果 step 为负值，确定 range 内容的公式仍然为 r[i] = start + step*i，但限制条件改为 i >= 0 且 r[i] > stop.
    如果 r[0] 不符合值的限制条件，则该 range 对象为空。 range 对象确实支持负索引，但是会将其解读为从正索引所确定的序列的末尾开始索引。
    元素绝对值大于 sys.maxsize 的 range 对象是被允许的，但某些特性 (例如 len()) 可能引发 OverflowError。
    一些 range 对象的例子:
    list(range(10))
    list(range(1, 11))
    list(range(0, 30, 5))
    list(range(0, 10, 3))
    list(range(0, -10, -1))
    list(range(0))
    list(range(1, 0))
    range 对象实现了 一般 序列的所有操作，但拼接和重复除外（这是由于 range 对象只能表示符合严格模式的序列，而重复和拼接通常都会违反这样的模式）。
    start   start 形参的值 (如果该形参未提供则为 0)
    stop    stop 形参的值
    step    step 形参的值 (如果该形参未提供则为 1)
    range 类型相比常规 list 或 tuple 的优势在于一个 range 对象总是占用固定数量的（较小）内存，不论其所表示的范围有多大（因为它只保存了 start, stop 和 step 值，并会根据需要计算具体单项或子范围的值）。
    range 对象实现了 collections.abc.Sequence ABC，提供如包含检测、元素索引查找、切片等特性，并支持负索引 (参见 序列类型 --- list, tuple, range):
    r = range(0, 20, 2)   
    r.index(10)
    r[5]
    r[:5]
    r[-1]
    使用 == 和 != 检测 range 对象是否相等是将其作为序列来比较。 也就是说，如果两个 range 对象表示相同的值序列就认为它们是相等的。 
    （请注意比较结果相等的两个 range 对象可能会具有不同的 start, stop 和 step 属性，例如 range(0) == range(2, 1, 3) 而 range(0, 3, 2) == range(0, 4, 2)。）

## 集合类型 --- set, frozenset
    set 对象是由具有唯一性的 hashable 对象所组成的无序多项集。 
    常见的用途包括成员检测、从序列中去除重复项以及数学中的集合类计算，例如交集、并集、差集与对称差集等等。 
    （关于其他容器对象请参看 dict, list 与 tuple 等内置类，以及 collections 模块。）
    集合与其他多项集一样，集合也支持 x in set, len(set) 和 for x in set 操作。 
    作为一种无序的多项集，集合并不记录元素位置或插入顺序。 相应地，集合不支持索引、切片或其他序列类的操作。    
    目前有两种内置集合类型，set 和 frozenset。 
    set 类型是可变的 --- 其内容可以使用 add() 和 remove() 这样的方法来改变。 由于是可变类型，它没有哈希值，且不能被用作字典的键或其他集合的元素。 
    frozenset 类型是不可变并且为 hashable --- 其内容在被创建后不能再改变；因此它可以被用作字典的键或其他集合的元素。
    1. 创建set对象 
       可以使用 set 构造器，
       非空的 set (不是 frozenset) 还可以通过将以逗号分隔的元素列表包含于花括号之内来创建，例如: {'jack', 'sjoerd'}。
    两个类的构造器具有相同的作用方式：   
    class set([iterable])
    class frozenset([iterable])
    返回一个新的 set 或 frozenset 对象，其元素来自于 iterable。 集合的元素必须为 hashable。
    要表示由集合对象构成的集合，所有的内层集合必须为 frozenset 对象。 如果未指定 iterable，则将返回一个新的空集合。
    2. set 和 frozenset 的实例提供以下操作：
    len(s)
    返回集合 s 中的元素数量（即 s 的基数）。    
    x in s
    检测 x 是否为 s 中的成员。    
    x not in s
    检测 x 是否非 s 中的成员。    
    isdisjoint(other)
    如果集合中没有与 other 共有的元素则返回 True。 当且仅当两个集合的交集为空集合时，两者为不相交集合。    
    issubset(other)
    set <= other
    检测是否集合中的每个元素都在 other 之中。    
    set < other
    检测集合是否为 other 的真子集，即 set <= other and set != other。    
    issuperset(other)
    set >= other
    检测是否 other 中的每个元素都在集合之中。    
    set > other
    检测集合是否为 other 的真超集，即 set >= other and set != other。    
    union(*others)
    set | other | ...
    返回一个新集合，其中包含来自原集合以及 others 指定的所有集合中的元素。    
    intersection(*others)
    set & other & ...
    返回一个新集合，其中包含原集合以及 others 指定的所有集合中共有的元素。    
    difference(*others)
    set - other - ...
    返回一个新集合，其中包含原集合中在 others 指定的其他集合中不存在的元素。    
    symmetric_difference(other)
    set ^ other
    返回一个新集合，其中的元素或属于原集合或属于 other 指定的其他集合，但不能同时属于两者。    
    copy()
    返回原集合的浅拷贝。    
    请注意，非运算符版本的 union(), intersection(), difference()，以及 symmetric_difference(), issubset() 和 issuperset() 方法会接受任意可迭代对象作为参数。 
    相比之下，它们所对应的运算符版本则要求其参数为集合。 这就排除了容易出错的构造形式例如 set('abc') & 'cbs'，而推荐可读性更强的 set('abc').intersection('cbs')。    
    set 和 frozenset 均支持集合与集合的比较。 
    两个集合当且仅当每个集合中的每个元素均包含于另一个集合之内（即各为对方的子集）时则相等。 
    一个集合当且仅当其为另一个集合的真子集（即为后者的子集但两者不相等）时则小于另一个集合。 
    一个集合当且仅当其为另一个集合的真超集（即为后者的超集但两者不相等）时则大于另一个集合。    
    
    set 的实例与 frozenset 的实例之间基于它们的成员进行比较。 
    例如 set('abc') == frozenset('abc') 返回 True，set('abc') in set([frozenset('abc')]) 也一样。    
    子集与相等比较并不能推广为完全排序函数。 例如，任意两个非空且不相交的集合不相等且互不为对方的子集，因此以下 所有 比较均返回 False: a<b, a==b, or a>b。    
    由于集合仅定义了部分排序（子集关系），因此由集合构成的列表 list.sort() 方法的输出并无定义。    
    集合的元素，与字典的键类似，必须为 hashable。    
    混合了 set 实例与 frozenset 的二进制位运算将返回与第一个操作数相同的类型。例如: frozenset('ab') | set('bc') 将返回 frozenset 的实例。
    
    3. set集合实例的操作：
    
    update(*others)
    set |= other | ...
    更新集合，添加来自 others 中的所有元素。
    
    intersection_update(*others)
    set &= other & ...
    更新集合，只保留其中在所有 others 中也存在的元素。
    
    difference_update(*others)
    set -= other | ...
    更新集合，移除其中也存在于 others 中的元素。
    
    symmetric_difference_update(other)
    set ^= other
    更新集合，只保留存在于集合的一方而非共同存在的元素。
    
    add(elem)
    将元素 elem 添加到集合中。
    
    remove(elem)
    从集合中移除元素 elem。 如果 elem 不存在于集合中则会引发 KeyError。
    
    discard(elem)
    如果元素 elem 存在于集合中则将其移除。
    
    pop()
    从集合中移除并返回任意一个元素。 如果集合为空则会引发 KeyError。
    
    clear()
    从集合中移除所有元素。
    
    请注意，非运算符版本的 update(), intersection_update(), difference_update() 和 symmetric_difference_update() 方法将接受任意可迭代对象作为参数。    
    请注意，__contains__(), remove() 和 discard() 方法的 elem 参数可能是一个 set。 为支持对一个等价的 frozenset 进行搜索，会根据 elem 临时创建一个该类型对象。
