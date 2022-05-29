import xml.etree.ElementTree as Et


def get_data(xml_file: str, teg: str, list_of_attributes: list):
    """
    :param xml_file: файл который ты хочешь разрбрать
    :param teg: тег в котором ты будешь искать данные атрибутов
    :param list_of_attributes: список атрибутов которые ты хочешь перебирать если тег соотвествует тому который ищешь
    :return: список списков в данным аттрибутов котоыре ты ищешь в тегах
    """
    result = []
    tree = Et.parse(xml_file)
    root = tree.getroot()
    for child in root:
        if child.tag == teg:
            # child.tag - это тег который ты хочешь разобрать
            # child.attrib - это словарь (dict)
            # раскоментируй следующую строку и увидешь что выводится
            # print("child.tag:", child.tag, "child.attrib:", child.attrib)
            tmp_attr = []   # временный список для добавления в общий возвращаемый. чиститься на каждой иттерации
            for attr in list_of_attributes:
                tmp_attr.append(child.attrib.get(attr))
            result.append(tmp_attr)
    return result


if __name__ == '__main__':
    data = get_data('file.xml', 'relation', ['entry1', 'entry1'])
    print(data)
