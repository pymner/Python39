# 获取yaml数据
import yaml


def loadyaml(filename):
    files = open(filename, 'r', encoding='utf-8')

    data = yaml.load(files, Loader=yaml.FullLoader)

    #print(data)

    return data


if __name__ == '__main__':
    loadyaml('../data/login.yaml')
