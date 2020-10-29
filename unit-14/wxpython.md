# wx.StaticText静态文件控件
``````
在屏幕上显示文本的例子作为开始，包括用作标签的静态文本域，有样式和无样式的都使用了。你可以创建用于用户输入的单行和多行文本域。
如何显示静态文本？
大概对于所有的UI工具来说，最基本的任务就是在屏幕上绘制纯文本。
在wxPython中，使用类wx.StaticText来完成。图7.1显示了这个静态文本控件。
在wx.StaticText中，你能够改变文本的对齐方式、字体和颜色。
简单的静态文本控件可以包含多行文本，但是你不能处理多种字体或样式。
处理多种字体或样式，要使用更精细的文本控件，如wx.html.HTMLWindow。
为了在静态文本控件中显示多行文本，我们要包括其中有换行符的字符串，并使控件的大小足够显示所有的文本。
那就是wx.StaticText有一个特点是组件不会接受或响应鼠标事件。
如何显示静态文本
wx.StaticText(parent, id, label, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name="staticText")
wx.StaticText构造函数的参数
parent：父窗口部件。
id：标识符。使用-1可以自动创建一个唯一的标识。
label：你想显示在静态控件中的文本。
pos：一个wx.Point或一个Python元组，它是窗口部件的位置。
size：一个wx.Size或一个Python元组，它是窗口部件的尺寸。
name：对象的名字，用于查找的需要。
style：样式标记。
wx.ALIGN_CENTER：静态文本位于静态文本控件的中心。
wx.ALIGN_LEFT：文本在窗口部件中左对齐。这是默认的样式。
wx.ALIGN_RIGHT：文本在窗口部件中右对齐。
wx.ST_NO_AUTORESIZE：如果使用了这个样式，那么在使用了SetLabel()改变文本之后，静态文本控件不将自我调整尺寸。你应结合使用一个居中或右对齐的控件来保持对齐。
``````