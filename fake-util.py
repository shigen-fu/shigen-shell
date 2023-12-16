# -*- encoding: utf-8 -*-
__date__ = '2023/12/16 16:44:34'

import argparse
from faker import Faker

fake = Faker('zh-CN')

def generate_data(data_type, count):
    if data_type == 'address':
        for _ in range(count):
            print(fake.address())
    elif data_type == 'company':
        for _ in range(count):
            print(fake.company())
    elif data_type == 'datetime':
        for _ in range(count):
            print(fake.date_time())
    elif data_type == 'email':
        for _ in range(count):
            print(fake.email())
    elif data_type == 'name':
        for _ in range(count):
            print(fake.name())
    elif data_type == 'phone':
        for _ in range(count):
            print(fake.phone_number())
    elif data_type == 'text':
        for _ in range(count):
            print(fake.paragraph())
    elif data_type == 'internet':
        for _ in range(count):
            print(fake.url())
    elif data_type == 'vehicle':
        for _ in range(count):
            print(fake.license_plate())

def main():
    parser = argparse.ArgumentParser(description='生成任意数量的模拟数据')
    parser.add_argument('-t', '--type', choices=['address', 'company', 'datetime', 'email', 'name', 'phone', 'text', 'internet', 'vehicle'], help='生成的数据类型')
    parser.add_argument('-c', '--count', type=int, default=1, help='生成模拟数据的数量')

    args = parser.parse_args()
    generate_data(args.type, args.count)

if __name__ == '__main__':
    main()
