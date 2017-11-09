# coding:utf-8
from xml.dom.minidom import parse
import xml.etree.ElementTree as Etree
import xml.dom.minidom
import setting

log = setting.logging


class Xml_Utils_For_File():
    def __init__(self, rev_xml):
        """
        初始化类并获取xml的domtree
        :param rev_xml: 接收xml文件，类型为目录或者文件
        """
        self.xml = rev_xml
        log.debug('xml文件名 %s ' % rev_xml)
        try:
            self.root = self.__get_domtree()
        except IOError:
            log.error('请检查rev_xml = %s 是否是文件或者目录' % rev_xml)

    def __get_domtree(self):
        """
        获取文档的根节点元素
        :return:返回根节点元素
        """
        __domtree = parse(self.xml)
        __root = __domtree.documentElement
        log.debug('已获取文档的根元素')
        return __root

    def find_elements_by_tag_name(self, rev_tagname):
        """
        通过tag_name获取元素列表
        :param rev_tagname: 接收标签名
        :return:返回元素列表（类型为列表）
        """
        __ele_list = self.root.getElementsByTagName(rev_tagname)
        log.debug('获取tag = %s 的元素列表list = %s' % (rev_tagname, __ele_list))
        return __ele_list

    def find_child_nodes(self, rev_ele):
        """
        查找元素的所有子节点
        :param rev_ele: 接收目标元素
        :return:返回目标元素的子元素列表
        """
        __child_nodes_list = rev_ele.childNodes
        log.debug('获取元素为 %s 的子元素列表： %s' % (str(rev_ele), __child_nodes_list))
        return __child_nodes_list

    def get_ele_data(self, rev_ele):
        """
        获取元素的text
        :param rev_ele:接收目标元素
        :return:返回元素的text
        """
        try:
            __data = rev_ele.data
            log.debug('获取元素为 %s 的data = %s' % (str(rev_ele), __data))
            return __data
        except AttributeError, e:
            log.error(e)
            raise AttributeError('参数 rev_ele= %s 没有data这个方法' % str(rev_ele))

    def get_ele_attribute(self, rev_ele, rev_att):
        """
        获取目标元素的attribute
        :param rev_ele: 接收目标元素
        :param rev_att: 返回目标元素的属性名称
        :return:返回属性值
        """
        try:
            __att = rev_ele.getAttribute(rev_att)
            log.debug('获取元素为 %s 的attribute = %s' % (str(rev_ele), str(__att)))
            return __att
        except AttributeError, e:
            log.error(e)
            raise AttributeError('参数 rev_ele= %s 没有getAttribute这个方法' % str(rev_ele))

    def get_node_name(self, rev_ele):
        """
        获取目标元素的节点名称
        :param rev_ele: 接收目标元素
        :return:返回目标元素的节点名称
        """
        __node_name = rev_ele.nodeName
        log.debug('元素 %s 的节点名称：%s' % (str(rev_ele), str(__node_name)))
        return __node_name

    def get_node_type(self, rev_ele):
        """
        获取目标元素的类型
        :param rev_ele:接收目标元素
        :return:返回目标元素的类型
        """
        __node_type = rev_ele.nodeType
        return __node_type

    def get_node_value(self, rev_ele):
        """
        获取目标元素的值
        :param rev_ele:接收目标元素
        :return:返回目标元素的值
        """
        __node_value = rev_ele.nodeValue
        return __node_value

    def get_ele_xml(self, rev_ele):
        """
        获取目标元素的xml
        :param rev_ele:接收目标元素
        :return:返回目标元素的格式化xml
        """
        __ele_xml = rev_ele.toxml()
        return __ele_xml


class Xml_Utils_For_Str():
    def __init__(self, rev_xml_str):
        self.__xml_str = rev_xml_str
        self.root = self.__get_domtree()

    def __get_domtree(self):
        __root = Etree.fromstring(self.__xml_str)
        return __root

    def get_ele_text(self, rev_ele):
        '''
        获取元素的text
        :param rev_ele:接收目标元素
        :return:返回元素的text
        '''
        try:
            __text = rev_ele.text
            log.debug('获取元素为 %s 的data = %s' % (str(rev_ele), __text))
            return __text
        except AttributeError, e:
            log.error(e)
            raise AttributeError('参数 rev_ele= %s 没有data这个方法' % str(rev_ele))

    def get_ele_attribute(self, rev_ele):
        """
        获取目标元素的所有attribute
        :param rev_ele: 接收目标元素
        :return:返回属性值
        """
        try:
            __att = rev_ele.attrib
            log.debug('获取元素为 %s 的attribute = %s' % (str(rev_ele), __att))
            return __att
        except AttributeError, e:
            log.error(e)
            raise AttributeError('参数 rev_ele= %s 没有getAttribute这个方法' % str(rev_ele))

    def get_ele_tag(self, rev_ele):
        """
        获取目标元素的tag
        :param rev_ele: 接收目标元素
        :return:返回tag
        """
        try:
            __att = rev_ele.tag
            log.debug('获取元素为 %s 的tag = %s' % (str(rev_ele), __att))
            return __att
        except AttributeError, e:
            log.error(e)
            raise AttributeError('参数 rev_ele= %s 没有tag这个方法' % str(rev_ele))

    def find_all_child_nodes(self, rev_ele, rev_tag):
        """
        通过tag获取目标的元素的子节点
        :param rev_ele: 接收目标元素
        :param rev_tag: 接收所找的tag
        :return:返回子节点的列表
        """
        __all_child_nodes = rev_ele.findall(rev_tag)
        return __all_child_nodes

    def find_first_child_node(self, rev_ele, rev_tag):
        """
        通过tag获取目标元素的第一个子节点
        :param rev_ele: 接收目标元素
        :param rev_tag: 接收所找的tag
        :return:返回第一个子节点
        """
        __first_child_node = rev_ele.find(rev_tag)
        return __first_child_node
