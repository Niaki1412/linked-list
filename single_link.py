# 单向链表:
#    单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和
# 一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。
#
# 表元素域elem用来存放具体的数据。
# 链接域next用来存放下一个节点的位置（python中的标识）
# 变量p指向链表的头节点（首节点）的位置，从p出发能找到表中的任意节点。

class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        """
        :param item:存放数据元素
        """
        self.item = item
        self.next = None  # 下一个结点的标识

"""单链表的操作
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""
class SingleList(object):
    """单链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head # 初始指向头结点
        count = 0
        # 尾结点指向None
        while cur != None: #未到达尾结点时
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("遍历结束")

    def add(self,item):
        """头部添加元素"""
        node = SingleNode(item) # 创建一个保存item的结点
        node.next = self.__head # 链接域指向头结点
        self.__head = node # 链表的头指向新结点

    def append(self,item):
        """尾部添加元素"""
        node = SingleNode(item)

        # 先判断链表是否为空，若是，将__head指向新结点,否则，将尾结点的链接域指向新结点
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """
        指定位置插入元素
        :param pos: 位置
        :param item: 元素
        :return:
        """
        # pos在第一个元素之前，头插入
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)

        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指示pos前一个位置pos-1，初始从头结点移动到指定位置
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 新结点node的链接域next指向插入位置的结点
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    fuck = SingleList()
    fuck.add(1)
    fuck.add(2)
    fuck.append(3)
    fuck.insert(2,8)
    print("链表长度：",fuck.length())
    fuck.travel()
    print(fuck.search(3))
    print(fuck.search(5))
    fuck.remove(1)
    print("链表长度：",fuck.length())
    fuck.travel()


